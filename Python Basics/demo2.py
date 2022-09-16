values = [3, 8, "puky", 89]

#list is like arrays but allows multiple values to be stored i.e both string and integers

print(values[0]) #positions of values in the string are numbered from 0,1,2...

print(values[-2]) #adding the minus will ask for the second last list item to be printed

print(values[0:3]) #this will print the values in the range minus one

values.insert(3, "mbogori") #this will insert mbogori in position 3

print(values)

values[0] = "Jenny" #updating values in the list

print(values)

del values[4] #deleting values in the list

print(values)

# Tuple is the same as list but immutable- mwaning cannot be updated and uses round brackets

val = (2, 6, "salamander", 79)

print(val)

#val[1] = "Vivian" # will bring an error cause update is not possible in tuples

#Dictionary

dic = {"a":4, 5:"Edward Mbogori", 7:"Karitas"}

print(dic[5])
print(dic["a"])