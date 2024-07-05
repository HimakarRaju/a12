#LTD = List, Tuple, Dictionary

# For Updating
# Lists
my_list = [1, 2, 3, 4, 5, 6, 7]
my_list[1] = 10
print(my_list)

# Tuple
my_tuple = (1, 2, 3, 4, 5)
temp_tuple = my_tuple[:2] + (10,) + my_tuple[3:]
print(temp_tuple)

# Dict
my_dict = {'name': 'saynam', 'age': 20, 'city': 'pune'}
my_dict['age'] = 40
print(my_dict)

# Sets
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print(my_set)
my_set2 = {7, 8, 9}
my_set.update(my_set2)
print(my_set)
