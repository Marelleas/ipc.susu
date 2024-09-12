ed = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
des = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
des1 = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
a = int(input())
b = a//100
c = (a-b*100)//10
d = a%10
if b>0:
    print(ed[b], end=" hundred")
    if c>0 or d>0:
        print(" ", end = "")
if c==1:
    print(des[d], end = "")
elif c > 1:
    print(des1[c], end = "")
    if d>0:
        print(" ", end = "")
if d > 0 and c != 1:
    print(ed[d], end = "")
print(".")