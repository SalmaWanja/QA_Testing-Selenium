str = "salmambogori@gmail.com "
str1 = "Student trying to learn"
str2 = "salmambogori"

print(str[1]) #prints letters in position 1 i.e. a

print(str[0:5]) #prints part of the string - substring

print(str+str1) #string concatenation

print(str2 in str) #substring check

var = str.split(".") #spilt a string from a specific point
print(var)
print(var[0])

str4 = " Salma "
print(str4.strip())
print(str4.rstrip())
print(str4.lstrip())