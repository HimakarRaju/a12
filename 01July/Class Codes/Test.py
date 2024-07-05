"""
write a function that takes a list and returns a dictionary
with each distinct element as the key and its frequency as the value
"""


def freq(lst):
    dictionary = {}
    for element in lst:
        if element in dictionary:
            dictionary[element] += 1
        else:
            dictionary[element] = 1
    return dictionary
