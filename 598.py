n = int(input())
i = 0
while 3**i < n:
    if 3**i == n:
        break
    i += 1
if 3**i == n:
    print("True")
else:
    print("False")