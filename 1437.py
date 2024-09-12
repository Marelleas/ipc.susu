n, vg, vs = map(int, input().split())
t = n / (vg + vs)
ng = (vg*t)//1
ns = (vs*t)//1
print(int(ng), int(ns))