my_set = {1, 2, 3, 4, 5}
print(my_set)  # Output: {1, 2, 3, 4, 5}
print(type(my_set))

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

# Removing an element using remove()
my_set.remove(2)
print(my_set)

# Removing an element using discard()
my_set.discard(3)   # Attempting to remove a non-existing element using remove() (raises KeyError) but discard() doesn't raise any error
print(my_set)  # Output: {1, 4}



set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)  # alternatively, union_set = set1 | set2
print(f"Union set: {union_set}")

intersection_set = set1.intersection(set2)  # alternatively, intersection_set = set1 & set2
print(f"Intersection set: {intersection_set}")

difference_set = set1.difference(set2)  # alternatively, difference_set = set1 - set2
print(f"Difference set: {difference_set}")


# Removing Duplicates from a List
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set = set(my_list)
unique_list = list(my_set)
print(unique_list)  # Output: [1, 2, 3, 4, 5]


# Finding Common Elements in Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elmnt = set(list1).intersection(set(list2))
print(common_elmnt)  # Output: {4, 5}