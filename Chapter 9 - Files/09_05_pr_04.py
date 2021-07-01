words = ["donkey", "kaddu", "mote"]

with open("sample.txt") as f:
    c = f.read()

for word in words:
    c = c.replace(word, "#")
    with open("sample.txt", "w") as f:
        f.write(c)
