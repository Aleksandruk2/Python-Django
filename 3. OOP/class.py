class Student:
    def __init__(self, name):
        self.name = name # name - public
        #  Це просто позначення. Доступ із зовні є
        self._age = 18 # protected для зберігання віку
        self.__friend = "Салоїд"

    def __str__(self):
        return f"---{self.name}---"
    def getFriend(self):
        return self.__friend

ivan = Student("Марко Рижий")
print(ivan.name)
print(ivan)
print(ivan._age)
print(ivan._Student__friend)
print(ivan.getFriend())
