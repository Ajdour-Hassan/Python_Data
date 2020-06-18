
# A Set is collection which is unordered and unindexed , No duplicate numbers!

# Create Set
Cars_Set = {"Bmw" , "Audi" , "Mercedes"}

# Check items in Set
print('Bmw' in Cars_Set)

#Add TO set
Cars_Set.add("hummer")
print(Cars_Set)

#ADD Duplicate => set does not allow to repeat the same item 
Cars_Set.add('Bmw')
print(Cars_Set)



#Remove on Set
Cars_Set.remove("Audi")
print(Cars_Set)

# Del set
#del Cars_Set
#print(Cars_Set)

#clear Set
Cars_Set.clear()
print(Cars_Set)

