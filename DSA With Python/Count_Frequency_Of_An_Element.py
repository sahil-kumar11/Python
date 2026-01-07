arr = [1, 4, 1, 2, 1, 3]
target = 1
count = 0
for i in range(len(arr)):
    if arr[i] == target:
        count += 1
print("The total count frequency of an element is:",count)