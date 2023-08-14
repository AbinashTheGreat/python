import random
# Create Question Type such as What and Where
# First Create a dictionary of question and answer
rand = ["apple", "orange","mango"]
fructose = {'apple': 'red', 'orange': 'orange','mango':"yellow"}
guess = rand[random.randrange(2)]
# Print out a random Question and take answer as input
print(guess)
ans = str(input("Relatable color: "))
# Process the answer and tell whether it is correct or not and continue using while loop
if ans == fructose[guess]:
    print("Bingo")
else: 
    print("Try Again!!!")