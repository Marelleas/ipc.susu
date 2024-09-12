n = int(input())
s = 0
i = 1

def recur(i, s, n):
    if i <= n:
        k = int(input())
        if s % k == 0:
            s += k
            i += 1
            recur(i, s, n)
        else:
            print("No")
            exit()
    else:
        print("Yes")
        exit()
recur(i, s, n)
