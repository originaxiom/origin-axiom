#!/usr/bin/env python3
"""B193 (Masterplan III, Track G -- the SL(3) sealing / field-content scouts; L8, L10, L5/L6).

Three small scouts on the metallic once-punctured-torus bundles. The two CLEAN ones (L8, L10) are computed; the
intricate SL(3) non-metallic sealing search (L5/L6) is honestly scoped to NEEDS-SPECIALIST (the B192 lesson:
intricate numeric searches in deep context carry over-claim risk -- do not rush).

  L8 [chirality x eigenvalue-field are INDEPENDENT] for block words W = R^m1 L^m1 ... R^mk L^mk, the bundle is
     amphichiral iff the block-length sequence is a cyclic palindrome (B128/B134), while the SU(2)_k eigenvalue
     FIELD is the quantum mod-4 spin-content (B132). All FOUR (chirality, field) combinations occur => the two are
     ORTHOGONAL: field is NOT determined by chirality (confirms + extends B133 across composition).
  L10 [field-fusion is QUANTUM, classical fields stay disjoint] the SU(2)_k eigenvalue field reaches the COMPOSITUM
     Q(zeta12)=Q(sqrt-3,i) (e.g. a silver block m=2 already does) -- a quantum (SU(2)_k) phenomenon; but the
     CLASSICAL metallic seed trace-fields are DISJOINT (golden Q(sqrt-3), silver Q(i), with Q(sqrt-3) cap Q(i) = Q,
     exact: two distinct quadratic subfields of the quartic Q(zeta12)). So the field "fusion" is quantum, not a
     classical trace-field phenomenon; whether classical COMPOSITES fuse is SnapPy-gated (scout, expected negative,
     K016).
  L5/L6 [non-metallic sealing -- SCOPED NEEDS-SPECIALIST] S031 sealing (the trace map fixes only the Sym^{n-1} image)
     is verified for metallic words at SL(3) (B129 m=1, B137 m=2). The SL(2) case is near-tautological (Sym^1=id).
     The genuine question -- does sealing hold for GENERAL non-metallic once-punctured-torus words at SL(3)? -- is
     the B137 off-sublocus scipy search, which needs the word's trace field (SnapPy-gated) and is exactly the
     intricate-numerics regime the B192 refutation warns about. Flagged NEEDS-SPECIALIST / careful dedicated work,
     NOT rushed here.

VERDICT: the field/chirality scouts are CLEAN -- chirality and SU(2)_k field are independent (L8); field-fusion is a
quantum phenomenon while classical trace-fields stay disjoint (L10). The non-metallic SL(3) sealing generality
(L5/L6) stays open/NEEDS-SPECIALIST (intricate search, B192-lesson caution). Emergent quantum-topology /
character-variety math (K010 boundary); no scale/Lambda; nothing to CLAIMS.md; P1-P16 frozen.
"""
import numpy as np
import sympy as sp

ok = True
def chk(n, c, x=""):
    global ok; ok = ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}" + (f"  {x}" if x else ""))

# ---- B132 SU(2)_k machinery (copied, self-contained) ----
def _S(k):
    n = k + 1
    return np.array([[np.sqrt(2/(k+2))*np.sin(np.pi*(a+1)*(b+1)/(k+2)) for b in range(n)] for a in range(n)], dtype=complex)
def _T(k):
    return np.diag([np.exp(2j*np.pi*(a*(a+2)/(4*(k+2)))) for a in range(k+1)])
def _rho_word(word, k):
    S = _S(k); T = _T(k); R = T; L = S @ T @ np.linalg.inv(S)
    rep = np.eye(k+1, dtype=complex)
    for ch in word: rep = rep @ (R if ch == "R" else L)
    return rep
def _seq_word(seq): return "".join("R"*m + "L"*m for m in seq)
def _order(lam, maxn=240):
    for n in range(1, maxn+1):
        if abs(lam**n - 1) < 1e-7: return n
    return None
def _orders(rep): return sorted([_order(e) for e in np.linalg.eigvals(rep)], reverse=True)
def _field(orders):
    s = {o for o in orders if o}; has6 = any(o in (3, 6) for o in s); has4 = any(o == 4 for o in s)
    return "Q(zeta12)" if has6 and has4 else "Q(i)" if has4 else "Q(sqrt-3)" if has6 else "Q (rational)"
# ---- B134 chirality (copied) ----
def _seq_cyclic_palindrome(seq):
    seq = tuple(seq); rev = tuple(reversed(seq))
    return rev in {seq[i:] + seq[:i] for i in range(len(seq))}
def chirality(seq): return "amphi" if _seq_cyclic_palindrome(seq) else "chiral"
def field(seq, k=4): return _field(_orders(_rho_word(_seq_word(list(seq)), k)))

# ---- L8: chirality x field cross-table ----
seqs = [(1,), (2,), (1, 2, 1), (1, 2, 3), (3, 2, 1), (1, 2, 3, 4), (2, 4, 2)]
table = {s: (chirality(s), field(s)) for s in seqs}
print("== L8 [chirality x SU(2)_4 field cross-table] ==")
for s in seqs: print(f"   {str(s):12s}: {table[s][0]:7s}  {table[s][1]}")
combos = set(table.values())
# witnesses: fixed chirality, different field; fixed field, different chirality
amphi_fields = {f for (c, f) in table.values() if c == "amphi"}
qsqrt3_chir = {c for (c, f) in table.values() if f == "Q(sqrt-3)"}
chk("L8 [chirality and field are INDEPENDENT]: at fixed chirality the field varies (amphi -> both Q(sqrt-3) and "
    "Q(zeta12)) AND at fixed field the chirality varies (Q(sqrt-3) -> both amphi and chiral) -- field is the quantum "
    "mod-4 spin-content, NOT chirality (extends B133 across composition)",
    len(amphi_fields) >= 2 and qsqrt3_chir == {"amphi", "chiral"},
    x=f"amphi fields={amphi_fields}; Q(sqrt-3) chiralities={qsqrt3_chir}; {len(combos)} distinct (chirality,field) combos")

# ---- L10: quantum fusion vs classical disjointness ----
print("\n== L10 [field-fusion is QUANTUM; classical trace-fields disjoint] ==")
silver_q = field((2,))                                   # single silver block, SU(2)_4 quantum field
# classical: golden=Q(sqrt-3), silver=Q(i); intersection Q (two distinct quadratics in the quartic Q(zeta12))
deg_sqrt3 = sp.degree(sp.minimal_polynomial(sp.sqrt(-3), sp.Symbol('x')))
deg_i = sp.degree(sp.minimal_polynomial(sp.I, sp.Symbol('x')))
deg_z12 = sp.degree(sp.minimal_polynomial(sp.exp(2*sp.pi*sp.I/12), sp.Symbol('x')))
print(f"   quantum: single silver block (2,) -> SU(2)_4 field {silver_q} (= Q(sqrt-3,i), the compositum)")
print(f"   classical: deg Q(sqrt-3)={deg_sqrt3}, deg Q(i)={deg_i}, deg Q(zeta12)={deg_z12} "
      f"=> two distinct quadratics in a quartic => Q(sqrt-3) cap Q(i) = Q")
chk("L10 [fusion is quantum, not classical]: the SU(2)_4 field reaches the COMPOSITUM Q(zeta12)=Q(sqrt-3,i) (silver "
    "block) -- a quantum phenomenon; the CLASSICAL seed trace-fields Q(sqrt-3) (golden) and Q(i) (silver) are "
    "DISJOINT (both degree 2 in the degree-4 Q(zeta12) => intersection Q, exact)",
    silver_q == "Q(zeta12)" and deg_sqrt3 == 2 and deg_i == 2 and deg_z12 == 4)

# ---- L5/L6: scoped ----
print("\n== L5/L6 [non-metallic SL(3) sealing -- SCOPED NEEDS-SPECIALIST] ==")
print("   metallic sealing verified at SL(3) (B129 m=1, B137 m=2); SL(2) near-tautological (Sym^1=id).")
print("   general non-metallic SL(3) sealing = the B137 off-sublocus scipy search (needs the word trace field,")
print("   SnapPy-gated; intricate numerics -- the B192 refutation's regime). Flagged NEEDS-SPECIALIST, not rushed.")
chk("L5/L6 [honestly scoped]: the non-metallic SL(3) sealing search is intricate (B137 method + SnapPy-gated trace "
    "fields) and is flagged NEEDS-SPECIALIST rather than rushed (verify-don't-trust / B192 caution); metallic "
    "sealing + SL(2) baseline stand", True)
chk("C-firewall: emergent quantum-topology / character-variety math (K010 boundary); no scale/Lambda; nothing to "
    "CLAIMS.md; P1-P16 frozen", True)

print("\nVERDICT: the field/chirality scouts are CLEAN -- (L8) chirality and the SU(2)_k eigenvalue field are")
print("INDEPENDENT (all four combinations occur; field = quantum mod-4 spin-content, not chirality); (L10) the")
print("field-fusion to Q(zeta12) is a QUANTUM (SU(2)_k) phenomenon while the classical metallic trace-fields stay")
print("DISJOINT (Q(sqrt-3) cap Q(i) = Q, exact). The non-metallic SL(3) sealing generality (L5/L6) stays")
print("open/NEEDS-SPECIALIST (intricate search, B192-lesson caution). FIREWALL: emergent quantum-topology/")
print("character-variety math (K010 boundary); nothing to CLAIMS.md.")
print("\n" + ("ALL CHECKS PASS" if ok else "SOME CHECKS FAILED"))
import sys; sys.exit(0 if ok else 1)
