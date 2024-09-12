def convert_to(number, base):
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ''
    while number > 0:
        result = digits[number % base] + result
        number //= base
    if result == "":
        result = "0"
    return result.upper()
b = int(input())
n = int(input())
print(convert_to(n, b))