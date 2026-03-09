# print("--- Завдання 1 ---")
# basketball_players = {
#     "Michael Jordan": 198,
#     "LeBron James": 206,
#     "Kobe Bryant": 198,
#     "Shaquille O'Neal": 216,
#     "Kevin Durant": 211,
#     "Stephen Curry": 188,
#     "Giannis Antetokounmpo": 211,
#     "Luka Dončić": 201,
#     "Dirk Nowitzki": 213,
#     "Magic Johnson": 206
# }

# def showMenu():
#     print("MENU:")
#     print("1. Додати")
#     print("2. Видалити")
#     print("3. Пошук за введеними символами")
#     print("4. Змінити значення.")
#     print("5. Показати список значень")
#     print("6. MENU")
#     print("0. EXIT")

# def add():
#     fullName = input("Введіть ПІБ: ")
#     height = input("Введіть зріст: ")
#     basketball_players[fullName] = height
#     print(f"Додавання {fullName} - {basketball_players[fullName]} пройшоло успішно")

# def remove():
#     fullName = input("Введіть ПІБ: ")
#     del basketball_players[fullName]
#     print(f"Видалення пройшоло успішно")

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searchedPlayers = {}
#     for key in basketball_players:
#         if search.lower() in key.lower():
#             searchedPlayers[key] = basketball_players[key]
#     return searchedPlayers

# def edit():
#     key = input("Введіть ПІБ: ")
#     resp = input("Введіть нове значення(зріст): ")
#     basketball_players[key] = resp
#     print(f"Редагуваня {key} - {basketball_players[resp]} пройшоло успішно")

# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         add()
#     elif resp == "2":
#         try:
#             remove()
#         except KeyError:
#             print("Такого гравця немає")
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         print(edit())
#     elif resp == "5":
#         print(basketball_players)
#     elif resp == "6":
#         showMenu()

# print("Exit...")


# print("--- Завдання 2 ---")
# eng_fr = {
#     "hello": "bonjour",
#     "goodbye": "au revoir",
#     "please": "s'il vous plaît",
#     "thank you": "merci",
#     "yes": "oui",
#     "no": "non",
#     "friend": "ami",
#     "family": "famille",
#     "food": "nourriture",
#     "water": "eau",
#     "house": "maison",
#     "car": "voiture",
#     "book": "livre",
#     "school": "école",
#     "city": "ville"
# }

# def showMenu():
#     print("MENU: Англо - Французький словник")
#     print("1. Додати")
#     print("2. Видалити")
#     print("3. Пошук за введеними символами")
#     print("4. Змінити значення.")
#     print("5. Показати список значень")
#     print("6. MENU")
#     print("0. EXIT")

# def add():
#     key = input("Введіть Англ. слово: ")
#     resp = input("Введіть Французький переклад: ")
#     eng_fr[key] = resp
#     print(f"Додавання {key} - {eng_fr[key]} пройшоло успішно")

# def remove():
#     key = input("Введіть Англ. слово: ")
#     del eng_fr[key]
#     print(f"Видалення пройшоло успішно")

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searched = {}
#     for key in eng_fr:
#         if search.lower() in key.lower():
#             searched[key] = eng_fr[key]
#     return searched

# def edit():
#     key = input("Введіть Англ. слово: ")
#     resp = input("Введіть Французький переклад: ")
#     eng_fr[key] = resp
#     print(f"Редагуваня {key} - {eng_fr[key]} пройшоло успішно")

# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         add()
#     elif resp == "2":
#         try:
#             remove()
#         except KeyError:
#             print("Такого слова немає")
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         edit()
#     elif resp == "5":
#         print(eng_fr)
#     elif resp == "6":
#         showMenu()

# print("Exit...")


# print("--- Завдання 3 ---")
# employees = {
#     "Іван Петренко": {
#         "phone": "+380501234567",
#         "email": "petrenko@company.com",
#         "position": "Backend Developer",
#         "office": 101,
#         "skype": "ivan.petrenko"
#     },
#     "Олена Ковальчук": {
#         "phone": "+380671112233",
#         "email": "kovalchuk@company.com",
#         "position": "Project Manager",
#         "office": 205,
#         "skype": "olena.kovalchuk"
#     },
#     "Андрій Шевченко": {
#         "phone": "+380931234321",
#         "email": "shevchenko@company.com",
#         "position": "QA Engineer",
#         "office": 310,
#         "skype": "andrii.shevchenko"
#     },
#     "Марія Бондар": {
#         "phone": "+380661234987",
#         "email": "bondar@company.com",
#         "position": "UI/UX Designer",
#         "office": 118,
#         "skype": "maria.bondar"
#     }
# }

# def showMenu():
#     print("MENU: Фірма")
#     print("1. Додати")
#     print("2. Видалити")
#     print("3. Пошук за введеними символами")
#     print("4. Змінити значення.")
#     print("5. Показати список значень")
#     print("6. MENU")
#     print("0. EXIT")

# def add():
#     key = input("Введіть ПІБ працвника: ")
#     tempDict = {}
#     phone = input("Введіть телефон: ")
#     email = input("Введіть електрону пошту: ")
#     position = input("Введіть посаду: ")
#     office = input("Введіть номер офісу: ")
#     skype = input("Введіть skype: ")
#     tempDict["phone"] = phone
#     tempDict["email"] = email
#     tempDict["position"] = position
#     tempDict["office"] = office
#     tempDict["skype"] = skype
#     employees[key] = tempDict
#     print(f"Додавання {key} - {employees[key]} пройшоло успішно")

# def remove():
#     key = input("Введіть ПІБ працвника: ")
#     del employees[key]
#     print(f"Видалення пройшоло успішно")

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searched = {}
#     for key in employees:
#         if search.lower() in key.lower():
#             searched[key] = employees[key]
#     return searched

# def edit():
#     key = input("Введіть ПІБ працвника: ")
#     tempDict = {}
#     phone = input("Введіть телефон: ")
#     email = input("Введіть електрону пошту: ")
#     position = input("Введіть посаду: ")
#     office = input("Введіть номер офісу: ")
#     skype = input("Введіть skype: ")
#     tempDict["phone"] = phone
#     tempDict["email"] = email
#     tempDict["position"] = position
#     tempDict["office"] = office
#     tempDict["skype"] = skype
#     employees[key] = tempDict
#     print(f"Редагування {key} - {employees[key]} пройшоло успішно")
# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         add()
#     elif resp == "2":
#         try:
#             remove()
#         except KeyError:
#             print("Такого працівника немає")
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         edit()
#     elif resp == "5":
#         print(employees)
#     elif resp == "6":
#         showMenu()

# print("Exit...")


# print("--- Завдання 4 ---")
# books = {
#     "1984": {
#         "author": "George Orwell",
#         "genre": "Dystopian",
#         "year": 1949,
#         "pages": 328,
#         "publisher": "Secker & Warburg"
#     },
#     "The Hobbit": {
#         "author": "J.R.R. Tolkien",
#         "genre": "Fantasy",
#         "year": 1937,
#         "pages": 310,
#         "publisher": "George Allen & Unwin"
#     },
#     "To Kill a Mockingbird": {
#         "author": "Harper Lee",
#         "genre": "Novel",
#         "year": 1960,
#         "pages": 281,
#         "publisher": "J.B. Lippincott & Co."
#     },
#     "The Little Prince": {
#         "author": "Antoine de Saint-Exupéry",
#         "genre": "Fable",
#         "year": 1943,
#         "pages": 96,
#         "publisher": "Reynal & Hitchcock"
#     }
# }

# def showMenu():
#     print("MENU: Книжкова колекція")
#     print("1. Додати")
#     print("2. Видалити")
#     print("3. Пошук за введеними символами")
#     print("4. Змінити значення.")
#     print("5. Показати список значень")
#     print("6. MENU")
#     print("0. EXIT")

# def add():
#     key = input("Введіть назву книги: ")
#     tempDict = {}
#     author = input("Введіть автора: ")
#     genre = input("Введіть жанр: ")
#     year = input("Введіть рік видання: ")
#     pages = input("Введіть кількість сторінок: ")
#     publisher = input("Введіть видавництво: ")
#     tempDict["author"] = author
#     tempDict["genre"] = genre
#     tempDict["year"] = year
#     tempDict["pages"] = pages
#     tempDict["publisher"] = publisher
#     books[key] = tempDict
#     print(f"Додавання {key} - {books[key]} пройшоло успішно")

# def remove():
#     key = input("Введіть назву книги: ")
#     del books[key]
#     print(f"Видалення пройшоло успішно")

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searched = {}
#     for key in books:
#         if search.lower() in key.lower():
#             searched[key] = books[key]
#     return searched

# def edit():
#     key = input("Введіть назву книги: ")
#     tempDict = {}
#     author = input("Введіть автора: ")
#     genre = input("Введіть жанр: ")
#     year = input("Введіть рік видання: ")
#     pages = input("Введіть кількість сторінок: ")
#     publisher = input("Введіть видавництво: ")
#     tempDict["author"] = author
#     tempDict["genre"] = genre
#     tempDict["year"] = year
#     tempDict["pages"] = pages
#     tempDict["publisher"] = publisher
#     books[key] = tempDict
#     print(f"Додавання {key} - {books[key]} пройшоло успішно")
# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         add()
#     elif resp == "2":
#         try:
#             remove()
#         except KeyError:
#             print("Такогї книги немає")
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         edit()
#     elif resp == "5":
#         print(books)
#     elif resp == "6":
#         showMenu()

# print("Exit...")