contact={}
while True:
    team=input('Виберіть команду')
    if team=="add":
        name=input("Введіть ім'я")
        number=input("Введіть номер")
        contact[name]=number
        print("Контакт збережено")
    elif team=="delate":
        name=input("Введіть ім'я")
        if name in contact:
            del contact[name]
            print("Контакт видалено")
        else:
            print("Контакт не знайдено")
    elif team=="search":
        name=input("Введіть ім'я")
        if name in contact:
            print(contact[name])
        else:
            print("Non found")
    elif team=="show":
        for k, v in contact.items():
            print(f"{k}, {v}")
    elif team=="exit":
        break