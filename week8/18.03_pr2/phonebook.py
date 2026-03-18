
phonebook = []

while True:
    command = input("Enter command (add/delete/search/show/exit):")
    if command == "exit":
        break
    elif command == "add":
        name = input("Enter name:")
        phone = input("Enter phone number:")
        phonebook.append({"name":name, "phone":phone})
    elif command == "delete":
        id = int(input("Enter the ID of the user to delete"))
        phonebook.pop(id)
    elif command == "search":
        name = input("Enter the name of the man of your dream")
        for person in phonebook:
            if person["name"] == name:
                print(f'User {person["name"]} - {person["phone"]}')
                break
        else:
            print("Person with such name is not found")
    elif command == "show":
        for i in range(len(phonebook)):
            print(phonebook[i]["name"], phonebook[i]["phone"])