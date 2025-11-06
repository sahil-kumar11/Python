numbers = [10, 20, 30, 40, 50]
# Input: 30
# Output: 2
n = int(input("Enter the number: "))
for i in numbers:
    if i == n:
        a = numbers.index(i)
        print(a)
        