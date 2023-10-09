# не зміню наступну строку
username = input()

# пиши свій код починаючи з 5 строчки ->
if 15 > len(username) > 3 and "@" not in username and "!" not in username: # перевіряю на довжину вводу символів та заборону знаків
 print("Username is valid")
else: 15 > len(username) > 3 and "@" is username and "!" is username # виводжу повідомлення про правильність введення даних, якщо порушені умови
print("Please, enter username from 3 to 15 characters and don't use ! or @")

