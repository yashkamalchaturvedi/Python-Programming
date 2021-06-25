def game():
    return 644


score = game()
with open("Python\Coding\Chapter 9\hiscore.txt") as f:
    hiscore = f.read()

if hiscore == '':
    with open("Python\Coding\Chapter 9\hiscore.txt", 'w') as f:
        f.write(str(score))

elif int(hiscore) < score:
    with open("Python\Coding\Chapter 9\hiscore.txt", 'w') as f:
        f.write(str(score))
