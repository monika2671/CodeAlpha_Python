import random
print("Welcome to the Hangman Game!")
words=["python", "hangman", "programming", "challenge", "developer"]
chosen_word=random.choice(words)
blanks=[]
for i in chosen_word:
    blanks.append("_")
blank=" ".join(blanks)
print(blank)
w_guess=0
while(w_guess<6 and "_" in blanks):
    letter=input("Guess a letter: ")
    if(letter in chosen_word):
        for index,letter in enumerate(chosen_word):
            if(letter==chosen_word[index]):
                blanks[index]=letter
        print("Correct guess!")        
        print(" ".join(blanks))
    else:
        w_guess+=1
        print("Wrong guess! You have", 6-w_guess, "guesses left.")
if(w_guess==6):
    print("You lost! The word was:", chosen_word)
else:
    print("Congratulations! you WON!")



