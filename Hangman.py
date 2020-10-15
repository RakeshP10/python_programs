import random

def hangman_graphic(guesses):
    if guesses == 1:
        print( "              ")
        print( "              ")
        print( "              ")
        print( "              ")
        print( "|             ")
        print( "|             ")
    elif guesses == 2:
        print( "              ")
        print( "              ")
        print( "              ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
    elif guesses == 3:
        print( "              ")
        print( "              ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
    elif guesses == 4:
        print( "              ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
    elif guesses == 5:
        print( "________      ")
        print( "|      |      ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
    elif guesses == 6:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|             ")
        print( "|             ")
        print( "|             ")
    elif guesses == 7:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /       ")
        print( "|             ")
        print( "|             ")
    elif guesses == 8:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /       ")
        print( "|             ")
        print( "|             ")
    elif guesses == 9:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /|      ")
        print( "|             ")
        print( "|             ")
    elif guesses == 10:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /|\     ")
        print( "|             ")
        print( "|             ")
    elif guesses == 11:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /|\     ")
        print( "|     /       ")
        print( "|             ")
    else:
        print( "________      ")
        print( "|      |      ")
        print( "|      0      ")
        print( "|     /|\     ")
        print( "|     / \     ")
        print( "|             ")
        print("YOU LOST")
        print( "GAME OVER!")



words=['computer','cpu','monitor','mouse','laptop','keyboard','printer','scanner','pendrive','drive','floopy']

word = random.choice(words)

print(word)
l=len(word)
s=''
for i in range(l):
    s=s+'_'

i=1
f=0

print("Welcome to the game . Guess a correct word and savew your friend . \n")

while i<=12:
    hangman_graphic(i)
    c=input("Guess a character")
    if c in word:
        k=0
        s=list(s)
        for j in range(l):
            if word[k] == c:
                s[k]=c
            k+=1
        s = ''.join(s)
        s=str(s)
    print(s)

    if '_' not in s:
        f=1
        break
    i+=1
    print("\n\n\n")

if f==1:
    print('Hurray!!!!You Saved the hang Man!')
else:
    print('So Sad! you were unable to save the Hangman!!!!!!!!')
