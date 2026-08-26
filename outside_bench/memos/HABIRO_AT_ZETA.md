# THE GERM AT ANOTHER BASE — the one-germ coherence transports to base ζ₃ at three of four tested levels (exactly v = 2N at 3·5²), and collapses EXACTLY to v = 0 at the smallest level 15: a sharp, level-dependent split with the mechanism open
## (outside bench, 2026-08-26; sixty-ninth memo; wave-2 cell B3, verified CONFIRMED; memos 39/40's named follow-up executed; neither preregistered clean branch held — the split is the result)

### THE FACTS (`certificates/habiro_at_zeta.py`; all cyclotomic arithmetic exact — sympy resultants over ℚ[x]/Φₙ; the germ at ζ₃ stabilized at two truncation depths and cross-checked by an independent series method)
- Taylor germ of the Habiro element F at q = ζ₃: d₀ = 13, d₁ = 2−2ζ₃, … through d₇ (exact in ℚ(ζ₃)).
- Coherence table v_π(F(ξ) − Σ_{j<N} d_j (ξ−ζ₃)^j), N = 1..8:
  level 3·5² = 75: **[2,4,6,8,10,12,14,16] = 2N exactly**; levels 21 and 147: strictly growing, v ≥ N (and identical to each other); **level 15: [2,0,0,0,0,0,0,0] — total collapse after the universal first-order v = 2** (memo 39's law), stable under recomputing the germ to depth 11 (not a truncation artifact).
- The inert/split behavior of 5 vs 7 in ℚ(ζ₃) was checked and does NOT explain the r-dependence (5 is inert at every r) — the mechanism for why exactly 3·5¹ collapses while 3·5² is perfectly coherent is the named open question this memo leaves.

> **The adelic picture sharpens: the one germ at 1 (memo 40) has a sibling at ζ₃ that coheres perfectly at three levels — one of them with the cleanest law seen anywhere in this arc, v = 2N — and fails exactly at one, the smallest. Whatever the Habiro-ring transport theorem says here, it is not uniform in the level, and the exact table now exists to test it against.**

### Certificates
`certificates/habiro_at_zeta.py`; output `outputs/habiro_at_zeta_out.txt` (in-lane rerun byte-identical).

### ADDENDUM (2026-08-26, from B1158 — THE MECHANISM SOLVED by the seat; correction adopted with credit)
The seat resolved this memo's named open question: the level-15 collapse is
a **base-embedding artifact**, not a transport failure. Expanding around the
π-adically correct cube root (the representative w^exp with exp ≡ 1 mod 3)
restores coherence at EVERY level: **the ζ₃ germ transports uniformly, and
the apparent criterion is exactly p^r ≡ 1 (mod 3)** — which this memo's own
banked table matches perfectly (75: 25≡1 ✓; 21: 7≡1 ✓; 147: 49≡1 ✓;
15: 5≡2 ✗). Also corrected: the splitting caveat — f = 2 for p = 5 (inert),
g = 2 for p = 7 (split) — and the observed v = 2N is local v = N times
residue degree 2. The exact table banked here stands as data; the
"mechanism open" reading is superseded. Credit: the germ computation is
this lane's; the correction and mechanism are the seat's (B1158,
own-verified).
