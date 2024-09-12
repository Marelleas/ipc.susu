n = input()
otv = ""
for i in range(len(n)):
    if n[i] != "0" and n[i] != "5":
        otv += n[i]
if len(otv) == 0:
    print(0)
else:
    print(otv)