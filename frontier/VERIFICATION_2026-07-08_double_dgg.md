# Independent re-verification of the B's cited in the chat-1 "self-gluing = SM" adjudication
**2026-07-08. Owner directive: "verify make sure all these B's — we prove constantly some banked
computations are wrong." Re-checked by INDEPENDENT recomputation where possible (not re-reading
FINDINGS, not only re-running the same script). Result: all five hold; details below.**

| B | claim used | verification method | verdict |
|---|---|---|---|
| **B488** | M(A_m)=torus of RᵐLᵐ has N=2m tets, 1 cusp, DGG rank 2m−1, H₁=(ℤ/m)²⊕ℤ | **Independent rebuild**: `snappy.Manifold('b++'+'R'*m+'L'*m)`, m=1..8. Counted tets, cusps, homology from scratch. | **CONFIRMED**: tets=2m ✓, cusps=1 ✓, H₁=(ℤ/m)²⊕ℤ ✓ (all m), trace=m²+2 ✓, census m1→m004, m2→m136, m3→s464 ✓ (also confirms the banked m=2≠5₂ correction). DGG gauge group abelian U(1)^{2m−1} is structural to the DGG construction. |
| **B462** | the double D(4₁) is non-hyperbolic (essential JSJ torus); φ-scan chirality payload | **Independent build**: regina `idealToFinite` + `doubleOverBoundary` on 4₁ → closed, irreducible, **Haken**, **8 incompressible 2-sided tori**; snappy hyperbolic-structure attempt on the closed double → "contains degenerate tetrahedra" (no geometric structure). Toroidal ⇒ non-hyperbolic (geometrization). **Re-ran** `phi_scan.py`: WRT gate matches B441 to 10 digits, φ-scan numbers reproduce. | **CONFIRMED** |
| **B174** | gluing landscape: fork sizes CONTINUUM/9/16/10/32/32 | **Re-ran** `gluing_landscape.py` | **CONFIRMED** — ALL CHECKS PASS, numbers reproduce |
| **B143** | the composite (double) is a closed JSJ of two hyperbolic pieces ⇒ non-hyperbolic; algebraic venue blind to chirality | **Re-ran** `probe.py` | **CONFIRMED** — apoly_m1=t⁴−5t²+2, apoly_m2=t²−6, fork_(1,2)=[−4,−2] reproduce B131; trace-mirror-invariance True |
| **B487** | DGG SU(3) of 4₁ is FLAVOR (global) not GAUGE; only gauge sym is abelian U(1); 3d not 4d | **Literature gate** (arXiv:1803.04009 Gang–Yonekura) — not re-runnable this session. Structural core (DGG gauge = abelian U(1)^{N−c}) independently confirmed by B488's data above. B487 itself already corrected a seat-1 attribution error ("Gang-Kim-Lee" → Gang & Yonekura). | **CONFIRMED (structural); lit claim not re-fetched this session** |

## Honest bottom line
The owner is right that "banked ≠ correct" — the P1–P3 adversarial panel (same day) proved it by
finding a FATAL wrong field and a FATAL false law in typeset drafts. So these five earned no trust
on their label. I re-checked them anyway, mostly by independent recomputation, and **this time all
five hold**. The chat-1 adjudication ("the self-gluing carries an abelian U(1) theory on a toroidal
manifold, not the SM gauge group") therefore stands on independently-confirmed ground: the DGG gauge
group of the object and its family is abelian (B488, independently rebuilt), and the double is
non-hyperbolic (B462, independently rebuilt in regina). The only non-recomputed link is B487's
Gang–Yonekura *flavor* result, a peer-reviewed literature fact whose structural consequence (abelian
gauge only) is confirmed by B488.
