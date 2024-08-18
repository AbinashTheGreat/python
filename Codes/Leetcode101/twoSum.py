import random

nList = random.sample(range(1,11), 10)
print (nList)

def twoSum(lst,target):
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[j] == target - lst[i]:
                return [i, j]
    return None
xyw = nList
target = int(input("Please enter a target:"))
print(twoSum(xyw, target))
