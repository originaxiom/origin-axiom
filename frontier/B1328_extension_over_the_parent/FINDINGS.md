# B1328 — extension over the discarded parent selects a central Z/2, and it is one mechanism

**Verdict: PROVED** (as a computational statement over the groups tested; the general proof is not
written).

## Three reports, one mechanism

| where | statement |
|---|---|
| codex R037 | exactly one of m004's two `2T` quotient classes extends over m000 |
| codex R039 | exactly one of each m004 `A4`-map's two `2T` lifts extends over m000 |
| §9 spin-lift row | extension-consistency with the non-orientable manifold the object double-covers "selects, over exactly one of the two lifts" |

The paper notes the resonance and claims nothing from it: *"the object discarded at the most fragile
fork in the chain is what later pays the last discrete bit."* Tested as a general statement, it is not
a resonance — it is a rule.

## The rule

For a finite group `Q`, restriction `Surj(pi_1 m000, Q) -> Surj(pi_1 m004, Q)` has fibres of size

> **`#{ z in Z(Q)[2] : z·phi is still surjective }`**

where the fibre is realised by the central twist `phi^w(g) = z^{w(g)} phi(g)`, `w` the orientation
character. When that count is **2**, exactly half the m004 classes extend, and the relation to m000
fixes **one bit**.

## The naive form is false, and the correction is the content

`fibre = |Z(Q)[2]|` is **refuted by C2 and C6**. The twist is always a homomorphism and always
satisfies the relators — `w` kills them automatically, since relators lie in `ker(w)` — but it can
**leave the surjections**. For cyclic `C_n` that happens exactly when `n = 2 (mod 4)`: `C6` has
`t + 3` even for every generator `t`, so the twist is never onto.

With surjectivity added, the rule holds on every group tested:

| group | `\|Z(Q)[2]\|` | fibre | rule |
|---|---|---|---|
| C2 | 2 | 1 | OK (twist leaves Surj) |
| C3 | 1 | 1 | OK |
| C4, C8, C12 | 2 | 2 | OK |
| C6 | 2 | 1 | OK (twist leaves Surj) |
| **SL(2,3) = 2T** | **2** | **2** | **OK — the object's own entry point** |
| C2xC2, C2xC4, Q8, D4, D6, SL(2,5), S3, S4, A5 | — | — | no surjection: no content |

That the object admits so few finite quotients in this range is itself worth noting, and `2T` is one
of them.

## The type is *relation*, not *selection*

Under B1327's typing this is **R**, and the second relatum is **m000** — the manifold axiom 5
discarded. The bit it fixes is precisely a **central `Z/2`**, which is exactly what a spin structure,
a `2T` lift and a `2T` quotient class each are.

**No observer appears anywhere in the statement.** The bit is fixed by a relation between the object
and the parent it double-covers, and both are named mathematical objects.

## The limit, stated

This explains the three instances and **does not** move the other rows B1327 flagged:

- **the colour frame** is a `Z/3` triality orbit — **no central involution**, so this mechanism is
  silent on it;
- **the Standard-Model shaping** is target knowledge, not a relation to any partner, and stays **S**.

One of B1327's proposed re-types gains a mechanism. The others do not, and saying so is the point of
having proposed them separately.

Reproduce: `verification/central_selection.py`.
