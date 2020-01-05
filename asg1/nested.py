def multiply(a, b):
    n = int(abs(min(a, b)))
    m = int(abs(max(a, b)))
    s = 0
    for i in range(n):
        s = s + m
    if a < 0 <= b or b < 0 <= a:
        return -s
    else:
        return s


def complex_multiply(a, b):
    re = multiply(a.real, b.real) - multiply(a.imag, b.imag)
    im = multiply(a.real, b.imag) + multiply(a.imag, b.real)
    return complex(re, im)


def main():
    print('Multiplication - Nested Loop')
    a = complex(input('Please enter the first number (x+yj): '))
    b = complex(input('Please enter the second number (x+yj): '))
    print('The result is:', complex_multiply(a, b))


if __name__ == '__main__':
    main()
