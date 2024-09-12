basa = []
n = int(input())
ps = [0]
for i in range(n):
    tek = input()
    if tek[0] == "+":
        basa.append(int(tek[1:]))
        ps.append(ps[-1] + int(tek[1:]))
    elif tek[0] == "-":
        print(basa[-1])
        basa = basa[:-1]
        ps.pop(-1)
    elif tek[0] == "?":
        k = int(tek[1:])
        print(ps[-1]-ps[-(k+1)])