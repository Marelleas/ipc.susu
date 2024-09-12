n = int(input())
def proverka_n(x, n):
    answ = []
    while x >= n:
        if x%n in answ:
            return False
        answ.append(x%n)
        x = (x-x%n)//n
    if x%n in answ:
        return False    
    return True
answ = []
for i in range(2, 37):
    if proverka_n(n, i):
        answ.append(i)
print(*answ)