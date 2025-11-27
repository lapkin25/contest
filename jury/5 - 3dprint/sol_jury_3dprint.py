import math

def integrand(z, a, b):
    return math.pi * (1 - z ** 2) / (a * (b ** z)) ** 2

def trapezoid(l, r, a, b):
    return 0.5 * (r - l) * (integrand(l, a, b) + integrand(r, a, b))

def sol_3dprint_numeric(a, b):
    assert(a > 0 and a <= 10)
    assert(b > 1 and b <= 10)
    l = -1
    r = 1
    N = 100000
    h = (r - l) / N
    V = sum([trapezoid(l + i * h, l + (i + 1) * h, a, b) for i in range(N)])
    return V

def sol_3dprint(a, b):
    assert(a > 0 and a <= 10)
    assert(b > 1 and b <= 10)
    k = 2 * math.log(b)
    V = 2 * math.pi / (a ** 2 * k ** 3) * \
        (k * (math.exp(k) + math.exp(-k)) + (math.exp(-k) - math.exp(k)))
    return V


if __name__ == "__main__":
    # здесь задаются тестовые входные данные
    a = 1.6
    b = 1.4
    V = sol_3dprint(a, b)
    print(f"V = {V}")
    V_numeric = sol_3dprint_numeric(a, b)
    print(f"V_numeric = {V_numeric}")
