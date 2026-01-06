def linear_search(arr,num):
    for i in range(0,num):
        if arr[i] == num:
            return i
    return -1

arr1 = [1,2,3,4,5]
num1 = 5
find = linear_search(arr1,num1)
print(find)