import math
def countdigits(n):
    count = int(math.log10(n) +1)
    return count


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print ("N:",n)
    digits = countdigits(n)
    print("The digits count number is:",digits)