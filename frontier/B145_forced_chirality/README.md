# B145 — Campaign 1′: chirality cannot be forced (canonicity ⟺ self-mirror)

B144's redirect: preferred handedness needs a **chirally-asymmetric input** (not more seeds). B145 asks whether such
an input can be **forced** — answer: **no.** Canonicity coincides with the self-mirror (amphichiral) condition.

**Framing (GHH/B128):** `b++W` amphichiral ⟺ `W` anti-palindromic (= palindromic continued-fraction period). The
metallic family `RᵐLᵐ` (the canonical/arithmetic family) is exactly the self-mirror family.

**Catalog (n=39 o-p-t bundles, length ≤7):** GHH ⟺ SnapPy `is_amphicheiral` on **all 39**; minimal-volume bundle =
figure-eight `RL` (amphichiral), minimal chiral = `RRL` (strictly larger); trace-field degrees amphichiral ∈ {2,8},
chiral ∈ {4,6,8,12} — **every quadratic (arithmetic-candidate) bundle is amphichiral** (no arithmetic chiral o-p-t
bundle). Simplest substitution (Fibonacci → `RL`) is self-mirror.

**Verdict (MATH):** canonical (minimal / arithmetic / simplest / palindromic) ⟺ self-mirror; chirality requires
leaving the canonical locus. **Aspiration (POSTULATED):** preferred handedness (parity) is **irreducibly contingent**
— the deepest firewall statement (forced ⟹ self-mirror ⟹ no parity). **Not a K-A revival** (opposite conclusion).

```
python -m pytest tests/test_b145_forced_chirality.py -q
~/.local/bin/sage-python frontier/B145_forced_chirality/probe.py
```

**Tier.** MATH. Nothing to `CLAIMS.md`; P1–P16, B85, B124–B144 untouched. See `FINDINGS.md`; ledger **V134**.
