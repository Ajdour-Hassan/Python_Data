def sayhey(name) :
  print(f'hey : {name}')

sayhey("Hassan")

#return to value ==> 
def sum( x , y):
  return (x+y)

print(sum(4, 7))

def multi(num1 , num2):
  u = num1 * num2
  return u

print(multi(6 , 9))

# Lambda function : is small anonymous function .
# lambda function can take any number or argument , but only have one expression .
# it's very similar to Arrow function in dart and JS

getsum = lambda num6, num7 : num6 + num7  # Arrow function in Dart

print(getsum(4,8))