
# Create a program capable of displaying questions to the user like KBC.
# Use List datatype to store the questions and their corrent answers.
# Display the final amount the person is taking home after playing the game.

questions = [
    ["Which language was used to create fb?","Python","French","JavaScript","Php","None",3],
    ["Which language was used to create YouTube?","Python","French","JavaScript","Php","None",1],
    ["Which language was used to create Wp ?","Python","French","JavaScript","Php","None",4]
    ]

levels = [1000,2000,4000,8000,20000,60000,120000,360000]

for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"{question[0]}")
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    reply = int(input("Enter your answer : "))
    if(reply == question[6]):
        print(f"Currect Answer, You have won Rs.{levels[i]}")
    else:
        print("Wrong Answer")
        break
        