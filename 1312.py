def vari(a,s):
    if len(a)<1:
        if s == 0:
            return 1
        else:
            return 0
    k = vari(a[1:], s + a[0])
    k += vari(a[1:], s - a[0])
    k += vari(a[1:], s * a[0])
    if s < 0:
        k += vari(a[1:], abs(s)//a[0]*(-1))
    else:
        k += vari(a[1:], s//a[0])
    return k
a = list(map(int, input().split()))
print(vari(a[1:], a[0]))