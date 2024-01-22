# Function 1
def wins_rock_scissors_paper(playerThrow, opponentThrow):
    playerThrow = playerThrow.lower()
    opponentThrow = opponentThrow.lower()

    if playerThrow == opponentThrow:
        return False  
    elif (
        (playerThrow == "rock" and opponentThrow == "scissors") or
        (playerThrow == "paper" and opponentThrow == "rock") or
        (playerThrow == "scissors" and opponentThrow == "paper")
    ):
        return True  
    else:
        return False  

# Function 2
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Function 3
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

# Function 4
def sum_to_goal(numbers, goal):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0

# Python Objects
class UpCounter:
    def __init__(origin, stepSize=1):
        origin.counterValue = 0
        origin.stepSize = stepSize

    def count(origin):
        return origin.counterValue

    def update(origin):
        origin.counterValue += origin.stepSize

class DownCounter(UpCounter):
    def update(origin):
        origin.counterValue -= origin.stepSize

