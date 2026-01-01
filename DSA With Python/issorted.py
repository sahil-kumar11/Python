def issorted(arr,n):
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            return False
    return True

arr1=[1,2,3,3,6,7]
n=len(arr1)
print("True" if issorted(arr1,n) else "False")