# Marging two dictionaries and modifying values using dictionary comprehension.

# Create dictionaris
dic1 = {'a':1, 'b':2, 'c':3}
dic2 = {'b':4, 'c':5, 'd':6}

# Marging and modifying values
merged_dic = {key:dic1.get(key,0) + dic2.get(key, 0) for key in set(dic2) | set(dic2)}

print('Merged and Modified Dictionary :', merged_dic)