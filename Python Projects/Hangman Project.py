import os

print("\nLet's play Hangman!")

word = input("Please choose a word. Don't show anyone! ").lower()

os.system("clear")
print(word)

building_word = ""
for i in range(len(word)):
    building_word += "_"

max_mistakes = 5
no_more = 0 

while True:
    print("\nYour word is:", building_word)
    guess = input("Please guess a letter: ").lower()
    if len(guess) == 1:
        if guess in word:
            for i, char in enumerate(word):
                if guess == char:
                    building_word = building_word[:i] + guess + building_word[i + 1:]
            if building_word == word:
                break
            else:
                print(f"\nGood job! {guess} was in the word!")
        else: 
            max_mistakes -= 1
            if max_mistakes == no_more:
                break
            print("\nThat one didn't work. Try again.")
            
        print("You have", max_mistakes, "mistakes left!")

    else:
        print("Please try again and guess 1 letter.")

if building_word == word:
    print("\nCongrats! You guessed the word", building_word, "!")
else: 
    print("\nYou're out of attempts! Would you like to play again?")