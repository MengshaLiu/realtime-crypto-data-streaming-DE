from websocket import create_connection
import json
import time
import logging
from kafka import KafkaProducer
import time
import uuid

def connect_to_tiingo_api():

    ws = create_connection("wss://api.tiingo.com/crypto")

    subscribe = {
        'eventName':'subscribe',
        'authorization':'YOUR_AUTHENTICATION_CODE',
        'eventData': {
            'thresholdLevel': 5
        }   
    }
    ws.send(json.dumps(subscribe))
    return ws 

def recieve_data_from_api(ws):
    recv=json.loads(ws.recv())
    return recv


def transform_data(recv):
    data={}
    data['id']=str(uuid.uuid4()) 
    data['ticker']=recv['data'][1]
    data['date']=recv['data'][2]
    data['exchange_platform']=recv['data'][3]
    data['trade_volume']=recv['data'][4]
    data['trade_price']=recv['data'][5]
    return data

if __name__=="__main__":
    curr_time= time.time()
    ws=connect_to_tiingo_api()
    producer = KafkaProducer(bootstrap_servers=['localhost:29092', 'localhost:39092'], retries=3, acks='all' )
    i=0
    while True:
        if time.time()>curr_time+60:
            print(f"{i} of transactions are streaming!")
            break
        try:
            recv=recieve_data_from_api(ws)
            trans_data=transform_data(recv)
            key=trans_data['ticker']
            print(trans_data)
            producer.send(topic='crypto_transactions', value=json.dumps(trans_data).encode('utf-8'), key=json.dumps(key).encode('utf-8'))
            i=i+1

        except Exception as e:
            logging.error(f'an error occured: {e}')

            continue

    producer.flush()