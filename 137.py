posl = input()
tekst = ""
ans = []
for i in posl:
    if i != "*":
        tekst += i
    else:
        ans.append(tekst[-1])
        tekst = tekst[:-1]
for i in ans:
    print(i, end = "")