x, y = map(int,input().split())
if -8 <= y <= 0:
    if -8 <= x <= 8:
        print("Yes")
    else:
        print("No")
else:
    if x <= 0:
        if 8 + x//2 == y:
            print("Yes")
        else:
            print("No")
    else:
        if 0 <= x <= 4:
            if y <= 8:
                print("Yes")
            else:
                print("No")
        elif 4 < x <= 8:
            if 16 - 2*x == y:
                print("Yes")
            else:
                print("No") 