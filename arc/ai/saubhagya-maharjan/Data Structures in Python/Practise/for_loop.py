fruits = ['apple','mango','banana']

for fruit in fruits:
    print(fruit)

for char in 'hello':
    print(char)

# using range() function , generates a sequence of numbers
for i in range(5):
    print(i)

# specify Start, Stop and Step in range()
for i in range(1,10,2):
    print(i)

# Using enumerate()

for index, fruit in enumerate(fruits):
    print(f"Index:{index}:{fruit}")

# break Statement ,exits the loop prematurely.

for num in range(10):
    if num == 5:
        break
    print(num)

#continue Statement, skips the current iteration and moves to the next.
for num in range(10):
    if num == 5:
        continue
    print(num)

#Nested for Loops:You can use nested for loops to iterate over nested sequences, such as lists of lists.  

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
for sublist in nested_list:  
    for item in sublist:
        print(item)
    
    