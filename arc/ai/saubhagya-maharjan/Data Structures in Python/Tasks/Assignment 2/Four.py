#find greatest number
list = [10 , 30 , 40 , 60 , 80 ,-10, 50]
greatest = max(list)
print(f"The gratest number is {greatest}.")

#OR using loop

list = [10 , 30 , 40 , 60 , 80 ,-10, 50]

greatest = list[0]

for num in list:
    if num > greatest:
        greatest = num

print(f"Greatest number is {greatest}")
