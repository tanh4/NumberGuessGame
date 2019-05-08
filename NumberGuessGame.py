from random import randint

target = randint(1, 100)

currentInput = int(input("Please input a number between 1 - 100:"))
if currentInput < 1 or currentInput > 100:
    print("OUT OF BOUNDS!")

lastDiff = abs(currentInput - target)
if lastDiff <= 10:
    print("Warm!")
elif lastDiff == 0:
    print("Win!")
else:
    print("Cold!")

while input != target:
    currentInput = input("Press Q to quit, otherwise input a guessed number:")
    if currentInput == 'Q':
        break
    currentInput = int(currentInput)
    diff = abs(currentInput - target)
    if currentInput < 1 or currentInput > 100:
        print("OUT OF BOUNDS!")
    elif diff == 0:
        print("Win!")
        break
    elif diff > lastDiff:
        print("Colder!")
    else:
        print("Warmer!")
    lastDiff = diff
    
