import math
# Volume of a sphere using function
def volume(rad): # def is for defining the function
    vols = 4 / 3 * math.pi * rad**3
    res = round(vols, 3)
    print(f"The volume of sphere is {res}m\u00b3")  # \u00b3 gives cube symbol
volume(int(input("Please enter the radius of sphere: ")))