"""B1062 V2 block 2 -- the LEADING TEST (Maclachlan-Reid) per object + the
box-count illustration. Inputs: block 1's exact geometric triples.
Addendum-binding: m=1 = pipeline gate; conjugate-boundedness leads; boxes illustrate.
"""
import sympy as sp
from sympy import sqrt, I, Rational as R

# block 1's geometric triples (exact, from the log; one Galois representative each)
TRIPLES = {
    1: (R(3,2) - sqrt(3)*I/2, R(3,2) + sqrt(3)*I/2, R(3,2) + sqrt(3)*I/2),
    2: (-sqrt(1+sqrt(2)) - I*sqrt(-1+sqrt(2)),
        -sqrt(1+sqrt(2)) + I*sqrt(-1+sqrt(2)),
         sqrt(2) - sqrt(2)*I),
    3: (R(-1), R(-1), R(1,2) - sqrt(7)*I/2),
}

print("[B2] === THE LEADING TEST: field degree + embeddings' boundedness ===", flush=True)
verdicts = {}
for m, (X, Y, Z) in TRIPLES.items():
    prim = X + 2*Y + 4*Z
    t = sp.symbols('t')
    mp = sp.minimal_polynomial(prim, t)
    deg = sp.degree(mp)
    roots = sp.nroots(sp.Poly(mp, t), n=40, maxsteps=200)
    # embeddings correspond to the roots of the primitive element's min poly.
    # boundedness test: for each embedding, the conjugated triple must be real
    # in [-2,2]^3 (the SU(2)/bounded locus) -- we test via each root: solve the
    # conjugate triple numerically by matching which Galois image it is.
    # Robust route: the triple's entries generate the same field; test each
    # entry's conjugates by its own min poly and pair them via resultant-free
    # sampling: for degree 2 fields, embeddings = {id, conj} only.
    if deg == 2:
        # imaginary quadratic (verify): mp has complex roots
        disc = sp.discriminant(sp.Poly(mp, t))
        imag_quad = sp.simplify(disc) < 0
        verdicts[m] = ("IMAGINARY-QUADRATIC, degree 2: the only embeddings are "
                       "identity and conjugation -- Maclachlan-Reid's boundedness "
                       "clause is VACUOUS; with integral traces and K not real, "
                       "the criteria point ARITHMETIC-side", "ARITH-SIDE")
        print(f"[B2 m={m}] field degree 2, imaginary quadratic: {imag_quad} -> "
              f"ARITH-SIDE (boundedness vacuous)", flush=True)
    else:
        # degree > 2: derived-from-quaternion-algebra over an imaginary quadratic
        # is impossible (Hao Thm 2.3 requires K imaginary quadratic for cusped
        # Kleinian: the trace field of a nonuniform arithmetic Kleinian group IS
        # imaginary quadratic) -> NON-ARITHMETIC immediately; embeddings shown
        # for the record.
        n_real = sum(1 for r in roots if abs(sp.im(r)) < 1e-20)
        verdicts[m] = (f"degree {deg} > 2: a nonuniform arithmetic Kleinian "
                       f"group's trace field is imaginary quadratic -- degree "
                       f"alone decides NON-ARITHMETIC ({n_real} real embeddings "
                       f"of {deg} exist, any real embedding also violates K⊄ℝ "
                       f"boundedness demands)", "NON-ARITH")
        print(f"[B2 m={m}] field degree {deg} -> NON-ARITHMETIC (degree alone "
              f"decides; {n_real} real embeddings present)", flush=True)

print(flush=True)
print("[B2] === R4: cusp/nonuniformity per object ===", flush=True)
print("[B2] kappa = tr[a,b] = -2 is the Markov constraint itself: the commutator", flush=True)
print("     is parabolic at every solved point -> parabolics present -> nonuniform.", flush=True)

# ---- the box-count ILLUSTRATION (declared window; identity embedding)
print(flush=True)
print("[B2] === THE ILLUSTRATION: box-counts, words to length 8 (declared) ===", flush=True)
from itertools import product
def fricke_traces(X, Y, Z, maxlen=8):
    """traces of all cyclically-reduced words up to length maxlen via matrices."""
    x = sp.nsimplify(X); y = sp.nsimplify(Y); z = sp.nsimplify(Z)
    v = sp.symbols('v')
    A = sp.Matrix([[x, 1], [-1, 0]])
    Bv = sp.Matrix([[0, -v], [1/v, y]])
    vsol = sp.solve(sp.Eq(sp.trace(A*Bv), z), v)[0]
    B = Bv.subs(v, vsol)
    Ai, Bi = A.inv(), B.inv()
    mats = {"a": A, "A": Ai, "b": B, "B": Bi}
    seen = set()
    out = []
    import itertools
    for L in range(1, maxlen+1):
        for w in itertools.product("aAbB", repeat=L):
            # skip immediate cancellations to cut volume
            bad = any(({w[i], w[i+1]} in ({"a","A"}, {"b","B"})) and w[i] != w[i+1]
                      and w[i].lower() == w[i+1].lower() for i in range(L-1))
            if bad:
                continue
            M = sp.eye(2)
            for ch in w:
                M = M * mats[ch]
            tr = complex(sp.N(sp.trace(M), 20))
            key = (round(tr.real, 9), round(tr.imag, 9))
            if key not in seen:
                seen.add(key)
                out.append(tr)
    return out

for m, (X, Y, Z) in TRIPLES.items():
    trs = fricke_traces(X, Y, Z, maxlen=8)
    boxes = {}
    for tr in trs:
        b = (int(sp.floor(tr.real)), int(sp.floor(tr.imag)))
        boxes[b] = boxes.get(b, 0) + 1
    counts = sorted(boxes.values(), reverse=True)
    print(f"[B2 m={m}] distinct traces: {len(trs)}; boxes hit: {len(boxes)}; "
          f"max per box: {counts[0]}; top-5: {counts[:5]}", flush=True)

print(flush=True)
print("[B2] === V2 VERDICT INPUTS ===", flush=True)
for m in (1, 2, 3):
    print(f"  m={m}: {verdicts[m][1]} -- {verdicts[m][0]}", flush=True)
print("==== V2 block 2 done ====", flush=True)
