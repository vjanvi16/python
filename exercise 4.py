
st = input("Enter the message : ")
coding = int(input("1 for coding 0 for decoding : "))
True if(coding==1) else False

if(coding):
    if(len(st)>3):
        r1 = "akd"
        r2 = "yei"
        st = r1 + st[1:] + st[0] + r2
        print(st)
    else:
        print(st[::-1])

else:
    if(len(st)>3):
        st2 = st[3:-3] 
        st2 = st2[-1] + st2[:-1]
        print(st2)
    else:
        print(st[::-1])