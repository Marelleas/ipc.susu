def prov(text, errors):
    for i in text.upper():
        if i in errors:
            return "no"
    return "yes"
errors = input()
n = int(input())
basa = []
for i in range(n):
    basa.append(prov(input(), errors))
for i in range(n):
    print(basa[i])