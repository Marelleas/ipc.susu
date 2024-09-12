R, r, h, d = map(int, input().split())
if R >= ((h+r-d)**2+r**2)**0.5:
    print("YES")
else:
    print("NO")