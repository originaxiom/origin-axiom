# THE OHTSUKI BRIDGE — every finite place reads the same germ: the Taylor expansion at q = 1 approximates each p-power evaluation to π-adic order ≥ its own length, and C-AD3's adelic picture becomes an exact table
## (outside bench, 2026-08-25; fortieth memo; campaign cell C2b — the follow-up memo 39 named, executed; every claim exact)

### The question memo 39 sharpened
Memo 39 proved the raw evaluations of the unified 4₁ element at p-power roots of unity
do NOT cohere with each other (universal v_π = 2). Habiro-ring theory says the
coherence lives elsewhere: every evaluation should be read against the single analytic
germ at q = 1. Preregistered two-outcome: v(N, p^r) := v_π(I(ζ_{p^r}) − Taylor_N(ζ−1))
≥ N for every cell of the table — or not.

### THE THEOREM (`certificates/c2b_ohtsuki_bridge.py`, exact throughout)
1. **The germ, as integers:** the unified element f(q) = Σ_k ∏_{j≤k}(1−q^j)(1−q^{−j})
   (t-adically convergent, term k has valuation 2k — so the truncation is complete,
   not approximate) has Taylor coefficients at q = 1:
   **[1, 0, −1, 1, 3, −7, −24, 90, 352, −1845, −8230, 55654]** (to t¹¹, t = q−1).
   The identity (1−q^j)(1−q^{−j}) = 2−q^j−q^{−j} makes memo 39's I(ζ) literally f's
   evaluation — checked exactly.
2. **The bridge, as a table:** for p^r ∈ {4, 8, 9, 27, 5, 25} and truncations
   N ∈ {4, 6, 8, 10}, the exact π-adic valuations of I(ζ_{p^r}) − Taylor_N(ζ−1):
   | p^r | N=4 | N=6 | N=8 | N=10 |
   |---|---|---|---|---|
   | 4 | 4 | 10 | 9 | 13 |
   | 8 | 4 | 9 | 9 | 12 |
   | 9 | 5 | 8 | 8 | 10 |
   | 27 | 5 | 8 | 8 | 10 |
   | 5 | 4 | 6 | 8 | 11 |
   | 25 | 4 | 6 | 8 | 11 |
   **v(N, p^r) ≥ N in every cell** — the preregistered gate, met with slack.

> **C-AD3's picture, both faces now exact: the finite places do not cohere with each
> other (memo 39's universal v = 2), but every one of them coheres with the single
> germ at 1 — one analytic object, many p-adic shadows, each reading it to the depth
> of the expansion. The integer list above is the shared germ; the corpus's banked
> Ohtsuki-tower arithmetic (B1133's C₀…C₄, the archimedean face) and this table (the
> finite face) are two readings of it.**

### Fences
Exact throughout; the coefficient list is in the bench's normalization of the unified
element (f as written; align conventions with the corpus's Ohtsuki tower before
comparing constants — same warning as the C3 handoff). The gate v ≥ N is the
preregistered floor; the observed slack (e.g. 13 at N=10, p^r=4) is reported, not
theorized. Gate 5 untouched.

### Certificates
`certificates/c2b_ohtsuki_bridge.py`; output `outputs/c2b_out.txt`. Deps: sympy only.

### One sentence for the ledger
The tower that refused to converge rung-to-rung converges perfectly rung-to-germ —
every p-adic shadow of the quantum invariant reads the same twelve integers at q = 1
at least as deeply as the expansion reaches — and with that, the adelic frame's
one-object-many-shadows claim stops being a picture and becomes a table.
