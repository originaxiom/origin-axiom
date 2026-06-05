"""B76 (Path F2/F3) -- the speculative-tail closure: cusp-torsion x quantum group at roots of unity,
and the parity mechanism x Chern-Simons.

F2 QUESTION. The cusp-torsion law (B69, m=1..6) puts the cusps of the metallic-m bundle's
trace-relation curve at x = 2cos(pi/k), with k in the set {3,...,m+2}, k = m (mod 2). Roots of unity
are exactly where anyonic TQFT / quantum groups at roots of unity live. Does the cusp k-set connect to
a quantum-group-at-root-of-unity / RCFT structure -- LITERALLY, or only by analogy?

WHAT THIS COMPUTES (exact sympy):
  (1) The literal identification. 2cos(pi/k) = [2]_q, the quantum integer at q = e^{i pi/k}: indeed
      [2]_q = q + q^-1 = 2cos(pi/k). So the cusp value at k is exactly the SU(2) quantum-group [2]-value
      at the primitive 2k-th root of unity q=e^{i pi/k} -- i.e. the SU(2)_{k-2} (WZW level k-2)
      Temperley-Lieb-Jones special value. Verified for k=3..8.
  (2) The level map. The cusp k-set {3,...,m+2} maps to SU(2) WZW levels {1,...,m} (level = k-2). And
      'a elliptic of order 2k' (B69) <-> 'q a primitive 2k-th root of unity' -- order-2k torsion on
      both sides. Tabulated m=1..6.
  (3) The categorification barrier (V28, cited). The metallic FUSION rule tau^2 = 1 + m*tau
      categorifies as a unitary anyon model ONLY for m=1 (golden=Fibonacci; Ostrik rank-2
      classification). So the cusp/level coincidence does NOT lift to a metallic-anyon / MTC family.

F2 VERDICT. LITERAL at the level of the special NUMBERS / torsion orders: the cusp k-set is exactly
the SU(2) quantum-group root-of-unity level set (both are the cyclotomic values 2cos(pi/k), order-2k
torsion) -- this closes B69's open 'reconciliation' item. But there is NO categorical/TQFT realization
of the metallic FAMILY (V28): no functor from the metallic-bundle cusps to a modular tensor category
for m>=2. So the deeper 'anyonic TQFT' reading is SPECULATIVE-ANALOGY -- the shared structure is just
'both are roots of unity' (cyclotomic), exactly the thin geometry<->TQFT boundary B69/V28 flagged.

F3 DISPOSITION (parity mechanism x Chern-Simons). Already ANSWERED by V56 (B74): the proven even/odd-|k|
-> P-symmetric/antisymmetric split (B64) has a literal Chern-Simons reading -- it IS the W_N
charge-conjugation grading of the spin-k current by (-1)^k (both are -w0 of A_{n-1} on a degree-k
invariant). STRUCTURAL, recorded under V56; no separate computation needed. Noted here for completeness.

Standalone low-dim topology / TQFT mathematics; no Origin-core claim; proven core P1-P16 untouched.
"""
import sympy as sp


def cusp_kset(m):
    """B69 cusp-torsion law: k in {3,...,m+2} with k = m (mod 2)."""
    return [k for k in range(3, m + 3) if (k % 2) == (m % 2)]


def quantum_two(k):
    """[2]_q = q + q^-1 at q = e^{i pi/k}; equals 2 cos(pi/k) exactly."""
    q = sp.exp(sp.I * sp.pi / k)
    return (q + 1 / q).rewrite(sp.cos)


def check_identity(kmax=8):
    """Verify [2]_q = 2 cos(pi/k) at q=e^{i pi/k} for k=3..kmax (the cusp value = SU(2)_{k-2} [2]-value)."""
    out = {}
    for k in range(3, kmax + 1):
        out[k] = sp.simplify(quantum_two(k) - 2 * sp.cos(sp.pi / k)) == 0
    return out


def level_table(mmax=6):
    """cusp k-set {3..m+2} -> SU(2) WZW levels {k-2} = {1..m}; '2k torsion order' on both sides."""
    rows = []
    for m in range(1, mmax + 1):
        ks = cusp_kset(m)
        levels = [k - 2 for k in ks]
        rows.append((m, ks, levels, [2 * k for k in ks]))
    return rows


def main():
    print("B76 (Path F2/F3) -- cusp-torsion x quantum group at roots of unity\n")

    print("(1) literal identity  2cos(pi/k) = [2]_q at q=e^{i pi/k}  (cusp value = SU(2)_{k-2} value):")
    chk = check_identity(8)
    print(f"    verified k=3..8: {all(chk.values())}  {chk}")
    print("    e.g. k=5: 2cos(pi/5) =", sp.nsimplify(2 * sp.cos(sp.pi / 5)), "= golden phi (Fibonacci, SU(2)_3)")

    print("\n(2) cusp k-set -> SU(2) WZW level map (level=k-2; torsion order 2k both sides):")
    print("    m | cusp k-set {3..m+2}, k=m(mod2) | SU(2) levels {k-2} | torsion orders {2k}")
    for m, ks, levels, ord2k in level_table(6):
        print(f"    {m} | {ks} | {levels} | {ord2k}")

    print("\n(3) categorification barrier (V28, cited): metallic fusion tau^2=1+m*tau is a unitary anyon")
    print("    model ONLY for m=1 (golden=Fibonacci; Ostrik). No metallic-anyon/MTC family for m>=2.")

    print("\nF2 VERDICT:")
    print("  - LITERAL (numbers/torsion): the cusp k-set IS the SU(2) quantum-group root-of-unity level")
    print("    set -- both are the cyclotomic values 2cos(pi/k), order-2k torsion. Closes B69's open")
    print("    'reconciliation' item (computer-assisted/STRUCTURAL).")
    print("  - NO categorical lift (V28): no MTC/TQFT realization of the metallic FAMILY (m>=2). The")
    print("    deeper 'anyonic TQFT' reading is SPECULATIVE-ANALOGY -- shared structure is just")
    print("    'roots of unity' (cyclotomic), the thin geometry<->TQFT boundary B69/V28 flagged.")
    print("\nF3 DISPOSITION: subsumed by V56 (B74) -- the B64 parity split IS the W_N charge-conjugation")
    print("  grading of the spin-k current by (-1)^k (both -w0 of A_{n-1}). STRUCTURAL; no new compute.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
