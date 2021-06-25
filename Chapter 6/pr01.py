text = input("enter text")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe" in text):
    spam = True
elif("click" in text):
    spam = True
else:
    spam = False

if(spam):
    print("text is spam")
else:
    print("not spam")
