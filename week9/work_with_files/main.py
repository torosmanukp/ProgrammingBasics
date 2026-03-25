with open("file.txt", "r", encoding="UTF-8") as file:
    print(file.read())

with open("teka/text2.txt", "r", encoding="UTF-8") as file:
    print(file.read())

with open("file.txt", "a", encoding="UTF-8") as file:
    file.write("Ivan")