age = int(input("What is your age?"))

if age <= 12:
    print(f"Enter your age: {age} You are a Child.")
elif age <= 17:
    print(f"Enter your age: {age} You are a Teen.") 
elif age <= 64:
    print(f"Enter your age: {age} You are an Adult.")
else:
    print(f"Enter your age: {age} You are a Senior.")