# Adding

# List
my_list = [1, 2, 3, 4, 5]
my_list.append(4)
print(my_list)

# Tuples- they are immutable

# Dict
my_dict = {'name': 'Saynam', 'Age': 30}
my_dict['city'] = 'pune'
print(my_dict)

# Sets
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# ===================================================================

# deleting

my_list = [1, 2, 3, 4, 5]
my_new_list = my_list.pop(3)
print(my_list)

# Extend
my_list.extend([5, 10, 4, 5, 6, 7, 8])
print(my_list)

# Tuples- no we dont do it

# Dict
my_dict = {'name': 'saynam', 'age': 30, 'city': 'pune'}
new_dict = my_dict.pop('age')

print(my_dict)

del my_dict['city']
print(my_dict)


# Sets
my_set = {1, 2, 3, 4, 5}
my_set.remove(3)
print(my_set)
