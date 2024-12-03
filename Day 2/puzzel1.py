f = open("Day 2/DayTwoInput.txt", "r")
reports = []
safe = 0

for report in f:
    levels = list(map(int, report.split())) 
    reports.append(levels)

for report in reports:
    increasing = all(j > i for i, j in zip(report, report[1:]))
    decreasing = all(j < i for i, j in zip(report, report[1:]))
    differences_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    if (increasing or decreasing) and differences_valid:
        safe += 1

print(safe)

