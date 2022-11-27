from random import sample


def get_random_password(n=8) -> str:  # TODO написать функцию генерации случайных паролей
    all_symbols = list(string.ascii_uppercase) + list(string.ascii_lowercase) + list(string.digits)
    list_symbol = sample(all_symbols, n)
    password = ''.join(list_symbol)
    return password


print(get_random_password())
