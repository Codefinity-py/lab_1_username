# не зміню наступну строку
username = input("Enter your username: ")

# пиши свій код починаючи з 5 строчки ->
    #перевірка на кількість символів
if len(username) >= 3 and len(username) <= 15:
    # Перевірка на відсутність символів '!' та '@'
    if '!' not in username and '@' not in username:
        print("Username is valid")
    else:
        print("Please, enter username from 3 to 15 characters and don't use ! or @")
else:
    print("Please, enter username from 3 to 15 characters and don't use ! or @")