# V-2' — THE ANTILINEAR COMPLETION: derivation notes, checksum catches, fences

**Question.** V-2 (B1125) proved no LINEAR sign-lift of the object's E6 embedding gives
compact su(3) color, and diagnosed the type reason: compact real forms come from an
ANTILINEAR conjugation, never a linear inner twist. The object's own antilinear structure
is the mirror (amphichirality, the diagram fold pi_mirror = the outer automorphism
swapping 27 <-> 27bar, TERMINOLOGY.md's "the fold / theta"). Does the object's own
mirror-conjugation, restricted to I2 (color), give (0,8)?

**VERDICT: COMPACT-FROM-MIRROR.** sigma_c control: global (0,78), I2 (0,8) — PASSED (the
"theta=identity" reading of B1125's compact-control LABEL is a red herring, see section 2;
theta_split is the correct linear shadow). sigma_mirror_primary (tau . theta_A_base,
antipodal/class A, the same base element that reproduces B1119's "variant A"): I2 = **(0,8),
compact**. Full 48-element torsor: exactly **4 of 48** antilinear conjugations give
compact I2 — all four in antipodal/class A, all four 300-trial re-verified — each giving
the identical signature (0,8). All 44 others land on (4,4,0) or (5,3,0), genuinely
indefinite. See section 6 for the full table and an unplanned bonus finding (the compact
hits' own ambient real form matches E6(-26), the exact near-miss B1125 flagged).

## 0. Why this had to be re-derived, not just imported

B1125's own code (`b1125_sweep.py`) builds 48 verified LINEAR automorphisms theta of
e6(C) (Chevalley bases, real/rational matrices throughout — no complex numbers anywhere
in that script) and reads compactness DIRECTLY off theta's own +-1 eigenspaces, RAW,
unflipped. That is the right question for a LINEAR torsor (does the theta-defined
"grading" of the split form's own coordinate space happen to look compact), and B1125
proved the answer is no, always landing on the fixed structural fact B|I2 = (5,3,0) or
an indefinite/impure mix.

It is NOT the right computation for an ANTILINEAR conjugation. An antilinear involution
sigma of e6(C) is not itself expressible as "an eigenspace restriction read raw" — its
associated real form is g_sigma = V+(theta) (+) i*V-(theta) for some LINEAR involution
theta with sigma = tau . theta (tau = a reference antilinear conjugation), and the
i on the V- summand FLIPS the sign of B's restriction there before it combines with
B|V+. This is the one piece of new mathematics this arc adds; see section 1.

## 1. The antilinear-signature formula (derived, then checked as a live control)

Fix tau := complex conjugation of coefficients relative to the Q-rational Chevalley
basis (6 h_i + 72 e_r) — the "split" conjugation, whose fixed points are the split real
form e6(6) itself. For ANY involutive automorphism theta of e6(C) with a real/rational
matrix in this basis (theta^2 = id, brackets preserved), sigma := tau . theta is ALSO
an antilinear involution:

  sigma(sigma(v)) = theta(tau(theta(tau(v))))
                   = theta(theta(tau(tau(v))))   [tau(theta(w)) = theta(tau(w)) for real theta]
                   = theta(theta(v)) = v.

Writing v = x + iy with x in V+(theta), y in V-(theta) (the real +-1 eigenspaces),
sigma(v) = theta(tau(v)) = theta(x - iy) = theta(x) - i*theta(y) = x - iy is exactly
v again iff... solving sigma(v)=v directly: the sigma-FIXED real form is

  g_sigma = { x + iy : x in V+(theta), y in V-(theta) } = V+(theta) (+) i*V-(theta).

theta preserves the ad-invariant form B (any Lie algebra automorphism of a simple
algebra preserves its essentially-unique invariant form up to scale, and here exactly,
since theta is built to preserve the bracket and B is the canonical ad-invariant form).
So B(theta u, theta v) = B(u,v) for all u,v, and for x in V+, y in V-:
B(x,y) = B(theta x, theta y) = B(x, -y) = -B(x,y) => B(x,y) = 0. V+ and V- are
B-orthogonal. Hence for x1,x2 in V+, y1,y2 in V-:

  B(x1+iy1, x2+iy2) = B(x1,x2) + i*B(x1,y2) + i*B(y1,x2) - B(y1,y2)
                     = B(x1,x2) - B(y1,y2)                                    [**]

(the cross terms vanish by orthogonality). So: **the raw signature of B on V-(theta)
gets its sign flipped before adding to the raw signature on V+(theta).** If B|V+ has
raw signature (p+,n+,z+) and B|V- has raw signature (p-,n-,z-), then

  signature(g_sigma) = (p+ + n-, n+ + p-, z+ + z-).                          [COMBINE]

This is `combine_antilinear()` in the script. It is the ONLY new formula this arc
introduces; every other layer (the corrected ad-invariant form, hatch/I1/I2, pi_mirror,
w0(I2), the F2 sign-lift solver) is a faithful, independent re-derivation of V-2's own
already-verified machinery, run again here as the trust-building step the task asked
for before extending it.

## 2. Which theta is sigma_c's linear shadow? (a labeling trap, caught before it mattered)

B1125's FINDINGS.md speaks of "the compact-involution control" returning character -78,
and refers to the element with family="permute", pi=id, eps=1 (theta = the IDENTITY
MAP, exactly). That element does carry character -78 (a fact about the classification
CHECKSUM: -tr(identity) = -78, the value uniquely diagnostic of the compact form under
the abstract classification theorem for real forms of E6). But theta=identity is not a
Cartan involution of anything — it is the trivial map. Composed with tau it gives
sigma = tau . id = tau itself, i.e. literally the SPLIT conjugation — its fixed-point
real form is the split form e6(6), not compact, and [COMBINE] applied to
(V+=everything, V-=0) just returns B's own native (indefinite) global signature
unchanged, (42,36) here (verified below, section 3) — NOT (0,78).

**This is flagged explicitly because the task's brief itself paraphrases B1125 as
"V-2 saw -78 globally for sigma_c" — read literally (theta=identity) this is the WRONG
element**, and using it would have failed the required control non-vacuously (a
genuine, informative near-miss, not a bug in the detector). The CORRECT linear shadow
of sigma_c is theta_split := the (antipodal, pi=id) element — B1125's own "split
control" (character +6, dims (36,42)) — which IS the genuine Chevalley/Cartan
involution of the split form (h -> -h, e_r -> eps(r) e_{-r} with the properly-solved,
non-uniform eps). Composed with tau via [COMBINE], THIS is what gives the fully compact
(0,78) globally and — the required check — (0,8) on I2. Both readings (the naive
theta=identity one, which fails, and the correct theta_split one, which passes) are
computed and reported below, not silently corrected away.

## 3. By-hand pre-verification (checked against the live sympy run, not a substitute for it)

Restricting theta_split to I2: theta(h) = -h sends I2's 2 coroot directions to their
own negatives (eigenvalue -1, landing in V-, raw B-value = the Cartan-positive entry,
so POSITIVE). theta(e_r) = eps(r) e_{-r} pairs each of I2's 3 positive roots with its
negative; on each 2-dimensional pair {e_r,e_{-r}} the matrix [[0,eps(r)],[eps(r),0]]
has eigenvalues +-1 REGARDLESS of eps(r)'s sign (char. poly lambda^2 - eps(r)^2 =
lambda^2 - 1), splitting 3 dimensions into V+ and 3 into V- — so dim(I2 cap V+) = 3,
dim(I2 cap V-) = 2 + 3 = 5, matching the (5,3)-shaped structural split B1125 already
established for the LINEAR reading. The raw B-value on the lambda=+1 eigenvector
e_r + eps(r) e_{-r} is -2 eps(r); on lambda=-1's e_r - eps(r) e_{-r} it is +2 eps(r).
Global purity (already verified and asserted in B1125's own split control, reproduced
independently in Layer 5 here) forces eps(r)=+1 uniformly on I2's 3 positive roots (a
DERIVED consequence of the general Cartan-decomposition purity theorem — B negative
definite on the whole 36-dim k, positive definite on the whole 42-dim p, hence on any
subspace of either — not a separate assumption). That gives raw sig_plus = (0,3,0)
[3 negative entries, -2] and raw sig_minus = (5,0,0) [2 Cartan-positive + 3 entries at
+2]. [COMBINE]: (0+0, 3+5, 0) = (0,8,0). This hand-computation is a cross-check, not
the certificate — the certificate is the exact sympy run in `V2prime_sweep.py` Layer 6,
which re-derives eps(r) from the actual F2 cocycle solve rather than assuming it.

## 4. The torsor and its ambiguity (enumerated, per the task's request)

"The mirror-conjugation" is not perfectly unique — pi_mirror (the diagram fold) has
TWO inequivalent signed Chevalley-automorphism lifts to a genuine linear involution
(the "antipodal" and "permute" families of B1125 section 4), crossed with 2 lattice
classes (A: identity on color: pi_mirror alone; B: pi_mirror . w0(I2), duality on
color), each with its OWN finite F2 kernel of further sign choices. Composing each with
tau gives the full antilinear torsor swept in Layer 7 — 48 elements, mirroring B1125's
own 48 exactly, now read through [COMBINE] instead of raw.

- PRIMARY candidate: sigma_mirror_primary := tau . theta_A_base, theta_A_base = the
  SAME (antipodal, class A) base element that reproduces B1119's "variant A" exactly
  under the LINEAR reading. This is reported first because it is the same family
  (antipodal) as theta_split's own control, keeping the sigma_c vs sigma_mirror
  comparison apples-to-apples (same Chevalley-automorphism SHAPE, only pi differs:
  id vs pi_mirror).
- FULL TORSOR: all 4 (family, lattice class) combinations, all kernel elements in
  each, 48 total — reported in `layer7_full_torsor_sweep`.
- SECONDARY / alternative construction (Layer 8b, a genuinely different antilinear
  map, only reported if well-defined): sigma' := tau . theta_split . theta_A_base
  (composing THREE maps — using the COMPACT form, not the split form, as the
  reference point for "the mirror"). This is only a valid involution if theta_split
  and theta_A_base's product is itself an involution (checked directly, not assumed —
  see Layer 8b's commutativity check); if it fails, this alternative is reported as
  ill-defined rather than silently dropped.
- REJECTED as a base point (Layer 8a): pi_mirror with eps identically +1 (the
  UNSIGNED diagram fold, no compensating signs at all) — checked directly whether
  this is even a valid Lie-algebra automorphism (theta^2=I and bracket-preserving);
  if not, "the mirror" cannot mean the bare permutation, only a genuine signed lift
  of it, which is exactly what the torsor already covers.

## 5. On "the object's own" Galois conjugation vs. this construction — an honest fence

The task's brief describes the mirror as, at the trace-field level, complex
conjugation on Q(sqrt(-3)) (sqrt(-3) -> -sqrt(-3)), the Galois twist paired with the
27 <-> 27bar swap. It is important to be precise about what is and is not being
computed here. B1114's own "no-swap argument" (`b1114_verify.py` Layer 3, reproduced
in spirit though not re-run verbatim in this arc) proves I1 and I2 are each cut out by
Q-RATIONAL linear conditions in the Chevalley basis, and are therefore individually
FIXED POINTWISE by any field automorphism of C/Q — including the actual
Q(sqrt(-3))-Galois twist. In other words: **the literal arithmetic Galois conjugation
of the trace field, applied directly to this Q-rational e6-combinatorial layer, acts
as the identity — it cannot be the source of any nontrivial antilinear structure here,
by B1114's own theorem.** That theorem is exactly why B1114 concluded the Lorentz
gluing (I1 <-> I2) needed EXTRA data, "the observer's choice of real structure, not the
object's."

What this arc computes instead is the construction the task's own phrasing directs
("the antilinear version composes pi_mirror with complex conjugation of the
Q(sqrt(-3))-structure"): tau, the GENERIC complex conjugation that is forced the
instant one allows non-real coefficients over this same Q-rational data (the same
operation that, restricted to the Q(sqrt(-3)) subfield the object's actual hyperbolic
holonomy lives in — a DIFFERENT, cited-not-rederived layer per B1114's own Layer-1
fence — specializes to exactly sqrt(-3) -> -sqrt(-3)), composed with pi_mirror's
verified signed lift (the LINEAR shadow, independently identified as the diagram fold
= the 27 <-> 27bar outer automorphism, TERMINOLOGY.md's "the fold / theta"). This is a
composite structure — generic complex conjugation ON TOP OF a combinatorial (not
arithmetic) symmetry of the root system — not a pure Galois action internal to the
object's own Q-rational data. It is the most literal computable reading of the task's
construction available at this layer, and it is reported as such rather than
overclaimed as "the object's own Galois twist made manifest." Gate 5 untouched (no SM
values are computed or compared here).

## 6. Results (the live run; see `V2prime_results.json` for the full machine record)

**Controls (Layer 5, reproducing V-2's linear torsor first — machinery trusted before
extending it):** split (antipodal,id): character +6, dims (36,42), exact match. theta=
identity (permute,id,eps=1): character -78, dims (78,0), exact match to B1125's LABEL.
Variant A base (antipodal, class A): character +2, color dims (3,5), color signature
raw sig_plus=(0,3,0), sig_minus=(5,0,0) — an EXACT match to B1119/B1125's reported
(5,3), reproduced independently. All three controls pass.

**Layer 6, THE REQUIRED CONTROL.** sigma_c := tau . theta_split:
- GLOBAL antilinear signature: **(0, 78, 0) — compact.** (Contrast: theta=identity's
  OWN antilinear reading, sigma=tau alone, gives (42,36,0) — NOT compact. This is the
  labeling trap of section 2, now shown numerically: the LINEAR "-78 control" and the
  ANTILINEAR "(0,78) control" are carried by two DIFFERENT theta's, not the same one.)
- I2 (COLOR) antilinear signature: **(0, 8, 0) — compact.** THE REQUIRED CONTROL PASSES.
  The detector genuinely sees compact color when it is present.

**Layer 7, sigma_mirror.** Primary candidate (tau . theta_A_base, antipodal/class A
base element):
- I2 (color) antilinear signature: **(0, 8, 0) — COMPACT.**
- Global antilinear signature: (26, 52, 0) — NOT the fully compact form (that's expected
  and fine: sigma_mirror need not itself be the compact real form of ALL of e6 for its
  I2 restriction to be compact — a compact subalgebra can sit inside a non-compact
  ambient real form, exactly as compact su(3) sits inside noncompact so(9,1) in the
  cited-but-different abstract embedding B1125's FINDINGS mentions).

  **Unplanned bonus finding.** (26,52) is exactly the (noncompact-complement,
  maxcompact) dimension split of **E6(-26) = EIV = M(O,C)** (maxcompact f4, dim 52) —
  the SAME real form whose maxcompact-dimension signature underlies the classification
  character -26 already used as this instrument's own checksum value throughout (the
  ALLOWED_CHARS set {6,2,-14,-26,-78} is exactly (p-k) for the 5 real forms with
  maxcompact dims (36,38,46,52,78); 26-52=-26 checks). This is the identical real form
  B1125's FINDINGS.md flagged as "the near-miss the classification checksum alone would
  have mis-called a hit" (reached there via the LINEAR permute/class-A route, where I2
  stayed pointwise-fixed at (5,3), never compact). **Here, via the ANTILINEAR route
  instead (a different theta entirely — antipodal/class-A, not permute/class-A — composed
  with tau), the SAME target real form is reached and THIS time I2 (color) really is
  (0,8).** This is a signature-level identification (matches the classification
  invariant this arc's own instrument already relies on) — not an independently
  reproven isomorphism via restricted-root-system data — and is reported at that
  strength, not overclaimed further.

**The full 48-element torsor (Layer 7 sweep, both families x both lattice classes):**

| family | class | n elements | characters (linear) | linear-color-pure | antilinear-color-compact |
|---|---|---:|---|---:|---:|
| antipodal | A | 16 | {+2} | 4/16 | **4/16 -- all (0,8,0)** |
| antipodal | B | 8 | {+2} | 0/8 | 0/8 -- all (4,4,0), indefinite |
| permute | A | 16 | {-26, +6} | 0/16 | 0/16 -- all (5,3,0), indefinite |
| permute | B | 8 | {+6} | 0/8 | 0/8 -- all (5,3,0), indefinite |

**Exactly the 4 elements already flagged by B1125's own linear-purity check
(`linear_color_pure`) as the only color-pure elements in the entire 48-element torsor are
the ones that become antilinear-compact here — and no others.** This is not a
coincidence needing further explanation: purity of B on each of theta's own raw
eigenspaces (V+, V-) restricted to I2 is EXACTLY the precondition [COMBINE] needs to
produce a definite (rather than indefinite) result; the only new fact this arc supplies
is that these 4 already-known-pure elements combine to (0,8) rather than the (5,3) their
raw/unflipped reading showed. All 4 give the IDENTICAL signature (0,8,0) (matching
B1125's own observation that all 4 linearly-pure antipodal/A elements share raw
sig_plus=(0,3,0), sig_minus=(5,0,0) exactly). All 4 were independently 300-trial
automorphism-reverified with **0 failures**, and theta^2=I reconfirmed.

**Layer 8 fences.**
- (a) The UNSIGNED diagram fold (pi_mirror with eps identically +1, no compensating
  signs): theta^2=I holds, but the bracket-automorphism check FAILS (**38/60 random
  trials**). So "the mirror" cannot mean the bare permutation of Chevalley generators;
  a genuine signed lift (as used throughout) is REQUIRED, not optional — checked
  directly, not assumed.
- (b) The secondary, compact-referenced construction sigma' := tau . theta_split .
  theta_A_base (mirror measured from the COMPACT reference rather than the split
  reference): theta_split and theta_A_base commute (verified) and their product is a
  genuine involution (verified) preserving I2 (verified), so sigma' IS a well-defined
  antilinear involution — but its I2 signature is **(5, 3, 0), NOT compact.** This is an
  honest negative for this SPECIFIC alternative construction: which reference point
  ("the mirror seen from split" vs "the mirror seen from compact") is used changes the
  answer. The PRIMARY, task-directed construction (tau . theta_A, "compose pi_mirror
  with complex conjugation" — a two-fold composition, matching the task's own phrasing
  most directly, and the one built from the SAME Chevalley-automorphism family as
  sigma_c itself, keeping the comparison apples-to-apples) is the one that gives
  COMPACT-FROM-MIRROR; this alternative does not, and both facts are reported rather
  than only the favorable one.

## 7. Summary verdict

**COMPACT-FROM-MIRROR.** The object's own mirror-conjugation (the antilinear completion
of the diagram fold pi_mirror = the 27<->27bar outer automorphism, composed with the
complex conjugation forced once non-real coefficients are allowed over the same
Q-rational Chevalley data B1125 already worked in) DOES give compact su(3) color: I2
signature exactly **(0, 8)**, for the primary candidate and for 4 of the 48-element full
antilinear torsor (all and only the ones already flagged linearly color-pure by V-2's
own purity check). The required control (sigma_c, the genuine antilinear compact
conjugation) independently gives global (0,78) and I2 (0,8), confirming the detector
works. The honest fences: (i) B1125's own "-78 control" LABEL (theta=identity) is a
red herring for building sigma_c antilinearly — flagged and worked around, not silently
fixed; (ii) a second, equally natural-looking antilinear construction (compact-
referenced rather than split-referenced) gives a DIFFERENT, non-compact answer for the
same base element — the construction is not perfectly canonical, and both readings are
reported; (iii) the compact hits' ambient real form matches E6(-26) at the signature
level, the same near-miss form B1125 already named, now reached by a different
(antilinear, not linear) route with I2 actually landing compact this time.
