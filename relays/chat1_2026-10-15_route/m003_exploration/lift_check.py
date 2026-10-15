# Is "N^2 | Q_gamma(w)" equivalent to "w = N v for some point v of order N^2 fixed by eps*gamma (mod N^2)"?
import math
exec(open("closing_threads.py").read().split("SECT =")[0])   # lyndon, mat, height
agree = disagree = 0; ex = []
for w in lyndon(12):
    if len(w) < 2: continue
    A, B, C, D = mat(w)
    for N in (3, 5, 7):
        for eps in (1, -1):
            for a in range(N):
                for b in range(N):
                    if (a, b) == (0, 0) or math.gcd(math.gcd(a, b), N) != 1: continue
                    if ((a*D + b*B) - eps*a) % N or ((a*C + b*A) - eps*b) % N: continue
                    Q = C*a*a + (A - D)*a*b - B*b*b
                    closes = (Q // N) % N == 0 if Q % N == 0 else None
                    M2 = N*N
                    lifts = any(((x*D + y*B) - eps*x) % M2 == 0 and ((x*C + y*A) - eps*y) % M2 == 0
                                for x in range(a, M2, N) for y in range(b, M2, N))   # v = (x,y)/N^2 with N v = w
                    # note: a point v of order N^2 with N*v = w has coordinates (x, y) = (a, b) + N*(i, j)
                    if closes == lifts: agree += 1
                    else:
                        disagree += 1
                        if len(ex) < 5: ex.append((w, N, eps, (a, b), Q, closes, lifts))
print("agree", agree, "disagree", disagree, ex)
