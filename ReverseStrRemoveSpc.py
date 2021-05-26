# Reverse every other word in a string and Remove special characters
#    Input: hi how are you!
#    Output: hi woh are uoy

input_value = 'hi how are you!'
str1 = ''.join([i for i in input_value if i.isalpha() or i.isspace()])
list1 = str1.split(' ')
str2 = ''
for i in range(len(list1)):
    if i % 2 != 0:
        str2 = str2 + str(list1[i])[::-1] + ' '
    else:
        str2 = str2 + list1[i] + ' '
print(str2)
