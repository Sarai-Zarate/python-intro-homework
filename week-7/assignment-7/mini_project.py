# Print today's date
from datetime import datetime
current_date = datetime.now()
readable_date = current_date.strftime("%B %d, %Y")
print(f"Today is {readable_date}.")

# Does the file exist 
import os

if os.path.exists("week-7/data/expenses.csv"):
    print("Found it!")
else:
    print("File not found.")

# Read data and return as dictionaries
import csv

with open('week-7/data/expenses.csv', 'r') as file:
    reader = csv.DictReader(file)
    expenses_stored = []
    for row in reader:
        print(row['date'], row['category'], row['description'], row['amount'])

# Convert the amount field to float for each row
    
        row['amount'] = float(row['amount'])
        expenses_stored.append(row)

# Filter the list to only rows where category is "Food"
category_food = []
total = 0
for row in expenses_stored:
    if row['category'] == 'Food':
        category_food.append(row)
        print(row)

#Calculate the total amount spent on Food (Accumulator)
total_food = 0
for row in expenses_stored:
    if row["category"] == "Food":
        total_food += row['amount']
print(f'Total food expenses: ${total_food:.2f}')

# Writing a txt food_report 
with open('food_report.txt', 'w') as file:
    file.write(f'Food Expense Report - generated {readable_date}')
    for row in category_food:
        file.write("\n"f'{row["date"]}: ${row["amount"]:.2f}')
    file.write("\n"f'Total food expenses: ${total_food:.2f}')    

    




