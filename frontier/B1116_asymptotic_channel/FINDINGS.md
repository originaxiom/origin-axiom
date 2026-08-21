# B1116 — THE ASYMPTOTIC VALUE CHANNEL: the archimedean door is not excluded by any banked no-go (scope audit) + the growth rate = Vol (numeric)

**Status: banked (frontier). Verdict PROVED (the scope audit is a complete quantifier
check; the numeric reproduction is CITED literature — the volume conjecture is proven
for 4₁, Garoufalidis–Zagier — reproduced here to confirm the memo's numbers). Harvest
arc (ASYMPTOTIC_CHANNEL.md; cloud seat credited). Gate 5 untouched. Lock
`tests/test_b1116_asymptotic.py`.**

## THE SCOPE AUDIT (the load-bearing half; the B959 lesson applied to the no-goes)

Every banked value/scale no-go quantifies over SINGLE-LEVEL invariants. A **growth
rate of a tower** — a difference of levels, needing no basepoint, no frame, no
section — is outside all of them. Checked one by one against the exact quantifier:

| no-go | its exact quantifier | growth rate excluded? |
|---|---|---|
| **scale-torsor** (B666 cell S) | G-EQUIVARIANT MAPS into a scale rep, fixed finite G (Hom(G,ℝ₊)=0) | **NO** — a rate is an N→∞ asymptotic, not a G-equivariant map |
| **type law** (B1032) | the COUPLING channel's single-level outputs (finite menu); its OWN scope: "other channels need their own closed form first" | **NO** — the Kashaev tower is another channel with its own closed form (the finite-level values it governs are exactly the arithmetic side of B1108) |
| **frame-relativity** (B936) | values of the twist form on a SINGLE pair, basis-dependent | **NO** — a rate is a basis-free scalar limit |
| **k-blindness** (B1012) | the object's OWN action S, k-independent (∂S/∂k = −CS = 0) | **NO** — the rate = Vol, the object's own volume, which it does have |

> **VERDICT: the archimedean/growth-rate channel is not excluded by any banked no-go —
> and the REASON is the adelic split itself. The no-goes are finite-place theorems;
> the growth rate is archimedean.** B1108's "right at every finite level, wrong in the
> limit" is the same statement: the finite places carry everything except the volume,
> and the volume IS the tower's growth rate.

## THE NUMERIC INSTANCE (verified; CITED literature)

The object's own Kashaev tower J_N(4₁) = Σₖ |(q;q)ₖ|², q = e^{2πi/N} — every finite
level an arithmetic object of the kind B1108 proved cannot carry the volume — carries
Vol in its growth. Three layers (reproduced by an independent mpmath bench):

- **exponent**: 2π·(growth rate) → **Vol = 2.0298832128193…**
- **power**: N^p, p = 3/2 (the one-loop layer)
- **constant**: → **3^{−1/4} = |disc ℚ(√−3)|^{−1/4}** (the torsion layer — the being
  field's discriminant appearing as the leading constant)

**Verified (this bench, mpmath dps=100, pushed to N-windows up to [12800, 102400] —
better agreement than the memo on every layer):**
- exponent = **2.02988321281908…** vs Vol 2.02988321281931… — agreement **2.2×10⁻¹³**
- power = **1.4999999999997…** vs 3/2 — agreement **2.7×10⁻¹³**
- constant = **0.75983568565413…** vs 3^{−1/4} = 0.75983568565159… — agreement **2.5×10⁻¹²**

The constant approaches |disc ℚ(√−3)|^{−1/4} to twelve digits: **a genuine limit, not a
near-coincidence** — the being field's discriminant IS the leading constant of the
object's own quantum tower. Controls: J_N hand-checked exact at N=2,3; the summand real-
positive (|·|²); a second summation route (2·Im Li₂(e^{iπ/3})) reproduces Vol to 30
digits as a cross-check.

## THE ARCHITECTURAL PLACEMENT (what is new here — not the asymptotic, its home)

1. **B1108's negative is exactly right at every finite level and exactly wrong in the
   limit.** Arithmetic CS lacks Vol level-by-level; the TOWER carries Vol as its
   growth rate. The archimedean place is the N→∞ boundary of the finite places
   (adelically standard) — converting B1108's "two doors" (Arakelov; quantum
   modularity) into one open door with a proven core on this very knot.
2. **Two instruments, one expansion.** The quantum-arithmetic tower (this arc) and the
   length spectrum / Ruelle tower (B1107, 15 significant figures, two-bench) compute
   the SAME expansion from opposite sides — tree level = Vol, the 3/2 power and
   3^{−1/4} constant = the torsion/one-loop layer. This gives VI.3's residues a third
   instrument.
3. **The withholding factorisation, realized.** B518's "SM value = (class invariant) ×
   (substrate scale)" is EXHIBITED by the tower: a transcendental/archimedean exponent
   (the growth rate) × an arithmetic coefficient tower (Ohtsuki coefficients, in
   trace-field-flavored rings). The two factors the programme proved it holds
   separately appear here as the two factors of ONE asymptotic.

## THE HONEST FENCE (stated first-class, not buried)

Surviving the no-goes means the channel is **not excluded** — NOT that it delivers SM
values. What is PROVEN through it is **Vol, a geometric value.** Whether SM values are
also growth-rates/periods of object-built towers is the OPEN question: it needs (a)
L180 (do the tower's arithmetic coefficients factor through the trace field's finite
places — a genuine Euler product, not a lone 3^{−1/4} coincidence?), and (b) the
identification of which tower/coupling/measurement yields a specific SM ratio. The
channel is the first honest path to values the programme has ever had; it is a path,
not an arrival. The seven sealed misses stand — re-typed as single-completion
questions, which have no global answers.
