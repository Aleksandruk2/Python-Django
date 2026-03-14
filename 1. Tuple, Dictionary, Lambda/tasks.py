# Завдання 1.
# Користувач вводить з клавіатури назву фрукта. Виведіть на екран кількість фруктів, що містяться в кортежі як елемент.
# print("--- Завдання 1 ---")
# fruitsTuple = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
# respond = input("Введіть назву фрукта: ")
# fruitCount = 0
# for fruit in fruitsTuple:
#     if respond == fruit:
#         fruitCount += 1
# print(f"Кількість {respond} = {fruitCount}")


# Завдання 2
# Додайте до першого завдання підрахунок кількості, коли назва фрукта є частиною елемента. Наприклад, «banana, apple, bananamango, mango, strawberry-banana».
# print("--- Завдання 2 ---")
# fruitsTuple = ("banana", "apple", "bananamango", "mango", "strawberry-banana")
# respond = input("Введіть назву фрукта: ")
# fruitCount = 0
# for fruit in fruitsTuple:
#     if respond in fruit:
#         fruitCount += 1
# print(f"Кількість {respond} = {fruitCount}")


# Завдання 3
# Маємо кортеж з назвами автовиробників (назва виробника може зустрічатися від 0 до N разів). Користувач вводить з клавіатури назву виробника та слово для заміни. Замініть в кортежі усі елементи з цією назвою на слово для заміни. Збіг за назвою має бути повним.
# print("--- Завдання 3 ---")
# cars = ["BMW", "Audi", "Toyota", "BMW", "Ford", "BMW"]
# print(f"Виробники: {cars}")
# respondOldCar = input("Введіть виробника: ")
# respondNewCar = input("Введіть слово для заміни: ")
# for i in range(len(cars)):
#     if cars[i] == respondOldCar:
#         cars[i] = respondNewCar
# carsTuple = tuple(cars)
# print("Кортеж із заміненими виробниками:")
# print(carsTuple)


# Завдання 4
# Маємо кортеж з цілими числами. Виведіть статистику за кількістю цифр в елементах кортежу. Наприклад:
# Одна цифра — 3 елементи;
# Дві цифри — 4 елементи;
# Три цифри — 5 елементів.
# print("--- Завдання 4 ---")
# numberTuple = (5, 12, 345, 7, 89, 42, 123, 4567)
# print(f"Кортеж чисел: {numberTuple}")
# one = 0
# two = 0
# three = 0
# four = 0

# for number in numberTuple:
#     if len(str(number)) == 1:
#         one += 1
#     elif len(str(number)) == 2:
#         two += 1
#     elif len(str(number)) == 3:
#         three += 1
#     elif len(str(number)) == 4:
#         four += 1

# print("Статистика за кількістю цифр:")
# print(f" • Одна цифра - {one} елементів")
# print(f" • Дві цифри - {two} елементів")
# print(f" • Три цифри - {three} елементів")
# print(f" • Чотири цифри - {four} елементів")


# Завдання 1 Частини 2 
# Маємо множину з назвами країн. Надайте користувачеві можливість:
# додавати країни;
# видаляти країни;
# пошуку країн за введеними символами;
# перевіряти, чи міститься країна в множині.
# print("--- Завдання 1 --- Частина 2 ---")
# countries = {"Ukraine", "France", "Germany"}

# def showMenu():
#     print("MENU:")
#     print("1. Додати країну")
#     print("2. Видалити країну")
#     print("3. Пошук країн за введеними символами")
#     print("4. Перевірити, чи міститься країна в множині.")
#     print("5. MENU")
#     print("6. Показати список країн")
#     print("0. EXIT")

# def addCountry():
#     country = input("Введіть назву країни: ")
#     countries.add(country)

# def removeCountry():
#     country = input("Введіть назву країни: ")
#     countries.remove(country)

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searchedCountries = set()
#     for country in countries:
#         if search.lower() in country.lower():
#             searchedCountries.add(country)
#     return searchedCountries

# def isInCountries():
#     resp = input("Введіть назву країни: ")
#     if resp in countries:
#         return True
#     else:
#         return False

# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         addCountry()
#     elif resp == "2":
#         removeCountry()
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         print(isInCountries())
#     elif resp == "5":
#         showMenu()
#     elif resp == "6":
#         print(countries)

# print("Exit...")


# Задача 2 Частини 2
# Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які є в обох множинах.
# print("--- Завдання 2 --- Частина 2 ---")
# cities1 = {"Kyiv", "Lviv", "Odessa", "Dnipro"}
# cities2 = {"Lviv", "Kharkiv", "Kyiv", "Chernihiv"}

# commonCities = cities1 & cities2
# print("Міста, що повторюються в обох множинах", commonCities)


# Задача 3 Частина 2
# Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які містяться в першій множині, але відсутні у другій.
# print("--- Завдання 3 --- Частина 2 ---")
# cities1 = {"Kyiv", "Lviv", "Odessa", "Dnipro"}
# cities2 = {"Lviv", "Kharkiv", "Kyiv", "Chernihiv"}
# uniqueCities = cities1 - cities2
# print("Міста, що містяться в першій множині, але відсутні у другій:", uniqueCities)

# Задача 4 Частина 2
# Маємо дві множини з назвами міст. Створіть третю множину з тими назвами, які містяться в другій множині, але відсутні в першій.
# print("--- Завдання 4 --- Частина 2 ---")
# cities1 = {"Kyiv", "Lviv", "Odessa", "Dnipro"}
# cities2 = {"Lviv", "Kharkiv", "Kyiv", "Chernihiv"}
# uniqueCities = cities2 - cities1
# print("Міста, що містяться в другій множині, але відсутні в першій:", uniqueCities)

# Задача 5 Частини 2
# Маємо дві множини з назвами міст. Створіть третю множину з унікальними назвами для кожної множини.
# print("--- Завдання 5 --- Частина 2 ---")
# cities1 = {"Kyiv", "Lviv", "Odessa", "Dnipro"}
# cities2 = {"Lviv", "Kharkiv", "Kyiv", "Chernihiv"}
# uniqueCities = cities1 ^ cities2
# print("Міста, що є унікальними для обох множин:", uniqueCities)

# Задача 6 Частини 2
# У словнику зберігається набір пар: Назва країни -> Столиця. Реалізуйте функ­ціо­наль­ність за додаванням, видаленням, пошуком, заміною.
# print("--- Завдання 6 --- Частина 2 ---")
# countries = {
#     "Ukraine": "Kyiv",
#     "France": "Paris",
#     "Germany": "Berlin"
#     }

# def showMenu():
#     print("MENU:")
#     print("1. Додати країну")
#     print("2. Видалити країну")
#     print("3. Пошук країн за введеними символами")
#     print("4. Змінити значення країни.")
#     print("5. Показати список країн")
#     print("6. MENU")
#     print("0. EXIT")

# def addCountry():
#     country = input("Введіть назву країни: ")
#     city = input("Введіть назву столиці: ")
#     countries[country] = city

# def removeCountry():
#     country = input("Введіть назву країни: ")
#     del countries[country]

# def searchBySymbol():
#     search = input("Введіть пошуковий запит: ")
#     searchedCountries = {}
#     for key in countries:
#         if search.lower() in key.lower():
#             searchedCountries[key] = countries[key]
#     return searchedCountries

# def editCountry():
#     key = input("Введіть назву країни: ")
#     resp = input("Введіть нове значення: ")
#     countries[key] = resp
#     return countries[key]

# showMenu()

# exit = True
# while(exit):
#     resp = input("-- Введіть значення: ")
#     if resp == "0":
#         break
#     elif resp == "1":
#         addCountry()
#     elif resp == "2":
#         try:
#             removeCountry()
#         except KeyError:
#             print("Такої країни немає")
#     elif resp == "3":
#         print(searchBySymbol())
#     elif resp == "4":
#         print(editCountry())
#     elif resp == "5":
#         print(countries)
#     elif resp == "6":
#         showMenu()

# print("Exit...")