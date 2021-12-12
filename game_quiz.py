print("welcome to my math game!")
playing = input("Do you want to play my game? ")

if playing.lower() != "yes":
    quit()

print("Ok let's go...")
score = 0

answer = input("What is 21 * 12? ")
if answer != "252":
    print("incorrect!")
else:
    print("correct!")
    score += 1

print("next question...")

answer = input("what is 10 - 112 * 12? ")
if answer != "-90":
    print("incorrect!")
else:
    print("correct!")
    score += 1

print("next question...")

answer = input("What is 1 * 3 * 5 - 6 ? ")
if answer != "9":
    print("incorrect!")
else:
    print("correct!")
    score += 1

print("next question...")

answer = input("what is 14 - 1? ")
if answer != "13":
    print("incorrect!")
else:
    print("correct!")
    score += 1

print("next question...")

answer = input("what is 11 + 5 / 3? ")
if answer != "12.6666666667":
    print("incorrect!")
else:
    print("correct!")
    score += 1

print("You got " + str(score) + " points" )
print("you got " + str((score / 5) * 100) + "%")

