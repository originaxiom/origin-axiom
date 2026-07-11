"""
Movement XIII — the object is a Pisot substitution with strong coincidence:
quasiperiodic (discrete-spectrum class), NOT mixing.  Corrects movement XI.

What is rigorously COMPUTED here (each verified in-sandbox):
  * The object is a primitive, IRREDUCIBLE, UNIMODULAR, PISOT substitution:
    char poly x^4-2x^3-5x^2-4x-1 is irreducible over Q; beta=3.6762 is Pisot
    (all Galois conjugates inside the unit circle); det M = -1.
  * It satisfies the Arnoux-Ito STRONG COINCIDENCE condition.  The check is
    validated on controls: Thue-Morse -> False (singular spectrum), Fibonacci
    and Tribonacci -> True (discrete spectrum).  The object -> True, and in fact
    TRIVIALLY: every image begins with 'a' (the movement-I "always re-begin from
    a" rule) => coincidence at the empty prefix for every letter pair.

CONSEQUENCE (theory-indicated, NOT certified here): this is exactly the
hypothesis class for PURE DISCRETE SPECTRUM (Arnoux-Ito; the Pisot substitution
conjecture, proven in many cases).  I.e. the object is expected to be measurably
a rotation on T^3 -- a cut-and-project QUASICRYSTAL, its Rauzy fractal tiling the
3d contracting space R^1 (+) C (movement XII).  The specialist-grade certificate
is the overlap / balanced-pair coincidence algorithm -- flagged, not run.

CORRECTION to movement XI: the letter-MI "mixing" reading is DOWNGRADED.
Substitution subshifts are never strongly mixing (Dekking-Keane); a Pisot
substitution with strong coincidence is quasiperiodic, not mixing.  The MI decay
over k<=400 is a finite-window artifact -- unreliable (the same numerics cannot
confirm Fibonacci's own known Bragg peaks; Fibonacci's MI recurrence appears only
near k~377).  Movement XI already flagged its constant as non-robust; XIII fixes
the interpretation: QUASIPERIODIC, not mixing.

No physics.
"""
import numpy as np
import sympy as sp

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def pisot_facts():
    x = sp.symbols('x')
    cp = x**4 - 2 * x**3 - 5 * x**2 - 4 * x - 1
    irred = sp.Poly(cp, x).is_irreducible
    roots = np.roots([1, -2, -5, -4, -1])
    beta = max(roots, key=lambda z: z.real).real
    pisot = all(abs(r) < 1 for r in roots if abs(r - beta) > 1e-6)
    M = np.array([[1, 1, 1, 1], [1, 0, 1, 0], [2, 1, 1, 1], [1, 1, 1, 0]], float)
    unimod = abs(round(np.linalg.det(M))) == 1
    # primitivity: some power all-positive
    P = np.linalg.matrix_power((M > 0).astype(int) + M.astype(int), 8)
    primitive = (P > 0).all()
    print(f"irreducible over Q: {irred} | beta={beta:.5f} Pisot: {pisot} | "
          f"|det|=1 unimodular: {unimod} | primitive: {primitive}")
    return irred and pisot and unimod and primitive


def strong_coincidence(sub, alph, maxn=14):
    def expand(s, n):
        for _ in range(n):
            s = ''.join(sub[c] for c in s)
        return s

    def abel(p):
        return tuple(p.count(c) for c in alph)
    for a, i in enumerate(alph):
        for j in alph[a + 1:]:
            ok = False
            for n in range(1, maxn):
                wi, wj = expand(i, n), expand(j, n)
                for p in range(min(len(wi), len(wj))):
                    if wi[p] == wj[p] and abel(wi[:p]) == abel(wj[:p]):
                        ok = True
                        break
                if ok:
                    break
            if not ok:
                return False
    return True


def coincidence_validated():
    tm = strong_coincidence({'a': 'ab', 'b': 'ba'}, 'ab')          # must be False
    fib = strong_coincidence({'a': 'ab', 'b': 'a'}, 'ab')          # must be True
    tri = strong_coincidence({'a': 'ab', 'b': 'ac', 'c': 'a'}, 'abc')  # must be True
    obj = strong_coincidence(SUB, 'abAB')
    print(f"strong coincidence -- controls: Thue-Morse={tm} (want False), "
          f"Fibonacci={fib} Tribonacci={tri} (want True) | OBJECT={obj}")
    # structural reason: every image starts with 'a'
    all_start_a = all(SUB[c][0] == 'a' for c in 'abAB')
    print(f"  (holds trivially: every image begins with 'a' = {all_start_a})")
    return (tm is False) and fib and tri and obj and all_start_a


if __name__ == "__main__":
    f = pisot_facts()
    c = coincidence_validated()
    print()
    print("BANKED (computed): irreducible unimodular primitive Pisot + strong coincidence =", f and c)
    print("CONSEQUENCE (theory-indicated): pure discrete spectrum -> a 3d quasicrystal (Rauzy fractal).")
    print("CORRECTS movement XI: quasiperiodic, not mixing.")
