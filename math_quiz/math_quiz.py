import random

def generate_random_integer(min_value, max_value):
    """Generate a random integer within the given range."""
    return random.randint(min_value, max_value)

def generate_operator():
    """Generate a random arithmetic operator: +, -, *."""
    return random.choice(['+', '-', '*'])

def calculate_result(num1, num2, operator):
    """
    Calculate the result of an arithmetic operation and return both the problem and the answer.
    """
    problem = f"{num1} {operator} {num2}"
    if operator == '+':
        answer = num1 + num2
    elif operator == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return problem, answer

def math_quiz():
    score = 0
    total_questions = 3  # You can change the number of questions here

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        num1 = generate_random_integer(1, 10)
        num2 = generate_random_integer(1, 5)  # Adjusted max value to an integer
        operator = generate_operator()

        problem, answer = calculate_result(num1, num2, operator)
        print(f"\nQuestion: {problem}")

        # Error handling for non-integer inputs
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break  # Break the loop if input is an integer
            except ValueError:
                print("Please enter a valid integer.")

        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {score}/{total_questions}")

