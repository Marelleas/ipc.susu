def fib(n, counter) -> str:
    global a
    if counter >= n:
        return
    a[-1], a[-2] = a[-1] + a[-2], a[-1]
    fib(n, counter + 1)

n, m, l = map(int, input().split())
a = ["b", "a"]
fib(n, 2)
if n == 1:
    print(a[0][m - 1:m - 1 + l:1])
    exit()
if n == 2:
    print(a[1][m - 1:m - 1 + l:1])
    exit()
print(a[-1][m - 1:m - 1 + l:1])