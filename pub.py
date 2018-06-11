#!/usr/bin/python
# -*- coding: utf-8 -*-

import random, json
from time import sleep
import paho.mqtt.client as mqtt

host = '127.0.0.1'
port = 1883
### パスワード認証を使用する時に使用する
#username = 'mqtt'
#password = 'mqtt'
### SSL
# port = 8883

topic = 'paho/mqtt'

def on_connect(client, userdata, flags, respons_code):
    """broker接続時のcallback関数
    """
    print('status {0}'.format(respons_code))
    
    for i in range(3):
        message = {
            'message': random.randint(50, 100),
        }
        message = json.dumps(message)
        
        client.publish(topic, message)
        sleep(0.2)

def on_publish(client, userdata, mid):
    """メッセージをpublishした後のcallback関数
    """
    client.disconnect()

if __name__ == '__main__':

    ### インスタンス作成時にprotocol v3.1.1を指定
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    ### パスワード認証を使用する時に使用する
    # #client.username_pw_set(username, password=password)

    ### callback function
    client.on_connect = on_connect
    client.on_publish = on_publish

    client.connect(host, port=port, keepalive=60)
    client.loop_forever()