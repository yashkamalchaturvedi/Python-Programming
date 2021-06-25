b = set()
print(type(b))
# Set

b.add(4)
b.add(5)
b.add(6)
# b.add([4,5,6]) list can be changed
# b.add((4,5,6)) tuple
# b.add({4: 6}) dictionary can be changed

print(b)
print(len(b))

b.remove(5)

print(b)

b.pop()

print(b)
