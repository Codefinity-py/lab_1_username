# не зміню наступну строку
username = input("Enter your username: ")

# пиши свій код починаючи з 5 строчки ->
if len(username)<3 or len(username)>15 or '!' in username or '@' in username:
    print("Please, enter username from 3 to 15 characters and don't use ! or @")
else:
    print("Username is valid")