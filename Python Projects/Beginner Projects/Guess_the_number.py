import random
n = random.randint(1, 100)
a = -1                #To initialize a with a value different from n so the loop starts.
guesses = 0          
while(a != n):        #To keep asking the user until the guessed number equals the secret number.
    
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number please")
        guesses +=1
print(f"You have gussessed the number {n} in {guesses} guesses")