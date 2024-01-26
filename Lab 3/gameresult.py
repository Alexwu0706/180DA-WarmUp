import random
import paho.mqtt.client as mqtt
import numpy as np

#-------------------------Game Program-----------------------------------------------------------------------------
def RPS(inputRPC1,inputRPC2):
    if(inputRPC1 == inputRPC2):
        print("no one wins")
    elif(inputRPC1 == "rock" and inputRPC2 == "paper"):
        print("Player2 win")
    elif(inputRPC1 == "rock" and inputRPC2 == "scissor"):
        print("Player1 win")
    elif(inputRPC1 == "paper" and inputRPC2 == "scissor"):
        print("Player2 win")
    elif(inputRPC1 == "paper" and inputRPC2 == "rock"):
        print("Player1 win")
    elif(inputRPC1 == "scissor" and inputRPC2 == "paper"):
        print("Player2 win")
    elif(inputRPC1 == "scissor" and inputRPC2 == "rock"):
        print("Player1 win")
    elif(inputRPC1 == "exit now()" or inputRPC2 == "exit now()"):
        print("exit now()")

#=========================Communication---------------------------------------------------------------------------
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connection returned result: " + str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
     client.subscribe("s2",1)
     client.subscribe("s1",1)
     client.subscribe("s",1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
              
# The default message callback.
# (won’t be used if only publishing, but can still exist)
        
counter = 0
User1input = ""
User2input = ""
def on_message(client, userdata, message):
    global counter
    global User1input
    global User2input
    if (message.topic == 'server0706_1'):      
        User1input = message.payload.decode()
        print("Received message: " + User1input + " on topic " + message.topic + " with QoS " + str(message.qos)) 
        print("you received " + str(counter) + " messages from others")
    elif (message.topic == "server0706_2"):
        User2input = message.payload.decode()
        print("Received message: " + User2input + " on topic " + message.topic + " with QoS " + str(message.qos)) 
        print("you received " + str(counter) + " messages from others")  

#--------------------------------------Control Panel---------------------------------------------------------------------------
#1 initialization a client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async("mqtt.eclipseprojects.io")

#2 get into a traffic flow
client.loop_start()

while(True):
    User1input = ""
    User2input = ""
    while(User1input == "" or User2input == ""):
        continue

    result = RPS(User1input,User2input)
    client.publish("s",result, 1)
    

client.loop_stop()
client.disconnect()