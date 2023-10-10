username = input("Enter your username: ")

# if 3 <= len(username) <= 15 and '!' or '@'not in username:
#     print("Username is valid")
# else:
#     print("Please, enter a username from 3 to 15 characters and don't use '!' or '@'")

if not(3 <= len(username) <= 15) or ('!' in username or '@' in username ):
    print("Please, enter a username from 3 to 15 characters and don't use ! or @")
    print("Please, enter username from 3 to 15 characters and don't use ! or @")
else:
    print("Username is valid")