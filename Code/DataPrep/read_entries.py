from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder

from pickle import TRUE
import re
import time as t
import json
import pandas as pd
import numpy as np
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import csv

ENDPOINT = "auwr8r23bm2np-ats.iot.us-east-1.amazonaws.com"
CLIENT_ID = "computerAcidentes"
PATH_TO_CERTIFICATE = (r'C:\Users\Carlos Ferreira\Documents\GitHub\Projeto-IoT-e-Data-Science\Code\DataPrep\Certificates\computerAcidentes.cert.pem')
PATH_TO_PRIVATE_KEY = (r'C:\Users\Carlos Ferreira\Documents\GitHub\Projeto-IoT-e-Data-Science\Code\DataPrep\Certificates\computerAcidentes.private.key')
PATH_TO_AMAZON_ROOT_CA_1 = (r'C:\Users\Carlos Ferreira\Documents\GitHub\Projeto-IoT-e-Data-Science\Code\DataPrep\Certificates\AmazonRootCA1.pem')
MESSAGE = "Estamos conectado"

TOPIC= "computer/acidentes"

RANGE = 20

if __name__ == '__main__':

    event_loop_group = io.EventLoopGroup(1)
    host_resolver = io.DefaultHostResolver(event_loop_group)
    client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)

    mqtt_connection = mqtt_connection_builder.mtls_from_path(
        endpoint=ENDPOINT,
        cert_filepath=PATH_TO_CERTIFICATE,
        pri_key_filepath=PATH_TO_PRIVATE_KEY,
        ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
        client_bootstrap=client_bootstrap,
        client_id=CLIENT_ID,
        clean_session=False,
        keep_alive_secs=6,
    )
    #return mqtt_connection
    print(f"Conectando: {ENDPOINT} o ID do cliente é '{CLIENT_ID}'...")
    connection_future = mqtt_connection.connect()
    connection_future.result()
    #return connection_future

    print("Conectado")

    iot_pb_df = pd.read_csv(r'C:\Users\Carlos Ferreira\Documents\GitHub\Projeto-IoT-e-Data-Science\Data\Raw\NYC_Motor.csv', encoding="utf-8")
    iot_pb_df.sort_values(by = 'CRASH_DATE', ascending=True)

    for nlinha, linha in iot_pb_df.iterrows():
        data = {'CRASH_DATE':linha.CRASH_DATE,
                'CRASH_TIME': linha.CRASH_TIME,
                'PERSON_INJURY': linha.PERSON_INJURY,
                'PERSON_AGE': linha.PERSON_AGE,
                'PERSON_SEX': linha.PERSON_SEX,
                'PERSON_INJURY_BIN': linha.PERSON_INJURY_BIN,
                'PERSON_SEX_BIN': linha.PERSON_SEX_BIN
        }
        try:
            #message = {"Acidentes_Fatais" :  iot_pb_df}
            mqtt_connection.publish(topic=TOPIC,
                                    payload=json.dumps(data),
                                    qos=mqtt.QoS.AT_LEAST_ONCE)    
            print("Published: '" + json.dumps(data))
            t.sleep(.1)
        except KeyboardInterrupt:
            # Disconnect
            print("Desconectando...")
            disconnect_future = mqtt_connection.disconnect()
            disconnect_future.result()
            print("Disconectado")
            t.sleep(4)