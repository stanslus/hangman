import random
import multiprocessing as  mp #parallel programming

def load_wordList():
    word_list = None
    sowpod = 'sowpod.txt'

    with open(sowpod, 'r+') as f:
        #split the list into line
        word_list = f.read().split('\n')

     
    return word_list


def main():
    
    word_list = load_wordList()
    magic_word = random.choice(word_list).lower()

    print('welcome and guess letters of a word till a word is formed')
    print('Here is a clue, the word has the same length as these dashes:')
    print("_ "*len(magic_word))
    placeholder = "-"
    my_guess = [ placeholder for l in magic_word ] #my empty word
    #print(my_guess)
    error_count  = 0
    while True:
        guess = input("Guess a letter or type 'quit' to Quit: ")

        if guess == 'quit':
            break
        if guess in magic_word:
            for index, letter in enumerate(magic_word):
                if guess is letter:
                    print(letter, end='')
                    my_guess[index] = guess
                elif my_guess[index] is letter:
                    print(letter, end='')

                else:
                    print("-", end=' ')
            print()
        else:
            error_count += 1
            print(f'[{6-error_count}]: Incorrect!')
        if error_count == 6:
            print("Game Over!!!")
            break
        elif not ('-' in my_guess):
            print("Cograts !!!!!")
            break
            

    print("The magic word was: ",magic_word)
    print("Goodbye  (O^O) ")





if __name__ == '__main__':
    main()
