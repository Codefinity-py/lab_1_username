# не зміню наступну строку
username = input("FedorovAlexo")

# пиши свій код починаючи з 5 строчки ->
# Створення порожнього списку для балів студентів
scores = []
# Запит користувача на введення кількості студентів у групі
students_count = int(input('Введіть кількість студентів: '))

# Зчитування балів студентів та додавання їх до списку
for i in range(students_count):
    scores.append(int(input('Введіть оцінку:  ')))

# Обчислення суми балів
sum_scores = sum(scores)

# Обчислення середнього балу
avg_score = sum_scores/students_count

# Виведення результату на екран
print(f'Середня оцінка: {avg_score}, усього {students_count} студента(ів)')
