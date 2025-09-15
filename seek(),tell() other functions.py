
# seek() function :-

with open('textfile.txt','r') as f :
    f.seek(10)       # Move to the 10th byte in the file.
    data = f.read(5)      # Read the next 5 bytes.
    print(data)


# tell() function :-

# The tell() function returns the current position within the file,in bytes.

with open('textfile.txt','r') as f:
    t = f.tell()
    print(t)


# truncate() function :-

# The truncate() function truncate the file to the specific size.

with open('textfile.txt','w') as f:
    f.write("Hello world!")
    f.truncate(5)

with open('textfile.txt','r') as f:
    print(f.read())