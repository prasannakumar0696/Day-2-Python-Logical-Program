# Find Highest scoring letter in a given string. you have to count total occurrences of each letter and return the
# highest scoring letter.
# If more than one letter scores the same, return the letter that appears earliest in the original string.
# Input: hi hello
# Output: h, total score 2

def remove_spc_char(string):
    return ''.join([j for j in string if j.isalpha() or j.isspace()])


input_value = 'hi how are you!!!'
input_value = remove_spc_char(input_value)
s1 = set(input_value.replace(' ', ''))
dict1 = {}
for i in sorted(s1):
    dict1[i] = input_value.count(i)
print(max(dict1, key=dict1.get), ', total score', dict1[max(dict1, key=dict1.get)])
