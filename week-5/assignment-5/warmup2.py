while True:
    answer = input("Enter a positive integer: ")
    if answer.isdigit() and int(answer) > 0:
        print(f"Got it: {answer}")
        break
    else:
        print("That's not a positive integer. Try again.")