def get_count_char(str_):
    str_ = str_.lower()
    main_str_dict = {}
    for letter in str_:
        if letter.isalpha():
            if letter in main_str_dict:
                main_str_dict[letter] += 1
            else:
                main_str_dict[letter] = 1
    return main_str_dict  # TODO посчитать количество каждой буквы в строке в аргументе str_


def percentage_dict(dict_):
    sum_of_dict_values = sum(dict_.values())
    dict_.values()
    for symbol in dict_:
        dict_[symbol] = round(dict_.get(symbol)*100/sum_of_dict_values,1)
    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dict1_ = {}
for symbol in main_str:
    if symbol in dict1_:
        dict1_[symbol] += 1
    else:
        dict1_[symbol] = 1
print(get_count_char(main_str))
print("Словарь символов:", dict1_)
print("Новый словарь:", percentage_dict(dict1_))
