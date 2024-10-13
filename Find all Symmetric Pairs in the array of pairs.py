'''# Initialize an empty list to store pairs
pairs = []

# Ask the user for the number of pairs
n = int(input("Enter the number of pairs: "))

# Take input for each pair
for i in range(n):
    pair_input = input(f"Enter pair {i+1} (format: x y): ")
    x, y = map(int, pair_input.split())  # Split input and convert to integers
    pairs.append((x, y))  # Add the pair to the list

print("\nInput pairs:", pairs)  # Display all input pairs

# Initialize an empty list to store symmetric pairs
symmetric_pairs = []

# Iterate through the list of pairs
for i in range(len(pairs)):
    first_element = pairs[i][0]
    second_element = pairs[i][1]
    
    # Print current pair
    print(f"\nChecking pair {i+1}: ({first_element}, {second_element})")
    
    # Look for the symmetric counterpart (second_element, first_element)
    for j in range(i + 1, len(pairs)):
        print(f"  Comparing with pair {j+1}: ({pairs[j][0]}, {pairs[j][1]})")
        if pairs[j][0] == second_element and pairs[j][1] == first_element:
            # If found, add both pairs as symmetric pairs
            print(f"  -> Symmetric pair found: ({first_element}, {second_element}) and ({second_element}, {first_element})")
            symmetric_pairs.append((first_element, second_element))
            symmetric_pairs.append((second_element, first_element))

# Print the final result
print("\nSymmetric Pairs:", symmetric_pairs)
#n=int(input())
# Input string
n ="(1, 2), (3, 5), (2, 1), (7, 9), (5, 3)"

# Initialize an empty list to store the pairs
l = []

# Initialize a temporary string to collect digits
temp = ""

# Iterate through each character in the input string
for char in n:
    if char.isdigit() or char == ',':
        temp += char
    elif char == ')':
        # When encountering a closing parenthesis, convert the collected digits to a tuple and add to the list
        if temp:
            # Split the temporary string into two parts (x and y) and convert them to integers
            x, y = map(int, temp.split(','))
            l.append((x, y))
            temp = ""  # Reset temp for the next pair

# Print the list of pairs
print(l)    
        
#print(n)
l=[]
for i in range(n):
    temp=[]
    for j in range(2):
        k=int(input())
        temp.append(k)
    l.append(temp)
print(l)
# Input string
n = input()

# Initialize an empty list to store the pairs
l = []

# Initialize a temporary string to collect digits
temp = ""

# Iterate through each character in the input string
for char in n:
    if char.isdigit() or char == ',':
        temp += char
    elif char == ')':
        # When encountering a closing parenthesis, convert the collected digits to a tuple and add to the list
        if temp:
            # Split the temporary string into two parts (x and y) and convert them to integers
            x, y = map(int, temp.split(','))
            l.append((x, y))
            temp = ""  # Reset temp for the next pair

# Print the list of pairs
print(l)'''
num_list=[1,2,3,4,5]
a_list=math.prod(num_list)
print(a)

