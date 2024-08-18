todo_list = []

def add_item(item):
    todo_list.append(item)
    print(f'Added "{item}" to the to-do list.')

def remove_item(item):
    if item in todo_list:
        todo_list.remove(item)
        print(f'Removed "{item}" from the to-do list.')
    else:
        print(f'Item "{item}" not found in the to-do list.')

while True:
    print("\nTo-Do List Menu:")
    print("1. Add item")
    print("2. Remove item")
    print("3. View to-do list")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        item = input("Enter the item to add: ")
        add_item(item)
    elif choice == '2':
        item = input("Enter the item to remove: ")
        remove_item(item)
    elif choice == '3':
        print("\nTo-Do List:")
        for i, item in enumerate(todo_list, start=1):
            print(f"{i}. {item}")
    elif choice == '4':
        break
    else:
        print("Invalid choice, please try again.")
