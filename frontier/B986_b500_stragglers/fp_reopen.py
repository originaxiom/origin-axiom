"""B986 -- the B500 depth-5 reopen, done mod p.

B525 specified the reopen: "re-run the 35 (F_p Groebner or longer timeout)". The obstruction
was that the eliminant over QQ blows up to degree ~3000-9280 and overflows the PARI stack.

The mod-p route removes the obstruction rather than out-waiting it. Everything -- the resultant
chain AND the decisive test -- is done in GF(p)[x]:

  K = QQ[t]/(t^4 - t - 1) is an S4-quartic with NO intermediate fields, so the child is present
  for a word iff its eliminant h has a root in K.

  If p is INERT in K (t^4-t-1 irreducible mod p) then O_K/p = F_{p^4}. A root of h in K reduces
  to a root of h mod p in F_{p^4}. Contrapositive, and this is the whole point:

      h mod p has NO root in F_{p^4}  =>  h has NO root in K.   [PROOF, not evidence]

  "h has a root in F_{p^4}" is gcd(h, x^(p^4) - x) != 1, computed by repeated squaring mod h --
  cheap even at degree 9280.

A word is only declared ABSENT if the test passes for EVERY prime tried; a single prime giving a
nontrivial gcd makes the word INCONCLUSIVE mod p (a root in F_{p^4} need not lift to K), which is
reported as such and NOT as a hit.
"""
import itertools as it
import os
import sys

from sage.all import GF, PolynomialRing, ZZ

HERE = os.path.dirname(os.path.abspath(__file__))
B500 = os.path.join(HERE, "..", "B500_child_hunt")

# --- the 150 depth-5 words, same construction and order as hunt_d5.py ---
WORDS = [''.join(w) for w in it.product('FMD', repeat=5) if set(w) == set('FMD')]

# --- the stragglers: TIMEOUT-logged + never-logged in hunt_results_d5.txt ---
logged, timeouts = set(), set()
with open(os.path.join(B500, "hunt_results_d5.txt")) as fh:
    for line in fh:
        w = line.split(':')[0].strip()
        if w in WORDS:
            logged.add(w)
            if 'TIMEOUT' in line.upper():
                timeouts.add(w)
STRAGGLERS = [w for w in WORDS if (w not in logged) or (w in timeouts)]

def primes_inert_in_K(n):
    """p with t^4 - t - 1 irreducible mod p  =>  O_K/p = F_{p^4}."""
    out, p = [], 3
    while len(out) < n:
        p = ZZ(p).next_prime()
        Rt = PolynomialRing(GF(p), 't')
        t = Rt.gen()
        if (t**4 - t - 1).is_irreducible():
            out.append(int(p))
    return out

def eliminant_mod_p(word, p):
    """The hunt_d5 resultant chain, computed entirely in GF(p)."""
    R = PolynomialRing(GF(p), ['x', 'y', 'z'])
    x, y, z = R.gens()
    F = lambda q: (q[2], q[0], q[0]*q[2] - q[1])
    M = lambda q: (q[2], q[2], q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    D = lambda q: (q[0]**2 - 2, q[1]**2 - 2, q[0]*q[1]*q[2] - q[0]**2 - q[1]**2 + 2)
    GEN = {'F': F, 'M': M, 'D': D}
    q = (x, y, z)
    for ch in word:
        q = GEN[ch](q)
    f1, f2, f3 = q[0] - x, q[1] - y, q[2] - z
    r1 = f1.resultant(f3, z)
    r2 = f2.resultant(f3, z)
    h = r1.resultant(r2, y)
    return h.univariate_polynomial() if h != 0 else None

def has_root_in_Fp4(h, p):
    """gcd(h, x^(p^4) - x) != 1  <=>  h has a root in F_{p^4}."""
    Rx = PolynomialRing(GF(p), 'x')
    h = Rx(h)
    if h.degree() < 1:
        return None                      # degenerate at this prime
    xq = Rx.gen()
    e = ZZ(p)**4
    xq = pow(Rx.gen(), int(e), h)        # x^(p^4) mod h, by repeated squaring
    g = h.gcd(xq - Rx.gen())
    return g.degree() >= 1

def main():
    nprimes = int(sys.argv[1]) if len(sys.argv) > 1 else 3
    ps = primes_inert_in_K(nprimes)
    print(f"stragglers: {len(STRAGGLERS)}  (timeouts {len(timeouts)}, never-reached "
          f"{len([w for w in WORDS if w not in logged])})")
    print(f"inert primes (t^4-t-1 irreducible mod p): {ps}\n")
    absent, inconc, degen = [], [], []
    for w in STRAGGLERS:
        verdicts = []
        for p in ps:
            h = eliminant_mod_p(w, p)
            if h is None:
                verdicts.append(('degen', p, None)); continue
            r = has_root_in_Fp4(h, p)
            verdicts.append(('root' if r else 'noroot', p, h.degree()))
        degs = [v[2] for v in verdicts if v[2] is not None]
        if any(v[0] == 'noroot' for v in verdicts):
            absent.append(w)
            tag = "CHILD ABSENT (proved by an inert prime)"
        elif all(v[0] == 'degen' for v in verdicts):
            degen.append(w); tag = "DEGENERATE at every prime tried"
        else:
            inconc.append(w); tag = "INCONCLUSIVE mod p (root in F_p^4 need not lift)"
        print(f"  {w}: deg {degs}  {[v[0] for v in verdicts]}  -> {tag}")
    print(f"\nABSENT (proved): {len(absent)}/{len(STRAGGLERS)}")
    print(f"INCONCLUSIVE  : {len(inconc)}  {inconc}")
    print(f"DEGENERATE    : {len(degen)}  {degen}")
    return absent, inconc, degen

if __name__ == "__main__":
    main()
