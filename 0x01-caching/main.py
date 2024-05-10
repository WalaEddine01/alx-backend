#!/usr/bin/python3
""" 0-main """
my_dict = {'a': 1, 'b': 2, 'c': 3}

my_dict.pop(list(my_dict.keys())[-1])

print(my_dict)
