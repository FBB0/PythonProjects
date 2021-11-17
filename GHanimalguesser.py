#Animal Guessing
import os

#EVALUATING QUESTIONS
i = 0           #variable for row that is being operated
k = 0           #list variable for new answers, corresponds to amount of Q's added
Yeslst = []     #List for new yes answers
Nolst = []      #List for new no answers

AnsFound = False
while AnsFound == False:
#READING FILE, make use of the animals.dat file in the github repository:
    f = open("animals.dat","r")
    lines = f.readlines()
    f.close
    table = []

    j = 0 #number of rows variable

    if j == 0:
        for line in lines:
            txt = line.lower()
            colomn = txt.split("--")

            Row = colomn[0].strip()
            Question = colomn[1].strip()
            IfYes = colomn[2].strip()
            IfNo = colomn[3].strip()

            table.append([Row, Question.capitalize(), IfYes, IfNo])
            j = j + 1

    if i == 0:
        print("Think of an animal, I will try to guess it!")
        dummy = input("Press enter to start")
        print(table[int(i)][1] + "? (Yes/No)")
    else:
        print(table[int(i)][1] + "? (Yes/No)")
    Answer = input()
    Answer = Answer.lower()
    
#EVALUATE ANSWER:
# Yes -- New Question    
    if Answer.startswith("y") == True and table[int(i)][2].isdigit() == True:
        i = int(table[int(i)][2]) #So that new loop starts at right question


# Yes -- Guess        
    elif Answer.startswith("y") == True and table[int(i)][2].isdigit() == False:
        print("I think I know it!","\nIs it a", table[int(i)][2]+ "?")
        FinalAns = input()
        FinalAns = FinalAns.lower()
        if FinalAns.startswith("y") == True:
            print("Yay!")
            AnsFound = True
    #NEW QUESTION:
        else:
            print("What was the correct animal?")
            CorAns = input()
            CorAns = CorAns.lower()
            print("Give a yes/no question to distinguish a(n)" + CorAns+ "from a(n)"+table[int(i)][2],":")
            YNQ = input()
            YNQ = YNQ.capitalize()
            YNQ = YNQ.replace("?","") #To avoid there be double question marks
            print("What is the answer to this question? (Yes/No)")
            YN = input()
            YN = YN.lower()
            WroAns = table[int(i)][2]

            if YN.startswith("y") == True:
                Nolst.append(WroAns) #Because "IfNoNew = WroAns" doesn't work
                Yeslst.append(CorAns)
            elif YN.startswith("n") == True:
                Yeslst.append(WroAns)
                Nolst.append(CorAns)

            IfNoNew = Nolst[k]
            IfYesNew = Yeslst[k]
            k = k+1
            table.append([j,YNQ, IfYesNew, IfNoNew])
            table[int(i)][2] = j #Make sure previous question's answer is updated
            j = j + 1
            print(table)

    #WRITING TO FILE:
            Exist = os.path.exists("animals.dat")   
            g = open("animals.dat","w")
            l=0
            while l<=j-1:
                print(table[l][0],"--", table[l][1],"--",table[l][2],\
                      "--", table[l][3], file = g)
                l = l + 1
            g.close()
            i = 0
      
#No -- New Question            
    elif Answer.startswith("n") == True and table[int(i)][3].isdigit() == True:
        i = int(table[int(i)][3]) #So that new loop starts at right question
#No -- Guess
    elif Answer.startswith("n") == True and table[int(i)][3].isdigit() == False:
        print("I think I know it!","\nIs it a", table[int(i)][3]+ "? (Yes/No)")
        FinalAns = input()
        FinalAns = FinalAns.lower()
        if FinalAns.startswith("y") == True:
            print("Yay!")
            AnsFound = True
    #NEW QUESTION:
        else:
            print("What was the correct animal?")
            CorAns = input()
            CorAns = CorAns.lower()
            print("Give a yes/no question to distinguish " + CorAns, "from",\
                  table[int(i)][3],":")
            YNQ = input()
            YNQ = YNQ.capitalize()
            YNQ = YNQ.replace("?","") #To avoid there be double question marks
            print("What is the answer to this question? (Yes/No)")
            YN = input()
            YN = YN.lower()
            WroAns = table[int(i)][3]
            if YN.startswith("y") == True:
                Nolst.append(WroAns)
                Yeslst.append(CorAns)
            elif YN.startswith("n") == True:
                Yeslst.append(WroAns)
                Nolst.append(CorAns)
            IfNoNew = Nolst[k]
            IfYesNew = Yeslst[k]
            k = k+1
            table.append([j,YNQ, IfYesNew, IfNoNew])
            table[int(i)][3] = j #Make sure previous question's answer is updated
            j = j + 1
            print(table)
    #WRITING TO FILE:
            Exist = os.path.exists("animals.dat")   
            g = open("animals.dat","w")
            l=0
            while l<=j-1:
                print(table[l][0],"--", table[l][1],"--",table[l][2],\
                      "--", table[l][3], file = g)
                l = l + 1
            g.close()
            i = 0