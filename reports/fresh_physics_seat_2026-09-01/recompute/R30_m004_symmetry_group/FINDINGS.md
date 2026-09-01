# R30 (filed 2026-09-01 as "R26", renumbered: R26 was already B1080/B1011) — Sym(m004) order and amphichirality (closes R3_REPORT §3 gap "D4 order not re-verified")

Date 2026-09-01. Independent SnapPy call, one line, nothing imported from the repo:

```
import snappy
M = snappy.Manifold('m004'); G = M.symmetry_group()
G.order() -> 8 ; G.is_amphicheiral() -> True ; str(G) -> 'D4'
N = snappy.Manifold('o10_150700'); N.chern_simons() -> -0.0833333 (= -1/12 mod 1/2 ≡ 5/12) ; N.volume() -> 10.149416064
N.symmetry_group().order() -> 2 ; is_amphicheiral() -> False
```

Verdict: **STANDS.** B302 (`frontier/B302_multiplicity_hidden_z3/FINDINGS.md` l.17–19: "Sym(m004) = D4 (order 8 = 2³)")
and B803 l.189 are reproduced. The o10_150700 line re-confirms L193 (chiral, |CS| = 1/12 ≡ 5/12) from the seat's
R24 addendum with a second independent call. No observable content is added by this fact; it is a structural lock
on the object's identity only.
