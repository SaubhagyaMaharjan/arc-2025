import pandas as pd
#create empty dictionary
data ={
"name":[],
"roll":[],
"address":[],
"age":[]
}

#Fill in 10 valid data samples in the dictionary asking from the user.
for i in range(10):
    print(f"Enter details of student:{i + 1}")
    name = input("Name:")
    roll = input("Roll:")
    address = input("Address:")
    age = int(input("Age:"))

    data['name'].append(name)
    data['roll'].append(roll)
    data['address'].append(address)
    data['age'].append(age)

#convert the dictionary to dataframe
dataframe = pd.DataFrame(data)

#add a new column to the dataframe called ‘category’
''' If the age is less than or equal to 15 then, category will be ‘Junior’, 
if its between 15 to 25(included), category will be ‘Mid’ and for the rest - category will be ‘Senior’
'''
def category(age):
    if age <= 15:
        return 'Junior'
    elif age > 15 and age < 25:
        return 'Mid'
    else:
        return 'Senior'

dataframe["category"] = dataframe['age'].apply(category)

# display dataframe
print(dataframe)

#average calculation
avg_age = dataframe['age'].mean()
print(f"Average age: {avg_age}")

#most frequent category
most_freq = dataframe['category'].mode()[0]
print(f"Most frequent Category is {most_freq}")



