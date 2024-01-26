import random

def RPS(inputRPC):
    result = ""
    output = ["rock","paper","scissor"]
    outputRPC = random.choice(output)
    if(outputRPC == inputRPC):
        result = "no winner"
    elif(outputRPC == "rock" and inputRPC == "paper"):
        result = "you win"
    elif(outputRPC == "rock" and inputRPC == "scissor"):
        result = "you lose"
    elif(outputRPC == "paper" and inputRPC == "scissor"):
        result = "you win"
    elif(outputRPC == "paper" and inputRPC == "rock"):
        result = "you lose"
    elif(outputRPC == "scissor" and inputRPC == "rock"):
        result = "you win"
    elif(outputRPC == "scissor" and inputRPC == "paper"):
        result = "you lose"
    else:
        result = "invalid input"

    return result

inputRPC = ""
while(inputRPC != "stop"):
    inputRPC = input("Please enter your gesture:")
    print(RPS(inputRPC))

