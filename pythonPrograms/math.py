import math
# Decimal to binary
def binaryConverter(num):
    if num > 1:
      binaryConverter(num//2)
    print(num % 2, end="")
deci = int(input("Enter the decimal: "))
binaryConverter(deci)
print()
