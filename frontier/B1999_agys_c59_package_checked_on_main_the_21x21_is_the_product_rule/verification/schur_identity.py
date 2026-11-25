"""B1999: main's check of the seat's E4 construction (identical in its C58 and C59 producers), main's own code.
The 21x21 matrix: diagonal blocks H_0..H_6 (agy: Y_0^H, Y_1, Y_2^H, ..., Y_6^H), superdiagonal blocks -s*I (agy: s = 1).
Claim to test: Y_raw = (C - D B^-1 A)^H equals (H_6 H_5 ... H_0)^H / s^6 exactly, for any blocks; so the singular-value ratios
do not depend on s, and the 'linear boundary-Dirac EFT' is the ordered 7-fold product rewritten."""
import mpmath as mp, random
mp.mp.dps = 40
random.seed(1)
def rnd():
    return mp.matrix([[mp.mpc(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(3)] for _ in range(3)])
def yraw(H, s):
    M = mp.zeros(21, 21)
    for m in range(6):
        for r in range(3): M[3*m + r, 3*(m+1) + r] = -s
    for n in range(7):
        for r in range(3):
            for c in range(3): M[3*n + r, 3*n + c] = H[n][r, c]
    A = M[:18, :3]; B = M[:18, 3:]; C = M[18:, :3]; D = M[18:, 3:]
    return (C - D * (B ** -1) * A).H
worst = 0; worst_ratio = 0
for trial in range(20):
    H = [rnd() for _ in range(7)]
    P = H[6]
    for n in range(5, -1, -1): P = P * H[n]
    for s in (1, 2, mp.mpf(1) / 3):
        Y = yraw(H, s)
        worst = max(worst, mp.mnorm(Y - P.H / s**6, 1) / mp.mnorm(P, 1) * s**6)
        sv1 = sorted(mp.svd_c(yraw(H, 1), compute_uv=False)); svs = sorted(mp.svd_c(Y, compute_uv=False))
        worst_ratio = max(worst_ratio, max(abs(sv1[k] / sv1[2] - svs[k] / svs[2]) for k in range(2)))
print("Y_raw = (H_6 ... H_0)^H / s^6 for 20 random block sets and s in {1, 2, 1/3}: worst relative deviation %s" % mp.nstr(worst, 3))
print("singular-value ratios independent of the step s: worst difference %s" % mp.nstr(worst_ratio, 3))
