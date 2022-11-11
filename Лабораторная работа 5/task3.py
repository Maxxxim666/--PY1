from random import randint


def get_unique_list_numbers() -> list[int]:  # TODO написать функцию для получения списка уникальных целых чисел
    list_numbers = []
    while len(list_numbers) < 15:
        rand_num = randint(-10, 10)
        if rand_num not in list_numbers:
            list_numbers.append(rand_num)

    return list_numbers


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
