#Задача 2

def lists(list1, list2, list1_and_list2):
    """ Принимает два списка чисел и возвращает новый список,
     содержащий только общие элементы из обоих списков."""
    list1 = []
    count = int(input("Сколько чисел хотите ввести?: "))
    for i in range(0, count + 1):
        list1.append(i)
    print(f"Передали первый список: {list1}")

    list2 = []
    count = int(input("Сколько чисел хотите ввести?: "))
    for i in range(0, count + 1):
        list2.append(i)
    print(f"Передали второй список: {list2}")

    list1_and_list2 = list1 + list2
    import collections
    numbers = print(f"Список с общими элементами 1 и 2 списков: {[item for item, count in collections.Counter(list1_and_list2).items() if count > 1]}")

    return numbers


numbers1 = []
numbers2 = []
list_result = []

result = lists(numbers1, numbers2, list_result)
print(result)