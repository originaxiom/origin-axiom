"""agy-002's A2-M51 (its branch at 8203f3987), section 1, on main's own construction of frame D1's Higgs direction h* (B1957's
checks/p873_zero_directions.py: the ground plane of U = T S^-1 T^-1 S on six modes, the direction with zeros at modes 2, 3, 4)
and main's own coupling Ymp (copied from that script).  Nothing of the seat's is run.
 R1  at the mark (a, b) = (2/5, 4/5), up sector, unshifted lift: G = M M^dagger with M = sum_k Y_k h*_k; the seat's involution
     R* = [[0, 0, -e^{i pi/3}], [0, 1, 0], [-e^{-i pi/3}, 0, 0]]: R* Hermitian, R*^2 = I, and |[R*, G]| / |G| at several tau.
 R2  the seat's u_- = (1, 0, e^{-i pi/3})/sqrt 2: |G u_- - (u_-^dagger G u_-) u_-| / |G| at the same tau.
 R3  the same two at a point that is not the mark, and in the down sector at the mark (a control: no identity is claimed there)."""
import functools
from fractions import Fraction as Fr
import numpy as np, mpmath as mp
print = functools.partial(print, flush=True)
k6 = np.arange(6); T6 = np.diag(np.exp(1j * np.pi * k6 ** 2 / 6)); S6 = np.exp(-1j * np.pi / 4) * np.exp(-2j * np.pi * np.outer(k6, k6) / 6) / np.sqrt(6)
inv = np.linalg.inv; U = T6 @ inv(S6) @ inv(T6) @ S6; ev, Vv = np.linalg.eig(U); ph = np.angle(ev) / np.pi
vp = Vv[:, int(np.argmin(abs(ph - 1 / 6)))]; vm = Vv[:, int(np.argmin(abs(ph + 1 / 6)))]; vp, vm = vp / np.linalg.norm(vp), vm / np.linalg.norm(vm)
rho = vp / vm; h = vp - rho[2] * vm; h = h / np.linalg.norm(h)
print("h*: zero entries at modes %s; moduli %s" % ([k for k in range(6) if abs(h[k]) < 1e-12], [round(abs(x), 6) for x in h]))
mp.mp.dps = 50
DELTA = {"up": 5, "down": -1, "lepton": -9}
def Ymp(tau, xi):                                   # copied from checks/p873_zero_directions.py
    y = mp.im(tau); pre = (3 * y) ** mp.mpf("0.25"); res = {}
    for i in range(3):
        for j in range(3):
            for m in (0, 1):
                kk = (i + j + 1 + 3 * m) % 6; aa = mp.mpf((i - j + 3 * m) % 6) / 6; n0 = mp.nint(aa + mp.im(xi) / y); s = mp.mpf(0)
                for n_ in range(-25, 26):
                    n = n_ + aa - n0; s += mp.exp(6j * mp.pi * xi * mp.im(xi) / y + 6j * mp.pi * n ** 2 * tau + 12j * mp.pi * n * xi)
                res[(i, j, kk)] = pre * mp.exp(2j * mp.pi * kk / 6) * s
    return res
# h* at 50 digits: the same construction in mpmath (U = T S^-1 T^-1 S on six modes; the eigenvectors of phase +-1/6; the
# combination vanishing at mode 2), so that the identity is tested beyond double precision
K = range(6); T6m = mp.diag([mp.exp(1j * mp.pi * k * k / 6) for k in K])
S6m = mp.matrix([[mp.exp(-1j * mp.pi / 4) * mp.exp(-2j * mp.pi * j * k / 6) / mp.sqrt(6) for k in K] for j in K])
Um = T6m * mp.inverse(S6m) * mp.inverse(T6m) * S6m; E, ER = mp.eig(Um)
def pick(target):
    i = min(range(6), key=lambda i: abs(mp.arg(E[i]) / mp.pi - target)); v = ER[:, i]; return v / mp.norm(v)
vpm, vmm = pick(mp.mpf(1) / 6), pick(-mp.mpf(1) / 6); hm = vpm - (vpm[2] / vmm[2]) * vmm; hm = hm / mp.norm(hm)
hz = [mp.mpc(0) if abs(hm[k]) < mp.mpf(10) ** -40 else hm[k] for k in range(6)]
print("h* at 50 digits: zero at modes %s; moduli %s; agrees with the double-precision h* up to a phase: %s" % ([k for k in K if hz[k] == 0], [mp.nstr(abs(x), 8) for x in hz], abs(abs(sum(mp.conj(hz[k]) * complex(h[k]) for k in K)) - 1) < 1e-12))
def G(tau, a, b, sec):
    fm = lambda q: mp.mpf(q.numerator) / q.denominator
    xi = mp.mpf(DELTA[sec]) * (fm(a) * tau + fm(b)) / 2; Y = Ymp(tau, xi)
    M = mp.matrix([[sum(Y.get((i, j, k), 0) * hz[k] for k in range(6)) for j in range(3)] for i in range(3)])
    return M * M.H
w = mp.exp(1j * mp.pi / 3)
R = mp.matrix([[0, 0, -w], [0, 1, 0], [-mp.conj(w), 0, 0]]); um = mp.matrix([1, 0, mp.conj(w)]) / mp.sqrt(2)
print("R1: R* Hermitian: %s; R*^2 = I: %s" % (mp.mnorm(R - R.H, 1) < mp.mpf(10) ** -45, mp.mnorm(R * R - mp.eye(3), 1) < mp.mpf(10) ** -45))
def test(lab, a, b, sec):
    out = []
    for tau in (mp.mpc("0.13", "1.7"), mp.mpc("0.37", "0.9"), mp.mpc("-0.21", "3"), mp.mpc("0.5", "0.6"), mp.mpc("0.13", "8")):
        g = G(tau, a, b, sec); n = mp.mnorm(g, 1)
        c = mp.mnorm(R * g - g * R, 1) / n; v = g * um; lam = (um.H * v)[0]; e = mp.norm(v - lam * um) / n
        out.append("tau %s: commutator %s, eigenvector residual %s" % (mp.nstr(tau, 3), mp.nstr(c, 2), mp.nstr(e, 2)))
    print("%s: %s" % (lab, "; ".join(out)))
test("R1/R2 at the mark, up", Fr(2, 5), Fr(4, 5), "up")
test("R3 up at (1/5, 2/5), not the mark", Fr(1, 5), Fr(2, 5), "up")
import itertools
worst = {}
for i5, j5 in itertools.product(range(5), repeat=2):
    if (i5, j5) == (0, 0): continue
    for la, lb in itertools.product((0, 1), repeat=2):
        g = G(mp.mpc("0.13", "1.7"), Fr(i5, 5) + la, Fr(j5, 5) + lb, "up"); n = mp.mnorm(g, 1)
        worst[(i5, j5, la, lb)] = mp.mnorm(R * g - g * R, 1) / n
hold = sorted(k for k, v in worst.items() if v < mp.mpf(10) ** -40)
print("R4: up sector, the 24 points of order 5 and four lifts at tau = 0.13 + 1.7i: the commutator vanishes (below 1e-40) in %d of 96 cases: points (5a, 5b, lift) %s" % (len(hold), hold))
test("R3 control, down at the mark", Fr(2, 5), Fr(4, 5), "down")
gen = []
for a, b in ((Fr(123, 1000), Fr(456, 1000)), (Fr(7, 11), Fr(3, 13)), (Fr(1, 3), Fr(1, 7))):
    for sec in ("up", "down", "lepton"):
        g = G(mp.mpc("0.13", "1.7"), a, b, sec); n = mp.mnorm(g, 1); gen.append("%s at (%s, %s): %s" % (sec, a, b, mp.nstr(mp.mnorm(R * g - g * R, 1) / n, 2)))
print("R5: points not of order 5, tau = 0.13 + 1.7i, the commutator: %s" % "; ".join(gen))
# R6: the seat's displayed matrix M(h*) (A = 1/sqrt 2, B = e^{i pi/12}/2, p = e^{i pi/3}; Theta_c = exp(6 pi i xi Im xi / y)
# theta[c/6, 0](6 xi, 6 tau)) against main's M at the mark, up, h* normalised so that its mode-0 entry is real and positive
def theta_c(c, tau, xi):
    y = mp.im(tau); s = mp.mpf(0)
    for n in range(-25, 26):
        q = n + mp.mpf(c) / 6; s += mp.exp(6j * mp.pi * q * q * tau + 12j * mp.pi * q * xi)
    return mp.exp(6j * mp.pi * xi * mp.im(xi) / y) * s
tau = mp.mpc("0.13", "1.7"); xi = mp.mpf(5) * (mp.mpf(2) / 5 * tau + mp.mpf(4) / 5) / 2; Y = Ymp(tau, xi)
ph0 = hz[0] / abs(hz[0]); hn = [x / ph0 for x in hz]
Mm = mp.matrix([[sum(Y.get((i, j, k), 0) * hn[k] for k in range(6)) for j in range(3)] for i in range(3)]) / (3 * mp.im(tau)) ** mp.mpf("0.25")
A, Bq, p = 1 / mp.sqrt(2), mp.exp(1j * mp.pi / 12) / 2, mp.exp(1j * mp.pi / 3); T = [theta_c(c, tau, xi) for c in range(6)]
Ms = mp.matrix([[p * Bq * T[0], Bq * T[2] / p, A * T[1]], [Bq * T[4] / p, A * T[3], p * Bq * T[2]], [A * T[5], p * Bq * T[4], Bq * T[0] / p]])
print("R6: main's h* normalised: %s; the seat's matrix against main's at the mark, up, tau = 0.13 + 1.7i: largest entry difference %s (largest entry %s); Theta_5 - Theta_1 %s, Theta_4 - Theta_2 %s"
      % ([mp.nstr(x, 6) for x in hn], mp.nstr(max(abs(Mm[i, j] - Ms[i, j]) for i in range(3) for j in range(3)), 2), mp.nstr(max(abs(Ms[i, j]) for i in range(3) for j in range(3)), 3), mp.nstr(abs(T[5] - T[1]), 2), mp.nstr(abs(T[4] - T[2]), 2)))
Rf = mp.matrix([[0, 0, w], [0, 1, 0], [mp.conj(w), 0, 0]]); g = G(tau, Fr(2, 5), Fr(4, 5), "up")
print("R7: the seat's falsifier PFA2M51-1, the sign of R*'s corner flipped: |[R, G]| / |G| = %s" % mp.nstr(mp.mnorm(Rf * g - g * Rf, 1) / mp.mnorm(g, 1), 3))
# C1: custody of A2-M51 (the seat's branch read as text; nothing run): commit order card < script < outputs < note, and the hashes
import subprocess, hashlib
git = lambda *a: subprocess.run(["git", *a], capture_output=True, text=True).stdout
t = {c: int(git("show", "-s", "--format=%ct", c).strip()) for c in ("ac8392b59", "19ca41b14", "5f857aa6b", "8203f3987")}
sha = lambda c, f: hashlib.sha256(subprocess.run(["git", "show", "%s:%s" % (c, f)], capture_output=True).stdout).hexdigest()
man = lambda c, f: dict((l.split()[1], l.split()[0]) for l in git("show", "%s:%s" % (c, f)).split("\n") if l.strip())
ms, mo = man("8203f3987", "relays/a2_m51/SCRIPT_SHA256.txt"), man("8203f3987", "relays/a2_m51/OUTPUT_SHA256.txt")
print("C1: order card %s, script %s, outputs %s, note %s (seconds from the card): %s; the script at its sealing commit and at 8203f3987 matches its manifest: %s, %s; the outputs at 5f857aa6b match theirs: %s; the outputs absent at the script's commit: %s"
      % ("ac8392b59", "19ca41b14", "5f857aa6b", "8203f3987", [t[c] - t["ac8392b59"] for c in t], all(sha("19ca41b14", f) == h for f, h in ms.items()), all(sha("8203f3987", f) == h for f, h in ms.items()), all(sha("5f857aa6b", f) == h for f, h in mo.items()), all(git("cat-file", "-t", "19ca41b14:" + f).strip() == "" for f in mo)))
# S1: its status page's totals for its four lanes at main's f1efc59dd, and the record placements it lists
V = "frontier/B1957_the_seats_claims_register/verification/"
sm = __import__("json").loads(git("show", "f1efc59dd:" + V + "SUMMARY.json"))["lanes"]; K = ("files", "statements", "VERIFIED", "REFUTED", "CONDITIONAL", "PARTIAL", "SUPERSEDED", "NOTED", "PENDING")
four = ("agy-002-verify", "agy-002-endgame", "agy-002-closure", "agy-002-foundations")
print("S1: agy-002's four lanes at f1efc59dd: %s; by lane: %s" % ({k: sum(sm[l][k] for l in four) for k in K}, {l: [sm[l][k] for k in K] for l in four}))
rec = lambda r: __import__("json").loads(git("show", "f1efc59dd:" + V + "records/%s.json" % r))
want = {"agy002-es-05": ["AGY002_ENDGAME_V2_MASTER_SYNTHESIS:30"], "agy002v-m33-04": ["M33_SM_C13_ORDER5_SECOND_COMPUTATION:33", "M33_SM_C13_ORDER5_SECOND_COMPUTATION:34"],
        "agy002-c5-02-r2n": [":13", ":19", ":20"], "agy002-c5-02-r3n": [":16"], "agy002-g6-01-r3p": [":8", ":9", ":10", ":13", ":22"]}
print("S1: the placements it lists, at f1efc59dd: %s" % {r: (rec(r)["verdict"], all(any(u.endswith(x) for u in rec(r)["units"]) for x in xs)) for r, xs in want.items()})
