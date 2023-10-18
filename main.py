# не зміню наступну строку
#username = input("Enter your username: ")

# пиши username = input("Enter yor username: ")
username = input("Enter yor username: ")
if any(char in username for char in ["!", "@"] ):
    print("Please, enter username from 3 to 15 characters and don't use ! or @")
elif len(username) <= 15 and len(username) >= 3:
    print("Username is valid")
else:
    print("Please, enter username from 3 to 15 characters and don't use ! or @")
