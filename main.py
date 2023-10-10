# не зміню наступну строку
username = input ()

# пиши свій код починаючи з 5 строчки ->
if len(username) >= 3 and len(username) <= 15  and '!' not in username and '@' not in username:
    print("Username is valid")

else :
    print ("Please, enter username from 3 to 15 characters and don't use ! or @")