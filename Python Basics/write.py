#open and read the file
#reverse the contents
#print the reversed content

with open('text.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('text.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)