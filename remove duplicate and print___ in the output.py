# Input array (not necessarily sorted)
arr = [2, 1, 2, 3, 1, 3, 2]           

# Step 1: Sort the array
arr.sort()#1 2 3 

# Step 2: Initialize the write_index to store unique elements
write_index = 1  # Start from the second position

# Step 3: Iterate through the sorted array to remove duplicates
for i in range(1, len(arr)):
    if arr[i] != arr[i - 1]:  # If the current element is different from the previous one
        arr[write_index] = arr[i]  # Place the unique element at write_index
        write_index += 1  # Move the write_index forward

# Step 4: Fill the remaining positions with '_'
while write_index < len(arr):
    arr[write_index] = "_"
    write_index += 1

# Output the modified array
print(arr)
#print(arr[2])
