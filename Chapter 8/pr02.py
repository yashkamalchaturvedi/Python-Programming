# this = "              yash                  is                    pro     "
# print(this)
# print(this.strip())

def remove_and_split(string, word):
    newStr = string.replace(word, "")
    return newStr.strip()


this = "              yash                  is                    pro     "
n = remove_and_split(this, "yash")
print(n)
