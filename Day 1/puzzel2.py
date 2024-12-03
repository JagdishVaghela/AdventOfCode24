f = open("Day 1/DayOneInput.txt", "r")
list1 = []
list2 = []
total = 0
for row in f:
    int1 = int(row[0:5])
    int2 = int(row[8:13])
    list1.append(int1)
    list2.append(int2)

for i in range(0,1000):
    count = 0
    for j in range(0,1000):
        if list1[i] == list2[j]:
            count += 1
    total += (count * list1[i])

print(total)