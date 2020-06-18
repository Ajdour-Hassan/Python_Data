# python has a functions for creating , deleting , updating ,reading files

# open a file
myfile = open('file.txt' , 'w')  # W means write/ create a file

# Get some info  about file

print('name: ' , myfile.name)
print('Is closed : ' , myfile.closed)
print('opening mode ' , myfile.mode)

# write into file
myfile.write('I love python ')
myfile.write(' and Dart ')
myfile.close()


# apped to file

myfile = open('file.txt','a') # a here means append/add to file
myfile.write('I also like react js')
myfile.close()

#Read in file
myfile = open('file.txt' , 'r+') # => r means read in a file
text = myfile.read()
print(text)

# delete in file  => d