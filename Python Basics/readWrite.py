#this is to open , close and read contents of a file
file = open('text.txt')

#print(file.read(8)) #read n number of characters by passing paramenter

#print(file.readline()) #prints single line by single line in realtime
#print(file.readline())

#file.close()

#NB: make sure to use only one of the read & readline methods at a time

#print line by line using the readline method

#line = file.readline()

#while line !='':
    #print(line)
    #line = file.readline()

#file.close()


#Difference between readline & readlines is that readlines stores the text in a list that you can iterate
# List = ['SALMA', 'WANJA', 'MBOGORI' , '25YRS']
for line in file.readlines():
    print(line)