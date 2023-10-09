# не зміню наступну строку
username = input("Enter your username: ")

# пиши свій код починаючи з 5 строчки ->
def username_requirements(username):
   if len(username < 3 or len(username) > 15): return False
   if '!' in username or '@' in username: return False
   return True

if username_requirements(username):
   print("Username is valid") 
else:
   print("Please, enter username from 3 to 15 characters and don't use ! or @")