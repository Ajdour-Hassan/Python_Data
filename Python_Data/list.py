# list is like arrays => ordered and changable


 # create a list

numbers = [1, 2, 3, 4]
print(numbers[1])

# Use Constructure with list

numbers1 = list((1,2,3,4))

# get value 
fruits = ["apple" , "orange" , "banana" ,"melon" , "grapes"]
print(fruits[0])

#Change value =>  (ornage => water melon)
fruits [1] = "water melon"

#Get length
print(len(fruits))

#Append to list
fruits.append("mango")
print(fruits)

# Remove an item in the list
fruits.remove("grapes")
print(fruits)

# Insert position
fruits.insert(1, "strawberries")
print(fruits)

# remove with pop
fruits.pop(5)
print(fruits)

#reverse the list 
fruits.reverse()
print(fruits)

# Sort => from A  to Z
fruits.sort()
print(fruits)

# Reverse Sort
fruits.sort(reverse=True)
print(fruits)