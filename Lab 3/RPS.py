import random

def RPS(inputRPC):
    output = ["rock","paper","scissor"]
    outputRPC = random.choice(output)
    if(outputRPC == inputRPC):
        print("your input is: " + inputRPC + ' And the computer input is: ' + outputRPC)
    elif(outputRPC == "rock" and inputRPC == "paper"):
        print("you win")
    elif(outputRPC == "rock" and inputRPC == "scissor"):
        print("you lose")
    elif(outputRPC == "paper" and inputRPC == "scissor"):
        print("you win")
    elif(outputRPC == "paper" and inputRPC == "rock"):
        print("you lose")
    elif(outputRPC == "scissor" and inputRPC == "rock"):
        print("you win")
    elif(outputRPC == "scissor" and inputRPC == "paper"):
        print("you lose")

inputRPC = ""
while(inputRPC != "stop"):
    inputRPC = input("Please enter your gesture:")
    RPS(inputRPC)

