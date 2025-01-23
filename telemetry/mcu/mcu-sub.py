import paho.mqtt.client as paho

def on_message(mosq, obj, msg):
    print("topic: ", msg.topic, "qos: ", msg.qos, "payload: ", msg.payload, "\n")
    mosq.publish('sensor/dist_ack', 'ack', 0)

def on_publish(mosq, obj, mid):
    pass

if __name__ == '__main__':
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish

    client.connect("10.70.4.38", 1883, 60)

    client.subscribe("sensor/distance", 1)

    while client.loop() == 0:
        pass