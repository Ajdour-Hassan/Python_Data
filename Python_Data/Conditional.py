x = 10
y = 6
# conditions types ( == , > , < , >= , <= , != ) Compartion Opertion used to compare values

if(x == y ) :
  print('it is')
else :
  print('no')


# Logical opertion =>

if (x > y ):
   print(f'{x} is greater than {y}')
elif(x == y):
   print(f' {x} equals to {y}')
else:
   print(f'{x} is lower that {x} ')



   # Nested if Statment => if inside id


if x >= y:
   if x == 7:
     print('x is greater that 7')

# Logical opertion (and , or , Not )

if (x >= 9 or x == 10 ) :
  print( 'your mark is good')
else:
  print('your mark is not good')

# If Not

if not(y == x):
   print(f'{x} is not equals {y}')

# Membership Operator (is , is Not) -Check item in list
numbers = [1,2,3,4,5]
if 3 in numbers:
   print(3 in numbers)

# IF not in 
if 3 not in numbers:
   print(3 not in numbers)

# is or is not :
if x is y:
   print(x is y)

# is Not

if x is not y :
   print( x is not y)
