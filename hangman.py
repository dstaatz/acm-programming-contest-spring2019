# hangman.py



def main():
    
    word = input()

    letters_correct = []
    for letter in word:
        letters_correct.append(False)
    
    guesses = input()

    chances = 10

    for guess in guesses:
        found = False
        for i, letter in enumerate(word):
            if letter == guess:
                letters_correct[i] = True
                found = True
        
        if found == False:
            chances -= 1
            # print(guess, chances)

        if chances == 0:
            print("LOSE")
            # print(letters_correct)
            # print(chances)
            return

        if all(letters_correct):
            print("WIN")
            return
    
    # print("IDK")
            

if __name__ == "__main__":
    main()