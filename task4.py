#Задача 4


def input_num():
    """Запрашивает у пользователя числа до тех пор, пока
    он не введёт отрицательное число."""

    a = int(input("Введите число (например: 3, -56, -7): "))
    # sum = a

    while a > 0:
        # print(f"Число {a} не отрицательное!")
        a = int(input("Внимание! Введите отрицательное число (например: -3, -56, -7): "))
        if a < 0:
            print("Вы ввели отрицательное число: ")

    
    # if a < 0:
    #     print("Вы ввели отрицательное число: ")
    #     sum += a
    # print((f"Сумма введеных положительных чисел равна: {sum}"))


enter_numbers = input_num()
print(input_num())