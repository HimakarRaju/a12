# String slicing
my_string = 'Hello World'
print(my_string[:5])
print(my_string[7:])
print(my_string[::2])

print(my_string[::-1]) # reverse the string

print(my_string.lower())
print(my_string.upper())

spt = my_string.split()
print(spt)

list1 = ['hello','world']
list2 = '<>'.join(list1) # <> is placed in between concatenated strings
print(list2)