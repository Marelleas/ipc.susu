n = int(input())
list = input().split()
k = 1
if (int(list[0]) + 1 == int(list[1])) or (int(list[1]) + 1 != int(list[2])):
    while k < n:
        k = k + 1
        if int(list[0]) + 1 != int(list[1]):
            break
        else:
            list.remove(list[0])
print(k)