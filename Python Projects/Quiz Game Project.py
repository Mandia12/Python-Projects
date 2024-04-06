print("Welcome to computer quiz!")

play = input("Would you like to play? ")

if play.lower() != "yes":
    quit()

print("Let's play!")

# Code for asking a question 

score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("That was incorrect! Try again.")

# Repeat question code ^^^ for new questions
    
print("You got", score, "question(s) correct!")
    
