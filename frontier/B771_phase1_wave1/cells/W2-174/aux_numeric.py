"""W2-174 auxiliary fast numeric verification (numpy; complements compute.py's
symbolic gates A1-C6 which all PASSED before this ran).  Computes in-cell:
  - the two witness reps numerically (all 24 elements, 27x27)
  - homomorphism all 576 pairs; injectivity / kernel
  - characters on the 7 classes; exact-integer-snapped decompositions
  - non-reality (9w at an order-3 class) for both witnesses
  - Sym^3 trivial multiplicities (V and V*)
  - nondegeneracy: dim Stab_{gl(27)}(I3) = 78, seeds 0 and 1, gap reported
Runs in seconds.  Same math as compute.py Parts D-E."""
import itertools, numpy as np

w = np.exp(2j * np.pi / 3)

def qmul(a, b):
    a0, a1, a2, a3 = a; b0, b1, b2, b3 = b
    return (a0*b0 - a1*b1 - a2*b2 - a3*b3, a0*b1 + a1*b0 + a2*b3 - a3*b2,
            a0*b2 - a1*b3 + a2*b0 + a3*b1, a0*b3 + a1*b2 - a2*b1 + a3*b0)
def qinv(a): return (a[0], -a[1], -a[2], -a[3])
def order(g):
    p, one = g, (1., 0., 0., 0.)
    for k in range(1, 13):
        if max(abs(p[i]-one[i]) for i in range(4)) < 1e-9: return k
        p = qmul(p, g)

elts = []
for pos in range(4):
    for s in (1., -1.):
        v = [0., 0., 0., 0.]; v[pos] = s; elts.append(tuple(v))
for s in itertools.product((0.5, -0.5), repeat=4):
    elts.append(tuple(s))
assert len(elts) == 24
def key(g): return tuple(round(2*c) for c in g)
IDX = {key(g): i for i, g in enumerate(elts)}

# classes
seen, classes = set(), []
for g in elts:
    if key(g) in seen: continue
    cl = {}
    for t in elts:
        r = qmul(qmul(t, g), qinv(t)); cl[key(r)] = r
    classes.append(sorted(cl.values())); seen |= set(cl.keys())
classes.sort(key=lambda c: (order(c[0]), c[0][0]))
reps = [c[0] for c in classes]; sizes = [len(c) for c in classes]
orders = [order(r) for r in reps]
assert len(classes) == 7 and sum(sizes) == 24

Q8 = [g for g in elts if all(abs(c) in (0.0, 1.0) for c in g)]
assert len(Q8) == 8
g3 = next(g for g in elts if order(g) == 3)
def coset_key(g): return frozenset(key(qmul(g, q)) for q in Q8)
COS = {coset_key((1.,0.,0.,0.)): 0, coset_key(g3): 1, coset_key(qmul(g3, g3)): 2}
def eps(g): return COS[coset_key(g)]
assert all((eps(qmul(g, h)) - eps(g) - eps(h)) % 3 == 0 for g in elts for h in elts)

def rho2(q):
    a, b, c, d = q
    return np.array([[a + 1j*b, c + 1j*d], [-c + 1j*d, a - 1j*b]])
def rho3(g):
    m = np.zeros((3, 3), complex); e = eps(g)
    m[0, 0] = w**e; m[1:, 1:] = (w**e) * rho2(g)
    return m
def rotR(q):
    a, b, c, d = q
    return np.array([[a*a+b*b-c*c-d*d, 2*(b*c-a*d), 2*(b*d+a*c)],
                     [2*(b*c+a*d), a*a-b*b+c*c-d*d, 2*(c*d-a*b)],
                     [2*(b*d-a*c), 2*(c*d+a*b), a*a-b*b-c*c+d*d]], dtype=complex)

I3m = np.eye(3)
def P_of(A):
    P = np.zeros((27, 27), complex)
    P[0:9, 0:9] = np.kron(A, I3m)          # (A, I, I): kron(A, conj(I)) etc.
    P[9:18, 9:18] = np.eye(9)
    P[18:27, 18:27] = np.kron(I3m, A.conj())
    return P

W2T = {key(g): (w**eps(g)) * P_of(rho3(g)) for g in elts}
WA4 = {key(g): (w**eps(g)) * P_of(rotR(g)) for g in elts}

ok = True
def gate(name, cond):
    global ok
    print(("PASS  " if cond else "FAIL  ") + name)
    ok = ok and cond

gate("N1: W2T hom all 576 pairs (<1e-10)",
     max(np.abs(W2T[key(qmul(g, h))] - W2T[key(g)] @ W2T[key(h)]).max()
         for g in elts for h in elts) < 1e-10)
gate("N2: WA4 hom all 576 pairs (<1e-10)",
     max(np.abs(WA4[key(qmul(g, h))] - WA4[key(g)] @ WA4[key(h)]).max()
         for g in elts for h in elts) < 1e-10)
gate("N3: W2T injective (kernel trivial)",
     sorted(k for k in W2T if np.abs(W2T[k] - np.eye(27)).max() < 1e-9) == [key((1.,0,0,0))])
gate("N4: ker WA4 = {+-1} (faithful A4)",
     sorted(k for k in WA4 if np.abs(WA4[k] - np.eye(27)).max() < 1e-9)
     == sorted([key((1.,0,0,0)), key((-1.,0,0,0))]))

# characters and decompositions over the exact 2T table
def snap(z, tol=1e-8):
    r = round(z.real); assert abs(z.real - r) < tol and abs(z.imag) < tol, z
    return int(r)
chi2T = [np.trace(W2T[key(r)]) for r in reps]
chiA4 = [np.trace(WA4[key(r)]) for r in reps]
irr = {'1': lambda g: 1.0, "1'": lambda g: w**eps(g), "1''": lambda g: w**(2*eps(g)),
       '2': lambda g: 2*g[0], "2'": lambda g: 2*g[0]*w**eps(g),
       "2''": lambda g: 2*g[0]*w**(2*eps(g)), '3': lambda g: 4*g[0]**2 - 1}
def dec(chi):
    return {nm: snap(sum(sizes[i]*chi[i]*np.conj(f(reps[i])) for i in range(7)) / 24)
            for nm, f in irr.items()}
d2T, dA4 = dec(chi2T), dec(chiA4)
print("  orders:", orders, "eps:", [eps(r) for r in reps], "sizes:", sizes)
print("  chi 27|W2T:", np.round(chi2T, 6))
print("  chi 27|WA4:", np.round(chiA4, 6))
print("  27|W2T =", {k: v for k, v in d2T.items() if v}, " 27|WA4 =", {k: v for k, v in dA4.items() if v})
gate("N5: 27|W2T = 3.1+9.1'+3.1''+3.2+0.2'+3.2''  (n1,n2)=(9,0)",
     d2T == {'1': 3, "1'": 9, "1''": 3, '2': 3, "2'": 0, "2''": 3, '3': 0})
gate("N6: 27|WA4 = 9.1' + 6.3 (no spinor irreps; genuine A4 assembly)",
     dA4 == {'1': 0, "1'": 9, "1''": 0, '2': 0, "2'": 0, "2''": 0, '3': 6})
gate("N7: DISCRIMINATING FACT 2T: chi non-real, = 9w at an order-3 class",
     any(abs(chi2T[i].imag) > 0.1 for i in range(7)) and
     any(orders[i] == 3 and (abs(chi2T[i] - 9*w) < 1e-9 or abs(chi2T[i] - 9*np.conj(w)) < 1e-9)
         for i in range(7)))
gate("N8: DISCRIMINATING FACT A4: chi non-real, = 9w at an order-3 class",
     any(abs(chiA4[i].imag) > 0.1 for i in range(7)) and
     any(orders[i] == 3 and (abs(chiA4[i] - 9*w) < 1e-9 or abs(chiA4[i] - 9*np.conj(w)) < 1e-9)
         for i in range(7)))

# Sym^3 trivial multiplicities
def sym3(chifun):
    tot = 0
    for g in elts:
        g2 = qmul(g, g); g3_ = qmul(g2, g)
        tot += (chifun(g)**3 + 3*chifun(g)*chifun(g2) + 2*chifun(g3_)) / 6
    return snap(tot / 24)
def chifun_of(Wdict): return lambda g: np.trace(Wdict[key(g)])
f2, f4 = chifun_of(W2T), chifun_of(WA4)
s = (sym3(f2), sym3(lambda g: np.conj(f2(g))), sym3(f4), sym3(lambda g: np.conj(f4(g))))
print("  Sym^3 trivial mult (2T V, 2T V*, A4 V, A4 V*):", s)
gate("N9: (Sym^3 V)^G, (Sym^3 V*)^G >= 1 for both witnesses (invariant cubic present)",
     all(x >= 1 for x in s))

# nondegeneracy of I3: dim Stab = 78, 2 seeds
def cof(M): return np.linalg.det(M) * np.linalg.inv(M).T
def I3_num(x):
    M1, M2, M3 = x[:9].reshape(3, 3), x[9:18].reshape(3, 3), x[18:].reshape(3, 3)
    return (np.linalg.det(M1) + np.linalg.det(M2) + np.linalg.det(M3)
            - np.trace(M1 @ M2 @ M3))
GIk, GTk = key((0., 1., 0., 0.)), key((.5, .5, .5, .5))
for seed in (0, 1):
    rng = np.random.default_rng(seed)
    rows = np.empty((900, 729), complex); pts = []
    for si in range(900):
        M = [rng.standard_normal((3, 3)) + 1j*rng.standard_normal((3, 3)) for _ in range(3)]
        grad = np.concatenate([(cof(M[0]) - (M[1] @ M[2]).T).ravel(),
                               (cof(M[1]) - (M[2] @ M[0]).T).ravel(),
                               (cof(M[2]) - (M[0] @ M[1]).T).ravel()])
        x = np.concatenate([m.ravel() for m in M])
        rows[si] = np.outer(grad, x).ravel(); pts.append(x)
    sv = np.linalg.svd(rows, compute_uv=False)
    rank = int((sv > sv[0]*1e-9).sum()); nullity = 729 - rank
    gap = sv[rank-1]/sv[rank] if rank < len(sv) else np.inf
    print(f"  [seed {seed}] Stab(I3) nullity = {nullity} (expect 78); gap ratio = {gap:.3e}")
    gate(f"N10(seed {seed}): dim Stab(I3) = 78 = dim e6, gap > 1e6 (nondegenerate)",
         nullity == 78 and gap > 1e6)
    inv2 = all(abs(I3_num(W2T[k] @ x) - I3_num(x)) < 1e-9*max(1, abs(I3_num(x)))
               for k in (GIk, GTk) for x in pts[:4])
    inv4 = all(abs(I3_num(WA4[k] @ x) - I3_num(x)) < 1e-9*max(1, abs(I3_num(x)))
               for k in (GIk, GTk) for x in pts[:4])
    gate(f"N11(seed {seed}): I3 numerically invariant under both witnesses at random pts",
         inv2 and inv4)

print("\nAUX VERDICT:", "ALL PASS -> RESOLVED-A (both omega-window groups realized)" if ok
      else "FAILURE -> see gates")
