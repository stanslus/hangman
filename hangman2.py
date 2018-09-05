import random
#making the variable word to be global
word='global'
def randomWord():
    with open("sowpod.txt",'r') as f:
        wordList=f.read()
    word=random.choice(wordList)
randomWord()
print('welcome to guess letters of a word till a word is formed')
print('_'*len(word))
while True:
    guess=input('guess a letter:' )
    guess.upper()
    for char in word:      
    # see if the character is in the players guess
        if char in guess:    
    
        # print then out the character
            print (char)    

        else:
    
        # if not found, print a dash
            print ("_",end="")     
            