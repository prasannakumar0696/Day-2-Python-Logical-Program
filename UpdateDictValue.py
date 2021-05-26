# Update same value to all the keys in the given dict
#    Input : {'a':10, 'b':20:, 'c':30}
#    Output : {'a':40, 'b':40, 'c':40}

dict1 = {'a': 10, 'b': 20, 'c': 30}
# scenario 1
# for i in dict1:
#     dict1[i] = 40
# print(dict1)

# scenario 2
dict2 = {i: 40 for i in dict1}
print(dict2)
