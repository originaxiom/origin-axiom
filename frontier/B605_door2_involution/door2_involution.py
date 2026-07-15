"""B605 — Door 2 settled mechanically: the fixed-set type of the
orientation-reversing symmetries of the figure-eight complement
(failure-enforcing on gates; the census is the deliverable).

CONTEXT (the incoming handoff, verify-don't-trust): a seat argued from
the 2-regular-ideal-tetrahedra decomposition that the amphichiral
involution tau is a REFLECTION (2-dim totally geodesic Fix), excluding
point-inversion via the tetrahedron point group. GAP IDENTIFIED: that
argument covers symmetries FIXING each tetrahedron; an involution
SWAPPING the two tetrahedra can have isolated fixed points on the shared
faces (locally rotation-by-pi x normal-flip = the -I model). So the type
must be computed, not inferred.

THE MECHANICAL ROUTE (exact, from the step-1 certified rep over
K = Q(sqrt-3), c = zeta_6): an orientation-reversing isometry of
H^3 = PSL(2,C).<conj> is tau_U : x -> U xbar; it normalizes
Gamma = rho(pi_1) iff U conjugates the Galois-mirror rep rhobar onto
rho o phi for some phi in Aut(Gamma). Classification of antiholomorphic
INVOLUTIONS: tau_U^2 = U Ubar = +I  => reflection type (Fix = a plane,
i.e. a totally geodesic surface downstairs); U Ubar = -I => antipodal
type (Fix = one point). The components of Fix(tau, M) correspond to
Gamma-conjugacy classes of involutive gU (g in Gamma): census their
signs over short words.

GATES: rho and rhobar satisfy the relator exactly; U solves the
intertwining EXACTLY over K; SnapPy cross-checks |Isom| = 8 and
amphichirality.

Run: python3 door2_involution.py   (~2 min)
"""
import itertools

import numpy as np
import sympy as sp

w3 = sp.sqrt(3) * sp.I
c = (1 + w3) / 2                              # zeta_6 (step-1 branch)
A = sp.Matrix([[1, 1], [0, 1]])
B = sp.Matrix([[1, 0], [c, 1]])
Ab = sp.Matrix([[1, 1], [0, 1]])
Bb = sp.Matrix([[1, 0], [sp.conjugate(c), 1]])


def word(mats, s):
    D = {'a': mats[0], 'b': mats[1], 'A': mats[0].inv(), 'B': mats[1].inv()}
    M = sp.eye(2)
    for ch in s:
        M = M * D[ch]
    return sp.expand(M)


REL = "abABaBAbaB"
assert sp.simplify(word((A, B), REL) - sp.eye(2)) == sp.zeros(2), "rho relator"
assert sp.simplify(word((Ab, Bb), REL) - sp.eye(2)) == sp.zeros(2), \
    "rhobar relator"
print("gate: both branches satisfy the relator exactly", flush=True)

# ---- find U: U rhobar(g) U^{-1} = rho(phi(g)), phi from a conjugate pool ----
CONJ = [""] + ["".join(t) for L in (1, 2)
               for t in itertools.product("abAB", repeat=L)]
POOL = []
for g in CONJ:
    for x in "aAbB":
        wrd = g + x + "".join(ch.swapcase() for ch in reversed(g))
        POOL.append(wrd)
An = np.array(Ab.evalf(30).tolist(), dtype=complex)
Bn = np.array(Bb.evalf(30).tolist(), dtype=complex)
targets = {}
seen_m = []
POOL_D = []
for wrd in POOL:
    Mn = np.array(word((A, B), wrd).evalf(30).tolist(), dtype=complex)
    if any(np.allclose(Mn, Sm, atol=1e-10) or np.allclose(Mn, -Sm, atol=1e-10)
           for Sm in seen_m):
        continue
    seen_m.append(Mn)
    targets[wrd] = Mn
    POOL_D.append(wrd)
print(f"target pool (deduped conjugates): {len(POOL_D)}", flush=True)
CAND = list(itertools.product(POOL_D, POOL_D))


def solve_numeric(wa, wb, sa, sb):
    """U Ab = sa*rho(wa) U ; U Bb = sb*rho(wb) U  (PSL sign freedom)."""
    rows = []
    for (M2, T) in ((An, sa * targets[wa]), (Bn, sb * targets[wb])):
        for i in range(2):
            for j in range(2):
                r = np.zeros(4, dtype=complex)
                for k in range(2):
                    r[i * 2 + k] += M2[k, j]
                    r[k * 2 + j] -= T[i, k]
                rows.append(r)
    Mm = np.array(rows)
    _, s, vh = np.linalg.svd(Mm)
    if s[-1] < 1e-10:
        return vh[-1].reshape(2, 2)
    return None


hits = []
for (wa, wb) in CAND:
    for sa, sb in itertools.product((1, -1), repeat=2):
        if solve_numeric(wa, wb, sa, sb) is not None:
            hits.append((wa, wb, sa, sb))
            break
print(f"numeric intertwiner hits (phi: a->wa, b->wb): {hits}", flush=True)
assert hits, "no simple phi admits an intertwiner — widen the search"

# ---- exact certification + type, for each hit -------------------------------
GLIDE_POOL = [""] + ["".join(t) for L in (1, 2, 3)
              for t in __import__("itertools").product("abAB", repeat=L)]


def classify(W):
    """tau_W: x -> W xbar (W exact, no free symbols). S = W Wbar.
    S = lam I, lam > 0 => reflection; lam < 0 => antipodal;
    S ~ Gamma-word => glide (tau^2 = that word); else other."""
    S = sp.simplify(W * sp.conjugate(W))
    if sp.simplify(S[0, 1]) == 0 and sp.simplify(S[1, 0]) == 0 and \
            sp.simplify(S[0, 0] - S[1, 1]) == 0:
        lam = sp.simplify(S[0, 0])
        if lam.is_real and lam != 0:
            return ("REFLECTION-type: Fix(lift) = totally geodesic plane"
                    if lam > 0 else
                    "ANTIPODAL-type: Fix(lift) = one point"), S
    for wg in GLIDE_POOL:
        G = word((A, B), wg) if wg else sp.eye(2)
        # S proportional to G by a positive real scalar?
        if sp.simplify(G[0, 0]) != 0:
            lam = sp.simplify(S[0, 0] / G[0, 0])
        elif sp.simplify(G[0, 1]) != 0:
            lam = sp.simplify(S[0, 1] / G[0, 1])
        else:
            continue
        if lam.is_real and lam != 0 and \
                sp.simplify(S - lam * G) == sp.zeros(2):
            return f"GLIDE (tau^2 ~ {wg or '(id)'} in Gamma): " \
                   f"no fixed point of this lift", S
    return f"OTHER: S = {S.tolist()}", S


x = sp.symbols('x0 x1 x2 x3')
# one representative family per phi(a)-type (the four or-reversing cosets)
reps = {}
for (wa, wb, sa, sb) in hits:
    key = wa if wa in "aAbB" else None
    if key and key not in reps:
        reps[key] = (wa, wb, sa, sb)
results = []
for key in "aAbB":
    if key not in reps:
        print(f"family {key}: no direct hit — skipped", flush=True)
        continue
    wa, wb, sa, sb = reps[key]
    U = sp.Matrix([[x[0], x[1]], [x[2], x[3]]])
    Ta = sa * word((A, B), wa)
    Tb = sb * word((A, B), wb)
    eqs = list(sp.expand(U * Ab - Ta * U)) + list(sp.expand(U * Bb - Tb * U))
    sol = sp.solve(eqs, x, dict=True)
    if not sol:
        sol = sp.solve(eqs, x[:3], dict=True)
    assert sol, f"exact solve failed for {(wa, wb, sa, sb)}"
    Ue = sp.simplify(U.subs(sol[0]))
    for xi in x:
        Ue = Ue.subs(xi, 1)
    Ue = sp.simplify(Ue)
    assert sp.simplify(Ue.det()) != 0, f"degenerate U for {(wa, wb)}"
    g1 = sp.simplify(Ue * Ab - Ta * Ue) == sp.zeros(2)
    g2 = sp.simplify(Ue * Bb - Tb * Ue) == sp.zeros(2)
    assert g1 and g2, f"exact certification failed for {(wa, wb, sa, sb)}"
    typ, S = classify(Ue)
    print(f"family phi(a)={wa}, phi(b)={wb}:  U = {Ue.tolist()}  ->  {typ}",
          flush=True)
    results.append((wa, wb, Ue, typ))

# ---- the Gamma-lift census (numeric to length 6; exact-certify hits) --------
print("\nthe Gamma-lift census (numeric length <= 6; hits exact-certified):",
      flush=True)
GEN_N = {ch: np.array(word((A, B), ch).evalf(30).tolist(), dtype=complex)
         for ch in "abAB"}
for (wa, wb, Ue, typ0) in results:
    Un = np.array(Ue.evalf(30).tolist(), dtype=complex)
    found = {"reflection": [], "antipodal": []}
    mats = {"": np.eye(2, dtype=complex)}
    frontier = [""]
    for L in range(1, 7):
        nf = []
        for wp in frontier:
            for ch in "abAB":
                if wp and wp[-1] == ch.swapcase():
                    continue
                nw = wp + ch
                mats[nw] = mats[wp] @ GEN_N[ch]
                nf.append(nw)
        frontier = nf
    for wp, g in mats.items():
        W = g @ Un
        S = W @ np.conj(W)
        if abs(S[0, 1]) < 1e-9 and abs(S[1, 0]) < 1e-9 and \
                abs(S[0, 0] - S[1, 1]) < 1e-9 and abs(S[0, 0].imag) < 1e-9 \
                and abs(S[0, 0]) > 1e-9:
            key = "reflection" if S[0, 0].real > 0 else "antipodal"
            found[key].append(wp or "(id)")
    # exact certification of numeric hits (up to the first few)
    for key in ("reflection", "antipodal"):
        cert = []
        for wp in found[key][:3]:
            g = word((A, B), wp) if wp != "(id)" else sp.eye(2)
            W = sp.simplify(g * Ue)
            typc, _ = classify(W)
            cert.append(typc.split(":")[0])
        print(f"  family phi(a)={wa}: {key}-type lifts (len<=6): "
              f"{len(found[key])}"
              + (f"; examples {found[key][:3]} exact: {cert}"
                 if found[key] else ""), flush=True)

print("\nSnapPy cross-checks:", flush=True)
import snappy
Mm = snappy.Manifold("4_1")
sg = Mm.symmetry_group()
print(f"SnapPy: |Isom| = {sg.order()}; amphichiral: "
      f"{sg.is_amphicheiral()}; group: {sg}", flush=True)
assert sg.order() == 8 and sg.is_amphicheiral()
# the Gieseking identification, COMPUTED: the free or-reversing involution
# <=> 4_1 double-covers the Gieseking manifold (nonorientable, 1 ideal
# regular tetrahedron, vol = vol(4_1)/2)
G = snappy.Manifold("m000")
try:
    nonor = not G.is_orientable()
except Exception:
    nonor = None
print(f"Gieseking candidate m000: vol = {float(G.volume()):.9f} "
      f"(vol(4_1)/2 = {float(Mm.volume())/2:.9f}); orientable: "
      f"{G.is_orientable()}; tetrahedra: {G.num_tetrahedra()}", flush=True)
assert abs(float(G.volume()) - float(Mm.volume()) / 2) < 1e-9
assert not G.is_orientable() and G.num_tetrahedra() == 1
covers2 = G.covers(2)
hit = any(len(c.is_isometric_to(Mm, return_isometries=False) or []) > 0
          if not isinstance(c.is_isometric_to(Mm), bool)
          else c.is_isometric_to(Mm) for c in covers2)
print(f"4_1 among the degree-2 covers of m000: {hit} "
      f"({len(covers2)} covers)", flush=True)
assert hit, "Gieseking double-cover identification failed"
print("\nB605 DONE", flush=True)
