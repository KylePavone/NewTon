"""
    Есть список вещественных чисел и целое число. Необходимо написать функцию, которая будет искать в
     списке вещественное число, округление которого будет равно целому числу. Пример:

    float_number_search(float_number_list, int_number)
    =>
    float_number

"""

lst = [3.231, 2.67, 8.93, 12.56]


def float_number_search_2(float_number_list: list, int_number: int):
    try:
        data = [i for i in float_number_list if int(i) == int_number]
        return data[0]
    except IndexError as ex:
        return f"Not founded! {ex}"

print(float_number_search_2(lst, 12))
