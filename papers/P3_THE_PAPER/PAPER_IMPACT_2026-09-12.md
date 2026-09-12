# What B1332–B1335 change in THE PAPER

*For the seat that owns `main.tex`. **Nothing here is an edit** — this bench did not touch the paper.
Each item names the line, quotes what is there now, and states what the record can now support.
Several of the stale sentences **understate** what has been done; one needs a new caveat.*

Arcs: B1332 (+3 addenda), B1333 (+2 addenda), B1334 (+1 addendum), B1335. All on
`claude/paper-verification-ufp0zn`, none on main.

---

## 1. §14 line 1191 — the named blocker is CLEARED

> *"The first is not yet a finite computation: the $54$ multi-cusped chiral covers to degree ten are
> named, but **the index on several boundary tori must first be derived from the same pair sequence**
> before it can be evaluated there."*

**Derived (B1333), and the covers are evaluated (B1333 addendum).** The formula is *unchanged* —
`I(V) = (a_0 - a*_0) + t*_0 - r_1`, in `D` `I = sum_i t_0^(i) - r_1`. Of B1297's five inputs, the two
that could have failed both survive `c > 1`: the exactness step needs `H^0(M;V*) -> H^0(dM;V*)`
injective (it is: `v -> (v,...,v)`, `M` connected), and the annihilator property survives because the
pairing on `H^1(dM)` is the direct sum of the per-torus ones. What changes underneath:
`B^1(dM) = (+)_i B^1(T_i)` — a naive extension gets `r_1` wrong there — and isotropy becomes a
condition on a *sum*, so it can vanish by cancellation between cusps.

Verified on 3532 sectors with zero identity failures, and it reproduces B1332's one-cusp numbers on
`s958` sector for sector.

## 2. §14 line 1191 and §8 line 817 — the computation is DONE, and it returns zero

> §8: *"The $54$ multi-cusped chiral covers, where such twists abound, **are the named next
> computation**."*

**Done.** All 54 (not 51 — the three that first resisted PSLQ were a normalisation artifact, every
trace including traces of squares lying in `Q(sqrt-3)`), three primes, **38070 sectors**, zero
identity failures, **1841 of them with two or more live cusps** — the regime that cannot exist on one
cusp. **Index zero in every one.** The two 5-cusped covers were redone *exactly* over `Q(zeta_12)`
(486 sectors, 58 with `>=2` live cusps) because `r_1` is a difference of ranks and a mod-`p` zero
does not force an exact one.

**The trigger does not fire.** Not proved unfireable: one germ shape on two covers for the exact
pass, and a lean germ set for the broad one.

## 3. §14 line 1193 — "the two unprotected sectors ... vanish for a reason not yet proved"

Still true that the reason is unproved. But the evidence base and the shape of the problem have both
moved:

- **A proof now exists on a stated domain (B1334).** On the identity component `S^0` of the
  cusp-trivial character group, `I = 0` — by cusp-triviality holding `t_1` constant, lower
  semicontinuity of `r_1`, the inversion-symmetric identity `r_1(chi) + r_1(chi^-1) = t_1`, and
  irreducibility of the torus. It needs **no Galois, no cusp-locality, no isotropy** — only the
  dimensions enter. Non-vacuous iff `dim S = b_1(M) - c > 0`: **2 of the 54 covers** (`d10_4`,
  `d10_35`), where the order-3 cusp-trivial characters are *exactly* the cube-root points of `S^0`,
  so every twist the programme uses on them is covered.
- **A no-go explains why it stops there.** Peripheral holonomy is unipotent, so `t_0 > 0` iff `chi`
  is cusp-trivial, and by T5 the index is identically zero off that locus. On a one-cusped manifold
  that locus is **finite**, so no character deformation can ever reach it; deforming `rho` fails too
  (off-parabolic ⇒ `t_0 = 0` ⇒ T5). All 23 one-cusped covers to degree ten have `b_1 = 1`.
- **Three proposed mechanisms are now excluded**: Galois (B1331 §3, the targets are chiral),
  strong cusp-locality (B1332 add. 1 — `L_psi` moves with `psi`), and isotropy *as the general
  reason* (B1333 add. 2 — it fails in 36 of 40 multi-cusp sectors while `I = 0` in all 40).
- **The one-cusped case reduces entirely to isotropy**, now its only live route, and that claim rests
  on **128 genuine scalar equations across nine manifolds** with an explicit vacuity audit
  (B1332 add. 3) — three exactly over `Q(zeta_12)`, six in characteristic zero on the geometric
  holonomy. It did not break under attack.

## 4. §8 lines 761–762 — a caveat that should be STRENGTHENED, not softened

> *"the index has returned zero on every sector examined, and whether it is ever non-zero on a
> one-cusped hyperbolic manifold in its domain is not established. Until it is, the index is a
> formula that has always returned zero, not a demonstrated instrument."*

Still true in characteristic zero. **But B1335 exhibits a non-zero index over `F_7` and `F_13`** on
the chiral one-cusped `m010`: `Sym^3 (x) chi`, in domain `D`, all four identities intact, relators
`+I` so the `-I` trap does not apply, peripherals genuinely unipotent, no theorem T2–T5 applying.
It **dies in characteristic zero** — `rho_geo(m010)` has `tr(mu) = -2`, so odd germs have `t_0 = 0`
and vanish by T5, and with valid even germs char 0 gives `I = 0` in all 10 sectors (singular-value
gaps `1e45`–`1e50`). So the programme's vanishing is untouched.

What it establishes is worth a sentence in §8 or §14: **the identities and the domain conditions do
not imply `I = 0`** — over a finite field they all hold while `I = +-1`. So no proof can be assembled
from them alone, and any proof must use something specific to characteristic zero or to the geometric
component. That closes off a class of attempts and explains why formal manipulation of the four
identities never worked.

## 5. A correction the paper does not currently carry

B1332 §1's reduction — "`I = 0` follows from isotropy alone" — **does not hold pointwise**. Isotropy
of `L_V` gives only `dim L_V <= t_1/2`; equality needs `L_{V*}` isotropic too. B1335's `m010` sector
is the counterexample (`L_V = 0` is isotropic, `I = 1`). As a statement about the *class* it is
sound. The paper does not state the reduction, so nothing there is wrong — but if a future draft
reaches for it, it must be the class version.

---

## Summary for §14's list

| what §14 says is owed | status now |
|---|---|
| derive the index on several boundary tori | **done** (B1333) |
| evaluate the 54 multi-cusped chiral covers | **done**, 38070 sectors, zero (B1333 add.) |
| the theorem that none exists | **proved where `dim S > 0`** (B1334); open elsewhere |
| is the index ever non-zero in its domain? | **not in char 0**; yes over `F_p` (B1335) |
| why the unprotected sectors vanish | reduced to one-cusped isotropy, its only live route |

The list in §14 is still "longer than one item" — the character-variety components, the `theta`-odd
non-abelian direction, the higher-rank components, the singular closing, and the two priced
identifications are all untouched by this work.
