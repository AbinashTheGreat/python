name = input("What's your name? ")

# Remove white spaces from str => name = name.strip().title()
# To Capitalize the code => name = name.capitalize()
# To Capitalize all the word => name = name.title()
fname , lname = name.split()
# Say hello to user
print(f"Hello, {fname}")