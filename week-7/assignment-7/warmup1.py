import os
path = os.path.join("week-7", "data", "notes.txt")
print(path)

with open(path, 'r') as file:
    lines = file.readlines()
    print(lines[0])

line_number = 1

for line in lines:
    print(f"Line {line_number}: {line.strip()}")

    line_number += 1
