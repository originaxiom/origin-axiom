"""S301-A check c_algebra (value-free; first principles + main's F_10 direction from B1821's cm_zero_line).
Theorem 31: Tr Y_16, Tr Y_16^2, Tr Y_16^3 in 6Y units; c_GJ = sqrt(K_lepton/K_down) with K_s = q_L^2 + q_R^2.  (The lane's
            tan-beta combination of the K_s is firewalled and is NOT formed here.)
Theorem 32: eps_KK = (alpha_12/(4 pi)) ln(M_3^2/M_12^2) with alpha_12^-1 = A Vol and ln(M_3/M_12) = B pi Vol is B/(2A) for
            every Vol and every (A, B): its 'independence of Vol' is the cancellation of two posited linear-in-Vol formulas.
            C_F(SU(3)) = 4/3.
Theorem 33: (I - P)(I + P/(1 - alpha)) = I for P = h h^T/|h|^2, alpha = h.h/|h|^2 (Sherman-Morrison; needs alpha != 1);
            P^2 = alpha P (P is a projector only when alpha = 1, where I - P is singular); alpha on main's F_10 direction;
            basis covariance of the seesaw (a tautology); B - L = diag(1/3, 1/3, 1/3, -1): quark/lepton = -1/3.
Theorem 38: theta_ct = -264 pi a b + (pi/2 - 132 pi a^2) Re tau cancels the cocycle (A: +264 pi a; T: -132 pi a^2 - pi/2;
            M: odd) -- symbolic; uniqueness within the affine class; N_theta on rational slopes = lcm of the two orders.
Theorems 34/40: the 'fresh Haar' referee check (singular values invariant under unitary rotations) is a tautology: shown."""
import os
for v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS"):
    os.environ.setdefault(v, "1")
import math, pathlib, sys
from fractions import Fraction as Fr
import numpy as np
import sympy as sp

print("c_algebra")
# ---- Theorem 31 ----
reps16 = [("Q", 6, 1), ("u^c", 3, -4), ("d^c", 3, 2), ("L", 2, -3), ("e^c", 1, 6), ("nu^c", 1, 0)]
diag = [q for _, m, q in reps16 for _ in range(m)]
assert len(diag) == 16
print("  T31: Tr Y16 = %d, Tr Y16^3 = %d, Tr Y16^2 = %d (6Y units; textbook anomaly cancellation, gcd of charges %d)"
      % (sum(diag), sum(q ** 3 for q in diag), sum(q * q for q in diag), math.gcd(*[abs(q) for q in diag if q])))
K = {"down": 1 ** 2 + 2 ** 2, "lepton": (-3) ** 2 + 6 ** 2}
print("  T31: (q_L, q_R)_lepton = 3 (q_L, q_R)_down = 3(-1, 2) up to sign, so K_lepton/K_down = %s and c_GJ = sqrt = %s"
      % (Fr(K["lepton"], K["down"]), sp.sqrt(sp.Rational(K["lepton"], K["down"]))))

# ---- Theorem 32 ----
A, Bc, Vol = sp.symbols("A B Vol", positive=True)
eps = (1 / (A * Vol)) / (4 * sp.pi) * (2 * Bc * sp.pi * Vol)
print("  T32: eps_KK = %s for every Vol (posited alpha^-1 = A Vol, ln(M3/M12) = B pi Vol); C_F(SU(3)) = %s"
      % (sp.simplify(eps), sp.Rational(3 ** 2 - 1, 2 * 3)))

# ---- Theorem 33 ----
rng = np.random.default_rng(20261104)
dev = 0.0; dev2 = 0.0
for _ in range(200):
    h = rng.normal(size=3) + 1j * rng.normal(size=3)
    n2 = np.vdot(h, h).real; al = (h @ h) / n2; P = np.outer(h, h) / n2
    dev = max(dev, np.abs((np.eye(3) - P) @ (np.eye(3) + P / (1 - al)) - np.eye(3)).max())
    dev2 = max(dev2, np.abs(P @ P - al * P).max())
hr = rng.normal(size=3).astype(complex); Pr = np.outer(hr, hr) / np.vdot(hr, hr).real
print("  T33: Sherman-Morrison inverse: max dev %.1e (200 random h); P^2 = alpha P: %.1e; for real h, |alpha - 1| = %.1e and"
      " det(I - P) = %.1e (I - P singular there, the inverse formula divides by zero; for h = e^{i phi} r, P^2 = e^{2 i phi} P: not a projector)" % (dev, dev2, abs((hr @ hr) / np.vdot(hr, hr).real - 1), abs(np.linalg.det(np.eye(3) - Pr))))
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parents[5] / "frontier/B1821_the_frames_mirror_symmetry_in_re_tau/verification"))
import cm_zero_line as Z
for t in (complex(0.45, 1.2), complex(0.4472, 2.618), complex(0.3, 3.0)):
    h = np.array(Z.direction("F_10", t)); al = (h @ h) / np.vdot(h, h).real
    print("       on main's F_10 direction at tau = %s: |alpha_h| = %.2e (T-FA-NORM: h.h ~ eta^12, so M_R -> b (I - P) with P nearly nilpotent)" % (t, abs(al)))
# basis covariance: m = -Y M^-1 Y^T - W/b transforms as U_L m U_L^T
dev = 0.0
for _ in range(50):
    Y = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Ms = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); Ms = Ms + Ms.T
    W = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3)); W = W + W.T; b = complex(*rng.normal(size=2))
    def haar():
        z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2); q, r = np.linalg.qr(z); return q * (np.diag(r) / np.abs(np.diag(r)))
    UL, UR = haar(), haar()
    m0 = -Y @ np.linalg.solve(Ms, Y.T) - W / b
    Y1 = UL @ Y @ UR.conj().T; M1 = UR.conj() @ Ms @ UR.conj().T; W1 = UL @ W @ UL.T
    m1 = -Y1 @ np.linalg.solve(M1, Y1.T) - W1 / b
    dev = max(dev, np.abs(m1 - UL @ m0 @ UL.T).max())
print("  T33: seesaw basis covariance m -> U_L m U_L^T under the lane's own transformation rules: %.1e (an identity of the rules, not a check of the physics)" % dev)
BL = np.diag([Fr(1, 3)] * 3 + [Fr(-1)])
print("  T33: B - L = diag(1/3, 1/3, 1/3, -1): trace %s, quark/lepton %s (textbook Pati-Salam)" % (sum(BL.diagonal()), BL[0, 0] / BL[3, 3]))

# ---- Theorems 34 / 40: the 'fresh Haar' check ----
M = rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))
def haar():
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2); q, r = np.linalg.qr(z); return q * (np.diag(r) / np.abs(np.diag(r)))
d = max(np.abs(np.sort(np.linalg.svd(M, compute_uv=False)) - np.sort(np.linalg.svd(haar() @ M @ haar().conj().T, compute_uv=False))).max() for _ in range(20))
print("  T34/T40: singular values of a RANDOM matrix under unitary rotations: %.1e (true of every matrix; the check cannot fail)" % d)

# ---- Theorem 38 ----
a, b, x = sp.symbols("a b x", real=True)
ct = -264 * sp.pi * a * b + (sp.pi / 2 - 132 * sp.pi * a ** 2) * x
dA = sp.simplify(ct.subs(b, b + 1) - ct)
dT = sp.simplify(ct.subs({b: b - a, x: x + 1}, simultaneous=True) - ct)
dM = sp.simplify(ct.subs({b: -b, x: -x}, simultaneous=True) + ct)
print("  T38: Delta_A theta_ct = %s (cancels +264 pi a); Delta_T theta_ct = %s (cancels -132 pi a^2 - pi/2); theta_ct(M) + theta_ct = %s"
      % (dA, sp.expand(dT), dM))
c1, c2, c0 = sp.symbols("c1 c2 c0")
f = c1 * b + c2 * x + c0
sol = sp.solve([sp.expand(f.subs(b, b + 1) - f + 264 * sp.pi * a), sp.expand(f.subs({b: b - a, x: x + 1}, simultaneous=True) - f - 132 * sp.pi * a ** 2 - sp.pi / 2),
                sp.expand(f.subs({b: -b, x: -x}, simultaneous=True) + f)], [c1, c2, c0], dict=True)
print("  T38: affine counterterms c1 b + c2 Re tau + c0 obeying A, T and M-oddness: %s (unique in that class; any invariant odd function can be added outside it)" % sol)
rows = []
for s in range(1, 13):
    for r in range(1, s):
        if math.gcd(r, s) != 1:
            continue
        al = Fr(r, s)
        oA = (132 * al).denominator; oT = (66 * al * al + Fr(1, 4)).denominator
        # order of the subgroup of Q/Z generated by 132a and 66a^2 + 1/4
        gens = [132 * al % 1, (66 * al * al + Fr(1, 4)) % 1]
        den = math.lcm(*(g.denominator for g in gens))
        grp = {Fr(0)}
        frontier_ = [Fr(0)]
        while frontier_:
            e = frontier_.pop()
            for g in gens:
                n = (e + g) % 1
                if n not in grp:
                    grp.add(n); frontier_.append(n)
        rows.append((al, math.lcm(oA, oT), len(grp)))
bad = [r_ for r_ in rows if r_[1] != r_[2]]
print("  T38: N_theta = lcm(ord A-step, ord T-step) equals the generated subgroup's order on all %d reduced slopes with s <= 12: %s; N_theta(2/5) = %d"
      % (len(rows), "yes" if not bad else "NO %s" % bad, [r_[1] for r_ in rows if r_[0] == Fr(2, 5)][0]))
