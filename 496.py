strok = input()
ctr = ''
stro = ''
for i in range(len(strok)):
    x = strok[i]
    if x.isdigit():
        if x != "0" or (stro != '' and stro[-1] == ".") or strok[i+1] == '.':
            ctr += x
    else:
        stro += ctr
        stro += x
        ctr = ''
print(stro+ctr)