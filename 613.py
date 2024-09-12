a = input()
otv = ""
for i in range(1, len(a)+1):
    otv += a[-i]
print(otv)