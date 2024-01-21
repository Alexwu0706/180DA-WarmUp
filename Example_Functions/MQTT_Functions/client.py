import paho.mqtt.client as mqtt
import numpy as np
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connection returned result: " + str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
# client.subscribe("ece180d/test")
    client.subscribe("nihao123",1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
              
# The default message callback.
# (won’t be used if only publishing, but can still exist)
        
counter = 0
def on_message(client, userdata, message):
    global counter
    print("Received message: " + str(message.payload) + " on topic " + message.topic + " with QoS " + str(message.qos)) 
    counter = counter + 1
    print("you received " + str(counter) + " messages from others")

#1 initialization a client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async("mqtt.eclipseprojects.io")

#2 get into a traffic flow
client.loop_start()
while True:
    msg = input("Enter the message that you want to send: \n" )
    client.publish("lol123",msg,1)
    if(msg == "exit now"):
        break

client.loop_stop()
client.disconnect()

