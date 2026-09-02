# R44 — Lie-theory checks on ASSERTED / IMPORTED claims (Phase C, tier C-3, batch 2)

`r44.py`: E6/E7/A4 root systems built from the Cartan matrices by reflection closure (exact), no Lie library; output in
`r44_output.txt`. Row index refers to `campaign/phaseC/unrecomputed_indexed.json`.

| # | arc | claim | computed here | verdict |
|---|---|---|---|---|
| 151 | B266 | McKay(2T) = affine E6, marks {1,1,1,2,2,2,3} | irrep dimensions of 2T, Σd² = 24 = \|2T\|; the Kac labels of Ê6 are (1,1,1,2,2,2,3) with sum 12 = h∨ | MATCH |
| 178 | B304 | E6 has 3 height-6 positive roots, mutually orthogonal; max root height 11 | 36 positive roots, height distribution 6,5,5,5,4,3,3,2,1,1,1; the three height-6 roots (1,1,1,2,1,0), (1,1,1,1,1,1), (0,1,1,2,1,1) have pairwise inner product 0; highest root (1,2,2,3,2,1), height 11 | MATCH |
| 466 | B687 | c(E6,1) = 6, h(27) = C2(27)/26 = 2/3 | C2(ω₁) = (ω₁, ω₁+2ρ) = 52/3, C2(θ) = 24 = 2h∨; c = 78/13 = 6; h = (52/3)/(2·13) = 2/3 | MATCH |
| 354/367 | B576/B582 | 27 of E6 is complex | ω₁ ≠ ω₆ (and R34: −w₀ω₁ = ω₆ ≠ ω₁) | MATCH |
| 703 | B950 | dim su(3)+su(2)+u(1)³ = 14, SM gauge algebra dim 12 | 8+3+3 = 14; 8+3+1 = 12 | MATCH |
| 704 | B951 | A2+A1 Levi of e6: dim 14, semisimple 11, centre 3 | Levi on nodes {1,3,6} (or {1,3,5}): dim 14, ss 11, centre 3 | MATCH |
| 706 | B951 | centralizer of su(3)+su(2) is 1-dim in su(5), 9-dim in e6 | in A4 no root is orthogonal to the A2+A1 ⇒ centre only, dim 1; in E6 three positive roots are orthogonal to the A2+A1 on {1,3,6} ⇒ dim 2·3 + 3 = 9 | MATCH |
| 707 | B952 | rank E6 = 6 = rank(su3+su2+u1³); rank SM = 4; deficit 2 | 6, 6, 4 | MATCH |
| 708 | B953 | dim E6 = 78 = 52 + 26; rank F4 = 4 | 2·36+6 = 78; 78 − 52 = 26 | MATCH |
| 728 | B964 | 78 → 45+16+16̄+1 (D5); 45 → 24+10+10̄+1 (A4) | D5 ⊂ E6 has 20 positive roots (dim 45); the other 32 roots are the 16+16̄; Cartan 6 = 5+1. A4 ⊂ D5: 24; 45−24 = 21 = 10+10̄+1 | MATCH |
| 333 | B549 | "E7 Cartan-matrix Perron spectrum: 1, 1.285575, 1.879385, 1.969616, 2.532089, 2.879385, 3.701666" (no script in the arc) | these are not eigenvalues; they are the entries of the Perron eigenvector of the E7 Dynkin adjacency matrix, min-normalised: (1, 1.285575, 1.879385, 1.969616, 2.532089, 2.879385, 3.701666) exactly; Perron root 1.969616 = 2cos(π/18) | MATCH (as a Perron eigenvector; the word "spectrum" in the reader's digest is a misnomer) |

**Summary.** 11 claim groups, 11 MATCH. B549's numbers reproduce from the E7 Dynkin diagram with a five-line
computation; the arc should carry that script (the reader's "no committed computation" flag stands as a record point,
not a correctness point).
