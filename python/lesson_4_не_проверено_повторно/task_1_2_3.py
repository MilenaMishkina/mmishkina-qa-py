# task_1
numbers = [1, 2, 3, 4, 5]
print(numbers[2])
numbers.append(10)
numbers.pop(1)
print(numbers)

# task_2

fruits = ['apple', 'banana', 'orange']
combined = numbers + fruits
len_of_combined = len(combined)
print(combined[-1])
slice_of_combined = combined[1:4]

# task_3

combined_copy = combined[:]
combined_copy.insert(0, 'яблоко')
print(combined)
print(combined_copy)