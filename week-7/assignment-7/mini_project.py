# Print today's date
from datetime import datetime
current_date = datetime.now()
readable_date = current_date.strftime("%B %d, %Y")
print(f"Today is {readable_date}.")

# Does the file exist 
import os
import sys

path = "../data/expenses.csv"

if os.path.exists(path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
    sys.exit(1)
  

# Read data and return as dictionaries
import csv

with open(path, 'r') as file:
    reader = csv.DictReader(file)
    expenses_stored = []
    for row in reader:
        print(row['date'], row['category'], row['description'], row['amount'])

        # Convert the amount field to float for each row
        row['amount'] = float(row['amount'])
        expenses_stored.append(row)

# Filter the list to only rows where category is "Food"
category_food = []
for row in expenses_stored:
    if row['category'] == 'Food':
        category_food.append(row)
        print(row)

#Calculate the total amount spent on Food (Accumulator)
total_food = 0
for row in expenses_stored:
    if row["category"] == "Food":
        total_food += row['amount']
print(f'Total: ${total_food:.2f}')

# Writing a txt food_report 
with open('food_report.txt', 'w') as file:
    file.write(f'Food Expense Report — generated {readable_date}')
    for row in category_food:
        file.write("\n"f'{row["date"]}: ${row["amount"]:.2f}')
    file.write("\n"f'Total: ${total_food:.2f}')    






