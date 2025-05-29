x = 8
y = 5
c = x % y
print(x ** y)

print(x // y) # floor division gives quotient

print(c) #modulo operation gives reminder
print(type(c)) #check type of result

z = complex(x,y) # complex number
print(z)

a = complex(40,30)
b = complex(10,20)

print(a + b)

#Casting to integers

a = int(1)
b = int(2.8)
c = int("3")

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#Casting to string

a = str(1)
b = str(2.8)
c = str("3")

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

#Casting to float

a = float(1)
b = float(2.8)
c = float("3")

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

name = input("Enter your name: ")
print(name)
print(type(name))

age = input("Enter your age: ")
print(age)
print(type(age))
