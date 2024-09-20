from pyspark.sql import SparkSession
import json
import logging
from pyspark.sql.types import StringType, StructField, StructType, ArrayType, DoubleType
from pyspark.sql.functions import from_json, col, date_format, expr, concat, to_timestamp

def create_spark_conn():
    try:
        spark=None
        spark = SparkSession \
        .builder \
        .appName("CtyptotrTransactipnApp") \
        .config("spark.jars.packages","org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.4," "org.apache.hadoop:hadoop-common:3.3.4," "org.apache.hadoop:hadoop-aws:3.3.4," "com.amazonaws:aws-java-sdk-bundle:1.12.262") \
        .getOrCreate()
        
        #Configure AWS Connector
        hadoop_conf = spark.sparkContext._jsc.hadoopConfiguration()
        hadoop_conf.set("fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
        hadoop_conf.set("fs.s3a.access.key", "YOUR_ACCESS_KEY")
        hadoop_conf.set("fs.s3a.secret.key", "YOUR_ACCESS_SECRET_KEY" )

        logging.info('Spark connection created successfully')
        spark.sparkContext.setLogLevel("ERROR")
        
    except Exception as e:
        logging.error(f"couldn't create the spark connection due to: {e}")
    
    return spark

def conncet_to_kafka(spark_conn):
    df = None

    df = spark_conn.readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", "localhost:29092,localhost:39092") \
        .option("subscribe", "crypto_transactions") \
        .option("startingOffsets","latest") \
        .load()
    
    return df

def transform_df_from_kafka(df):
#Write JSON schema for the value feild
    json_schema = StructType([StructField('ticker', StringType(), False), \
    StructField('date', StringType(), False), \
    StructField('exchange_platform', StringType(), False), \
    StructField('trade_volume', DoubleType(), False), \
    StructField('trade_price', DoubleType(), False)])
    
# Parse value from binay to string    
    df = df.selectExpr("cast(value as string) as value")
    expanded_df = df.withColumn("value", from_json(df["value"], json_schema)).select("value.*")
    
    transformed_df = expanded_df.withColumn("date", to_timestamp(concat(
        date_format(expanded_df["date"], "yyyy-MM-dd'T'HH:mm:ss.SSS"),
        expr("'+0000'"))
    ))
    
    return transformed_df

if __name__=="__main__":    
    spark_conn = create_spark_conn()
    if spark_conn is not None:
        df = conncet_to_kafka(spark_conn)
        transformed_df = transform_df_from_kafka(df)      
        # Write the output to console sink to check the output
        writing_df = transformed_df.writeStream \
            .option("checkpointLocation","s3a://Bucket_name/checkpoint_dir") \
            .format("json") \
            .option("path", "s3a://Bucket_name/transformed") \
            .start()

        writing_df.awaitTermination()    

