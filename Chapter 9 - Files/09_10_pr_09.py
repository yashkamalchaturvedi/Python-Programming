# Renaming File

import os

on = "old.txt"
nn = "new.txt"

with open(on) as f:
    c = f.read()

with open(nn, "w") as f:
    f.write(c)

os.remove(on)