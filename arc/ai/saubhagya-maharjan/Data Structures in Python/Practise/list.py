fruits = ["apple", "banana", "cherry", "date", "elderberry"]

#specifying step size
print(fruits[::2]) #[start:stop:step] Extracts elements from the start index up to, but not including, the stop index, with a specified step.
print(fruits[1:4:2])
print(fruits[::-1]) # Negative step size will reverse the list

fruits.insert(1, "strawberry") # insert() will add an element at the specified index
print("After inserting strawberry: ", fruits)

# pop() will remove an element from the list and return the removed element
fruit = fruits.pop(2)
print("Fruits after removing 2nd element: ", fruits) 

list1 = [1, 2, 3]
list2 = [4, 5, 6]
lst = list1 + list2
print(lst) 
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list1.extend(list2)
print(list1)
print(len(lst))

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements
print(nested_list[0][0])  # Output: 1
print(nested_list[1][2])  # Output: 6
print(nested_list[2][1])  # Output: 8

# Modifying elements
nested_list[0][1] = 20
nested_list[2][0] = 70
print(nested_list)