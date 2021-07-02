myDict = {
    "Aaa" : "Bbb",
    "Ccc" : "Ddd",
    "Eee" : "Fff"
}

# print("options", myDict.keys())
a = input("enter word")
print("meaning", myDict.get(a))
print("meaning", myDict[a])