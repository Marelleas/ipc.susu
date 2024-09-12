mk = 10**7
def mn(s, k, a):
    global mk
    if a >= k:
        if a < mk:
            mk = a
        return
    for i in s:
        if int(i) != a%10:
            mn(s, k, a*10+int(i))

s = input()
k = int(input())
if len(s) == 1 and k>int(s[0]) or len(s) == 0:
    print(-1)
else:
    mn(s, k, 0)
    print(mk)