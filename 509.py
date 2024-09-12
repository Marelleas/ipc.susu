a = input()
b = ""
def del_prob():
    global a
    while a[0] == " ":
        a = a[1:]

while len(a) != 0:
    if a[0] != " ":
        b += a[0]
        a = a[1:]
    else:
        b += "."
        a = a[1:]
        del_prob()
print(b)