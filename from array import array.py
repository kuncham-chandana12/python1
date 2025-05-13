from array import array

# Create an array of integers
numbers = array('i', [10, 20, 30, 40, 50])

# Print the array
print("Array elements:", numbers)

# Access elements by index
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# Append a new element
numbers.append(60)
print("Array after appending:", numbers)

# Remove an element
numbers.remove(30)
print("Array after removing 30:", numbers)

# Iterate through the array
print("Iterating through the array:")
for num in numbers:
    print(num)