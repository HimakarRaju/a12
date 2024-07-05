# in keyword in action
# in keyword is used to check if a value is present in a sequence
# it returns true if the value is present in the sequence and false if not
# it is used with if statement
# it is also used with for loop to iterate over a sequence
# it is also used with while loop to iterate over a sequence
# it is also used with try except block to catch errors


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(3 in my_list)
print(10 in my_list)

my_str = "Hello World"
print('Hello' in my_str)

cities = ('pune', 'mumbai', 'bengaluru', 'delhi')
print('delhi' in cities)

cities = {'pune', 'mumbai', 'bengaluru', 'delhi'}

print('mumbai' in cities)


for i in range(5):
    print(i)

text = "Hello"
for i in text:
    print(i)


my_dict = {'name': 'saynam', 'age': 30, 'city': 'pune'}
for key in my_dict:
    print(key, my_dict[key])
