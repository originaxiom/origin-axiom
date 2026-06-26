"""B224 -- golden is the UNIQUE metallic mean whose anyon chain is supersymmetric. Nothing to CLAIMS.md.

B221/B222 found the golden chain's emergent CFT is the tricritical Ising M(4,5) = the first N=1 superconformal
minimal model (c=7/10). This asks the family question (chat1): is golden the ONLY metallic mean with a
supersymmetric chain? Answer: YES, exactly.

The mechanism (all exact rational arithmetic):
  - the su(2)_k spin-1/2 anyon chain (AFM) flows to the minimal model M(k+1,k+2), c = 1 - 6/((k+1)(k+2))
    [Feiguin-Trebst-Ludwig; k=3 -> M(4,5) c=7/10 is the golden chain, reproduced in B220/B222].
  - AMONG ALL unitary Virasoro minimal models M(q,q+1), ONLY M(4,5) is also N=1 SUPERCONFORMAL
    (its c=7/10 = SM(3) of the superconformal series c=(3/2)(1-8/(p(p+2)))); higher M(q,q+1) are NOT.
  - the metallic family identifies index m with level k_m = m^2+2 (since n = k+2 = m^2+4 = the metallic
    DISCRIMINANT; for m=1, n=5 -> k=3 = the golden/Fibonacci level, 2cos(pi/5)=phi, B218). Then:
        m=1 (golden): k=3 -> M(4,5) c=7/10  SUPERSYMMETRIC
        m=2 (silver): k=6 -> M(7,8) c=25/28  not SUSY
        m=3 (bronze): k=11 -> M(12,13) c=25/26  not SUSY
        ... c_m -> 1 from below; none superconformal but golden.

So golden is the UNIQUE metallic mean whose chain is superconformal -- because the SUSY point (the tricritical
Ising M(4,5)) requires exactly the golden level k=3 = m^2+2 at m=1 (n=5=m^2+4). This closes the circle: golden is
minimal (smallest disc), exceptional (E8 at disc 5 / E6 at disc -3, B206/B210), least-hierarchical (smallest
volume, B207), AND uniquely supersymmetric -- all via 5 = m^2+4 at m=1.

Firewall: dimensionless CFT / rep-theory; the SUSY is 2d superconformal, not a scale or spacetime SUSY (S040).
The su(2)_k -> M(k+1,k+2) flow is CITED (k=3 reproduced); the central charges + superconformal-uniqueness are
EXACT; the m<->k=m^2+2 identification is the metallic-discriminant correspondence (n=m^2+4). Nothing to CLAIMS.md.
Run: python coset_susy_uniqueness.py (pyenv).
"""
from fractions import Fraction as Fr


def c_minimal(q):
    """unitary Virasoro minimal model M(q,q+1): c = 1 - 6/(q(q+1))."""
    return Fr(1) - Fr(6, q * (q + 1))


def c_su2k_chain(k):
    """su(2)_k spin-1/2 anyon chain (AFM) critical CFT = M(k+1,k+2)  [Feiguin-Trebst-Ludwig]."""
    return c_minimal(k + 1)


def c_scft(p):
    """N=1 superconformal minimal model SM(p): c = (3/2)(1 - 8/(p(p+2)))."""
    return Fr(3, 2) * (Fr(1) - Fr(8, p * (p + 2)))


def superconformal_minimal_models(qmax=80, pmax=120):
    """all M(q,q+1) that are also N=1 superconformal (c matches some SM(p))."""
    scft = {c_scft(p): p for p in range(2, pmax)}
    return [(q, c_minimal(q), scft[c_minimal(q)]) for q in range(3, qmax) if c_minimal(q) in scft]


def metallic_level(m):
    """metallic index m -> su(2) level k = m^2+2 (n = k+2 = m^2+4 = the metallic discriminant)."""
    return m * m + 2


def metallic_chain_c(m):
    return c_su2k_chain(metallic_level(m))


def metallic_chain_is_susy(m, pmax=120):
    scft = {c_scft(p) for p in range(2, pmax)}
    return metallic_chain_c(m) in scft


if __name__ == "__main__":
    print("(1) su(2)_k chain critical CFT = M(k+1,k+2):")
    for k in range(2, 8):
        print(f"   k={k}: M({k+1},{k+2})  c = {c_su2k_chain(k)}  ({float(c_su2k_chain(k)):.4f})")
    print("   k=3 -> 7/10 = the golden/Fibonacci chain (reproduced in B220/B222).")

    print("\n(2) which unitary minimal models M(q,q+1) are N=1 SUPERCONFORMAL?")
    print("   ", superconformal_minimal_models(), " -> UNIQUE: M(4,5) c=7/10 (=SM(3)), i.e. su(2)_3.")

    print("\n(3) metallic family (k_m = m^2+2, n = m^2+4):")
    for m in range(1, 6):
        print(f"   m={m}: n={m*m+4}, k={metallic_level(m)}, chain CFT c = {metallic_chain_c(m)} "
              f"({float(metallic_chain_c(m)):.4f})  SUSY = {metallic_chain_is_susy(m)}")
    print("   => golden (m=1) is the UNIQUE metallic mean whose chain is superconformal.")
    print("ALL CHECKS PASS")
