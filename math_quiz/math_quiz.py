import random


def function_A(minimum, maximum):
    """
    Generates a random integer between min_value and max_value (inclusive).
    """
    return random.randint(int(minimum), int(maximum))


def function_B():
    """
    Generates a random arithmetic operator (+, -, *).
    """
    return random.choice(['+', '-', '*'])


def function_C(number_1, number_2, operator):
    """
    Calculates the result of the arithmetic expression.
    """
    problem = f"{number_1} {operator} {number_2}"
    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    else:
        result = number_1 * number_2
    return problem, result



def math_quiz():
    """
    Conducts a math quiz game.
    """
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = function_A(1, 10) # we get a random number between 1 and 10
        num2 = function_A(1, 5)  # we get a random number between 1 and 5.5
        operator = function_B() # perform a random operation

        problem, correct_answer = function_C(num1, num2, operator)

        print(f"\nQuestion: {problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            user_answer = 0

        if user_answer == correct_answer: # we check if our solution is actually correct or not
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {correct_answer}.") # if not we will get correct answer displayed

    print(f"\nGame over! Your score is: {score}/{total_questions}") # we print here the score out of number of questions i.e, 3

if __name__ == "__main__":
    math_quiz()
