# Print current working directory
import os
print(os.getcwd())

# Does expenses.csv exist (expenses.csv not found)
if os.path.exists("week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")  

# Build a path for expenses.csv (week-7/data/expenses.csv)
path = os.path.join("week-7", "data", "expenses.csv")      
print(path)


