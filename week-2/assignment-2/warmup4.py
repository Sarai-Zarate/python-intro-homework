dog_years = 7
dog_name = input("What is your dog's name? ")
dog_age = int(input("How old is your dog? "))

print(f'{dog_name} is {dog_age * 7}')

# Error Message: ValueError: Unknown format code 'f' for object of type 'str'
# What caused it: (input("How old is your dog? ") The input must be converted into a string
# How it was fixed: int(input("How old is your dog? ")) Ran the input through and int() function 