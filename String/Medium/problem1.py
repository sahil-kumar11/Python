my_str = "Programming is fun"
vowels = "aeiou"
count = 0

for char in my_str.lower():    
    if char in vowels:
        count += 1

print(count)  
