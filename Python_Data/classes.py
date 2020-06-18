
# Create class
class User :

 # create a constructor in
  def __init__(self, name , age , nationality):
    self.name = name
    self.age  = age
    self.nationality = nationality

# we call a method inside the class :
  def intro(self):
    return f'hello this is my name: {self.name}, and I am {self.age}'
  
  def birth(self):
   return self.age + 1
   # OR 
   #self.name += 1
 

# => main app()
# Init user object
item = User('hassan' , 35 , 'Morocco')
print(item.age)

# call a method
print(item.intro())

print(item.birth())
