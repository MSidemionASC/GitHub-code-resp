# problem 1
numberList = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

# problem 2
zeroList = [0, 0, 0, 0, 0]

#problem 3
emptyList = []

# problem 4
i = 0
zeroListEmpty = []
while i < 5:
    zeroListEmpty.append(0)
    i = i + 1
print(zeroListEmpty)
print(len(zeroListEmpty))

# problem 5
randList = ["a", 5, "doodle", 3, 10]
print(len(randList))

# problem 6

del randList[2]
print(randList)

# problem 7
randList.append("scribble")
print(randList)

# problem 8
randList[0] = 8.4
print(randList)

# problem 9 
randList.insert(0, 7)
print(randList)

# problem 10
userAmt = int(input("enter a number"))
oddList = []
n = 0
while n <= userAmt:
    if n%2 == 1:
        oddList.append(n)
    n = n + 1
print(oddList)
        
        
