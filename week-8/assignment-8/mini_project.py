import csv
import sys 

clean_data = []
skipped_data = []

try:
    with open("../data/messy_data.csv") as file:
        reader = csv.DictReader(file)
        for row_number, row in enumerate(reader, start=1):
            if None in row:
                skipped_data.append(f'Row {row_number}: extra column detected — skipped')
                continue
            try:
                name = row['name'].strip()
                category = row['category'].strip()
                amount = float(row['amount'])

                if not name or not category:
                    raise ValueError("Missing name or category") 
                
                clean_data.append({
                   "name": name,
                   "category": category,
                   "amount": amount,
                })

            except (KeyError, ValueError, TypeError) as error:
                skipped_data.append(f'Row {row_number}: {type(error).__name__} — {error}')
                
                   
except (FileNotFoundError, OSError) as e:
    print(f'Could not read file: {e}')
    sys.exit(1)

rows_attempted = len(clean_data) + len(skipped_data)

print("\n=== CSV Report ===")
print(f'Rows attempted: {rows_attempted}')
print(f'Rows parsed: {len(clean_data)}')
print(f'Rows skipped: {len(skipped_data)}')
print()

if skipped_data:
    print("Skipped rows:")
    for item in skipped_data:
        print(f'  {item}')
        
print()
if clean_data:
    print("Clean data:")  
    for entry in clean_data:
        print(f"  {entry['name']} | {entry['category']} | ${entry['amount']:.2f}") 
print()             