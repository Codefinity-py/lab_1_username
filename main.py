# не зміню наступну строку
username = input("Enter your username: ")

# пиши свій код починаючи з 5 строчки ->
def is_valid_username(username):
    if len(username)<3 or len(username)>15 or '!' in username or '@' in username:
        return False
    else:
        return True

if is_valid_username(username):
    print("Username is valid")
else:
    print("Please, enter username from 3 to 15 characters and don't use ! or @")



