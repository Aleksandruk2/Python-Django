print("Робота із словниками (dictionaries)")
# У .NET словник називається Dictionary, у Python - dict
# Словник - це набір елементів - ключ значення. При цьому ключ не може повторюватися
student = {
    "name": "Іван Марков",
    "age": 20,
    "grade": 95 # стобальна система - 95 балів
}

print(student)

print(student["name"])
print(student.get("name"))

# Додавання елемента до словника
student["email"] = "ivan.markov@example.com"
print(student)

# Виделення елемента зі словника
del student["grade"]
print(student)

# Перебір елементів словника
for key in student:
    print(f"{key}: {student[key]}")