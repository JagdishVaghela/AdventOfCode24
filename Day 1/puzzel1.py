f = open("Day 1/DayOneInput.txt", "r")
list1 = []
list2 = []
total = 0
for row in f:
    int1 = int(row[0:5])
    int2 = int(row[8:13])
    list1.append(int1)
    list2.append(int2)

list1.sort()
list2.sort()

for i in range (0,1000):
      dist = abs(list1[i]-list2[i])
      total = total + dist

print(total)
