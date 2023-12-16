import random
import time


name=input("Enter your name : ")
print(f" Hello! {name.upper()}...")
time.sleep(1)
print("Welcome to Hangman game....")
time.sleep(1)
print("INSTRUCTIONS TO PLAY HANGMAN GAME")
time.sleep(1)
print("1.Guess the correct word that was choosen randomly")
print("2.You have 6 chances & for every wrong guess chances will reduce by 1")
print("3.When user word matches with choosen word You WIN")
print("4.Score will be your chances double")
score=0
play='yes'
while play.lower()=='yes':
    list_words=["red","onee","hundred","twenty"]
    choosen_word=random.choice(list_words)
    # print(choosen_word)
    choosen_word1=[]
    for char in choosen_word:
        choosen_word1.append(char)
    # print(choosen_word1)
    st=[]
    for i in range(len(choosen_word)):
        st.append("_")
    # print(st)
    chances=6
    chance=""
    while chances>0:
        user_guess=input("Enter your guess : ")
        flag=[]
        word_s=""
        print(user_guess)
        for i in range(len(choosen_word1)):
            if user_guess.lower()==choosen_word1[i].lower():
                st[i]=choosen_word1[i]
                flag.append(True)
            else:
                flag.append(False)
        count=flag.count(True)
        if count > 0:
            print("You have guessed correctly! you have {chances} chances")
            
        else:
            chances -= 1
        
            print("You have guessed incorrectly! you have {chances} chances ")
        print(st)
        for char in st:
            word_s+=char
        chance=chances
        if choosen_word.lower()==word_s.lower():
            print("You WON ! you have {chances} more")
            score = chances * 2
            print(f"Your Score was : {score} POINTS")
            chances=0
    if chance==0:
        print("YOU Lost !")
        score = chances*0
        print("Your score was {score} points....")
    play = input("Enter yes if you want to play no if you don't want to play : ")
if play.lower() == 'no':
    print("Thank you {name} for playing the HANGMAN......")
    print("Hope you liked it pretty WELL....")
    print("You have chosen to exit")