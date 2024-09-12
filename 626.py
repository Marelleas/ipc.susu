from math import factorial
x, e = map(float, input().split(" "))
yk1 = x
yk = 0
i=1 
while abs(yk1-yk)>=e:
    yk=yk1 
    i+=2 
    if (i//2)%2==0:
        yk1 = yk1+(x**i)/factorial(i)
    else: yk1 = yk1 - (x ** i) / factorial(i)
print("%.6f"%yk)