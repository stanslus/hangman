import random

def randomWord():
    with open("sowpod.txt",'r') as f:
        wordList=f.read()
    word=random.choice(wordList)
    print(word)
randomWord()
