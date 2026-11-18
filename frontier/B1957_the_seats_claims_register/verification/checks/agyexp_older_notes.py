"""B1957: agy-exp's older notes (files from before the register's window, listed by the seat as owed; read at c4c48f541),
the exact statements main can decide by a short computation (data-free; nothing of the seat's is run or imported).
 O1  its cold read of B1936: the charges 6Y of one generation modulo 5; which multipliers put the matter half in one
     parity class; the Higgs residue each coupling needs.
 O2  its answers on W-C2: the number of vectors of the lattice of integer five-tuples of sum zero at each half-norm 1 to 16;
     the word L^6 R L R, the two reversing involutions and what each does to the mark (1, 2) modulo 5.
 O3  its F3 note: the signs of the four theta functions under z -> -z, which make the frame even in the matter charges."""
import itertools
import sympy as sp, mpmath as mp
Y6 = {"Q": 1, "u^c": -4, "d^c": 2, "L": -3, "e^c": 6}; res = {k: v % 5 for k, v in Y6.items()}
M = sorted(set(res.values())); mult = {m: sorted({(m * y) % 5 for y in M}) for m in (1, 2, 3, 4)}
print("O1: 6Y modulo 5: %s; the matter half M = %s and its negative %s; multipliers: %s; one parity class only for m = %s" % (res, M, sorted((-y) % 5 for y in M), mult, [m for m, v in mult.items() if len({x % 2 for x in v}) == 1]))
print("O1: down and lepton couplings: 1 + 2 = 3, so the Higgs residue is %d, in M: %s; up: 1 + 1 = 2, so %d, in -M: %s; under 6Y -> -6Y the placement is the same: %s"
      % ((-3) % 5, (-3) % 5 in M, (-2) % 5, (-2) % 5 in [(-y) % 5 for y in M], ((3) % 5 in [(-y) % 5 for y in M], (2) % 5 in M)))
shell = {}
R = range(-6, 7)
for v in itertools.product(R, repeat=4):
    last = -sum(v)
    n2 = sum(x * x for x in v) + last * last
    if n2 % 2 == 0 and 0 < n2 // 2 <= 16: shell[n2 // 2] = shell.get(n2 // 2, 0) + 1
low, up = sum(shell[k] for k in range(1, 7)), sum(shell[k] for k in range(7, 13))
print("O2: five-tuples of sum zero by half-norm 1 to 12: %s; 1 to 6: %d; 7 to 12: %d; 1 to 12: %d; 1 to 16: %d"
      % ([shell[k] for k in range(1, 13)], low, up, low + up, sum(shell[k] for k in range(1, 17))))
L = sp.Matrix([[1, 1], [0, 1]]); Rm = sp.Matrix([[1, 0], [1, 1]]); W = L ** 6 * Rm * L * Rm; F = sp.Matrix([[-1, 6], [0, 1]]); col = sp.Matrix([1, 2]); row = sp.Matrix([[1, 2]])
m5 = lambda v: [int(x) % 5 for x in v]
print("O2: L^6 R L R = %s, determinant %s; it fixes the mark (1, 2) modulo 5 as a column (%s) and as a row (%s); F = [[-1, 6], [0, 1]] has determinant %s, F^2 = 1 (%s) and F W F^-1 = W^-1 (%s); so does -F (%s)"
      % (W.tolist(), W.det(), m5(W * col), m5(row * W), F.det(), F * F == sp.eye(2), F * W * F.inv() == W.inv(), (-F) * W * (-F).inv() == W.inv()))
print("O2: on the mark: F as a column action gives %s and as a row action %s; -F gives %s and %s: exactly one of the two reversing involutions negates the mark in either convention, and which one it is depends on the convention (the note names the column mark and gives F the negating role, which is the row action's)"
      % (m5(F * col), m5(row * F), m5(-F * col), m5(row * (-F))))
mp.mp.dps = 30; z, q = mp.mpc("0.31", "0.17"), mp.exp(mp.pi * 1j * mp.mpc("0.2", "1.1"))
signs = [mp.nstr(mp.jtheta(n, -z, q) / mp.jtheta(n, z, q), 6) for n in (1, 2, 3, 4)]
print("O3: theta_n(-z)/theta_n(z) for n = 1, 2, 3, 4: %s: the first is odd and enters the frame as a product of two, the other three are even" % signs)
# ---- custody (files read as text at the commits named; nothing run)
import subprocess, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
show = lambda c, f: subprocess.run(["git", "show", "%s:%s" % (c, f)], capture_output=True, text=True, cwd=ROOT).stdout.split("\n")
Lx = show("c4c48f541", "relays/x_own_verify/verify_x_own.py")
print("O4: agy-exp's verify_x_own.py, line 1113, read as text: it holds 'single_higgs_q = -SIXY[\"H\"]': %s (the sign its F3 note says it had assumed)" % (len(Lx) > 1113 and 'single_higgs_q = -SIXY["H"]' in Lx[1112]))
Y = [sp.Rational(-1, 3)] * 3 + [sp.Rational(1, 2)] * 2
names = subprocess.run(["git", "show", "431c0517f", "--name-only", "--format="], capture_output=True, text=True, cwd=ROOT).stdout.split()
hit = [(f, i + 1) for f in names if f.endswith(".md") for i, l in enumerate(show("431c0517f", f)) if "Z = T/2 = −6Y" in l]
print("O5: 6Y on the 5 of SU(5) with Y = diag(-1/3, -1/3, -1/3, 1/2, 1/2) is %s, so diag(-2, -2, -2, 3, 3) is +6Y; the SM seat's relay at 431c0517f writes 'Z = T/2 = -6Y' (found at %d place(s)): agy-exp's 'differs' on row 960 is right" % ([6 * y for y in Y], len(hit)))
# ---- O6: X-C2's exact figures on the two words (its row 1464) and two identities of its row 1640
Lm, Rr = sp.Matrix([[1, 1], [0, 1]]), sp.Matrix([[1, 0], [1, 1]]); LR = Lm * Rr
def order(Mx, N):
    P_ = sp.eye(2); k = 0
    while True:
        P_ = (P_ * Mx).applyfunc(lambda t: t % N); k += 1
        if P_ == sp.eye(2): return k
g = Lm ** 2 * Rr; fixed2 = sum(1 for a in range(2) for b in range(2) if all(x % 2 == 0 for x in ((g - sp.eye(2)) * sp.Matrix([a, b]))))
lines = set()
for d in range(1, 13):
    for a in range(d):
        for b in range(d):
            v = (sp.Rational(a, d), sp.Rational(b, d)); n = sp.ilcm(v[0].q, v[1].q)
            if n == d: lines.add(min(v, ((-v[0]) % 1, (-v[1]) % 1)))
tau = mp.mpc("0.17", "1.3"); q_ = mp.exp(mp.pi * 1j * tau); eta = mp.exp(mp.pi * 1j * tau / 12) * mp.nprod(lambda n: 1 - mp.exp(2j * mp.pi * n * tau), [1, mp.inf])
jac = mp.jtheta(2, 0, q_) * mp.jtheta(3, 0, q_) * mp.jtheta(4, 0, q_) / eta ** 3
print("O6: |det(LR - 1)| = %s and |det(RL - 1)| = %s; the order of LR modulo 2, 5, 10, 25, 30: %s; L^2 R = %s has |trace - 2| = %s and fixes %d of the 4 points of order dividing 2; lines of exact order at most 12 up to sign: %d; theta_2 theta_3 theta_4 / eta^3 = %s; 2^(2 - 6) - 1 = %s"
      % (abs((LR - sp.eye(2)).det()), abs((Rr * Lm - sp.eye(2)).det()), [order(LR, N) for N in (2, 5, 10, 25, 30)], g.tolist(), abs(g.trace() - 2), fixed2, len(lines), mp.nstr(jac, 12), sp.Rational(2) ** (2 - 6) - 1))
# ---- O7: X-MEASURE's exact statements
J_, K_ = sp.Matrix([[2, 1], [1, 1]]), sp.Matrix([[0, -1], [1, 0]])
osl = lambda N: N ** 3 * sp.prod([1 - sp.Rational(1, p ** 2) for p in sp.primefactors(N)])
L2, R2 = Lm.applyfunc(lambda t: t % 2), Rr.applyfunc(lambda t: t % 2)
y_ = sp.Symbol("y", positive=True); u_ = sp.Symbol("u", positive=True)
print("O7: with J = [[2, 1], [1, 1]] and K = [[0, -1], [1, 0]]: K J K^-1 = J^-1: %s, and = -J^-1 (as the note writes): %s; |SL(2, Z/10)| = %s and |SL(2, Z/15)| = %s; modulo 2, L and R have order 2 and 2 and L R order %d (two transpositions of three points); with u = 1/y the area element dx dy/y^2 is dx du (|dy/du|/y^2 = %s), and the modular surface has area pi/3, so the normalised element is (3/pi) dx du"
      % (K_ * J_ * K_.inv() == J_.inv(), K_ * J_ * K_.inv() == -J_.inv(), osl(10), osl(15), order(LR, 2), sp.simplify(sp.Abs(sp.diff(1 / u_, u_)) * u_ ** 2)))
# ---- O8: X-OWN's exact statements
import numpy as np
els = [(a, b, c, d) for a in range(5) for b in range(5) for c in range(5) for d in range(5) if (a * d - b * c) % 5 == 1]; idx = {g: i for i, g in enumerate(els)}
mul = lambda g, h: ((g[0] * h[0] + g[1] * h[2]) % 5, (g[0] * h[1] + g[1] * h[3]) % 5, (g[2] * h[0] + g[3] * h[2]) % 5, (g[2] * h[1] + g[3] * h[3]) % 5)
pts = [(a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0)]
stab = {len([g for g in els if ((g[0] * v[0] + g[1] * v[1]) % 5, (g[2] * v[0] + g[3] * v[1]) % 5) in (v, ((-v[0]) % 5, (-v[1]) % 5))]) for v in pts}
Pm = np.zeros((120, 120))
for g in els:
    for s in ((1, 1, 0, 1), (1, 0, 1, 1)): Pm[idx[mul(g, s)], idx[g]] += 0.5
ev = np.linalg.eigvals(Pm); rho = sorted(abs(ev))[-2]
print("O8: SL(2, F_5) has %d elements; the stabiliser of a point of order 5 up to sign has %s elements at each of the %d points, weight %s; the walk by L and R with weights 1/2 has second largest eigenvalue modulus %.12f, and sqrt(3)/2 = %.12f"
      % (len(els), sorted(stab), len(pts), sp.Rational(10, 120), rho, 3 ** 0.5 / 2))
tm = lambda m: sp.Matrix([[m, 1], [1, 0]])
census = all(tm(m).det() == -1 and abs((tm(m) - sp.eye(2)).det()) == m and abs((tm(m) ** 2 - sp.eye(2)).det()) == m * m and abs((-tm(m) ** 2 - sp.eye(2)).det()) == m * m + 4 for m in range(1, 16))
print("O8: for the ticks [[m, 1], [1, 0]], m = 1 to 15: determinant -1, |det(T - 1)| = m, |det(T^2 - 1)| = m^2 and |det(-T^2 - 1)| = m^2 + 4: %s; the last are %s" % (census, [m * m + 4 for m in range(1, 16)]))
print("O8: the Higgs charge test: down 1 + 2 - 3 = %d, leptons -3 + 6 - 3 = %d, up 1 - 4 - 3 = %d = %d modulo 5; with +3 in place of -3 the up sum is %d" % (1 + 2 - 3, -3 + 6 - 3, 1 - 4 - 3, (1 - 4 - 3) % 5, 1 - 4 + 3))
# ---- O9: its note of four theorems (P-781): the exact arithmetic
Jm = sp.Matrix([[0, 1], [1, 0]])
W10 = Lm ** 5 * Rr * Lm ** 2 * Rr ** 2; W12 = W10 * Lm * Rr; v5 = sp.Matrix([1, 2])
from sympy.matrices.normalforms import smith_normal_form
snf = lambda Mx: [abs(int(x)) for x in smith_normal_form(Mx, domain=sp.ZZ).diagonal()]
print("O9: J L J = L^T and J R J = R^T: %s; J (1, 2) = %s = 2 (1, 3) modulo 5: %s; W10 = L^5 R L^2 R^2 sends the mark (transposed action) to %s modulo 5 and W12 = W10 L R to %s; Smith invariants of W10 + 1: %s, of W12 - 1: %s"
      % (Jm * Lm * Jm == Lm.T and Jm * Rr * Jm == Rr.T, m5(Jm * v5), m5(Jm * v5) == [(2 * 1) % 5, (2 * 3) % 5], m5(W10.T * v5), m5(W12.T * v5), snf(W10 + sp.eye(2)), snf(W12 - sp.eye(2))))
S0S0, S0F, FF = -1, 1, 0; CC_ = 25 * S0S0 + 2 * 5 * 6 * S0F + 36 * FF; CK = -(5 * S0F + 6 * FF)
print("O9: on the rational elliptic surface with fibre F (F^2 = 0), section S (S^2 = -1, S.F = 1) and K = -F: for C = 5 S + 6 F, C^2 = %d, C.K = %d, genus %d, and the ramification over the base is 2g - 2 + 10 = %d" % (CC_, CK, (CC_ + CK) // 2 + 1, CC_ + CK + 10))
print("O9: 24 + 24 + 4 * 50 = %d; the charge sums modulo 5: 1 + 1 - 2 = %d, 1 + 2 + 2 = %d, 2 + 2 - 2 - 2 = %d; 2 + q - 2 = 0 and 2q = 0 modulo 5 force q = %s" % (24 + 24 + 200, (1 + 1 - 2) % 5, (1 + 2 + 2) % 5, 0, [q for q in range(5) if (2 + q - 2) % 5 == 0 and (2 * q) % 5 == 0]))
# ---- O10: four findings of its Review 80 reading that main's review arc had marked 'not checked' (B1898's table): the
#      faulty line at the commit the seat read, and main's files now
import importlib.util
ROOT_ = ROOT
spots = [("F9", "frontier/B1895_the_mends_of_b1881_read_and_what_its_second_convention_is/verification/test_b1895_the_mends_of_b1881_read.py", 'blocks = [text] if f.endswith'),
         ("F11", "frontier/B862_global_form/global_form.py", "    if grid % need:"), ("F13", "tests/test_b1028_freedom_ledger.py", 'prose = " ".join('), ("F14", "tests/test_b734_m004_congruence.py", 'text = json.loads(text).get("claim_one_line", "")')]
then = {k: sum(1 for l in show("c40446392", f) if t in l) for k, f, t in spots}
notes = {"F6": "frontier/B1891_the_foundation_at_version_1_66/verification/test_b1891_the_foundation_at_version_1_66.py", "F7": "frontier/B1894_review_79_the_second_round/verification/quote_check.py",
         "F9": spots[0][1], "F10": "frontier/B1861_the_closure_programme/verification/build_programme.py", "F13": spots[2][1], "F14": spots[3][1]}
named = {k: ("finding %s" % k) in (ROOT_ / f).read_text() for k, f in notes.items()}
spec = importlib.util.spec_from_file_location("gf", ROOT_ / "frontier/B862_global_form/global_form.py"); gf = importlib.util.module_from_spec(spec); spec.loader.exec_module(gf)
def tries(g):
    try: return "returns %d elements" % len(gf.kernel_exact(g, charges=(-2, 3)))
    except ValueError: return "raises"
print("O10: at c40446392 the four lines its findings F9, F11, F13, F14 quote stand in main's files: %s; main's files now carry a dated note naming each of the findings %s as mended: %s; main's kernel_exact at a grid of 0, -6, 6: %s"
      % (then, sorted(named), all(named.values()), [tries(g) for g in (0, -6, 6)]))
# ---- O11: its Review 79 second-round finding RF-01
roots209 = [x for x in range(209) if (x * x - x - 1) % 209 == 0]; two_to_200 = [N for N in range(2, 201) if sum(1 for x in range(N) if (x * x - x - 1) % N == 0) > 2]
print("O11: x^2 - x - 1 has the roots %s modulo 209 = 11 * 19, four of them; moduli up to 200 with more than two roots: %s" % (roots209, two_to_200))
