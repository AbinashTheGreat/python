def celi():
    global cel
    cel = int(input("Please enter the temperature in celsius: "))
celi()
faren = (cel*180) / 100 + 32
print(f"{cel}°C is equal to {faren}°Farenheit.")