from random import randint
i=0
r=1
k=0
hand=[]
comhand =[]
sc=[]

def roll(r):
    i=0
    ndice = 0
    print("This is roll",r)
    
    while ndice>=0:
        hand.append(randint(1,6))
        comhand.append(randint(1,6))
        i+=1
        ndice = 4-i
    print("The computer rolled:", comhand)
    print("You rolled:", hand)


def rollagain(k):
    k=0
    print("Which dice do you want to throw again? (1,2,3,4 and or 5)")
    a=input("Your answer:")
    while len(a)>k:
        b=int(a[k])-1
        hand[b]=randint(1,6)
        k+=1
        
#def score():


def calc_score(hand):
    score=0
    unique = sorted(list(set(hand)))
    hand = sorted(hand)
    if len(unique)==1:
        score = 1
        print("5 of a kind")
    if len(unique)==2:
        if hand[3] == hand[1] == hand[2]:
            score= 2
            print("4 of a kind")
        else:
            score= 3
            print("Full house")
    if len(unique)==3:
        if hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
            score = 5
            print("3 of a kind")
        else: 
            score = 6
            print("double pair")
    if len(unique)==4:
        score = 7
        print("pair")
    if len(unique)==5:
        if hand == [1,2,3,4,5] or hand==[2,3,4,5,6]:
            score = 4
            print("Straight")
        else:
            score = 8
            print("Bust")
    sc.append(score)

def select(x):
    unique= set(x)
    x = sorted(x)
    b=[0,1,2,3,4]

    if len(unique) == 5:
        if x == [1,2,3,4,5] or x == [2,3,4,5,6]:
            print(1)
        else:
            x[0]=randint(1,6)
            print(x)
     
    if  len(unique)<5:
        l=0
        x.append(9)
        while l<5:
            if x[l]==x[l+1] or x[l]==x[l-1] :
                u=l
                b.remove(u)
            l+=1
        k=0
        while len(b)>k:
            x[int(b[k])]=randint(1,6)
            k+=1
        x.remove(9)
    print("Computer has: ", x)
    global comhand
    comhand = x


"""----Main loop-----"""
AnsFound = False
print("Welcome to Dice Poker! Beat the computer by getting the highest score.")
while AnsFound == False:
    while r == 1:
        roll(r)   
        rollagain(k)
        r+=1
    while r == 2:
        print("Round 2")
        select(comhand)
        print("You have ", hand)
        rollagain(k) 
        r+=1

    while r == 3:
        print("Round 3")

        select(comhand)
        print("You have ", hand)
        rollagain(k)
        
        r+=1
    while r==4:
        print("Round 4")
        
        print("The computer has a :")
        calc_score(comhand)
        print(comhand)
        print("You have a : ")
        calc_score(hand) 
        print(hand)   
        r+=1
        if sc[0]>sc[1]:
            print("You won!")
        if sc[0]<sc[1]:
            print("The computer won!")
        if sc[0]==sc[1]:
            p=0
            while comhand[p]==hand[p]:
                p+=1
            if comhand[p]<=hand[p]:
                print("You won!")
            if comhand[p]>=hand[p]:
                print("The computer won!")


            

    AnsFound = True

    


