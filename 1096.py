n = int(input())
a = 1
b = 0
c = 0
x = a*100 + b*10 + c
while x < n:
    if a != b and a != c and b != c:
        print(x, end = " ")
    c += 1
    if c >= 10:
        c -= 10
        b += 1
    if b >= 10:
        b -= 10
        a += 1
    x = a * 100 + b * 10 + c