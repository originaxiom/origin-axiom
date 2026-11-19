# Which imaginary quadratic orders (discriminant D < 0) contain an element of norm 5?
# Norms of O_D are the values of the principal form x^2 + b x y + c y^2, b = D mod 2, c = (b - D)/4.
import math
hits = []
for D in range(-3, -20001, -1):
    if D % 4 not in (0, 1):
        continue
    b = D % 2
    c = (b * b - D) // 4
    ok = any(x * x + b * x * y + c * y * y == 5
             for y in range(0, 4) for x in range(-6, 7))
    if ok:
        hits.append(D)
print("discriminants with an element of norm 5 (|D| <= 20000):", hits)
# reduced forms and Im tau for each
for D in hits:
    forms = []
    for a in range(1, int(math.isqrt(-D // 3)) + 2):
        for b in range(-a + 1, a + 1):
            if (b * b - D) % (4 * a):
                continue
            c = (b * b - D) // (4 * a)
            if c < a or (c == a and b < 0) or math.gcd(math.gcd(a, abs(b)), c) != 1:
                continue
            forms.append((a, b, c))
    for a, b, c in forms:
        y = math.sqrt(-D) / (2 * a)
        print(D, (a, b, c), "Re tau = %s/%d" % (-b, 2 * a), "Im tau = %.4f" % y, "eps = %.3e" % math.exp(-math.pi * y))
