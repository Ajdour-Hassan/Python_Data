
colors = ["orange" , "green" , "red" , "black"]
# for loop s with break
for x in colors:
  if x == "orange":
    print(f" current colors that are availabe: {x}")
  break

# for loop s with Continue
for x in colors:
   if x == "orange":
     continue
   print(f" current colors that are availabe: {x}")


# Range
for i in range(len(colors)):
    print(colors[i])
    

# Rnge numbers
for i in range(0, 8):
   print(f'number : {i}')


# While loops
count = 0
while count <= 5 :
  print(f'count {count}')
  count += 1
  

