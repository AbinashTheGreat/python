# Imported string and random for the working of code
import string , random
#Created list of alphabet from a-z 
guess = list (string.ascii_uppercase)
# Below Line of code first prints a random and Suggests the right alphabet if wrong
i = 4
while i < 5: 
    rand = guess[random.randrange(27)]
    print(rand)
    ans = int(input("Guess the number:  "))
    if guess[ans - 1] == rand:
        print("BINGO!")
    else:
        print(f"{ans} is for {guess[ans - 1]}")
