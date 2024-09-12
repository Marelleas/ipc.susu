def prt(a):
    print(a[0], end = '')
    for i in range(1, len(a)):
        print("+", a[i], sep='', end = '')
    print()
def pri(a, n):
    if sum(a) == n and len(a)>1:
        prt(a)
        return
    b = n- sum(a)
    for i in range(1, b+1):
        if len(a) == 0 or len(a)>0 and a[-1] <= i:
            pri(a + [i], n)
n = int(input())
c = []
pri(c, n)