t1, t2 = map(int, input().split())
rezhim = input()
if rezhim == "fan": print(t1)
elif rezhim == "auto": print(t2)
elif rezhim == "freeze": print(min(t1, t2))
else: print(max(t1, t2))