# f = open('D:\Data Science\Python\Coding\Chapter 9\sample.txt', 'r')
# data = f.read(5)
# data = f.readline()
# print(data)


# f = open('another.txt', 'w')
# f = open('another.txt', 'a')

# f.write("Harsh is good boy")
# f.close()

# with open('another.txt', 'r') as f:
#     a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("me")
    print(a)
