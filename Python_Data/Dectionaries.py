# A Dictionary is a collections which is unordered , changeable and indexed , No duplicate member

#It's similar to Object In Dart programming language

# Create a Dictionary
Person = {
   "name" : 'hassan',
   "age" : '23',
   "height" : '1.89',
}
#print(Person, type(Person))

# We can USe also Constrauctor to creat a Dictionary

Person1 = dict(name="Sara" , age="20")
print(Person1, type(Person1))
print(Person1['name'])

# Access to evey single value in Dictionary
print(Person['age'])

#Another way!
print(Person.get('height'))

#ADD Key/value
Person ['phone'] = 'O628163681'
print(Person)

# Get item form Dictionary
print(Person.get('phone'))


# Get dict keys
print(Person.keys())

# Get dict Items
print(Person.items())

#Copy Dic
person2 = Person.copy()
person2 ['city'] = 'Sale'

# del item in Dictionary
#del(person2["age"])

# Or Use pop
#person2.pop('name')
#print(person2)

# clear
#Person.clear()

#length
print(len(Person))

# Create list of dictionary

Users = [
  {'name' : 'marta' , 'age' : 23},
  {'name' : 'meryam' , 'age' : 23},

]
#
#print(Users)

# let's print first item in primary dictionary on the list
print(Users[0]['name'])


