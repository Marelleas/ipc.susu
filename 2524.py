n = int(input())
m = int(input())
s = 0
while n > 0:
    if n % 2 != 0:
        s = s + m + 1
    m = m * 2
    n = n//2
print(s)