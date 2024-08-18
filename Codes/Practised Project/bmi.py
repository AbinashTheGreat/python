def bmicalc(weight,height):
    result = weight / ((height / 100) ** 2)
    return round(result,2)

weight = float(input("Please enter your weight(kg): "))
height = float(input("Please enter your height(cm): "))

ans = bmicalc(weight,height)

print(ans)

if ans < 18.5:
    print("You are underweight!!!")
elif 18.5 <= ans <= 24.9:
    print("Your weight is normal!!!")
elif ans > 24.9:
    print("You are overweight!!!")
else:
    print("Go to the gym!!!")