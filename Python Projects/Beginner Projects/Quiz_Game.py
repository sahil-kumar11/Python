print("Welcom to my Computer Game")

print("Do you want to play? ")

playing = input("Enter 'yes' to play, 'no' to quit: ")

if playing.lower() != 'yes':
    quit()

score = 0


Answer = input("What does CPU stand for: ")
if Answer.lower() == 'central processing unit':
    print("That is correct!")
    score +=1
else:
    print("That is incorrect.")


Answer = input("What does GPU stand for: ")
if Answer.lower() == 'graphics processing unit':
    print("That is correct!")
    score +=1
else:
    print("That is incorrect.")


Answer = input("What does RAM stand for: ")
if Answer.lower() == 'random accessing memory':
    print("That is correct!")
    score +=1
else:
    print("That is incorrect.")


Answer = input("What does PSU stand for: ")
if Answer.lower() == 'power supply unit':
    print("That is correct!")
    score +=1
else:
    print("That is incorrect.")

print("Your score is: " + str(score))