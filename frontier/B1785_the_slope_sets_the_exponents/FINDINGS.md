# B1785 — THE SLOPE SETS THE EXPONENTS (MAIN'S PLAN, STEP 1, GROUNDWORK): IN B1656'S FRAME THE LEADING EXPONENTS OF EVERY SECTOR'S MASS RATIOS DEPEND ON THE LINE'S SLOPE ALONE — THE OFFSET MOVES ONLY PREFACTORS; ON α = 2/5 AND α = 1/10 THE SECOND-GENERATION EXPONENTS ARE (UP, DOWN) = (3/10, 1/5); ON MANY SLOPES THE PAIR IS {x, ½ − x} WITH x THE HIGGS'S TWIST ‖3α‖

**Verdict: PROVED (a census, computed; data-free; one comparison with data, post hoc, labelled in § 3).** cc (main),
2026-10-27, step 1 of main's plan (the reductions; docs/MAINS_PLAN.md; P-393). **0 of 19.**

## 1. The census (`verification/exponents.py` → `exponents.json`)

Every flat line on record — B1713's 266 of order ≤ 12 and B1755's 396 of order 13, 14, 15, 20, 662 in all — at Re τ = 1/3
and Im τ = 4, 5, 6 with B1726's sealed `compute()` (B1656's frame at B1667's end, the Higgs DR, both readings, both
horocycles). For each sector, reading, horocycle and ratio (m₂/m₃, m₁/m₃), the exponent e = −d ln(ratio)/d(2π Im τ) from
a least-squares line through the three heights; the residual of that line is ≤ 0.07 everywhere (the leading power has set
in up to sub-leading terms).

> *Corrected 2026-10-29 (S256; the web seat's THE FRAME NULL relay § 5, the owner's no-lead-lost sweep, recounted on main;
> P-444). "≤ 0.07 everywhere" is false on this arc's own `exponents.json`: 585 of the 15 888 three-height fits exceed
> 0.07 (515 of them m₁/m₃), 67 exceed 1 (52 of them the leptons' m₁/m₃), the largest 5.52 (leptons, L₂, S̃, m₁/m₃ on
> (0, 1/12)), where the fitted exponent is near zero or negative: no leading power at these heights. On those fits the
> exponent is not a leading power; whether the slope-alone statement holds on them is B1788's closed form's question.* No measured value is read.

> *Noted 2026-11-18 (register row P-444, its remaining part;
> `frontier/B1788_the_closed_form_of_the_exponents/verification/p444_window_fits.py` and its run file). **Where the 585
> sit:** 240 are in the torsion degeneracy, all of them m₁/m₃, where m₁ = 0 exactly (B1716) and no exponent exists; 345
> are in the closed form's domain (275 m₁/m₃, 70 m₂/m₃). **What does not change:** § 2's statement on the up sector's
> m₂/m₃ in the seat's reading holds with every fit counted (largest spreads 0.251 at the slope ¼ and 0.042 at 0); the
> medians on 2/5 and 1/10 are the same with the bad fits left out (one moves by 0.001). **The slope-alone statement on
> the bad fits:** as window fits it fails on them: of the 561 that share a slope and key with a good fit, 151 lie more
> than 0.25 from that slope's good median. As leading exponents it holds on the seven lines run at 40 digits to height
> 14 (the worst residuals among those that differ from the closed form): all 28 cases there approach B1788's closed
> form, which is a function of the slope alone; the nine bad fits among them end within 0.003 of it, except one line of
> closed value ½, at 0.017 and still rising (the logarithmic prefactor B1788 describes). The other bad fits were not
> run at height. So the title's statement is about leading exponents; the window at Im τ 4 to 6 has not reached them
> on these fits.*

## 2. What it shows (the seat's reading: up S̃, down S, leptons S; L_max)

- **The exponents depend on the slope alone.** Over the offsets b of one slope the up sector's m₂/m₃ exponent varies by
  at most 0.042 (0.25 only at α = ¼, a tie); the offset moves the O(1) prefactors — which is why the offset is selective at
  each order (B1755) while the exponents are not.
- **On α = 2/5 and on α = 1/10 the second-generation pair is (up, down) = (3/10, 1/5)** (medians 0.301, 0.199 and 0.300,
  0.199), and the leptons equal the down quarks on α = 2/5 at the exponent level (B1728's identity). The first generation
  separates them: (up, down, leptons) m₁/m₃ exponents 0.806, 0.550, 0.549 on 2/5 against 0.652, 0.700, 0.498 on 1/10.
- **A regularity, observed, not proven:** on many slopes the second-generation pair is {x, ½ − x} with x = ‖3α‖, the
  distance of the Higgs's twist 3α (6Y_H = 3) from an integer — on α = 2/5, 3α = 6/5 and x = 1/5; which sector takes x
  depends on the slope's range (on α = 1/15 the same x = 1/5 goes the other way: up 0.197, down 0.301). It fails on some
  slopes (4/15, 2/11, 4/9); a closed form from the theta characteristics is the next sub-step.
- **Contrast:** in B1653's point-coupling frame the exponent stayed ½ in every sector on every line (B1692); in B1656's
  four-channel frame the slope sets it.

## 3. Against the data (POST HOC, labelled — one look, at two numbers)

HZ2021's ln(m_c/m_t) = −5.63 and ln(m_s/m_b) = −3.96 divided by 2π × 3.03 give 0.296 and 0.208 — the pair (3/10, 1/5).
Read the other way: the slope 2/5 (or 1/10) carries the measured ratio of the second-generation exponents, 3 : 2, and Im τ
is the scale at which they are met (2.99 from the up quarks, 3.15 from the down quarks; the strip's 3.03 between). The first
generation needs large prefactors (about e^3.5) at both slopes — the offset's job.

## 4. What it means for the plan (P-384, P-393)

- **What a principle for the slope must do:** give the Higgs's twist ‖3α‖ = 1/5 with the up quarks on the ½ − x branch —
  i.e. the measured 3 : 2 between the up and down second-generation exponents; that ratio is the slope's whole content at
  leading order. A principle that gives α = 1/10 instead would need the first generation to choose between them.
- **Not a reduction yet:** the census explains what the slope does; it does not force it.
- **Next:** the closed form of the exponents from the theta characteristics (which branch each sector takes), then the
  candidate principle stated before its check, then the sealed prediction at untested orders (25, 30).

## Seen first

`VERDICT topic-sweep /exponent|hierarchy exponent|q-exponent|leading power|Froggatt|slope/ (full text): 320 of 1532 arcs on main match (NEGATIVE 80, OPEN 10, PROVED 227, RETRACTED 2, no verdict file 1)`
— bearing on it: B1691 (exponents at the two fixed points), B1692 (the line keeps the exponent ½ in B1653's frame), B1693
(sealed against data), B1728, B1755. **The register:** P-169, P-227, P-240, P-384, P-392. **Literature:** Froggatt–Nielsen
hierarchies from charges (1979); modular-flavour hierarchies near the cusp (the check of 2026-10-24, P-382).

## Files

`verification/exponents.py` → `exponents.json`, `exponents_run.txt`. The lock: `tests/test_b1785_the_slope_sets_the_exponents.py`.
