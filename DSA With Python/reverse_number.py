number = int(input("Enter number: "))
reverse = 0
while number > 0:
    id = number % 10
    reverse = (reverse * 10) + id
    number = number//10

print(reverse)