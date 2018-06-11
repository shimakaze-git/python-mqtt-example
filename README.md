# python-mqtt-example
paho-mqttを使用してmqttを試すサンプル

# Setup

依存ライブラリの導入
```
apt-get update
apt-get install gcc make g++ uuid-dev libssl-dev libc-ares-dev 
```

ソースからインストール
```
cd /usr/local/src
sudo wget http://mosquitto.org/files/source/mosquitto-1.4.3.tar.gz
sudo tar zxvf mosquitto-1.4.3.tar.gz
cd mosquitto-1.4.3
sudo make
sudo make install
```

pythonパッケージの導入
```
sudo pip install -r requirements.txt
```

# 起動
```
mosquitto
python sub.py
python pub.py
```

# 参考資料

- https://librabuch.jp/blog/2015/09/mosquiito_paho_python_mqtt/
- https://qiita.com/n-yamanaka/items/91dbd7bd9fed5b3fbed4
- http://www.steves-internet-guide.com/mqtt-username-password-example/
