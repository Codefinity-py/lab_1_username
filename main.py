# не зміню наступну строку
username = input ()

# пиши свій код починаючи з 5 строчки ->
def validate_username(username):
    if 3 <= len(username) <= 15 and '!' not in username and '@' not in username:
        return True
    else:
        return False

# Приклад використання
username = input("Введіть username: ")

if validate_username(username):
    print("Введений username є допустимим.")
else:
    print("Введений username не відповідає вимогам.")
