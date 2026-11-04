while True:
    answer = input("Enter a positive integer: ")
    if answer.isdigit():
        number = int(answer)
        if number > 0:
            print(f"Got it: {number}")
            break
    else: 
        print("That's not a positve integer. Try again.")