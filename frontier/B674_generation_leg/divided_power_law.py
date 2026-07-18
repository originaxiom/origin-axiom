"""The divided-power law: v5(den c_n) = v5(5^n n!) for (q;q)^{-3/5}, n<=120."""
from fractions import Fraction

N = 121


def series():
    ser = [Fraction(0)]*N
    ser[0] = Fraction(1)
    a = Fraction(-3, 5)
    for m in range(1, N):
        fac = [Fraction(1)]
        k, c = 1, Fraction(1)
        while m*k < N:
            c = c * (a - (k-1)) / k * (-1)
            fac.append(c)
            k += 1
        out = [Fraction(0)]*N
        for i, ci in enumerate(ser):
            if ci:
                for k2, ck in enumerate(fac):
                    if i + m*k2 < N:
                        out[i + m*k2] += ci*ck
        ser = out
    return ser


def v5den(x):
    d, v = x.denominator, 0
    while d % 5 == 0:
        d //= 5
        v += 1
    return v


def s5(n):
    s = 0
    while n:
        s += n % 5
        n //= 5
    return s


if __name__ == "__main__":
    ser = series()
    bad = [(n, v5den(ser[n]), n + (n - s5(n))//4)
           for n in range(1, N) if v5den(ser[n]) != n + (n - s5(n))//4]
    bad3 = [n for n in range(N) if ser[n].denominator % 3 == 0]
    print("exceptions:", bad)
    print("3-in-denominator:", bad3)
    assert not bad and not bad3
    print("THE DIVIDED-POWER LAW: 120/120 exact; being prime absent")
