s = ""
a = ""
def fun(a,open1,gde,open2):
    global n, s
    if len(a) == n:
        print(a)
        return
    if n-1-gde>open1+open2:
        a += "("
        s += "("
        fun(a, open1+1, gde+1, open2)
        s = s[:len(s)-1]
        a = a[:gde] + a[gde+1:]
        a += "["
        s += "["
        fun(a, open1, gde + 1, open2 + 1)
        s = s[:len(s) - 1]
        a = a[:gde] + a[gde+1:]
    if len(s) != 0 and s[len(s)-1] == "(":
        a += ")"
        h = s
        s = s[:len(s) - 1]
        fun(a, open1 - 1, gde + 1, open2)
        s = h
        a = a[:gde] + a[gde+1:]
    if len(s) != 0 and s[len(s)-1] == "[":
        a += "]"
        g = s
        s = s[:len(s) - 1]
        fun(a, open1, gde+1, open2-1)
        s = g
        a = a[:gde] + a[gde+1:]

n = int(input())
fun(a, 0, 0, 0)