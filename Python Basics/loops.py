greetings = "Good Morning"

if greetings == "Good Morning":
    print("Conditions Match and is fulfilled")
else:
    print("Loop conditions have not been met")

print("Salma is a very smart and hot gyal")

#For Loops

#print the list
obj = [1,3,5,7,9]

for i in obj:
    print(i)

#print the list in multiples of 2
for i in obj:
    print(i*2)

#Print the summation of the list
#range (i,j) -> i to j-1

summation = 0
for j in range(1,6):  #for(i=0; i<6; i++;)
    summation = summation + j
print(summation)

print("********************************")
#print a list while skpping some numbers
#print while adding 2 values

for k in range(1,10,2):
    print(k)

#print withount insicating the first index will print value index 0 until last value minus 1

print("********************************")
for l in range(10):
    print(l)