def largestNumber(arr,n):
    largest = arr[0]
    for i in range(1,n):
        if arr[i] > largest:
            largest = arr[i]
    return largest
if __name__ == "__main__":
    arr1=[10,20,50,30,70,40]
    n=len(arr1)
    max=largestNumber(arr1,n)
    print("The Largest Number is:",max)