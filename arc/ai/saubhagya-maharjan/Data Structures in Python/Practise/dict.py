# Creating non-empty dictionary
student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}

#Accesssing Values Using get() Method, When we use get() method, we can pass default value so that it will not raise any error even when the key is not present.
print(student.get("name"))
print(student.get("address", "Unknown"))
print(student.get("age"))
print(student.get("courses"))

del student['age']
print(f"student dictionary after deleting age: \n {student}")

  # pop() method removes the item with the specified key name and we can specify a default value
address = student.pop('address', "Not Found")
print(f"Student dictionary after deleting address: \n{student}")

student = {
    "name": "John",
    "age": 20,
    "courses": ["Math", "Science", "History"]
}

keys = student.keys()
print(keys)

values = student.values()
print(values)

items = student.items()
print(items)

for key, value in student.items():
    print(f"Key: {key}, Value: {value}")

# Looping through value only
for value in student.values():
    print(value)
