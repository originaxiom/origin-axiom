# B1040 — the isomonodromy cluster restored, and the cluster's own `[exact]` tag does not survive contact

**Date:** 2026-08-11 · **Lane:** the consolidation refresh, campaign **step 5** (*"re-verify the
identities before restoring, **never restore from memory**"*). Gate 5 untouched; zero anchors;
nothing to `CLAIMS.md`.
**Files:** `verify.py` → `results.json` (17 checks) · lock `tests/test_b1040_isomonodromy.py`.

**Three debt rows — B164 · B169 · B150 — into one law.** The fourth of B1037's seven clusters, and
the first whose numerical half is re-runnable here, *because it ships with a control*.

---

## 1. THE LAW

The seed's Betti object is the once-punctured-torus `(1,1)` Fricke cubic. **`dim = 6g−6+2n = 2` at
exactly two surfaces** — `(1,1)` and `(0,4)` — so the **4-punctured sphere is the object's only
dim-2 partner**. It carries the **Jimbo–Fricke cubic**, whose **three Vieta involutions** generate
the Painlevé-VI / mapping-class dynamics; it **meets the seed at one fibre** (`tᵢ = 0` sends `Φ` to
the OPT cubic at **`κ = 2`, the void fibre**); and the **same `SL(2,ℤ)`** acts with metallic
dynamical degree `λ_m²`. Its Schlesinger flow is a genuine **monodromy-preserving** deformation —
**but its time is a dimensionless modulus and the system is scale-free**, so the Hitchin side
**relocates** the firewall rather than crossing it.

**Re-derived here, not quoted:** all three Vieta maps are involutions **and preserve `Φ`
symbolically in all seven variables** (the four boundary traces stay free — the cubic as a *family*,
not one fibre); the `κ = 2` bridge; and — the piece that makes the comparison a comparison of *one*
object — **`κ = tr[A,B] = λ + λ⁻¹` exactly**, so B150's class-S cubic and the seed's κ level sets
are **the same equation**, with `κ = −2 ⟺ λ = −1`.

## 2. WHAT RE-VERIFICATION SHARPENED — three corrections, and none of them is cosmetic

### (i) The `[exact]` tag is on the wrong thing

B169's **P1 is tagged `[exact]`**. What its script computes is an **eigenvalue identity**.

> **No Picard lattice and no homological action is computed anywhere in the cluster.** The
> *identification* of `λ_m²` as the **dynamical degree** on the cubic is **Cantat–Loray's theorem**,
> carried by citation. The exactness is the **algebra's**, not the identification's.

The algebra itself generalises, which is worth banking: `λ_m = (m+√(m²+4))/2` and `λ_m²` has minimal
polynomial `u² − (m²+2)u + 1` — verified **symbolically in `m`**, where B164 and B169 checked
`m = 1,2,3`.

### (ii) The dimension count was carried by citation — and is **classical, not ours**

B164 states *"`dim = 6g−6+2n = 2` only at `(1,1)` and `(0,4)`"* as an **inline parenthetical**. A
repo-wide search for `6g−6` returns **exactly two hits, neither a computation**. It is a two-line
exhaustive argument: `3g+n = 4` with `2g−2+n > 0` gives `g=0 → n=4`, `g=1 → n=1`, and `g ≥ 2` forces
`n = 4−3g < 0`. **Proved here.**

> **And this is emphatically not a discovery.** The fact is classical (Fricke; Cantat–Loray), and
> **`docs/OPEN_LEADS.md:209` says so in as many words** — *"the 'exactly two cubic surfaces'
> dim-count is **classical-known** … **not a discovery**"*. What changed is only that the corpus now
> **checks** what it had only cited. **A verification, not a result** — and saying which is the
> whole point of the exercise.

### (iii) A supersession the row had to respect, and an assertion that computes nothing

**B164's C4 is superseded by B169's P1** — C4's point-orbit-norm proxy tracked the *naive*
(cancellation-free) degree, not the dynamical one, and B164 records the refutation itself. Restoring
C4 as written would restore a superseded reading.

And **B169's two P3 checks pass `True` literally** — they assert, they do not compute. Its one
formalisable sub-claim, **scale-freeness**, is checked here for the first time: under `s → cs`,
`t → ct` the flow `dA_i/ds = [A_3,A_i]/(s−t_i)` is homogeneous, so no dimensionful parameter
appears. **The verdict stays POSTULATED anyway** — a verified homogeneity does not promote a
structural reading to a theorem.

## 3. THE NUMERICAL HALF, AND WHY IT COUNTS AS EVIDENCE

Re-run here via B169's own reproducer (invoked, not reimplemented — the B1033 pattern):

| | measured here |
|---|---|
| Schlesinger flow, max invariant drift over `s: 2→3` | **4.25 × 10⁻¹⁰** |
| **non-Schlesinger control** | **1.63 × 10¹** |
| ratio | **≈ 4 × 10¹⁰** |

> **The control is the evidence, not the drift.** RK4 at `h = 0.01` carries `O(h⁴)` truncation, so
> `4×10⁻¹⁰` is what a *correct integration of anything* would give. What shows the monodromy is
> conserved is that a **wrong ODE breaks it by ten orders of magnitude**. A restoration that banks
> the drift without the control banks a number that proves nothing.

A second non-vacuity check, added here: the **composite** `s_y ∘ s_x` is verified **not** to be an
involution. Three involutions generating only involutions would be a finite group, and there would
be no Painlevé-VI dynamics to speak of.

## 4. CARRIED BY CITATION — named, not implied

**Painlevé-VI itself** (that the `(0,4)` Vieta dynamics *is* the Painlevé-VI monodromy action —
Jimbo–Miwa, Boalch). **B150's class-S dictionary** — a *tagged literature comparison*
(FORCED / PERMITTED / RHYME), not a sandbox computation, whose **τ-modularity face is tagged
RHYME**: same group name, different space, a **homonym**. **The dynamical-degree identification**
(Cantat–Loray). **The Hitchin/Higgs side** — the hyperkähler metric and spectral curve, where the
external scale would live explicitly — **NEEDS-SPECIALIST in B169's own words**, and not attempted.

---

**Three debt rows retired.** Band B100–B199 goes **23 → 20**, corpus **217 → 214** —
*exactly the three rows, no drift*; the first pair is measured with rows written by B1040
and later removed. **The three clusters left in this band cannot be closed in this
sandbox** — arithmeticity needs SnapPy, the collective and the open arrow need heavy
numerics — and they stay **PENDING with the blocker named**, reusing the triage's own word
rather than coining a fourth.

**Verdict: PROVED**, with each part at its own tier — `[exact]` for the algebra, `[num]` **with its
control** for the flow, **POSTULATED** for the relocation verdict. 17 checks.

## 5. A LOCK THAT THE CAMPAIGN'S OWN SUCCESS BROKE

Landing this arc **broke a passing lock in B1033** — the third time in this refresh that acting on
a measurement moved it. The check asserted that stratifying the debt ledger by the `claim ≥ 500`
bar *"would discard the entire early corpus"*, and implemented that as **`> 200` rows dropped**.

**B1038, B1039 and B1040 retired thirteen rows, and the count crossed at 198 of 216.**

> **The finding never moved.** The lowest above-bar row is still **B870**; the share discarded is
> still **92 %**. What broke was an **absolute count used to express a structural claim** — inside a
> campaign whose entire purpose is to make that count smaller.
>
> **And B1033 had already written the right form in prose:** *"the lock bounds the share rather
> than pinning the integer, precisely so ordinary consolidation work does not break it."* **The
> check simply did not implement its own stated design.** Amended to a share bound (`> 0.85`), with
> the raw count still reported beside it.

*A lock whose threshold your own programme is trying to cross is a lock that will fail on success.*

**The pattern across four restorations is now stable enough to state.** B1038 found nothing wrong.
B1039 found a **false slogan** and an **unstated hypothesis**. B1040 found an **`[exact]` tag over a
computation that was never done**, a **citation standing in for a two-line proof**, and **two checks
that assert `True`**. In every case the defect was *invisible from the claim line* and *visible
within minutes of recomputing*. **That is the campaign's step 5 earning its cost** — not as a
formality before restoring, but as the only thing that finds these at all.
