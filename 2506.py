def convert_from(number, base):
    dict = {}
    for i in range(0, 36):
        if i < 10:
            dict[str(i)] = i
        else:
            dict[chr(i+55)] = i
    rasryad = len(number) - 1
    answer = 0
    for i in number:
        answer += dict[i]*(base **(rasryad))
        rasryad -= 1
    return answer
b = int(input())
n = input()
print(convert_from(n, b))