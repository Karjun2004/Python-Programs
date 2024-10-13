array1 = input().strip().split()  
array2 = input().strip().split()
a = [int(x) for x in array1]
b = [int(x) for x in array2]
is_subset = True
for x in a:
    if x not in b:
        is_subset = False
        break
if is_subset:
    print("array1 is a subset of array2")
else:
    print("array1 is not a subset of array2")


