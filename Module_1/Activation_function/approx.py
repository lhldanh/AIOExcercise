def fact(n):
    res = 1
    for i in range(2, n + 1):
        res *= i
    return res

def sin(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i * x**(2*i + 1) / fact(2*i + 1)
    return res

def cos(x, n):
    res = 0
    for i in range(n):
        res += (-1)**i * x**(2*i) / fact(2*i)
    return res

def sinh(x, n):
    res = 0
    for i in range(n):
        res += x**(2*i + 1) / fact(2*i + 1)
    return res

def cosh(x, n):
    res = 0
    for i in range(n):
        res += x**(2*i) / fact(2*i)
    return res

def main():
    x = float(input("x = "))
    n = int(input('n = '))

    print(sin(x, n))
    print(cos(x, n))
    print(sinh(x, n))
    print(cosh(x, n))
    
    return

if __name__ == '__main__':
    main()