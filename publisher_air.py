import paho.mqtt.client as mqtt
import random, time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    temp = round(random.uniform(24,35),2)
    hum = round(random.uniform(50,90),2)
    pm25 = round(random.uniform(10,120),2)

    client.publish("airquality/lab1/temperature", temp, qos=0)
    client.publish("airquality/lab1/humidity", hum, qos=1)
    client.publish("airquality/lab1/pm25", pm25, qos=2)

    print("Data sent")
    time.sleep(5)
