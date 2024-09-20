from kafka import KafkaConsumer
import json
import logging
import boto3

try:
    s3=boto3.client('s3',
                      aws_access_key_id='YOUR_ACCESS_KEY_ID',
                      aws_secret_access_key='YOUR_ACCESS_SECRET',
                      region_name='YOUR_REGION')
    consumer = KafkaConsumer('crypto_transactions',
                             bootstrap_servers=['localhost:29092', 'localhost:39092'],
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')),
                            )
    for message in consumer:
        with open('data.json','w+') as f:
            json.dump(message.value,f)
        s3.upload_file(Filename='data.json', Bucket='uniswap-transaction-streaming', Key=f"raw/{message.value['id']}.json")
        
except Exception as e:
    logging.error(f'Kafka consumer initilization failed due to {e}')
