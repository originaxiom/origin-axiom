# MEMO 180 — WHAT THIS LINE TOOK FROM THE PAPER, AND WHICH PARTS WERE ACTUALLY CHECKED

**Banked 2026-09-08 · outside bench (lane 1B).**
Owner instruction, three times: ***"papers are old, dont rely on them, verify all."***
This memo answers it for every Gukov–Manolescu input memos 174–179 used.

**GM = Gukov–Manolescu**: Sergei Gukov (Caltech) and Ciprian Manolescu (Stanford),
*"A two-variable series for knot complements"*, arXiv:1904.06057v2 (29 June 2020), 79 pp.
The abbreviation was used throughout memos 173–179 without ever being expanded. Fixed here.

---

## 1. The ledger

| GM input | what it was used for | verified on this bench? |
|---|---|---|
| **eq (166)** — `J_n(4₁)` in Habiro form | the colored Jones tail (memo 177 add. 4) | ✅ **independently reproduced** by the from-scratch `R`-matrix calculator, `N = 2,3,4` (memo 179, control C5) |
| **eq (168)** — `J_n(e^ℏ) = 1 + (n²−1)ℏ² + …` | — | ✅ **independently reproduced** by the same calculator (memo 179, C6) |
| **recursion (171)–(172)** | the entire `Ξ` generator | ✅ its printed `q = 1` limits checked before use, and its output reproduces eq (11), eq (13), all nine Table-10 series and eq (175) |
| **eq (11)** — `Ξ` through `x^{7/2}` | control C1 | ✅ reproduced from the recursion |
| **eq (13)** — `Ẑ₀(S³_{−1/2}(4₁))`, ten coefficients | control C3 | ✅ reproduced, with no spurious term below `q¹⁶` |
| **Table 10** — `Ẑ₀(S³_{−1/r}(4₁))`, `r = 2…10` | control | ✅ **all nine**, incl. `r = 6`'s isolated `+q¹¹²` |
| **eq (175)** — `Ẑ₀(−Σ(2,3,7)) = F₀(q)` | the identity of memo 177 §1 | ✅ termwise to `q³⁰⁰⁰` |
| **Thm 1.2 + eq (1)** — the Laplace transform | the whole assembly | ✅ **by consequence** — everything above is built through it |
| **§6.8** — spin`^c` labels `a ∈ ℤ + (r+1)/2` | block placement | ✅ **by consequence** — `a = 0` kills every term; the published series only come out with §6.8's labels |
| **condition (177)**, `c = −1/16`, range `(−4,0)` | the threshold | ✅ **strengthened** — `c = −1/16` derived in closed form here; the paper reaches it *"experimentally, by calculating more terms"* |
| **Thm 1.3** — `F_K` for torus knots | memo 177 add. 2's torus arm | ⚠️ **not independently verified.** Now checkable with memo 179's calculator; not yet done |
| **Thm 1.4 / page 6** — the `F_K`↔stability relation is *"specific to negative torus knots"* | memo 177 **addendum 8's downgrade of my own results** | ❌ **not verified, and not verifiable here — and it is an EXPECTATION, not a theorem** |
| **Armond–Dasbach** — tail of `4₁` is `(q;q)_∞` | the mechanism | ✅ computed here from eq (166), and eq (166) is itself now independently verified |

**Eleven of thirteen were checked, most of them decisively.** The paper is not being trusted; it
is being tested, and it passes everywhere it was tested. That is worth saying plainly: the
verification found **no error in GM**.

## 2. The one place deference did damage — and it is mine

The single unverified input in the table is the one I used to **downgrade my own verified
results**. Memo 177 addendum 8 read page 6 —

> *"This direct connection between `F_K(x,q)` and the stability series is specific to negative
> torus knots; for example, it even fails for the positive trefoil."*

— and Remark 7.6's *"**we cannot expect** this to hold for arbitrary knots"*, and on that basis
wrote that my `4₁` mechanism *"has no support beyond this one knot"* and that its universality
*"should not have been written as the likely answer."*

**Two things were conflated there, and only one of them was correct.**

* **The credit correction stands, and is a verifiable fact about the paper.** Theorem 1.4 is
  theirs; the head/tail mirror statement in §7.5 is theirs; the positive trefoil as a
  counterexample to the *direct* relation is printed on page 6. I rediscovered all three and
  should have read the introduction first. That part of addendum 8 is correct and stays.
* **The downgrade does not stand.** *"We cannot expect"* is an authors' expectation from 2019–20,
  not a theorem. My `4₁` result — block edge `2θ/(q;q)_∞`, colored Jones tail `(q;q)_∞`, both
  computed here, the second from a formula I have now independently reproduced — **is a fact**,
  and `4₁` is not a torus knot, so it lies outside everything Theorem 1.4 covers. A verified
  computation is not weakened by an expectation that it would not exist.

> **ADDENDUM 9 TO MEMO 177 (below) restores the standing of the computed facts and keeps the
> credit correction.**

## 3. What "verify" costs, and what it bought here

The instruction is not free: reproducing eq (166) required building a colored Jones calculator
from scratch (memo 179), which took two wrong `R`-matrix formulas before the controls caught
them. It bought:

* eq (166) and eq (168) now rest on **this bench's own arithmetic**, not on the paper;
* the `4₁` tail — the input to the whole mechanism — is therefore verified end to end;
* and a tool that can test **Thm 1.3** (the one remaining unverified GM input) and, if the
  resummation lands, `F_{5₂}`.

## 4. What is still unverified, stated so it is not forgotten

1. **Thm 1.3**, `F_K` for torus knots. Memo 177 addendum 2's torus arm rests on it. Now
   checkable; queued.
2. **Page 6's pessimism.** Not verifiable without `F_K` for a second non-torus knot — which is
   the same open item as everything else on this line.
3. **The `c_eff` literature** (`arXiv:2308.05360`, `arXiv:2508.10087`) — unread, egress-blocked,
   fenced in memo 177's head note. That fence stays.

## 5. Fences

* Nothing in memos 174–178's *computations* changes. This memo changes what one of them is
  allowed to conclude from someone else's expectation.
* Gate 5 untouched.

---

# ADDENDUM 1 (2026-09-08, same day) — **THM 1.3 IS NOW VERIFIED. The ledger's one ⚠️ closes, and a ✅ elsewhere needs a footnote**

**Certificate** `certificates/gm_thm13.py` · **Output** `outputs/gm_thm13_out.txt`

## 1. The row that was open

```
| Thm 1.3 -- F_K for torus knots | memo 177 add. 2's torus arm |
     NOT independently verified.  Now checkable with memo 179's calculator; not yet done |
```

§5 listed it first among what remained. It is done, and not with memo 179's calculator — with a
better instrument that did not exist when the ledger was written: **Park's large color `R`-matrix
on the lowest weight Verma module**, built in memo 183 addendum 1 and controlled there against
every block Park prints for `m(5₂)`. So the check is against a **different paper's machine**, and
neither theorem is used to derive the other.

The negative torus knot `T(2,−t)` is the closure of `σ₁^{−t}` on two strands, which is exactly
where Park's construction is at its safest.

| | `T(2,−3)` | `T(2,−5)` |
|---|---|---|
| `f_0` | `−q^{−1}` | `0` |
| `f_1` | `0` | `−q^{−2}` |
| `f_2` | `+q^{−2}` | `0` |
| `f_3` | `+q^{−3}` | `+q^{−3}` |
| `f_4` | `0` | `0` |
| `f_5` | `−q^{−6}` | `0` |
| `f_6` | `−q^{−8}` | `+q^{−6}` |
| `f_7` | `0` | `0` |
| `f_8` | `+q^{−13}` | `−q^{−9}` |
| `f_9` | `+q^{−16}` | `0` |

> ### Every one of these is **exactly** GM eq (2)–(3), with no normalisation factor:
> the sign `ε_m`, the exponent `(s−1)(t−1)/2 + (m² − (st−s−t)²)/(4st)` (negated for the mirror,
> GM p.5), and the whole **vanishing pattern** — `ε_m = 0` gives exactly `0`, at `j = 1,4,7` for
> `T(2,−3)` and `j = 0,2,4,5,7,9` for `T(2,−5)`, which is six of ten blocks on a knot the
> instrument knows nothing about.

Two knots, two different `ε` patterns, two different vanishing sets. **Thm 1.3 is verified.**

## 2. What this does to memo 177 addendum 2's torus arm

Addendum 2 concluded *"torus knots give `c_eff = 0`, exactly, at every slope"* because Thm 1.3
makes every block a single monomial, so there is no widening edge. **That premise is now checked
rather than taken.** The arm stands on verified ground.

## 3. A footnote the ledger's last line now needs

§1 ended: *"the verification found **no error in GM**."* That is still true, and this addendum
strengthens it — twelve of thirteen rows now checked, and the paper passes everywhere. But it sat
next to an implicit reading that the three papers were all sound. **Memo 183 found an error in
one of them** — Park arXiv:2004.02087v2 eq (32) — so the sentence should be read as scoped to GM,
which is how it was written and how it remains true.

## 4. What is still not verified

The ledger's other non-✅ row is unchanged and unchangeable here: **Thm 1.4 / page 6**, the claim
that the `F_K`↔stability relation is *"specific to negative torus knots"*. It is an expectation in
the paper's own voice, not a theorem with a proof this bench can run, and register rule R80-1
says an author's stated expectation is evidence about what was known when it was written and
never about what is true. It stays ❌.
