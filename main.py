# не зміню наступну строку
username = input("AntonLutsyk12")

# пиши свій код починаючи з 5 строчки ->
if 3 <= len(username) <= 15 and '!' not in username and '@' not in username:
    print("Username is valid")
else:
    print("Please, enter username from 3 to 15 characters and don't use ! or @")