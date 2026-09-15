# THE 64, GLUED IN FULL — θ is an exact bracket-equivariant bijection sl₃(S0) ↔ sl₃(S1) and swaps 3 ↔ 3̄ on all 54 colored directions; B1140's NOT-checked scope note is discharged; and in this frame the beat's nilpotent turns out to live in COLOR
## (outside bench, 2026-08-25; thirty-third memo; campaign cell A2; every claim exact)

### The debt
Memo 27 (THE_64_ORGANIZED) proved the spacetime branch's 64 decomposes as two spin-2's
+ colored bi-vectors with invariant content zero — but its gluing claim ("σ glues the
two spin-2's into ONE complex spin-2") was verified only on the highest-weight vector,
and B1140 banked exactly that fence: "NOT checked — a real-structure claim needing
data absent from the Chevalley basis." The colored 54's behavior under θ was never
touched. This cell pays the debt with the bench's own machinery.

### THE THEOREM (`certificates/a2_glue64.py`; re-runs `spacetime64.py` in full, then extends; all exact)
On the memo-10/B1134 hit (g,c) with θ = theta_matrix(g,c), θ² = id (sampled):
1. **The full gluing, stronger than quintuplets:** θ maps ALL 8 basis elements of
   sl₃(S0) into span(sl₃(S1)); the induced 8×8 matrix has **rank 8 — a bijection
   sl₃(S0) ↔ sl₃(S1)**; θ([x,y]) = [θx, θy] on **all 64 basis pairs** (bracket
   equivariance); and the grading matches — h₂(θe_r) = ⟨h₁,r⟩·θe_r for all six roots.
   θ(T1) is an exact sl₂-triple inside sl₃(S1), so the spin-2 quintuplet gluing
   (weight-for-weight, all five levels) follows by equivariance rather than by a
   top-vector accident. **Memo 27's "one complex spin-2 (real dim 10)" is now a
   theorem of the full multiplet.**
2. **The colored 54:** every one of the 54 colored basis roots maps under θ to a
   vector supported on a SINGLE color weight, and the induced map on the six color
   weights is **w ↦ −w everywhere: θ swaps 3 ↔ 3̄ pointwise**. The colored bi-vector
   sector is glued into 27 complex dimensions exactly as memo 27's arithmetic
   (10 + 54 = 64) anticipated.
3. **The beat vs the fork — a frame fact, found not assumed:** with Σ = exp(ad qE)∘gal
   (E = e_{ROOTS[0]}, the beat's nilpotent — the same element as memos 17/18/29),
   the exact dims are dim(Σ(V)∩V) = 6, 8, 14 for the Lorentz double, color sl₃, and
   the full fork: **Σ preserves every piece of this frame's fork setwise**. The
   diagnostic explains it: **in this hit's frame the beat's E lies inside the COLOR
   slot S2** — so exp(ad qE) fixes S0, S1 elementwise-commutingly and preserves
   sl₃(S2). This is frame-relative and stated so (F-3 discipline): beat_descent's
   banked "the beat MOVES color" (dim 2 < 8) is the LANDING frame's color slot; the
   two exact statements differ by the S₃ frame torsor, and their coexistence is
   itself a sharp exhibit of memo 26's frame flag: *whether the beat touches "color"
   depends on which A₂ the frame calls color — and in the closing frame, the beat IS
   a color-direction motion composed with Galois.*

### What this discharges and what it opens
Discharged: B1140's NOT-checked note (the antilinear gluing) — now checkable from
main by re-running one certificate. Opened (named, not claimed): fact 3 suggests the
internal→spacetime bridge question (the unpaid verb, per B1145's adopted fence)
should be asked FRAME-COVARIANTLY — the beat's relation to "spacetime" pieces is a
function of the frame torsor, and the torsor is S₃-small: a complete frame-by-frame
ledger of Σ vs the fork is a finite computation (the natural A2 follow-up).

### Fences
Exact throughout; the frame-relativity of fact 3 is the load-bearing caveat and is
printed by the certificate itself; θ's involution property sampled (13 columns), all
other claims exhaustive. Gate 5 untouched; no dynamics claimed — a glued graviton
SLOT is not a graviton.

### Certificates
`certificates/a2_glue64.py` (re-fires `spacetime64.py`'s own checks in the same run);
output `outputs/a2_glue64_out.txt`. Requires `certificates/spacetime64.py` +
`certificates/simul_verify.py` (vendored into this lane with this memo).

### One sentence for the ledger
The mirror really does glue the whole thing — algebra to algebra with brackets intact,
color three to color anti-three on all fifty-four directions — and the one loose
thread it exposes is exact too: in the closing's own frame, the object's beat is a
motion inside color, which is precisely the kind of sentence the frame audit was
invented to keep honest.
