N = int(input())
S = input()
if len(S) > N:
    x = len(S) - N
    ans = S[x:]
else:
    x = N - len(S)
    ans = '.' * x + S
print(ans)