def my_view_message(msg):
    message = msg[0:9] # локальна зміна
    def private_fun():
        print(message)
    return private_fun

closure = my_view_message("Сало - це круто")
closure() # Викликаємо вказівник на метод, який є всередині