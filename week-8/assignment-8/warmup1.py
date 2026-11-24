import math
while True:
    number = input("Enter any number. ")
    
    try:
        number = float(number)
        if not math.isfinite(number):
            raise ValueError
        break
    except ValueError:
        print("That is not a valid number. Please try again.") 
print(f'You entered {number}')            