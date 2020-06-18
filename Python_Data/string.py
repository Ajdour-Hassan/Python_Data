#String 

name = "hassan"
age = 23

#Concantante
print("my name is :  " + name + " my age is : " + str(age))

print("my name is " , name , "my age is : " , age)

#Formatting
#Argument by Positions
print("my name is {name} , and I am {age} ".format(name=name , age=age))


#(F-String , it works only in python 3.6+)

print(f'hello , my name is {name} , and I am : {age}')

#String  Method :

#Captilalizing String
n = "hassan"
print(n.capitalize())

#Make uppercase
print(n.upper())

#Make lowercase
print(n.lower())

#Make swapcase
print(n.swapcase())

#Get length => calculate the amount of caracters in the string
print(len(n))

#Replace  => the element inside string
print(n.replace("hello" , "world"))

# count 
has = "Get"
print(n.count(has))

#Starts with  => True or false

print(n.startswith('hey'))

#ends with =>  true or false
print(n.endswith('n'))

#splite
print(n.split())

#find position
print(n.find('n'))

# is all alphunomic
print(n.isalnum())

# is all alphabetic
print(n.isalpha())

# is all numeric
print(n.isnumeric())

