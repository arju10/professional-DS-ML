# performing union, intersection and symmetric difference with three sets

# Create Stes
set1 = {1,2,3,4,5,6}
set2 = {345,3,4,5,6,7}
set3 = {4,65,3,6,8,7}

# Performing set operations
union_result = set1 | set2 | set3
intersecion_result = set1 & set2 & set3
symmetric_difference_result = set1 ^ set2 ^ set3

print("Uniof of Sets : ",union_result)
print("Intersection of sets: ", intersecion_result)
print("Symmetric Difference of Sets: ", symmetric_difference_result)