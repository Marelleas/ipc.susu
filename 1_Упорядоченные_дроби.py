def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def has_common_factor(n, d):
    return gcd(n, d) > 1

def gen_fractions(n):
    fractions = [(num, d) for d in range(2, n + 1) for num in range(1, d) if not has_common_factor(num, d)]
    return fractions

if __name__ == "__main__":
    n = int(input())
    fractions = gen_fractions(n)
    
    fractions.sort(key=lambda frac: frac[0] / frac[1])
    
    for num, den in fractions:
        print(f"{num}/{den}")