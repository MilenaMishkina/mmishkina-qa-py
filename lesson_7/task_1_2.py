# task_1
my_list = []
for value in range(101):
    my_list.append(value)
print(my_list)

# task_2
element = len(my_list) - 1
while element > 50:
    del my_list[element]
    element -= 1

print(my_list)