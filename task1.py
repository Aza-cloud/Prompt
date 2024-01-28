# Задача 1


def even_numbers(list1):
    """Принимает список чисел и возвращает новый список, содержащий только
    четные числа из исходного списка."""
    evens = []
    for num in list1:
        if (num % 2 == 0):
            evens.append(num)
    return evens

list1 = []
count = int(input("Сколько чисел хотите ввести?: "))
for i in range(0, count+1):
    list1.append(i)
print(f"Передали список: {list1}")

print(f"Получили список: {even_numbers(list1)}")
