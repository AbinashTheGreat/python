name = input("What's your name? ")

# Remove white spaces from str => name = name.strip().title()
# To Capitalize the code => name = name.capitalize()
# To Capitalize all the word => name = name.title()
spliter = name.split()
if len(spliter) == 2:
    while len(spliter) == 2:
        print("You dont have a Middle name, if so:", end=" ")
        name = input("What's your name: ")
        spliter = name.split()
        break
# Say hello to user
fname , mname , lname = name.split()
print(f"So, your middle name is {mname}")