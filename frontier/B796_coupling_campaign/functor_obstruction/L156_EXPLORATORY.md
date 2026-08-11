# L156 — EXPLORATORY. Unsealed, owner-authorised, **NOT BANKABLE**. cc to run it properly.

**cc3, 2026-08-11.** Owner directed: *"just run without seal, were exploring, then
we can inform cc to do it right way."* **No seal, no prior held, no look-elsewhere
ledger. Nothing here is evidence. It is a scouting report for a cell cc should
seal.** Gate 5-Q: measured values appear as filter inputs only.

---

## FINDING 1 — **cc3's forced set was WRONG. The banked set has FIVE values, not eight.**

Tonight's screen (`eligibility_screen.py`, `R12_SCREEN_RESULT.md`) used

`{0, 1/(4φ), 1/4, 1/(2φ), φ/4, 1/2, φ/2, 1}` — **eight values, called "θ-even".**

**The banked set is FIVE:**

> `{0, 1/(2φ), 1/2, φ/2, 1}` — B652 `GRAMMAR_TABLE.md:20` *"the five-tone set
> {0, 1/(2φ), ½, φ/2, 1} + Plancherel ¼–¼ | **FORCED** (given the branch) | B641"*;
> B654 *"the five tones ARE |χ_golden|/2 over the 2I classes — the census
> {0:90, 1/(2φ):72, ½:120, φ/2:72, 1:6} reproduces EXACTLY as class-sizes ×3"*;
> B663 *"tones = 2I class cosines"*.

**Search run:** `git grep -inE "1/\(4 ?\*? ?phi\)|phi ?/ ?4|0\.4045|0\.1545"` over
`*.md *.py`. **Returned no tone-set match.** The three quarter-values are not
banked as tones anywhere the search reached.

**And the root of the error is a name collision, the same shape the campaign keeps
finding.** In this corpus **"θ-even" is the F₄ EXPONENT SET {1,5,7,11}** — a Lie
parity label (B352, B569, B576, B583, B585) — **not a value set.** cc3 read a
parity label as a list of numbers and manufactured three values from it.

> **Same class as two conductors, two levels, two E₆'s, three σ's. B980: *"the
> algebra was always right; what failed is what the symbols denote."* cc3 made the
> corpus's signature error while writing the instrument that grades it.**

**Consequence — every base rate in `R12_SCREEN_RESULT.md` is wrong**, and wrong in
the direction that flattered the conclusion:

| set | mean gap | within 1% | within 3% | within 5% |
|---|---|---|---|---|
| **FIVE (banked)** | **0.0660** | **8.0 %** | **24.0 %** | **40.0 %** |
| EIGHT (cc3 used) | 0.0466 | 14.1 % | 41.9 % | 64.7 % |

**Fewer values ⟹ a close landing is RARER, so agreements are worth MORE than cc3
said, not less.**

## FINDING 2 — **cc3's "neutral" declared map discarded the corpus's own live result.**

The screen mapped angles by **`cos`**. **The field's convention — and the corpus's —
is `sin²`.** Under `sin²`, θ₁₂ moves from a 36 % row to the best row on the table.

**This is the R12′ failure mode cc3 named tonight, demonstrated on cc3, in the same
hour, on the instrument built to catch it.** The freedom is in the map, and cc3
declared one blind and lost the signal.

## FINDING 3 — recomputed against the banked five, **one row survives and it is not one of the four crossings.**

| target | value | nearest tone | gap | **P(random does better)** |
|---|---|---|---|---|
| **sin²θ₁₂ PMNS** | 0.3030 | **1/(2φ) = 0.3090** | **0.0060** | **4.8 %** |
| sin²θ₁₃ PMNS | 0.0220 | 0 | 0.0220 | 17.7 % (**vs 0 — vacuous, MB12**) |
| sin²θ₁₂ CKM | 0.0503 | 0 | 0.0503 | 40.3 % (**vs 0 — vacuous**) |
| **cos δ₁₃ quark — B1027** | 0.3616 | 0.3090 | 0.0526 | **42.1 %** |
| sin²θ₂₃ PMNS | 0.5720 | 0.5 | 0.0720 | 57.6 % |
| sin²θ_W | 0.2312 | 0.3090 | 0.0778 | 62.2 % |
| **\|V_us\| — B929** | 0.2243 | 0.3090 | 0.0847 | **67.7 %** |

> **The four sealed crossings were spent on rows at 42 %–68 %. The 4.8 % row was
> never crossed.** It has sat in the corpus since ~B594–B633 (git log, first
> appearance of `1/(2phi)` predates B660's 2026-07-17 prereg).

### And it was never run as a crossing — by the corpus's own record

**B660 `PREREG_SQ.md` line 1, verbatim:** *"Structure-to-structure only; **no value
comparison anywhere**; Gate 5 absolute"*. Its S1 asks *"whether
sin^2 = (sqrt5-1)/4 **appears anywhere**"* — **in the LITERATURE.**

**That is a NOVELTY gate, not a crossing.** It establishes that no one else
published 1/(2φ) for solar mixing (`FINDINGS_S1A`, `SWEEP_RESULTS:142`, searches
2007–2023). **Novelty is not evidence.** No seal, no declared prior, no
before-contact prediction, no look-elsewhere ledger over targets or maps.

**The corpus already says this about itself** — B659 `SWEEP_RESULTS:40`, adversarial
caveat, verbatim: *"the five values are just |cos(kπ/5)|-type numbers native to any
pentagonal geometry, so **the value-set match alone has low discriminating
power**; the load-bearing novel clause is the **class-size multiplicity match
(30/24/40/24/2)**."*

### The look-elsewhere nobody has written down

**4.8 % is a SINGLE-TARGET figure.** The available trial space is roughly
**7 dimensionless targets × 2–3 natural map forms ≈ 14–21 trials.** At 4.8 % per
trial the **expected number of hits is ≈ 0.7–1.0.**

> **One hit at this level is exactly what chance delivers.** Unpriced, it looks
> like the programme's best result. Priced, it is consistent with nothing.

---

## WHAT chat1's BOUND ACTUALLY SAYS — and cc3 misused it

**Located in exactly one place:** `SEALS/phase1b/chat1_PHASE1_construction.md:84`.
**§5 states its own scope, verbatim:**

> *"The bound says a forced quantity cannot carry **fine arithmetic**; it does not
> say a forced quantity cannot carry a **finite label**."*

**So the bound is a RESOLUTION statement, not a membership list.** It says forced
values are **coarse — they resolve the object only to its group data.** cc3 read it
as *"the object's forced outputs are quantized to a specific set"* and built R13's
base rate on that reading.

**Under the correct reading the conclusion is STRONGER and differently typed:** a
generic real like `|V_us| = 0.2243` is **fine arithmetic and therefore not in the
image at all.** Not *"10 % off"* — **not the kind of thing the object can force.**

> **The base rate was a symptom. The mechanism is a TYPE constraint** — which is cc's
> C0/C2 (*under-specified* / *emits only vacuously*) arriving from the other side.

**Domain verdict (exploratory): NARROW-BUT-STATED.** chat1 states the scope in §5;
no other document located by the searches above restates or extends it. **`c = 6` is
out of domain** — it is not of the form `Re χ_V(M)/dim V` (unnormalized; character
values lie in `[-1,1]`). **cc3's pre-declared refutation via `c` does not land.**

---

## WHAT SHOULD BE SEALED — for cc, properly

**The 4.8 % row cannot be crossed by us: the match is already known.** A crossing
needs something held out. Two candidates, both discrete, neither run:

1. **THE MULTIPLICITY TEST (B659's own load-bearing clause).** The tone census is
   `{0:90, 1/(2φ):72, ½:120, φ/2:72, 1:6}`. **If sin²θ₁₂ landing on 1/(2φ) is the
   object speaking, the multiplicity structure should constrain WHICH tone —
   and it makes a prediction the value-match does not.** B659 says explicitly this
   is where the discriminating power lives. **cc3 has not searched for whether it
   was ever tested; that search is not run, and this sentence is not an
   absence-claim (WORKING_RULES §0).**

2. **THE COMPANION TEST.** If the object forces solar mixing to a tone, **why not
   θ₂₃ (57.6 %) and θ₁₃ (17.7 %, and vs the vacuous tone 0)?** A mechanism that
   emits one tone and misses the other two needs to say why — **and that "why" is
   sealable before looking.**

**Required on either cell, from tonight's lessons:** declare the **map form** with
the target (Finding 2); use the **five-tone set** (Finding 1); state the
**trial-space count** and the expected-hits figure (Finding 3); and cite chat1's
**§5 scope**, not the one-line bound (above).

## WHAT cc3 IS WITHDRAWING

- **`R12` — withdrawn** (already self-refuted in `R12_SCREEN_RESULT.md`: it
  licensed B1027 and rewards imprecision).
- **`R13`'s NUMBERS — withdrawn.** The rule *"price the base rate"* stands; **every
  figure cc3 quoted for it is void** — computed against a set cc3 manufactured.
- **"The coupling channel is numerically exhausted" — REFUTED**, by the corpus, at
  4.8 %. **cc3 said it two messages after being bound not to.**
