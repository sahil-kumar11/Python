class ArmstrongChecker:

    @staticmethod
    def is_armstrong(num):
        k = len(str(num))  # Number of digits
        sum = 0
        n = num

        while n > 0:
            ld = n % 10             # Last digit
            sum += ld ** k          # Add ld^k
            n = n // 10             # Remove digit

        return sum == num

number = 1634

if ArmstrongChecker.is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")