from random import sample


def get_random_password(n=8) -> str:  # TODO написать функцию генерации случайных паролей
    all_symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + list('abcdefghijklmnopqrstuvwxyz') + list('0123456789')
    list_symbol = sample(all_symbols, n)
    password = ''.join(list_symbol)
    return password


print(get_random_password())
