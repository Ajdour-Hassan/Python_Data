# Json is commonly used with Data API ,
#  Here we can perse JSON in python dictionnary

import json

# create a simple json
userJson = '{"name":"hassan" , "age":"23" , "number":"5"}'

# Parse to Dic
user = json.loads(userJson)
print(user)
print(user['name'])

#let's Do opposite 
car = {'name': 'ford' , 'model': 2010 , 'price' : '1000£'}
carJson = json.dumps(car)

print(carJson)






