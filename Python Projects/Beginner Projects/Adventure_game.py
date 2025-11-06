name = input("What is your name: ")
print(f"Welcome, {name} to this adventure game!")

answer = input("You came into this game,Now you have to tpye left or right: ")

if answer == "left":
    answer = input("You came to the river side, Now you can walk around it and swim across it, Type walk for walk and swim for swim: ")

    if answer == "walk":
        print("You walked around the river and ran out of water and lost the game")

    elif answer == "swim":
        print("you swam across the river and eaten by the crocodile")

    else : 
        print("Invalid input")

elif answer == "right":
    answer = input("You came to a bridge its looks wobbly , you want to cross it or want to head back (cross/back)? ")

    if answer == "back":
        print("you just came back safe")

    elif answer == "cross":
        answer = input("you cross the bridge safe and there is a stranger infront of you want to meet him or not (meet/not)? ")

        if answer == "meet":
            print("You meet the stranger and he gives you the GOLD! YOU WON!")

        elif answer == "not":
            print("You just ignore the stranger and you lost the game")
        
        else :
            print("Invalid input")

    else :
        print("Invalid input")
else :
    print("Invalid Statement")