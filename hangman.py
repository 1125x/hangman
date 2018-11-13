import random

print("let's play hangman!") 
words=["hello","what","how","personalausweis"] #generieren einer Wortliste für das Spiel
handycap=7

z=random.randint(0,len(words)-1) #auswählen eines wortes aus dem array
word=words[z] 
print(word)
print(len(word))

letters=list(word)
    

print("the word you want to guess is: ")#erstelllen der Anzeige
i=0
score=[]
while i < len(word):
    score.append("_")
    i+=1
i=0
while i<len(score):
    print(score[i],end=" ")
    i+=1

while handycap>0:
    guess=input("What letter do you guess?")
    
    check=0
    lose=0

    z=0 
    while z<len(word):
        if letters[z]==guess:
            score[z]=guess
            z+=1

        else:
            z+=1
            check+=1

    if check==len(word):
        handycap-=1

    y=0
    while y<len(score):
            print(score[y],end=" ")
            y+=1

    if "_" not in score:
            print("")
            print("You won!")
            break   

print("You lost!")
print("The word you were looking for was " +word)
