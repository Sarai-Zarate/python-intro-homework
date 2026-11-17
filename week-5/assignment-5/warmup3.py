guests = ["Varun", "Sarai", "Tom", "Nancy", "Kyle"]
target_name = input("Enter a name to search for: ")
found = False

for i in range(len(guests)):
    if guests[i].lower() == target_name.lower():
        print(f'Found "{guests[i]}" at index {i} on the guest list.')
        found = True
        break

if not found:
    print(f'"{target_name}" was not found on the guest list.')