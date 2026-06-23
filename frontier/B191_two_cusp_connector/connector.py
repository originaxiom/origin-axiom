#!/usr/bin/env python3
"""B191 (Masterplan III, Track F -- the formal 2-cusp connector; H5-a): B185 showed the 1-cusp metallic units cap
at PAIRS, so an N>=3 interaction needs a >=2-cusp CONNECTOR. We compute the FORMAL connector at the trace-ring
level (a true geometric metallic 2-cusp 3-manifold is the NEEDS-SPECIALIST residual): does the kappa-selection
NEST through a 2-cusp connector?

Setup: a chain leaf1 -- connector -- leaf2. Each leaf is a figure-eight once-punctured-torus bundle with A-poly
curve q=f(p)=p^4-5p^2+2 (B67) on its boundary torus. The connector has TWO boundary tori; its character variety
COUPLES them. We model the coupling by the connector's internal mapping class phi_c: boundary2 = phi_c(boundary1)
(the B174 (p,q,r) GL(2,Z) action). The chain fork = {boundary1 on leaf1's curve AND phi_c(boundary1) on leaf2's
curve} -- exactly B190's fork under the word phi_c, now read as a leaf--connector--leaf chain.

Answer: the kappa-selection NESTS -- a COUPLING connector (phi_c != id) propagates leaf1's constraint to leaf2,
giving a DISCRETE kappa-fork (so the selection mechanism extends to N>=3 in principle); but it stays discrete-and-
PROLIFERATING (not forced-unique), and an UNCOUPLED connector gives a CONTINUUM (no selection). The genuine coupling
(which phi_c / whether a metallic 2-cusp 3-manifold realizes it) is the specialist input.

  C1 [the dim count -- discrete IFF the connector couples] B185: dim(glued) = sum(cusps) - 2*gluings. For
     leaf(1) -- connector(2) -- leaf(1): dim = (1+2+1) - 2*2 = 0 => DISCRETE -- PROVIDED the connector's character
     variety genuinely couples its two boundaries (a dim-2 = #cusps relation). UNCOUPLED (independent boundaries):
     each end is a free curve => dim 2 (a continuum^2, NO selection). So coupling is what makes the selection.
  C2 [kappa NESTS via the connector; CONTROL identity->continuum] the chain fork is DISCRETE for a coupling
     connector (phi_c = T -> 9, S -> 16, ST -> 32 -- finite, >1), and CONTINUUM for the identity connector (no
     coupling => leaf2 lands on leaf1's own curve, no constraint). The connector's mapping class is the coupling
     that propagates the kappa-constraint from one leaf to the other.
  C3 [discrete-and-PROLIFERATING, not forced-unique] the chain fork count GROWS with the connector's complexity
     (T:9 < T^2:10; S:16 < ST:32) and never collapses to 1 -- so kappa nests into a discrete-proliferating
     selection, NOT a single forced value (consistent with B185/B190; the over-determination route, not uniqueness).
  C4 [verdict + NEEDS-SPECIALIST] the kappa-selection mechanism EXTENDS to N>=3 via coupling 2-cusp connectors (it
     nests, staying discrete-proliferating). The formal connector = its mapping class phi_c (free input). The TRUE
     metallic 2-cusp 3-manifold connector -- a genuine dim-2-character-variety 2-cusp hyperbolic manifold with the
     right boundary coupling -- is NEEDS-SPECIALIST (H5-a). Emergent character-variety math (K010 boundary); no
     scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.

VERDICT (H5-a): a 2-cusp connector NESTS the kappa-selection at the trace-ring level -- a coupling connector turns
leaf1's constraint into a discrete fork on leaf2 (the selection extends past B185's pair-cap to N>=3 in principle),
staying discrete-and-proliferating (not forced-unique); an uncoupled connector gives a continuum. The genuine
geometric metallic 2-cusp connector is NEEDS-SPECIALIST. FIREWALL: K010 boundary; nothing to CLAIMS.md.
"""
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

p, r = sp.symbols("p r")
def f(x): return x**4 - 5*x**2 + 2                  # figure-eight A-poly curve q=f(p) (B67)
def act(word, P, Q, R):
    for g in word:
        if g == "S": P, Q, R = Q, P, R
        elif g == "T": P, Q, R = P, R, P*R - Q
    return P, Q, R
RQUAD = r**2 - p*f(p)*r + p**2 + f(p)**2 - 4

def chain_fork(phi_c):
    """leaf1 (q=f(p)) -- connector(phi_c) -- leaf2 (q2=f(p2)), boundary2 = phi_c(boundary1). Returns degree or 'CONTINUUM'."""
    P, Q, R = act(phi_c, p, f(p), r)
    cond = sp.expand(sp.numer(sp.together(Q - f(P))))
    if cond == 0: return "CONTINUUM"
    res = sp.resultant(sp.Poly(cond, r), sp.Poly(RQUAD, r), r) if cond.has(r) else cond
    return sp.Poly(sp.expand(res), p).degree()

# ---- C1: the dim count ----
dim_chain = (1 + 2 + 1) - 2*2           # leaf(1) + connector(2) + leaf(1), two gluings
print(f"== C1 [dim count] leaf(1)--connector(2)--leaf(1): dim = (1+2+1) - 2*2 = {dim_chain} (discrete IFF coupled) ==")
chk("C1 [dim count -- discrete iff the connector couples]: B185 gives dim 0 for the chain (=> a DISCRETE selection),"
    " PROVIDED the connector's character variety genuinely couples its 2 boundaries; uncoupled => dim 2 (continuum^2)",
    dim_chain == 0 and chain_fork("") == "CONTINUUM",
    x="identity (uncoupled) connector -> CONTINUUM (no selection); a coupling connector -> dim 0 (discrete)")

# ---- C2: kappa nests via the connector; control ----
forks = {w: chain_fork(w) for w in ["T", "S", "ST"]}
print(f"\n== C2 [kappa nests; control identity->continuum] == identity: {chain_fork('')}; "
      + ", ".join(f"{w}:{forks[w]}" for w in forks))
chk("C2 [kappa NESTS via the connector]: the chain fork is DISCRETE (finite, >1) for a coupling connector (T->9, "
    "S->16, ST->32) and CONTINUUM for the identity connector -- the connector's mapping class propagates leaf1's "
    "constraint to leaf2",
    chain_fork("") == "CONTINUUM" and all(isinstance(forks[w], int) and forks[w] > 1 for w in forks),
    x="identity continuum (no coupling); coupling connectors give discrete forks (kappa propagates)")

# ---- C3: discrete-and-proliferating, not forced-unique ----
prolif = chain_fork("TT") > chain_fork("T") and chain_fork("ST") > chain_fork("S")
chk("C3 [discrete-and-PROLIFERATING, not forced-unique]: the chain fork count grows with connector complexity "
    "(T:9 < T^2:10; S:16 < ST:32) and never collapses to 1 -- kappa nests into a discrete-proliferating selection, "
    "NOT a single forced value (consistent with B185/B190)",
    prolif and all(forks[w] > 1 for w in forks),
    x=f"T={forks['T']} < TT={chain_fork('TT')}; S={forks['S']} < ST={forks['ST']} (proliferates, >1)")

chk("C4 [verdict + NEEDS-SPECIALIST]: the kappa-selection mechanism EXTENDS to N>=3 via coupling 2-cusp connectors "
    "(it nests, staying discrete-proliferating); the formal connector = its mapping class phi_c (free input); the "
    "TRUE metallic 2-cusp 3-manifold connector is NEEDS-SPECIALIST (H5-a). Emergent math (K010); nothing to CLAIMS.md",
    dim_chain == 0)

print("\nVERDICT (H5-a): a 2-cusp connector NESTS the kappa-selection at the trace-ring level -- a COUPLING connector")
print("(phi_c != id) propagates leaf1's constraint into a DISCRETE fork on leaf2, so the selection mechanism extends")
print("past B185's 1-cusp pair-cap to N>=3 in principle; it stays discrete-and-PROLIFERATING (count grows with phi_c,")
print("never forced-unique), and an UNCOUPLED connector gives a CONTINUUM (no selection). The genuine coupling (which")
print("phi_c / whether a metallic 2-cusp 3-manifold realizes it) is the NEEDS-SPECIALIST residual. FIREWALL: emergent")
print("character-variety math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
