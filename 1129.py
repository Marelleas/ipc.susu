a = input()
n = 0
for i in range(65, 91):
    if chr(i) in a:
        n += 1
print(n)