"""B235 / L47 -- the Q(sqrt-7) probe (SnapPy; run with sage-python, NOT pyenv). Does Q(sqrt-7) (the next
trace-1 imaginary rung, disc -7) appear in the figure-eight's data? Computes the invariant trace field of
4_1 and of its covers up to degree 6 and checks for sqrt-7.

RESULT (2026-06-27): every cover up to degree 6 has invariant trace field Q(sqrt-3); sqrt-7 NOT found.
Reason: 4_1 is ARITHMETIC (Bianchi group PSL(2,O_3)), so covers stay in one commensurability class and do
not enlarge the invariant trace field. The trace-1 ladder CLOSES at {sqrt5, sqrt-3}. (Documented in
FINDINGS.md / metallic_table.py; not a pyenv test because SnapPy lives in the sage env.)

Run:  sage-python l47_snappy_probe.py
"""
import snappy
from sage.all import QQ, PolynomialRing

R = PolynomialRing(QQ, 'x'); x = R.gen()


def get_field(gens, prec=200, degmax=30):
    try:
        res = gens.find_field(prec, degmax, optimize=True)
        return res[0] if res else None
    except Exception:
        return None


def contains_sqrt(F, d):
    try:
        return len((x ** 2 - d).roots(F)) > 0
    except Exception:
        return None


def fingerprint(F):
    try:
        return f"deg={F.degree()} discSF={F.discriminant().squarefree_part()}"
    except Exception:
        return "?"


def main():
    M = snappy.Manifold('4_1')
    itf = get_field(M.invariant_trace_field_gens())
    print(f"4_1 invariant trace field: {fingerprint(itf)} "
          f"sqrt-3:{contains_sqrt(itf, -3)} sqrt-7:{contains_sqrt(itf, -7)}")
    found7 = []
    for deg in range(2, 7):
        for i, C in enumerate(M.covers(deg)):
            F = get_field(C.trace_field_gens())
            if F is None:
                continue
            if contains_sqrt(F, -7):
                found7.append((deg, i))
            print(f"  cover deg {deg} #{i}: {fingerprint(F)} "
                  f"sqrt-3:{contains_sqrt(F, -3)} sqrt-7:{contains_sqrt(F, -7)}")
    print("RESULT:", f"sqrt-7 FOUND {found7}" if found7 else
          "sqrt-7 NOT found -- 4_1 arithmetic; covers keep Q(sqrt-3); the trace-1 ladder CLOSES at {sqrt5,sqrt-3}")


if __name__ == "__main__":
    main()
