def repl(str, k):
    n = ord(str)
    if n in range(65, 91):
        n = n + k
        if n > 90:
            n = 65 + n - 91
    if n in range(97, 123):
        n = n + k
        if n > 122:
            n = 97 + n - 123
    return chr(n)
k = int(input())
str = input()
for i in str:
    if i.isalpha():
        print(repl(i, k), end = "")
    else:
        print(i, end = "")