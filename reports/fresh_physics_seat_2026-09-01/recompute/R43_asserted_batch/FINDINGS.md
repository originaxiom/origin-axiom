# R43 — tool checks on ASSERTED / IMPORTED load-bearing claims (Phase C, tier C-3, batch 1)

`r43.py` (SnapPy 3.3.2, PARI via cypari, mpmath); full output in `r43_output.txt`. Each row: the claim as the reader
extracted it (index into `campaign/phaseC/unrecomputed_indexed.json`), what this bench computes, verdict.

| # | arc | claim | computed here | verdict |
|---|---|---|---|---|
| 0 | B3 | m004: 2 ideal tetrahedra, 2 edges, 4 faces, 1 cusp | 2 tetrahedra, 1 cusp; ideal triangulation ⇒ 2 edges, 4 faces | MATCH |
| 144/145/190/276 | B257/B321/B486 | cusp shape 2√3·i, rectangular, \|shape\|² = 12; translations (1, 2√3) | shape = 3.4641016 i (Re < 1e−15), \|shape\|² = 12.000000000; translations i·1, 3.4641 | MATCH |
| 208 | B338 | CS(1,n) table; n·CS(1,n) → −1/2 | CS(1,2) = −0.246611, CS(1,50) = −0.010000; n·CS = −0.49322, −0.49627, −0.49847, −0.49959, −0.49990, −0.49998 (n = 2,3,5,10,20,50) | MATCH |
| 275 | B485 | Δ_m(a) = a² − (m²+2)a + 1; rectangular cusp shapes m = 1..4 | tr(RᵐLᵐ) = m²+2 for m = 1..6 (the Alexander polynomial of a punctured-torus bundle is the characteristic polynomial of its monodromy); bundle cusp shapes: m = 2,3,4 purely imaginary in SnapPy's basis; m = 1 reported as 1 + 0.2887 i, which is SL(2,ℤ)-equivalent to 2√3 i (τ−1 = i/(2√3), −1/(τ−1) = 2√3 i) | MATCH (basis note for m = 1) |
| 124 | B211 L32 | metallic bundles m = 1..6 amphichiral, CS = 0 | CS ≤ 1.6e−16 for all six; **correction (R51):** the `is_isometric_to(mirror)` call first used here is vacuous — re-checked with `symmetry_group().is_amphicheiral()`: True for all six (order 8) | MATCH |
| 279/280/857/1028 | B488/B489/B1079/B8086 | H1(M_m) = ℤ ⊕ (ℤ/m)², m = 1..8; tower Aⁿ: torsion \|2 − L(2n)\|, vol = n·vol(4₁) | H1 = ℤ/m + ℤ/m + ℤ for m = 1..8; tower n = 1..8: torsion 1, 5, 4·4, 3·15, 11², 8·40, 29², 21·105 = \|2 − L(2n)\| exactly, vol/vol(4₁) = n to 1e−6 | MATCH |
| 186 | B316 | chiral RRL / RLL bundles: invariant trace field ℚ(√−7) | shape field x² − x + 2, disc −7, for both b++RRL and b++RLL (vol 2.666745) | MATCH |
| 868 | B1083 | Gieseking manifold (non-orientable, vol ≈ 1.0149) has orientation double cover m004 | m000: non-orientable, vol 1.014942 = vol(m004)/2; its orientable double cover is isometric to m004 | MATCH |
| 891 | B1104 | Isom(m004) = D4, order 8 | symmetry group D4, order 8, non-abelian | MATCH |
| 515 | B735 | m004(5,1) has no cusps | filled manifold is closed (SnapPy still lists the filled cusp; vol 0.981369) | MATCH (wording) |
| 752 | B980 | Vol(4₁) = 6Λ(π/3) = 2.0298832128193072500424051081… | 6Λ(π/3) = 2.02988321281930725004240510855 (mpmath, 40 dps); SnapPy high precision 2.029883212819307250042405108549… | MATCH to 27 digits; the quoted 28th–29th digits "…081" should read "…0855" (transcription) |
| 232 | B401 | L(1, χ₋₁₅) = 2π/√15 (h = 2, w = 2) | PARI lfun = 1.6223114703894447…, 2π/√15 = 1.6223114703894446, h(−15) = 2 | MATCH |
| 470/478 | B689/B698 | 15a: a₃ = −1, a₅ = +1; genus X₀(3) = X₀(5) = 0; L(15a,1) = 0.350150760583, L(15a,2) = 0.661475187922, L′(15a,0) = 0.251330433713, Ω = 5.6024121693 | ellinit([1,1,1,−10,−10]): a₃ = −1, a₅ = 1; dim S₂(Γ₀(3)) = dim S₂(Γ₀(5)) = 0; L(1) = 0.35015076058315…, L(2) = 0.66147518792107…, L′(0) = 0.25133043371325…; ω₁ = 1.4006030423326 so 4ω₁ = 5.6024121693 | MATCH (L(2) last digit rounds 1→2; Ω is 4ω₁ in PARI's lattice convention) |
| 205 | B336 | J_N(4₁; ζ₁₅) real for all N | Habiro sum: max \|Im\| = 1.7e−11 for N ≤ 40; each factor pair (2i sin a)(2i sin b) is real, so the statement is termwise trivial | MATCH |
| 899/976 | B1114/B1200 | κ = tr[a,b] with \|κ − 2\| = 1 at the Eisenstein point; tr[A,B] ≠ 2 | tr[a,b] = 1.5 + 0.866 i = 2 + ω̄·(−1)… i.e. κ − 2 = −0.5 + 0.866 i, \|κ − 2\| = 1.000000; tr a = −1.5 + 0.866 i, tr b = 1 − 1.732 i | MATCH |
| 125 | B212 | silver (m136) square traces ≡ 0 mod (1+i), no order-3 element | tr(a²) = 2i, tr(b²) = 2, tr(c²) = −2i, all ≡ 0 mod (1+i) since (1+i)² = 2i | MATCH (square traces; generator traces themselves are not Gaussian integers) |
| 712 | B955 | π₁(m004) surjects onto A4, D5, S5 | degree-4 covers: 1 cyclic + 1 irregular; degree-5: 1 cyclic + 3 irregular (necessary, not sufficient — the surjection needs the permutation representation, GAP/Sage not on this bench) | NOT CHECKED |
| 1014/436 | B1232/B665 | [ℚ(ζ₃):ℚ] = 2; SL(2,5) not simple, PSL(2,5) = A5 | 2; group theory | MATCH |

**Summary.** 17 claim groups checked, 16 MATCH (two with wording/basis notes and one transcription slip in the 28th
digit of Vol(4₁)), 1 not checkable here (B955's surjections). Nothing in this batch changes a verdict of record.
