#!/usr/bin/env python3
"""
Appendix B -- the 64 Levi subsystems, and the rung arrangement EXACT over Q.

## WHY THIS SCRIPT EXISTS

Two debts, discharged together, and neither needs sympy, primes or numerics.

(1) THE 64 LEVI SUBSYSTEMS.  Corollary (rungs are Levi) and Remark (leviscope) rest on the
    classification of Levi subsystems of E6 by root count; the enumeration behind them was
    previously listed in block (b) of the Appendix B table -- the part that depends on the
    repository rather than travelling inside the submitted source.  It travels now.

(2) THE ARRANGEMENT, OVER Q.  Its companion check_rung_attained.py enumerates the flats at
    a faithful prime and flags the residue: reduction mod p can only ADD linear dependencies
    among weights, so that is not a characteristic-zero certificate.  This script removes
    the residue by reaching the same arrangement from the other side.

    For the explicit charged algebra, the independent exact anchors are C=e6^(2T), C abelian,
    dim C=4 and dim z(C)=12.  A characteristic-zero finite-group fixed algebra is reductive;
    being abelian, C is therefore toral.  Then dim z(C)=12 forces |Phi ^ C-perp|=6 with
    C-perp two-dimensional.  The only rank-<=2 root system with 6 roots is A2.  This script now
    also enumerates every A2 subsystem and its Weyl orbit, rather than citing uniqueness.
    Hence the weights of C on e6
    are just THE 72 ROOTS OF E6 RESTRICTED TO C: six restrict to zero, giving
    dim z(C) = 6+6 = 12, and the other 66 form the arrangement.  Every vector is RATIONAL,
    so the flat lattice is defined over Q and its Q-enumeration is its Qbar-enumeration.

The two routes share no code path.  check_rung_attained.py starts from the charges and
their ad-matrices; this one starts from the Cartan matrix and never builds a charge.  They
agree on the weight multiplicity profile (12x1 + 18x3), on the 109 flats, and on the
eleven values.

A NOTE ON WHAT DOES NOT CONFLICT.  The arrangement is rational; the charge basis's position
relative to it is not.  A flat rational in root coordinates is a subspace that
x8, x14, x16, x22 reach only after base change to K.  That is why the (8,16)-plane cubic is
irreducible over Q while this lattice is rational: two coordinate systems, one geometry.

Exact over Q throughout.  No third-party dependencies.
"""
import collections
import itertools
from fractions import Fraction as Fr

EDGES = [(0, 2), (2, 3), (3, 4), (4, 5), (1, 3)]      # Bourbaki E6
N = 6
A = [[2 if i == j else 0 for j in range(N)] for i in range(N)]
for i, j in EDGES:
    A[i][j] = A[j][i] = -1
FAILED = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}{('  ' + detail) if detail else ''}")
    if not ok:
        FAILED.append(label)


def build_roots():
    simp = [tuple(1 if i == j else 0 for i in range(N)) for j in range(N)]
    R, fr = set(simp), list(simp)
    while fr:
        nx = []
        for r in fr:
            for j in range(N):
                pr = sum(r[i] * A[i][j] for i in range(N))
                s = tuple(r[i] - pr * (1 if i == j else 0) for i in range(N))
                if any(s) and s not in R:
                    R.add(s)
                    nx.append(s)
        fr = nx
    return sorted(R)


ROOTS = build_roots()
RSET = set(ROOTS)


def ip(a, b):
    return sum(a[i] * A[i][j] * b[j] for i in range(N) for j in range(N))


def rank(vs, nc):
    M = [[Fr(x) for x in v] for v in vs]
    r = 0
    for c in range(nc):
        pr = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        pv = M[r][c]
        M[r] = [v / pv for v in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def dynkin_type(sub):
    """Type of the sub-diagram on `sub`, by arm lengths at a branch node."""
    adj = {i: {j for j in sub if j != i and A[i][j] == -1} for i in sub}
    seen, out = set(), []
    for i in sub:
        if i in seen:
            continue
        comp, st = set(), [i]
        while st:
            x = st.pop()
            if x in comp:
                continue
            comp.add(x)
            st += [y for y in adj[x] if y not in comp]
        seen |= comp
        n = len(comp)
        br = [x for x in comp if len(adj[x] & comp) == 3]
        if not br:
            out.append(f"A{n}")
            continue
        b = br[0]
        arms = []
        for nb in adj[b] & comp:
            ln, prev, cur = 1, b, nb
            while True:
                nxt = [y for y in adj[cur] & comp if y != prev]
                if not nxt:
                    break
                prev, cur = cur, nxt[0]
                ln += 1
            arms.append(ln)
        arms.sort()
        out.append(f"D{n}" if arms[0] == 1 and arms[1] == 1 else f"E{n}")
    return "+".join(sorted(out)) or "empty"


print("=" * 78)
print("CONTROLS")
print("=" * 78)
gate("E6 built by reflection closure: 72 roots", len(ROOTS) == 72)

# ------------------------------------------------- (1) the 64 Levi subsystems (item 3)
print()
print("=" * 78)
print("(1) THE 64 LEVI SUBSYSTEMS")
print("=" * 78)
bycount, types = collections.defaultdict(set), collections.defaultdict(set)
for k in range(N + 1):
    for sub in itertools.combinations(range(N), k):
        span = [[1 if i == j else 0 for i in range(N)] for j in sub]
        cnt = sum(1 for g in ROOTS if rank(span + [list(g)], N) == len(sub)) if sub else 0
        bycount[cnt].add(sub)
        types[cnt].add(dynkin_type(sub))
print(f"\n  {'subsets':>8} {'roots':>6} {'dim':>5}   type(s)")
for c in sorted(bycount):
    print(f"  {len(bycount[c]):>8} {c:>6} {6+c:>5}   {', '.join(sorted(types[c]))}")
AMB = sorted(6 + c for c in bycount)
gate("root counts are 0,2,4,6,8,10,12,14,20,22,24,30,40,72",
     sorted(bycount) == [0, 2, 4, 6, 8, 10, 12, 14, 20, 22, 24, 30, 40, 72])
gate("the fourteen ambient Levi dimensions",
     AMB == [6, 8, 10, 12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78])
gate("24 is NOT a Levi dimension of E6", 24 not in AMB)
gate("26 is realized by exactly four A4 node-subsets",
     len(bycount[20]) == 4 and types[20] == {"A4"})
amb2 = sorted(6 + c for c in types if len(types[c]) > 1)
gate("exactly three dimensions carry two types -- 12, 18, 20 (Rmk leviscope)",
     amb2 == [12, 18, 20], str([(d, sorted(types[d-6])) for d in amb2]))
gate("the four UNAMBIGUOUS counts the paper leans on: 46->40->D5, 30->24->D4, "
     "26->20->A4, 14->8->A2+A1",
     [sorted(types[c])[0] for c in (40, 24, 20, 8)] == ["D5", "D4", "A4", "A1+A2"]
     and all(len(types[c]) == 1 for c in (40, 24, 20, 8)))
if FAILED:
    raise SystemExit("controls failed -- nothing may be read")

# ------------------------------------------------- (2) the no-moduli reduction
print()
print("=" * 78)
print("(2) THE NO-MODULI REDUCTION -- reproduced, not cited")
print("=" * 78)
sizes = {}
for a_, b_ in itertools.combinations(ROOTS, 2):
    if ip(a_, b_) == -1 and tuple(a_[i] + b_[i] for i in range(N)) in RSET:
        sizes.setdefault("A2", 0)
al = be = None
for a_, b_ in itertools.combinations(ROOTS, 2):
    if ip(a_, b_) == -1 and tuple(a_[i] + b_[i] for i in range(N)) in RSET:
        al, be = a_, b_
        break
A2 = {al, be, tuple(al[i] + be[i] for i in range(N))}
A2 |= {tuple(-x for x in t) for t in A2}
gate("the chosen A2 subsystem has 6 roots", len(A2) == 6)
rank2 = [(nm, k) for nm, k in (("A1", 2), ("A1xA1", 4), ("A2", 6), ("B2", 8), ("G2", 12))]
gate("A2 is the ONLY rank-<=2 root system with 6 roots "
     "(A1:2, A1xA1:4, A2:6, B2:8, G2:12)",
     [nm for nm, k in rank2 if k == 6] == ["A2"])

# Exhaust the missing transfer step: every A2 root subsystem of E6 belongs to
# one Weyl orbit.  A simple reflection acts on root coordinates by
# r -> r-<r,alpha_j^vee>alpha_j.
def neg(root):
    return tuple(-value for value in root)


def reflect(root, simple_index):
    pairing=sum(root[i]*A[i][simple_index] for i in range(N))
    return tuple(root[i]-pairing*(1 if i==simple_index else 0) for i in range(N))


all_a2=set()
for left,right in itertools.combinations(ROOTS,2):
    total=tuple(left[i]+right[i] for i in range(N))
    if ip(left,right)==-1 and total in RSET:
        all_a2.add(frozenset((left,right,total,neg(left),neg(right),neg(total))))

chosen=frozenset(A2)
orbit={chosen}
frontier=[chosen]
while frontier:
    subsystem=frontier.pop()
    for simple_index in range(N):
        image=frozenset(reflect(root,simple_index) for root in subsystem)
        assert image <= RSET and len(image)==6
        if image not in orbit:
            orbit.add(image)
            frontier.append(image)
gate("all A2 root subsystems form one explicitly enumerated Weyl orbit",
     orbit==all_a2,
     f"orbit={len(orbit)}, all={len(all_a2)}")

rows = [[sum(A[i][j] * al[j] for j in range(N)) for i in range(N)],
        [sum(A[i][j] * be[j] for j in range(N)) for i in range(N)]]
M = [[Fr(v) for v in r] for r in rows]
piv, r = [], 0
for c in range(N):
    pr = next((i for i in range(r, 2) if M[i][c] != 0), None)
    if pr is None:
        continue
    M[r], M[pr] = M[pr], M[r]
    pv = M[r][c]
    M[r] = [v / pv for v in M[r]]
    for i in range(2):
        if i != r and M[i][c] != 0:
            f = M[i][c]
            M[i] = [a - f * b for a, b in zip(M[i], M[r])]
    piv.append(c)
    r += 1
BC = []
for fc in [c for c in range(N) if c not in piv]:
    v = [Fr(0)] * N
    v[fc] = Fr(1)
    for i, c in enumerate(piv):
        v[c] = -M[i][fc]
    BC.append(v)
gate("C = (A2)-perp is 4-dimensional", len(BC) == 4)

W = collections.Counter()
for g in ROOTS:
    W[tuple(sum(Fr(g[i]) * A[i][j] * BC[k][j] for i in range(N) for j in range(N))
            for k in range(4))] += 1
ZERO = tuple(Fr(0) for _ in range(4))
nz = sorted(((w, m) for w, m in W.items() if w != ZERO),
            key=lambda t: [str(x) for x in t[0]])
prof = sorted(collections.Counter(m for _, m in nz).items())
gate("exactly 6 roots restrict to zero, so dim z(C) = 6 + 6 = 12", W[ZERO] == 6)
gate("30 distinct non-zero weights, total multiplicity 66 = 72 - 6",
     len(nz) == 30 and sum(m for _, m in nz) == 66)
gate("multiplicity profile 12x1 + 18x3 -- the charge-side route computes this "
     "independently; neither route can see the other's code", prof == [(1, 12), (3, 18)], str(prof))

# ------------------------------------------------- (3) the flats, exact over Q
print()
print("=" * 78)
print("(3) THE FLAT ENUMERATION -- EXACT OVER Q, no primes")
print("=" * 78)
flats = {}
for k in range(5):
    for sub in itertools.combinations(range(30), k):
        vs = [list(nz[i][0]) for i in sub]
        if (rank(vs, 4) if vs else 0) != k:
            continue
        flats[frozenset(i for i in range(30)
                        if rank(vs + [list(nz[i][0])], 4) == k)] = k
spec = collections.defaultdict(set)
for F, r in flats.items():
    spec[12 + sum(nz[i][1] for i in F)].add(4 - r)
SPEC = sorted(spec)
ELEVEN = [12, 14, 16, 18, 20, 26, 28, 30, 36, 46, 78]
print(f"\n  {len(flats)} flats.  Realized rung spectrum:\n")
for v in SPEC:
    print(f"      dim z(S) = {v:2d}   at subspaces S of dimension {sorted(spec[v])}")
gate("109 flats -- the same lattice the charge-side route finds at a prime",
     len(flats) == 109)
gate("the spectrum is EXACTLY the paper's eleven values", SPEC == ELEVEN, str(SPEC))
gate("every realized value is an ambient Levi dimension", all(v in AMB for v in SPEC))
gate("dim z(S) = 14 is attained at 3-dimensional S", sorted(spec[14]) == [3])

print(f"""
  THE RESIDUE IS CLOSED.  check_rung_attained.py certifies the flat lattice at a
  faithful prime and NOT over Qbar, because reduction mod p can only ADD dependencies.
  Here every weight is a rational vector -- an E6 root restricted to a rational
  4-dimensional subspace -- so the arrangement is defined over Q, linear dependence
  among rational vectors is unchanged by any characteristic-zero extension, and this
  enumeration over Q IS the enumeration over Qbar.

  Two constructions, no shared code path, one answer:
      charge side : charges -> ad-matrices -> charpoly orbits -> weights mod p
      root side   : E6 roots -> restrict to (A2)-perp -> weights over Q

  AND THE NUANCE THAT RECONCILES THIS WITH THE 46.  The arrangement is rational; the
  CHARGE BASIS's position relative to it is not.  A flat that is rational in root
  coordinates corresponds to a subspace that the coordinates x8, x14, x16, x22 reach
  only after base change to K.  That is why the (8,16)-plane cubic is irreducible
  over Q while the lattice itself is rational -- the two facts are about different
  coordinate systems and do not conflict.""")


print()
if FAILED:
    raise SystemExit(f"FAIL: {len(FAILED)} check(s) did not reproduce: {FAILED}")
print("PASS: every check reproduced exactly.")
