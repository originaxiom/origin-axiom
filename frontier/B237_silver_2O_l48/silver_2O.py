"""B237 / L48 (+ L47 cross-check) -- the DEFINITIVE silver-2O computation (SnapPy + GAP; run with
sage-python, NOT pyenv). Does the silver bundle's pi_1 surject onto 2O (binary octahedral, E7)? And the
manifold-specific binary-polyhedral quotient structure of the metallic bundles. Nothing to CLAIMS.md.

L48 question: silver (m=2) has trace field containing Q(sqrt2) = the octahedral group 2O's character field
(the field golden excludes). Does pi_1(silver bundle) actually carry a 2O *quotient*, or is Q(sqrt2) only a
field coincidence? chat1's partial answer: 'almost certainly no; and ALL metallic bundles carry 2T (mod 3)
and 2I (mod 5).' This computes it definitively via GAP GQuotients (all surjections pi_1 -> G, up to Aut).

RESULT (2026-06-27, calibrated):
  bundle          2T(E6)  2I(E8)  2O(E7)  S4(oct. rotation)
  golden m004      2       0       0       -
  silver b++RRLL   0       0       0       2
  bronze b++RRRLLL 10      2       0       -
 => (i) L48 ANSWER: silver does NOT carry 2O (GQuotients=0) -- the Q(sqrt2) match is a FIELD-only
        coincidence; the group never closes (consistent with |2O|=48 != p(p^2-1), B234).
    (ii) CORRECTS chat1: NOT 'all metallic bundles carry 2T and 2I' -- it is MANIFOLD-SPECIFIC
        (golden->2T only; silver->S4 [octahedral *rotation*], neither binary 2T/2I/2O; bronze->2T+2I).
   (iii) 2O is ABSENT from golden, silver, AND bronze -- the only binary-polyhedral group that never
        appears as a pi_1-quotient. Silver realizes the octahedral group only at the ROTATION level (S4),
        never the binary/spin level (2O). [Note: golden's E8=2I is the HOMOLOGICAL-monodromy McKay (the
        Q(sqrt5) field, B210), NOT a pi_1(bundle) quotient -- hence 2I:0 for golden here; GQuotients sees
        the GEOMETRIC-holonomy quotients, where golden gives 2T=E6.]

L47 cross-check: m009/m010 (vol 2.667) are the d=-7 (Q(sqrt-7)) commensurability class -- contain sqrt-7,
not sqrt-3 -- DISTINCT from the figure-eight (m004, d=-3). Confirms the ladder closes at {sqrt5, sqrt-3}
(B235): Q(sqrt-7) exists in 3-manifold land but never in the figure-eight's (arithmetic) commensurability
class. Source: Goodman-Heard-Hodgson arXiv:0801.4815 Table 1.

Run: sage-python silver_2O.py
"""
import snappy
from sage.all import libgap, QQ, PolynomialRing

R = PolynomialRing(QQ, 'x'); x = R.gen()


def gap_fp_group(M):
    G = M.fundamental_group(simplify_presentation=True)
    rels = G.relators(); n = len(G.generators())
    F = libgap.FreeGroup([chr(ord('a') + i) for i in range(n)])
    fg = [F.GeneratorsOfGroup()[i] for i in range(n)]
    idx = {chr(ord('a') + i): i for i in range(n)}
    def word(s):
        w = F.Identity()
        for ch in s:
            w = w * (fg[idx[ch]] if ch.islower() else fg[idx[ch.lower()]] ** -1)
        return w
    return F / [word(r) for r in rels]


def nsurj(M, order, gid):
    return int(libgap.Length(libgap.GQuotients(gap_fp_group(M), libgap.SmallGroup(order, gid))))


def trace_field(M):
    try:
        res = M.trace_field_gens().find_field(200, 30, optimize=True)
        return res[0] if res else None
    except Exception:
        return None


GROUPS = [("2T(E6)", 24, 3), ("2I(E8)", 120, 5), ("2O(E7)", 48, 28), ("S4", 24, 12)]


def main():
    print("=== L48: binary-polyhedral pi_1-quotients of the metallic bundles (GAP GQuotients) ===")
    print(f"{'bundle':>12} " + " ".join(f"{g[0]:>8}" for g in GROUPS))
    rows = {}
    for nm in ('m004', 'b++RRLL', 'b++RRRLLL'):
        M = snappy.Manifold(nm)
        rows[nm] = [nsurj(M, o, i) for _, o, i in GROUPS]
        print(f"{nm:>12} " + " ".join(f"{v:>8}" for v in rows[nm]))
    silver_2O = rows['b++RRLL'][2]
    print(f"\n  L48 VERDICT: silver carries 2O? {'YES (revise!)' if silver_2O else 'NO -- field-only coincidence'}")
    print("  (chat1's 'all carry 2T,2I' CORRECTED: manifold-specific; 2O absent from all three.)")

    print("\n=== L47 cross-check: d=-7 manifolds exist but are NOT the figure-eight's class ===")
    for nm in ('m004', 'm009', 'm010'):
        M = snappy.Manifold(nm); F = trace_field(M)
        if F:
            print(f"  {nm}: vol={M.volume():.4f} sqrt-3:{len((x**2+3).roots(F))>0} "
                  f"sqrt-7:{len((x**2+7).roots(F))>0}")


if __name__ == "__main__":
    main()
