"""B1957: agy-exp's HARVEST REVIEW FOR MAIN (its status page at c4c48f541) and its note of 2026-11-18, the statements
main can decide by its own computation or by reading its own record (2026-11-18; data-free; nothing of the seat's run).
 R1  its recount of the register at the commit it read (c34a926a2), from main's own SUMMARY.json at that commit.
 R2  the words it quotes from main's harvest rows, each looked up in main's ledger at that commit.
 R3  its section 3: the four places where it says main's record is short or stale, at that commit.
 R4  the lines it names as carrying the withdrawn selection: its X-UNIFY-3 note and card at its head.
 R5  the scale witness with the prefactor kept as a variable: rank and nullity of the two rows on 21 columns.
 R6  a Hermitian matrix commuting with the clock and the shift of order 3 is a multiple of the identity.
 R7  the two copies of E6 in E8 (the centraliser of the colour su(3) and that of a second su(3)), their intersection, a
     copy of su(4) + su(2) + su(2) in the second containing colour, its intersection with the first, and the element
     s(e0-e4) s(e4-e1) s(e1-e3) s(e2-e5)."""
import itertools, json, pathlib, re, subprocess
from fractions import Fraction as Fr
import numpy as np, sympy as sp
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
show = lambda c, p: subprocess.run(["git", "show", "%s:%s" % (c, p)], capture_output=True, text=True, cwd=ROOT).stdout
READ, HEAD = "c34a926a2", "c4c48f541"
# R1
sm = json.loads(show(READ, "frontier/B1957_the_seats_claims_register/verification/SUMMARY.json")); lane = sm["lanes"]["agy-exp"]
fs = [v for k, v in sm["files"].items() if v["lane"] == "agy-exp"]
print("R1: at %s main's summary has for the lane: files %d, statements %d, pending %d; files with a pending statement %d, files with none %d (the seat: 88, 2,099, 2,027, 83 and 5)"
      % (READ, lane["files"], lane["statements"], lane["PENDING"], sum(1 for v in fs if v["PENDING"]), sum(1 for v in fs if not v["PENDING"])))
# R2
hl = show(READ, "docs/HARVEST_LEDGER.md"); row = lambda n: next((l for l in hl.split("\n") if l.startswith("| %d |" % n)), "")
Q = {1678: "NOTHING ELSE READ", 1710: "OWED", 1719: "", 1729: "OWED", 1734: "NOT READ", 1739: "NOT CHECKED", 1788: "", 1797: "RECEIVED", 1799: "not recomputed", 1815: "OWED", 1833: ""}
found = {n: (bool(row(n)) and (not w or w.lower() in row(n).lower())) for n, w in Q.items()}
print("R2: main's rows it cites exist and hold the words it quotes: %d of %d (%s)" % (sum(found.values()), len(found), ", ".join("%d %s" % (n, "yes" if v else "NO") for n, v in found.items())))
# R3
rec = json.loads(show(READ, "frontier/B1957_the_seats_claims_register/verification/records/web-wc2-05.json")); units = json.loads(show(READ, "frontier/B1957_the_seats_claims_register/verification/UNITS.json"))
b56 = show(READ, str(next((ROOT / "frontier").glob("B1956_*")).relative_to(ROOT)) + "/FINDINGS.md").split("\n"); seat = show(READ, "docs/seats/agy-exp.md")
print("R3: (a) the record web-wc2-05 leaves clauses to this lane's records: %s, and the theorems' file is in the register there: %s; (b) B1956's line 35 says no one has read X-FOUNDATION: %s, and row 1877 says no second reader: %s; (c) row 1875 names X-APEX's repairs of the two defects: %s; (d) the page's foot still waits on X-C1a to X-C1d: %s"
      % ("remain agy-exp" in (rec.get("how", "") + rec.get("note", "")), any("P781_MASK_SAFE" in u[0] for u in units["units"]), "no one" in b56[34].lower() or "nobody" in b56[34].lower(), "no second reader" in row(1877).lower(),
         "X-APEX" in row(1875) and "repair" in row(1875).lower(), "X-C1a to X-C1d" in seat.split("## What main is waiting for from you")[-1]))
# R4
note = show(HEAD, "relays/AGY_EXP_TO_PHYSICAL_AND_CC_2026-11-16_X_UNIFY_3_RESULTS.md").split("\n"); card = show(HEAD, next(p for p in show(HEAD, "relays/cards").split("\n") if "X-UNIFY-3" in p) if False else "relays/cards/" + next(l for l in subprocess.run(["git", "ls-tree", "--name-only", HEAD, "relays/cards/"], capture_output=True, text=True, cwd=ROOT).stdout.split("\n") if "X-UNIFY-3" in l).split("/")[-1]).split("\n")
has = lambda lines, a, b: any(re.search(r"bubble|pi/6|Sigma_H|M_H\^2|Level6Higgs|Level-`6`", l) for l in lines[a - 1:b])
print("R4: the selection stands in its X-UNIFY-3 note at line 19: %s, at lines 46 to 49: %s; in the card, among lines 25 to 30, at line(s): %s (the seat cites 25 to 29)" % (has(note, 19, 19), has(note, 46, 49), [i + 25 for i, l in enumerate(card[24:30]) if re.search(r"Part 3C|Level-`6`", l)]))
# R5
A = sp.zeros(2, 21); A[0, :20] = sp.ones(1, 20); A[1, 0] = 1; A[1, 19] = -1; A[1, 20] = -1
print("R5: with the prefactor's logarithm as a 21st variable the two rows have rank %d and nullity %d; without that column, on 20: rank %d and nullity %d" % (A.rank(), 21 - A.rank(), A[:, :20].rank(), 20 - A[:, :20].rank()))
# R6
w = np.exp(2j * np.pi / 3); X = np.roll(np.eye(3), 1, axis=0); Z = np.diag([1, w, w * w])
K = np.vstack([np.kron(np.eye(3), G) - np.kron(G.T, np.eye(3)) for G in (X, Z)]); print("R6: the matrices commuting with the clock and the shift of order 3 form a space of dimension %d; with the clock alone: %d" % (9 - np.linalg.matrix_rank(K), 9 - np.linalg.matrix_rank(K[9:])))
# R7
roots = []
for i, j in itertools.combinations(range(8), 2):
    for si in (1, -1):
        for sj in (1, -1):
            v = [Fr(0)] * 8; v[i] = Fr(si); v[j] = Fr(sj); roots.append(tuple(v))
roots += [tuple(Fr(s, 2) for s in sg) for sg in itertools.product((1, -1), repeat=8) if sum(1 for s in sg if s < 0) % 2 == 0]
dot = lambda a, b: sum(x * y for x, y in zip(a, b)); e = lambda i: tuple(Fr(int(k == i)) for k in range(8)); sub = lambda a, b: tuple(x - y for x, y in zip(a, b))
a2 = lambda tr: [sub(e(i), e(j)) for i in tr for j in tr if i != j]; COL, HID = a2((0, 1, 2)), a2((3, 4, 5))
cent = [r for r in roots if all(dot(r, c) == 0 for c in COL)]; gut = [r for r in roots if all(dot(r, c) == 0 for c in HID)]; both = [r for r in cent if r in set(gut)]
rk = lambda vs: sp.Matrix([list(v) for v in vs]).rank() if vs else 0
dim = lambda rts, cart: len(rts) + cart
print("R7: roots of the two centralisers: %d and %d (dimension %d each); common roots %d, common Cartan directions %d: the intersection has dimension %d" % (len(cent), len(gut), dim(cent, 8 - rk(COL)), len(both), 8 - rk(COL + HID), dim(both, 8 - rk(COL + HID))))
dims = set(); a1, a2_ = sub(e(0), e(1)), sub(e(1), e(2)); S = set(gut)
for a3 in gut:
    if dot(a2_, a3) == -1 and dot(a1, a3) == 0:
        span = sp.Matrix([list(a1), list(a2_), list(a3)]).T
        su4 = [r for r in gut if sp.Matrix.hstack(span, sp.Matrix(list(r))).rank() == 3]
        lr = [r for r in gut if all(dot(r, x) == 0 for x in su4)]
        g422 = su4 + lr; inter = [r for r in g422 if all(dot(r, c) == 0 for c in COL)]
        cart = sp.Matrix([list(v) for v in g422]).rank(); M = sp.Matrix([list(v) for v in g422]); N = sp.Matrix([list(v) for v in COL])
        common = cart - rk(COL)                                # the span of g422's roots contains colour's; what is orthogonal to colour inside it
        dims.add((len(su4), len(lr), len(g422) + cart, len(inter), common, len(inter) + common))
print("R7: for every su(4) in the second copy that contains colour (roots of su(4), roots commuting with it, dimension of their sum, its roots commuting with colour, its Cartan directions commuting with colour, dimension of the intersection): %s" % sorted(dims))
refl = lambda a: sp.eye(8) - 2 * sp.Matrix(list(a)) * sp.Matrix(list(a)).T / dot(a, a)
W = refl(sub(e(0), e(4))) * refl(sub(e(4), e(1))) * refl(sub(e(1), e(3))) * refl(sub(e(2), e(5)))
toF = lambda v: tuple(Fr(int(sp.Rational(x).p), int(sp.Rational(x).q)) for x in v); act = lambda r: toF(W * sp.Matrix(list(r))); order = next(k for k in range(1, 13) if W ** k == sp.eye(8))
a3 = next(a for a in gut if dot(a2_, a) == -1 and dot(a1, a) == 0); span = sp.Matrix([list(a1), list(a2_), list(a3)]).T
su4 = [r for r in gut if sp.Matrix.hstack(span, sp.Matrix(list(r))).rank() == 3]; lr = [r for r in gut if all(dot(r, x) == 0 for x in su4)]
fixes = []
for a3 in gut:
    if dot(a2_, a3) == -1 and dot(a1, a3) == 0:
        sp4 = sp.Matrix([list(a1), list(a2_), list(a3)]).T; s4 = [r for r in gut if sp.Matrix.hstack(sp4, sp.Matrix(list(r))).rank() == 3]
        fixes.append(all(act(r) == r for r in gut if all(dot(r, x) == 0 for x in s4)))
print("R7: the element has determinant %d and order %d; it carries the colour roots onto the second su(3)'s: %s; the first copy's roots onto the second's: %s; onto the first's: %s; it fixes each root commuting with the su(4), for %d of the %d choices of su(4); its square carries the first copy onto itself: %s"
      % (W.det(), order, {act(r) for r in COL} == set(HID), {act(r) for r in cent} == set(gut), {act(r) for r in cent} == set(cent), sum(fixes), len(fixes), {toF(W * W * sp.Matrix(list(r))) for r in cent} == set(cent)))
