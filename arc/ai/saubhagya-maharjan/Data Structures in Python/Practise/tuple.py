marks = (10, 20, 30, 40, 50)  # Tuple of integers
print(marks)

fruits = ("apple", "banana", "cherry")   # Tuple of strings
print(fruits)
fruits[0] = "blueberry"  # This will raise a TypeError
print(fruits)

nested_tuple = (1, 2, ("a", "b"), (3, 4))
print(nested_tuple[2])  # Output: ('a', 'b')
print(nested_tuple[3][1])  # Output: 4

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
result = tuple1 + tuple2
print(result)  # Output: (1, 2, 3, 4, 5, 6)