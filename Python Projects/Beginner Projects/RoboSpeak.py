import os
print("Welcome to RoboSpeaker, created by Sahil")
while(True):
    x = input("Enter what you want me to speak: ")
    if x == "s":
        print("say bye bye my friend'")
        break
    command = 'say' , x
    os.system(command)