f = open("Day 2/DayTwoInput.txt", "r")
reports = []
safe = 0

for report in f:
    levels = list(map(int, report.split()))  
    reports.append(levels)

def is_safe(report):
    increasing = all(j > i for i, j in zip(report, report[1:]))
    decreasing = all(j < i for i, j in zip(report, report[1:]))
    differences_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    return (increasing or decreasing) and differences_valid

for report in reports:
    if is_safe(report):
        safe += 1
    
    for i in range(len(report)):
        newreport = report[:i] + report[i + 1:]  
        if is_safe(newreport):
            safe += 1
            break

print(safe)


