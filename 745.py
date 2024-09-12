st = input()
var = []
for i in range(len(st)):
    var.append(st[:i] + st[i+1:])
print(sorted(var)[0])