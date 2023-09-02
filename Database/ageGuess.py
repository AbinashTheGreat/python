import json, random
firstInput = str(input("Select \na => Input data | b => for revision| \n:"))

def openFile():
  with open ("data.txt", "r") as fp:
    global data
    data = json.load(fp)

openFile()
if firstInput == "a":
  name = str(input("Enter a name: "))
  age = int(input("Enter age: "))
  update = [name, age]
  data.append(update)
  with open("data.txt", "w") as fp:
    json.dump(data, fp)
elif firstInput == "b":
  openFile()
  rand = random.randrange(len(data) - 1)
  randomizer = data[rand] [0]
  guess = int(input(f"what is the age of {randomizer} ? \n:"))
  if guess == data[rand][1]:
    print("Bingo!!!")
  else:
    print(f"You are wrong. The age of {randomizer} is {data[rand][1]}")
  
print(data)