def findAvg(listNums, length):
    total = 0
    for i in range(0,len(listNums)):
        total = total + listNums[i]

    avg = total / length
    return avg

#Driver Code
listNums = [5,5,5,5,5]
length = int(len(listNums))
print(length)
average = findAvg(listNums, length)
print(average)