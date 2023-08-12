import string , random
guess = list (string.ascii_uppercase)
rand = guess[random.randrange(27)]
print(rand)
ans = int(input("Guess the number:  "))
if guess[ans - 1] == rand:
    print("BINGO!")
else:
    print(f"{ans} is for {guess[ans - 1]}")