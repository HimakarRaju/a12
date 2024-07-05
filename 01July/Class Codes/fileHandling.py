# Opening and Closing the file
file = open('file1.txt', 'r')
# changes to file1 done here
file.close()

# reading the file
with open('file1.txt', 'r') as file:
    content = file.read()
    print(content)
file.close()

# write the file
with open('file1.txt', 'w') as file:
    file.write("This is my updated new text")

# Append the file
with open('file1.txt', 'a') as file:
    file.write("\nMore text in that file")
