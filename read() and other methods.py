
#  Readline method():-

f = open("textfile2.txt","r")
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break 
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in Math is : {m1}")
    print(f"Marks of student {i} in Science is : {m2}")
    print(f"Marks of student {i} in English is : {m3}")


#  Writelines method() :-

f = open("textfile2.txt",'w')
lines = ["line1\n","line2\n","line3\n"]
f.writelines(lines)
f.close()

# If you want add new line with for loop :-

f = open("textfile2.txt",'w')
lines = ["line4","line5","line6"]
for line in lines:
    f.write(line + '\n')
f.close()