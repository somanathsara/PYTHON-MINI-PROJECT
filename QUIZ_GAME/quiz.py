import json
import random,time
# with open("question.json","r")as file:
#     data = json.load(file)
while True:
    print("1.Start quiz")
    print("2.View High Score")
    print("3.Exit")
    choice = input("Enter your choice here: ")
    if choice == '1':
        score = 0
        start = time.time()
        print("1.Pyhton")
        print("2.Javascript")
        print("3.C")
        print("4.GK")
        category = input("Enter category here: ")
        if category == '1':
            with open("question/python.json","r")as file:
                data= json.load(file)
        elif category == '2':
            with open("question/javascript.json","r")as file:
                data= json.load(file)
        elif category == '3':
            with open("question/c.json","r")as file:
                data= json.load(file)
        elif category == '4':
            with open("question/gk.json","r")as file:
                data= json.load(file)
        for i in range(len(data)):
            print(f"Question {i+1} :")
            print("-"*20)
            print(data[i]["question"],end = "\n")
            random.shuffle(data[i]["options"])
            for j in range(4):
                print(chr(65+j),end = ". ")
                print(data[i]["options"][j],end = "\n")
            try:
                ans = input("Enter your answer (A/B/C/D)")
                if data[i]["options"][ord(ans.upper())-65] == data[i]["answer"]:   #ord is used for str to ascii
                    score += 1
                    print("Correct Answer.")
                else:
                    print("Wrong Answer !")
                    print(f"Correct Answer is {data[i]["answer"]}")
            except IndexError,TypeError:
                print("-"*25)
                print("Please give a valid answer")
                print("-"*25)
        end = time.time()
        elapsed = end - start
        print("-"*30)
        print("Quiz finished")
        print(f"Score : {score}")
        print(f"Correct answer: {score}")
        print(f"Wrong answer: {5-score}")
        print(f"Time required: {round(elapsed,2)}sec.")
        if score  < len(data)//2:
            print('Keep practicing.')
        elif(score > len(data)*90/100):
            print("Excellent!")
        elif(score > len(data)*70/100):
            print('Very Good')
        elif(score > len(data)*50/100):
            print("Good")
        print("-"*30)
        with open("highscore.json","r") as file:
            data = json.load(file)
        high_score = data["high_score"]
        if(score > high_score):
            print("New high score!")
            data["high_score"] = score
            with open("highscore.json","w")as file:
                json.dump(data, file, indent = 4)
                
    elif choice == '2':
        with open("highscore.json","r") as file:
            score = json.load(file)
        print("-"*25)
        print(f"High score : {score["high_score"]}")
        print("-"*25)
    elif choice == '3':
        exit()
    else:
        print("-"*25)
        print("Please enter valid option.")
        print("-"*25)