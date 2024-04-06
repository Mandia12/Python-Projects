with open("story.txt", "r") as f:
    story = f.read()

target_start = "<"
target_end = ">"

words = set()
start_of_word = -1

for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

print("Welcome to the Madlib Generator!\n")

for word in words:
    answer = input("Please enter a word for " + word + ": ")
    answers[word] = answer


for word in words:
    story = story.replace(word, answers[word])

print(story)
