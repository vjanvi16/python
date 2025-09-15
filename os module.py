
# OS Modules in python :-

import os

# if(not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(1,100):
#     os.mkdir(f"data/Day")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)