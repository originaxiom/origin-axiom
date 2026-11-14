"""Which line orders N make one sector's twist pair coincide with another's (main, 2026-11-14 night)? The frame's charges
(6Y: Q 1, u -4, d 2, L -3, e 6); the sector pairs up (Q, u), down (Q, d), leptons (L, e). A coincidence: equal,
transposed, negated, or negated and transposed, modulo N. Negation leaves the matter part unchanged (the centre's
identity), so negated coincidences copy the matter matrix too. Exact; N from 2 to 60."""
import itertools
Y = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
S = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
ops = {"equal": lambda a, b: (a, b), "transposed": lambda a, b: (b, a), "negated": lambda a, b: (-a, -b), "negated+transposed": lambda a, b: (-b, -a)}
for s1, s2 in itertools.combinations(S, 2):
    p1 = (Y[S[s1][0]], Y[S[s1][1]]); p2 = (Y[S[s2][0]], Y[S[s2][1]])
    for name, f in ops.items():
        q = f(*p1)
        Ns = [N for N in range(2, 61) if (q[0] - p2[0]) % N == 0 and (q[1] - p2[1]) % N == 0]
        if Ns:
            print("%-5s vs %-5s %-19s at N in %s" % (s1, s2, name, Ns))
