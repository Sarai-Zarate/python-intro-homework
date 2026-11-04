numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
                swapped = True
    return data


while True:
    print("=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        smallest = numbers[0]
        for num in numbers:
            if num < smallest:
                smallest = num
        print(f"The minimum is {smallest}.")

    elif choice == "2":
        largest = numbers[0]
        for num in numbers:
            if num > largest:
                largest = num
        print(f"The maximum is {largest}.")

    elif choice == "3":
        target = input("Enter a number to search for: ")
        if target.isdigit():
            target = int(target)
            found = False
            for i in range(len(numbers)):
                if numbers[i] == target:
                    print(f"Found {target} at index {i}.")
                    found = True
                    break
            if not found:
                print(f"{target} was not found in the list.")
        else:
            print("Please enter a whole number.")

    elif choice == "4":
        bubble_sort(numbers)
        print(numbers)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Please choose 1 to 5.")