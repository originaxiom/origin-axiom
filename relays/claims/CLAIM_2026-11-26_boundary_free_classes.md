# CLAIM CARD — the three boundary-free classes of H¹(fibre, ad Q₈) all move the cusp; FL-08 prices only the lines

- seat, branch, commit: SM seat, this seat's branch (as on its page on main), the commit that adds this card
- kind: computation
- touches: P-635, P-567 (FL-08 as the register states it)
- effect: conditions — P-635: FL-08 prices the 2 line classes only. Holding the cusp at −1 is one discrete end condition
  that removes all 3 Q₈ classes; on m004 one survives. The CKM step is undefined in the frame as built.
- imports: the identification of m004's monodromy as a ↦ ab, b ↦ bab (only its abelianised class is checked)
- premises on main: B1836 § 5 (P-635's dimensions), B1656 and B1723's b1656_funcs (the frame's Q₈ constants), B1945
  (the half-period channels), B1653 (the null quaternion)
- decisive script: relays/sm_r635/run.py, SHA-256 028eb8e8622d5a83, depends on sympy, plus main's checkout (argv[1],
  for the frame's constants only), run as `python3 -B run.py MAIN_CHECKOUT run`, outputs: r635_run.txt SHA-256
  d0a9d4b5f681d6c2 and r635_results.json SHA-256 2029f473f77b7402
- second computation: none by another seat. The dimensions 0/0/3 agree with B1836's reader C6, which was written
  independently (hand cocycle formula; no shared code)
- already on main?: `grep -il "boundary free\|ad Q₈\|ad Q8" frontier/*/FINDINGS.md` on be8c83d4f: B1836 only (the
  dimensions, without the boundary motion, the family or the monodromy); closest arc B1836
- what would make it fail: a boundary-free direction with κ = tr[A, B] staying at −2. F3 (restriction rank 3) and F6b
  (Hessian 8·1₃) rule this out. Plants P1 to P4 (reducible pair, generic pair, trivial rep) come out as required.
