def sum_polynomials(poly1, poly2):
    """
    Функция принимает два списка коэффициентов многочлена в порядке убывания степеней переменной,
    возвращает список коэффициентов суммы многочленов.
    """
    result = []
    # определяем длину более длинного многочлена
    max_length = max(len(poly1), len(poly2))
    # дополняем списки коротких многочленов нулями до длины более длинного многочлена
    poly1 += [0] * (max_length - len(poly1))
    poly2 += [0] * (max_length - len(poly2))
    # складываем коэффициенты многочленов поэлементно
    for i in range(max_length):
        result.append(poly1[i] + poly2[i])
    return result

# открываем файлы и считываем данные
with open('n:/VS_Code_projects/Python/DZ/Seminar_4/file1.txt', 'r') as f1, open('n:/VS_Code_projects/Python/DZ/Seminar_4/file2.txt', 'r') as f2:
    # считываем коэффициенты многочленов в списки
    poly1 = [int(coeff) for coeff in f1.readline().strip().split()]
    poly2 = [int(coeff) for coeff in f2.readline().strip().split()]
    # находим сумму многочленов
    result = sum_polynomials(poly1, poly2)
    # выводим результат в консоль
    print(result)
