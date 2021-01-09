letter = ''' Dear <|NAME|>,
You are selected!

Date: <|DATE|>
'''
name = input("enter name\n")
date = input("enter date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|DATE|>", date)
print(letter)