
# Excercise 2 :-

import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
hour = int(time.strftime('%H'))
hour = int(input("Enter the hour : "))
# print(timestamp)
# timestamp = int(time.strftime('%M'))
# print(timestamp)
# timestamp = int(time.strftime('%S'))
# print(timestamp)
print(hour)
if(hour>=0 and hour<12):
    print("Good morning Sir")
elif(hour>=12 and hour<17):
    print("Good Afternoon Sir")
elif(hour>=17 and hour<20):
    print("Good evening Sir")
elif(hour>=20 and hour<24):
    print("Good night Sir")
else:
    print("You entered invalid time.")
