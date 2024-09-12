n, x, y = map(int, input().split())
left, right = 0, (n - 1) * max(x, y)
while right > left + 1:
    p = (right + left) // 2
    if (p // x + p // y) < n - 1:
        left = p
    else:
        right = p
print(right + min(x, y))