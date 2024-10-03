def nums_square(list_of_nums:list) -> list:
    """
    Фуункция, которая принимает список чисел и возвращает новый список,
    содержащий квадраты этих чисел
    функцию, которая принимает список чисел и возвращает новый список, содержащий квадраты этих чисел"""
    squared_list = []
    for num in list_of_nums:
        squared_list.append(num**2)
    return squared_list

test_list = [1, 2, 3]
nums_square(test_list)