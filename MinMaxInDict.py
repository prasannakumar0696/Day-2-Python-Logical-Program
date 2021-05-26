# Write a program to get Max and Minimum value in a dict
#     Input : {'a':100, 'b':320, 'c':1223}
#     Output:
#       Max Value : 1223
#       Min Value : 100

dict1 = {'a': 2000, 'b': 32, 'c': 1223}
# scenario 1
minimum = min(dict1, key=dict1.get)
maximum = max(dict1, key=dict1.get)
print('Min Value : ', dict1[minimum], '\nMax Value : ', dict1[maximum])

# scenario 2
min_val, max_val = dict1['a'], dict1['a']
for i in dict1:
    if dict1[i] < min_val:
        min_val = dict1[i]
    if dict1[i] > max_val:
        max_val = dict1[i]

print('Min Value : ', min_val, '\nMax Value : ', max_val)