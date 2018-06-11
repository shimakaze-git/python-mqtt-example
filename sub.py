#!/usr/bin/python
# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
import ssl

host = '127.0.0.1'
port = 1883
### パスワード認証を使用する時に使用する
#username = 'mqtt'
#password = 'mqtt'
# SSL
# port = 8883
# cacert = './cert/ca.crt'
# clientCert = './cert/client.crt'
# clientKey = './cert/client_nopass.key'

topic = 'paho/mqtt'

def on_connect(client, userdata, flags, respons_code):
    """broker接続時のcallback関数
    """
    print(flags)
    
    print('status {0}'.format(respons_code))
    client.subscribe(topic)

def on_message(client, userdata, msg):
    """メッセージ受信時のcallback関数
    """
    print(msg.topic + ' ' + str(msg.payload))

if __name__ == '__main__':
    ### インスタンス作成時にprotocol v3.1.1を指定
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    ### パスワード認証を使用する時に使用する
    #client.username_pw_set(username, password=password)
    
    ### callback function
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)
    client.loop_forever()