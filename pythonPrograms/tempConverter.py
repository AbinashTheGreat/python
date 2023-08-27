selec = int(input("Please select: 1. C => F 2. C => K 3. F => C 4. F => K  5. K => F 6. K => C "))
# Function for celsius, Fahrenheit, Kelvin
def cel():
    global celi
    celi = int(input("Please enter the temperature in celsius: "))
def farh():
    global feri
    feri = int(input("Please enter the temperature in fahrenheit: "))
def kelv():
    global keli
    keli = int(input("Please enter the temperature in Kelvin: "))
# Switch statement for the optional Calculator
match selec:
    case 1:
        cel()
        faren = (celi*180) / 100 + 32
        print(f"{celi}°Celsius is equal to {faren}°Farenheit.")
    case 2:
        cel()
        kelvin = celi + 273
        print(f"{celi}°Celsius is equal to {kelvin}°Kelvin")
    case 3:
        farh()
        celsius = (feri - 32) * 100 / 180
        print(f"{feri}°Fahrenheit is equal to {celsius}°Celsius")
    case 4:
        farh()
        kelvin = ((feri - 32) * 100) / 180 + 273
        print(f"{feri}°Fahrenheit is equal to {kelvin}°Kelvin")
    case 5:
        kelv()
        faren = ((keli -273) * 180 / 100) + 32
        print(f"{keli}°Kelvin is equal to {faren}°Fahrenheit")
    case 6:
        kelv()
        celsius = (keli -273) * 180 / 100
        print(f"{keli}°Kelvin is equal to {celsius}°C")