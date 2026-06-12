# MQTT Air Quality Monitoring

## Install
pip install -r requirements.txt

## Run Broker
mosquitto -v

## Run Publisher
python publisher_air.py

## Run Subscriber
python subscriber_monitor.py

## Wildcard +
python subscriber_room.py

## Wildcard #
python subscriber_all.py
