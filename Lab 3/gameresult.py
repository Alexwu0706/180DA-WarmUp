import random
import paho.mqtt.client as mqtt
import numpy as np

#-------------------------Game Program-----------------------------------------------------------------------------
def RPS(inputRPC1,inputRPC2):
    result = ""
    if(inputRPC1 == inputRPC2):
        result = "no one wins"
    elif(inputRPC1 == "rock" and inputRPC2 == "paper"):
        result = "Player2 win"
    elif(inputRPC1 == "rock" and inputRPC2 == "scissor"):
        result = "Player1 win"
    elif(inputRPC1 == "paper" and inputRPC2 == "scissor"):
        result = "Player2 win"
    elif(inputRPC1 == "paper" and inputRPC2 == "rock"):
        result = "Player1 win"
    elif(inputRPC1 == "scissor" and inputRPC2 == "paper"):
        result = "Player2 win"
    elif(inputRPC1 == "scissor" and inputRPC2 == "rock"):
        result = "Player1 win"
    elif(inputRPC1 == "exit now()" or inputRPC2 == "exit now()"):
        result = "exit now()"

    return result

#=========================Communication---------------------------------------------------------------------------
# 0. define callbacks - functions that run when events happen.
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    #print("Connection returned result: " + str(rc))
# Subscribing in on_connect() means that if we lose the connection and
# reconnect then subscriptions will be renewed.
    client.subscribe("player1",1)
    client.subscribe("player2",1)

# The callback of the client when it disconnects.
def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected Disconnect")
    else:
        print("Expected Disconnect")
              
# The default message callback.
# (won’t be used if only publishing, but can still exist)
        
User1input = ""
User2input = ""
def on_message(client, userdata, message):
    global User1input
    global User2input
    if (message.topic == "player1"):      
        User1input = message.payload.decode()
        print("Received message: " + User1input + " on topic " + message.topic + " with QoS " + str(message.qos)) 
    elif (message.topic == "player2"):
        User2input = message.payload.decode()
        print("Received message: " + User2input + " on topic " + message.topic + " with QoS " + str(message.qos)) 

#--------------------------------------Control Panel---------------------------------------------------------------------------
#1 initialization a client
client = mqtt.Client()
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_message = on_message
client.connect_async("mqtt.eclipseprojects.io")

#2 get into a traffic flow
client.loop_start()

flag1 = 0
flag2 = 0
while(True):
    User1input = ""
    User2input = ""
    while(User1input == "" or User2input == ""):
        continue

    result = RPS(User1input,User2input)
    if(result == "Player1 win"):
        flag1 = flag1 + 1
    elif(result == "Player2 win"):
        flag2 = flag2 + 1
    client.publish("result","result: " + result + '\n',1)
    client.publish("result","       scoreboard     " + '\n',1) 
    client.publish("result","player1 uses "+ User1input + '    ' + str(flag1) + '\n',1)
    client.publish("result","player2 uses "+ User2input + '    ' + str(flag2) + '\n',1)

    

client.loop_stop()
client.disconnect()