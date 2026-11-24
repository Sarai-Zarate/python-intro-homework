numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    result = numerator / denominator 
except ZeroDivisionError:
    print("You can't divide by zero.")
else:
    print(f"{numerator} ÷ {denominator} = {result:.1f}")