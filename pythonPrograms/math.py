import math
# Volume of a sphere using function
'''def volume(rad): # def is for defining the function
    vols = 4 / 3 * math.pi * rad**3
    res = round(vols, 3)
    print(f"The volume of sphere is {res}m\u00b3")  # \u00b3 gives cube symbol
volume(int(input("Please enter the radius of sphere: ")))'''

# Temperature converter
# Celsius to farenheit
'''cel = int(input("Please enter the temperature in celsius: "))
faren = (cel*180) / 100 + 32
print(f"{cel}°C is equal to {faren}°Farenheit.")'''

# Number Checker
# If the number is odd or even
''' num = int(input("Enter a number to check if it is odd or even: "))
checker = num % 2
if checker == 1:
    print(f"{num} is an odd number.")
else:
    print(f"{num} is an even number") '''

# Which number is the greatest
'''num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the Second number: "))
num3 = int(input("Enter the Third number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest.")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest.")
else:
    print(f"{num3} is the greatest")'''
    
# Decimal to binary
def binaryConverter(num):
    if num > 1:
      binaryConverter(num//2)
    print(num % 2, end="")
deci = int(input("Enter the decimal: "))
binaryConverter(deci)
print()
