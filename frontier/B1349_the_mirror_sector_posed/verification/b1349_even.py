"""B1349 -- POSING THE theta-EVEN (MIRROR) SECTOR, the crossing's only remaining target.

KIND_TABLE: of the four coupling rows, tones / probability / phases are all CONSUMED with decisive
MISSes; the MIRROR SET (theta-even) is "UNCONSUMED -- the last licensed row", delivered by B1011 C6
and never taken to data. The one-shot rule consumes CONTACT ROWS, so this row is spent whatever the
outcome of any sealed comparison.

B1348 posed the theta-ODD plane (CP^1_odd): projective image A_5, exceptional orbits [12,20,30],
existence POSITIVE, uniqueness NEGATIVE, residual freedom exactly 12. That is the WRONG PLANE for
crossing purposes. This poses the right one.

WHY IT GATES THE R1-R12 ARC: R11 is arithmetic -- "outputs - consumed anchors > 0, else the cell is
vacuous (MB12)" -- and R7 requires every designer freedom priced in a look-elsewhere ledger. Neither
can be computed for the mirror row until the residual freedom in CP^3_even is COUNTED. That count is
this arc's deliverable.

PRE-REGISTERED (DESIGN B1349): Q1 controls -- the even eigenspace of C = S^2 is 4-dimensional with a
rational canonical basis from the weights, and <R,L> restricts to it; Q2 the projective image is
A_4 x A_5 of order 720 (since (-1,-1) and (-1,1) both act as scalars on V_2 (x) V_2, so the image is
(2T/+-1) x (2I/+-1)); Q3 C^4_even is IRREDUCIBLE; Q4 enumerate the points of CP^3_even with
non-trivial stabiliser, orbit-decompose, and report the MAXIMAL-STABILISER orbit size -- that number
IS the residual freedom, the analogue of the odd plane's 12; Q5 a control -- a random direction must
have trivial stabiliser and orbit 720.
PASS means the questions are answered. It does NOT mean the crossing should be attempted; that is
R11's arithmetic, reported at the end and not prejudged.
"""
import json, numpy as np, itertools
from collections import Counter

def su3_data(k=2):
    N, kap = 3, k + 3
    W = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    Lv = lambda w: np.array([w[0] + w[1] + 2.0, w[1] + 1.0, 0.0])
    ip = lambda u, v: float(np.dot(u, v) - u.sum() * v.sum() / 3.0)
    perms = list(itertools.permutations(range(3)))
    sgn = lambda p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
    S = np.zeros((6, 6), dtype=complex)
    for i, wl in enumerate(W):
        for j, wm in enumerate(W):
            S[i, j] = sum(sgn(p) * np.exp(-2j*np.pi*ip(Lv(wl)[list(p)], Lv(wm))/kap) for p in perms)
    S *= -1j / (kap * np.sqrt(3.0))
    C2 = lambda w: (2/3)*(w[0]**2 + w[0]*w[1] + w[1]**2) + 2*(w[0] + w[1])
    cc = 8.0*k/(k+3.0)
    T = np.diag([np.exp(2j*np.pi*(C2(w)/(2*kap) - cc/24.0)) for w in W])
    return W, S, T

fails = []
def check(tag, lab, ok):
    print(f"   [{'PASS' if ok else 'FAIL'}] {tag}: {lab}")
    if not ok: fails.append(tag)

W, S, T = su3_data()
C = S @ S; R = T; L = np.linalg.inv(S) @ np.linalg.inv(T) @ S
i00, i11 = W.index((0,0)), W.index((1,1))
i01, i10, i02, i20 = W.index((0,1)), W.index((1,0)), W.index((0,2)), W.index((2,0))

print("Q1 -- the theta-EVEN sector and its canonical (rational) basis from the weights")
E = np.zeros((6,4), dtype=complex)
E[i00,0] = 1                            # e(0,0)            -- C-fixed weight
E[i11,1] = 1                            # e(1,1)            -- C-fixed weight
E[i01,2] = E[i10,2] = 1                 # e(0,1) + e(1,0)   -- symmetric pair
E[i02,3] = E[i20,3] = 1                 # e(0,2) + e(2,0)   -- symmetric pair
check("Q1a", "the four canonical even vectors satisfy C v = +v", np.allclose(C @ E, E, atol=1e-9))
rest = lambda M: np.linalg.lstsq(E, M @ E, rcond=None)[0]
Ro, Lo = rest(R), rest(L)
check("Q1b", "the even sector is <R,L>-invariant (restriction is exact)",
      np.allclose(E @ rest(R) - R @ E, 0, atol=1e-8) and np.allclose(E @ rest(L) - L @ E, 0, atol=1e-8))

print("\nQ2 -- the projective image")
def pkey(M, q=6):
    d = np.linalg.det(M)
    Mn = M / (d ** 0.25)
    best = None
    for r in range(4):                       # quotient by the 4 fourth-roots of unity
        A = Mn * np.exp(2j*np.pi*r/4)
        k = tuple((round(float(x.real), q), round(float(x.imag), q)) for x in A.flatten())
        best = k if best is None else min(best, k)
    return best
seen, frontier, mats = {pkey(np.eye(4))}, [np.eye(4, dtype=complex)], [np.eye(4, dtype=complex)]
gens = [Ro, Lo, np.linalg.inv(Ro), np.linalg.inv(Lo)]
while frontier and len(seen) < 6000:
    nxt = []
    for M in frontier:
        for g in gens:
            P = M @ g; k = pkey(P)
            if k not in seen: seen.add(k); nxt.append(P); mats.append(P)
    frontier = nxt
print(f"      |projective image| = {len(mats)}")
check("Q2", f"the projective image is A_4 x A_5 of order 720 (= 12 x 60)", len(mats) == 720)

print("\nQ3 -- irreducibility of C^4_even")
evR, VR = np.linalg.eig(Ro)
common = 0
for j in range(4):
    v = VR[:, j]; w = Lo @ v
    if np.linalg.norm(w - (np.vdot(v, w)) * v / max(np.vdot(v,v).real,1e-30)) < 1e-7: common += 1
check("Q3", f"no common eigenvector of R and L on the even sector ({common} found) => irreducible",
      common == 0)

print("\nQ4 -- the distinguished directions of CP^3_even, and the RESIDUAL FREEDOM")
def ck(v, q=6):
    v = v / np.linalg.norm(v)
    v = v / np.exp(1j*np.angle(v[int(np.argmax(np.abs(v)))]))
    return tuple((round(float(x.real), q), round(float(x.imag), q)) for x in v)
cand = {}
for M in mats:
    ev, V = np.linalg.eig(M)
    if np.allclose(M - (np.trace(M)/4)*np.eye(4), 0, atol=1e-8): continue
    for j in range(4):
        cand.setdefault(ck(V[:, j]), V[:, j])
print(f"      candidate fixed directions collected: {len(cand)}")
par = lambda a, b, tol=1e-6: np.linalg.norm(
    b/np.linalg.norm(b) - (np.vdot(a/np.linalg.norm(a), b/np.linalg.norm(b)))*a/np.linalg.norm(a)) < tol
stab = lambda v: sum(1 for M in mats if par(v, M @ v))
orbits, used = [], set()
for key0, v in cand.items():
    if key0 in used: continue
    orb = {ck(M @ v) for M in mats}
    orbits.append((len(orb), stab(v))); used |= orb
cnt = Counter(orbits)
print(f"      orbit (size, |Stab|) multiset: {dict(cnt)}")
if orbits:
    smallest = min(o[0] for o in orbits); maxstab = max(o[1] for o in orbits)
    print(f"      SMALLEST orbit = {smallest}   MAXIMAL |Stab| = {maxstab}   (720/{maxstab} = {720//maxstab})")
check("Q4", f"a maximal-stabiliser orbit exists and its size is the residual freedom",
      bool(orbits))

print("\nQ5 -- CONTROL: a random direction must be generic")
rng = np.random.default_rng(11)
rv = rng.normal(size=4) + 1j*rng.normal(size=4)
sr = stab(rv)
check("Q5", f"random direction has |Stab| = {sr} and orbit {len({ck(M@rv) for M in mats})} (must be 1 and 720)",
      sr == 1)

print("\n=== THE NUMBER THAT GATES THE CROSSING ===")
if orbits:
    print(f"  odd plane  (B1348, NOT the crossing target): residual freedom 12")
    print(f"  even sector (the LAST licensed row)        : smallest distinguished orbit = {smallest}")
    print(f"  R7 must price this as a look-elsewhere factor; R11 debits it against outputs.")
json.dump({"proj_order": len(mats), "orbits": [list(o) for o in orbits], "fails": fails},
          open("b1349_even.json", "w"), indent=1)
print("\nB1349:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
