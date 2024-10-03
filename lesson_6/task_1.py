student = {"name": "Milena", "age": 25, "subjects": ["Math", "Biology"], "average_score": 4.75}

student["subjects"].append("History")

student.pop("age")

if "age" in student:
    print("Ключ 'age' существует")
else:
    print("Ключа 'age' не существует")

if "gender" in student:
    print("Ключ 'gender' существует")
else:
    print("Ключа 'gender' не существует")

keys = student.keys()
print(keys)
values = student.values()
print(values)
