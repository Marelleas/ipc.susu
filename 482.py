def delskob(str):
    ans = ""
    n = 0
    for i in range(len(str)):
        if str[i] == "(":
            n = 1
        if n != 1:
            ans += str[i]
        if str[i] == ")":
            n = 0
    return ans
str = input()
print(delskob(str))