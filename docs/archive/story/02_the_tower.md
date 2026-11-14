# 02 — The tower

> Narrative, not claim. Cites the mathematics one-way.

Perturb the **trivial representation** — the one where every holonomy is the identity, the "void" of the trace
map — and read off the Jacobian. The result is the project's first deep structure: the **Dickson tower**. The
characteristic polynomial of that Jacobian factors as a clean product over the powers of the companion matrix,

```
   char( J(m) )  =  ∏_k char( ±M^k )          (the Dickson catalog)
```

This was assembled rung by rung. SL(3) and SL(4) were pinned exactly over `ℤ[m]` (**B63/B65**, V14/V16); the
SL(4) metallic tower was then proved *from first principles* via a CRT / `F_p` symbolic-`m` Jacobian (**B80**,
resolving an earlier stall); SL(5) and SL(6) were pushed numerically and hit a characteristic wall — the
eps-series `pinv` becomes gauge-degenerate at repeated sectors (**B61/B66**, V11/V17), a *computational* ceiling,
not a structural gap.

A second, independent route reached the same object without the heavy machinery (**B103**, V87): because inner
automorphisms act trivially on traces, the Jacobian factors through the abelianization `N ∈ GL(2,ℤ)`, so
`char(J)` is a **class function** — a bounded polynomial in `(tr N, det N)` — and therefore equals the catalog
*universally*, for metallic and non-metallic monodromies alike. The all-`n` tower was thereby reframed as a single
representation-theory question: **decompose `ρ_n`** (the `GL(2,ℤ)`-representation on the SL(n) trace ring) into its
`Sym^d` pieces. The explicit module-isomorphism `P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}` was proved exact over `ℚ[m]`
at `n = 3, 4`.

The tower had a meaning, too — though that meaning would later be the source of the sharpest *negative* (chapter
07): at the golden seed every tower eigenvalue is `±φᵏ` (**B107**), one self-similar scale.

→ `03_degree_rank_and_the_knot.md`.
