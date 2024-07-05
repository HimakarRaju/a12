def find_max_element(my_list):
    if len(my_list) == 0:
        return None
    max_value = my_list[0]
    for i in my_list:
        if i > max_value:
            max_value = i
    return max_value


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(find_max_element(my_list))
