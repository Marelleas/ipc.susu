import math
a = math.atan(3/4)
d, w, h = map(int, input().split())
s = (d**2) * math.cos(a) * math.sin(a)
a2 = math.atan(w/h)
d2 = (s/(math.cos(a2)*math.sin(a2)))**0.5
print("%.6f" % d2)