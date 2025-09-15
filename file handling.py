
#  read (r) :
#  This mode opens the file for the reading only and gives an error if the file doesn't exist.
#  This is the defalt mode if no mode pass as a parameter .

#  write (w) :
#  This mode opens the file for writing only and create new file if file doesn't exits.

#  append (a) :
#  This mode opens the file for appending only and create new file if file doesn't exits.

#  create (x) :
#  This mode creates file and gives an error if the file already exits.

#  binary (b) :
#  Used to handle binary files (images,pdfs,etc.)


#  Opening a file :-

f = open('textfile.txt','r')
txt = f.read()
print(txt)
f.close()

#  Reading from file :-

f = open("textfile.txt")
txt = f.read()
print(txt)
f.close()


#  Writing to a file :-

f = open("textfile.txt","w")
f.write("Hello World!")
f.close()


#  Append to a file :-

f = open('textfile.txt','a')
f.write("\nHello World!")
# f.close()


#  The with statement :-

#  We don't need to close our file when we use with statment.

with open('textfile.txt','a') as f:
    f.write('Hey! I m Good boy')