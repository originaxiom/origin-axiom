"""
Movement XX — the old/new coarse-graining (interleaving): golden ratio kept,
simplicity not.

Map each letter to its GENERATION: old {a,b} -> 0, new {A,B} -> 1.  The resulting
binary "interleaving" sequence -- does the object simplify when you only watch
which generation each letter belongs to?

  * FREQUENCY: new:old = sqrt(phi) exactly (freq(new) = sqrt(phi)/(1+sqrt phi) =
    0.5599).  The bridge/breath constant survives coarse-graining: each generation
    is sqrt(phi) times the previous.

  * COMPLEXITY: NOT Sturmian.  p(1)=2 but p(2)=4 (> 3), and p(n) ~ 3n -- nearly as
    complex as the object itself (~3n+1).  So the coarse-graining does NOT reduce
    the object to a simple 1-D golden (Sturmian) sequence; the interleaving is a
    genuinely complex aperiodic binary word.

  * It IS morphic: a letter-to-letter projection of the (primitive substitutive)
    object -- but not a fixed point of a simple binary substitution (the image of
    '0' depends on whether it came from a or b), and not Sturmian.

Honest flat-ish result: golden RATIO preserved, SIMPLICITY lost.  Report the flat
with the same care as the gems.  No physics.
"""
import numpy as np

PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def old_new(n=600000):
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    u = u[:n]
    return ''.join('0' if c in 'ab' else '1' for c in u)


def facts(b=None):
    if b is None:
        b = old_new()
    f_new = b.count('1') / len(b)
    p = [len({b[i:i + n] for i in range(len(b) - n)}) for n in range(1, 12)]
    return dict(
        f_new=f_new,
        f_new_is_golden=abs(f_new - SQ / (1 + SQ)) < 1e-3,      # sqrt(phi)/(1+sqrt phi)
        new_over_old=f_new / (1 - f_new),                       # = sqrt(phi)
        p=p,
        sturmian=all(p[n] == n + 2 for n in range(len(p))),     # p(n)=n+1 for all n
        p2=p[1],                                                # p(2); 4 (>3) => not Sturmian
    )


if __name__ == "__main__":
    f = facts()
    print(f"frequency of NEW = {f['f_new']:.5f}  (sqrt(phi)/(1+sqrt phi) = {SQ/(1+SQ):.5f}, "
          f"golden: {f['f_new_is_golden']})")
    print(f"new:old = {f['new_over_old']:.5f} = sqrt(phi) = {SQ:.5f}")
    print(f"complexity p(1..11) = {f['p']}")
    print(f"Sturmian (p(n)=n+1)? {f['sturmian']}  (p(2)={f['p2']} > 3 => NO)")
    print("=> coarse-graining keeps the golden RATIO but not the SIMPLICITY: a complex morphic word, not Sturmian.")
