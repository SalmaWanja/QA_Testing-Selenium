#Expectptions and Assertions are used to fails a text when a condition is not met

itemsCart = 0
#2 items will be added to the cart

if itemsCart != 2:
    #raise Exception('conditions have not been met')

    pass

assert(itemsCart == 0)

#try catch mechanism

try:
    with open('nofile.txt', 'r') as reader: #use text.txt for text to pass
        reader.read()

except:
    print('Error in try block')


try:
    with open('nofile.txt', 'r') as reader: #use text.txt for text to pass
        reader.read()

except Exception as e:
    print(e)

#finally is executes weather a test passes or fails
finally:
    print('cleaning up data')