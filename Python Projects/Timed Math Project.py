import random
import time

MIN_OPERAND = 2
MAX_OPERAND = 12
OPERATORS = ["+", "-", "*"]
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)

    return expr, answer

wrong = 0

print("\nReady for the timed Math Quiz?")
input("Press enter to begin!")
print("----------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
   
    while True:
        guess = input("Problem " + str(i + 1) + ": " + expr + " = ")
        if guess == str(answer):
            break
        else:
            wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)
            
print("----------------------")
print("Nice job! You completed", TOTAL_PROBLEMS, "problems in", total_time, "seconds!")
print("You got", wrong, "questions wrong")
  