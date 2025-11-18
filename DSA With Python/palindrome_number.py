def palindrome(n):
    revNum = 0
    dup = n

    while n > 0:
        id = n % 10
        revNum = revNum * 10 + id
        n = n // 10

    return dup == revNum


def main():
    number = int(input("Enter your number: "))
    if palindrome(number):
        print(number, "is Palindrome")
    else:
        print(number, "is not Palindrome")


if __name__ == "__main__":
    main()
