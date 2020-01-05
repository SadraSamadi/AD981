def no_of_dec(n):
    if n.endswith('.0'):
        return 0
    for i, d in enumerate(n):
        if d == '.':
            return len(n) - i - 1


def rm_dec(n, dec):
    s = len(n)
    if dec == 0:
        return int(n[:s - 2])
    return int(n[:s - dec - 1] + n[s - dec:])


def multiply(a, b):
    n = int(abs(min(a, b)))
    m = int(abs(max(a, b)))
    s = 0 if n % 2 == 0 else m
    while n > 1:
        n = int(n / 2)
        m = m + m
        if n % 2 == 1:
            s = s + m
    return s


def float_multiply(a, b):
    if a == 0 or b == 0:
        return 0
    u = str(abs(a))
    v = str(abs(b))
    n_dec = no_of_dec(u)
    n = rm_dec(u, n_dec)
    m_dec = no_of_dec(v)
    m = rm_dec(v, m_dec)
    p = multiply(n, m)
    s = p / pow(10, n_dec + m_dec)
    if a < 0 <= b or b < 0 <= a:
        return -s
    else:
        return s


def main():
    print('Multiplication - Halving and Doubling')
    a = float(input('Please enter the first number: '))
    b = float(input('Please enter the second number: '))
    print('The result is:', float_multiply(a, b))


if __name__ == '__main__':
    main()
