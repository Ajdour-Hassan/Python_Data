class User :
#create a constructor inside the class
  def __init__(self, name , age , nationality):
    self.name = name
    self.age  = age
    self.nationality = nationality

# method we can call 
  def greeting(self):
    return f'my name is {self.name} , and I am {self.age} '


 # extends a class  => inhirate the class above!
class customer(User):

  def __init__(self, name , age , nationality) :
    self.name = name
    self.age  = age
    self.nationality = nationality
    # add an objetc to inherited class
    self.balance = 0
  
  def set_balance(self, balance):
    self.balance = balance
  
  def Getting(self):
    return f'my name is {self.name} , and I am {self.age} , my balance is {self.balance}'


items = customer('hassan' , 34 , 'morocco' )

#print(items.age)
#items.greeting()

#print(items.greeting())

print(items.Getting())

print(items.balance)
  
   
