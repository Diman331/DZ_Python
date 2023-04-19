def calculate_pi(accuracy):
    pi = 0
    for k in range(accuracy):
        pi += (1/pow(16, k)) * (4/(8*k+1) - 2/(8*k+4) - 1/(8*k+5) - 1/(8*k+6))
    return round(pi, accuracy)

while True:
    accuracy_str = input("Введите точность вывода (целое положительное число): ")
    if not accuracy_str.isdigit():
        print("Ошибка: точность должна быть целым положительным числом.")
        continue
    accuracy = int(accuracy_str)
    if accuracy < 1:
        print("Ошибка: точность должна быть положительным числом.")
        continue
    break

print("Значение числа π:", calculate_pi(accuracy))
