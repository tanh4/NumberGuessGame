from random import randint

def IsInt(str):
    try: 
        int(str)
        return True
    except ValueError:
        return False

target = randint(1, 100)

currentInput = "initial value"
while not IsInt(currentInput):
    currentInput = input("Please input 1 - 100! Or input Q to quit.")
    if currentInput == 'Q':
        quit()
lastDiff = abs(int(currentInput) - target)

currentInput = int(currentInput)
if currentInput < 1 or currentInput > 100:
    print("OUT OF BOUNDS!")
else:
    lastDiff = abs(currentInput - target)
    if lastDiff <= 10:
      print("Warm!")
    elif lastDiff == 0:
        print("Win!")
    else:
        print("Cold!")

while input != target:
    currentInput = input("Press Q to quit, otherwise input a guessed number between 1 - 100:")
    if currentInput == 'Q':
        break
    if not IsInt(currentInput):
        continue
        
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
    
