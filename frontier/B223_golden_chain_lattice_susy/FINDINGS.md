# B223 / Act II — where the SUSY lives: emergent on the golden chain, lattice-exact on the Fendley–Schoutens sibling

**Date:** 2026-06-26. **Status:** Act II of the SUSY thread. B221/B222 established the golden chain's **emergent**
N=1 superconformal SUSY (`c=7/10`, the supercurrent). This asks whether that SUSY is **lattice-exact** or
**IR-only** — and answers both halves cleanly. Firewall: dimensionless quantum-algebra; **nothing to `CLAIMS.md`;
P1–P16 untouched.** Ledger **V226**.

## (A) The golden chain has no exact lattice SUSY grading — its SUSY is emergent/IR-only

A graded (lattice) SUSY algebra needs a **conserved fermion parity** `(−1)^F` with `H` decomposing into graded
blocks. The natural candidate — **τ-parity** `(−1)^{#τ}` — is **not conserved**: the `(τ,τ)`-block off-diagonal
term flips a single `l_i` (`0↔1`), changing the τ-count by `±1`, while the diagonal terms preserve it, so `H`
has both parity-even and parity-odd parts:

```
   ‖[H_golden, (−1)^F]‖ = 0.972   (N = 8, 10, 12)   ≫ 0   →  no graded structure
```

So the golden chain's supersymmetry is **emergent (IR-only)**, with no exact lattice supercharge. (Consistent with
the literature: the golden chain's SUSY appears only in the tricritical-Ising continuum limit.)

## (B) Lattice-exact N=2 SUSY *does* exist — on the same Fibonacci/Lucas Hilbert space (Fendley–Schoutens)

Hard-core fermions with **no two adjacent occupied** (the same Lucas `L_N` counting as the golden chain — verified
`L=6,9,12 → 18,76,322`), with the Fendley–Schoutens supercharge

```
   Q = Σ_i (−1)^{n₁+…+n_{i−1}} c†_i (1−n_{i−1})(1−n_{i+1})   (add a fermion only if both neighbours empty)
```

is **exactly** supersymmetric:

| L | dim | \|Q²\| | \|[H_FS,(−1)^F]\| | Witten Tr(−1)^F | E_gs |
|--:|----:|------:|------:|------:|------:|
| 6 | 18 | 0 | 0 | +2 | ~1e−15 |
| 9 | 76 | 0 | 0 | −2 | ~9e−15 |
| 12 | 322 | 0 | 0 | +2 | ~1e−14 |

`Q²=0` (nilpotent), `H_FS={Q,Q†}`, `(−1)^F` conserved, **integer Witten index** `W=±2` (the SUSY hallmark), and
`E_gs=0` to machine precision → **unbroken** lattice-exact SUSY. So lattice-exact supersymmetry is entirely
possible on a Fibonacci Hilbert space — just not for the golden chain itself.

## The honest statement

- The **golden chain**'s SUSY is **emergent/IR-only** (no conserved `(−1)^F`, no lattice `Q`). `[TESTED-NEGATIVE]`
- The **Fendley–Schoutens** model is a **lattice-exact N=2 SUSY sibling** on the same Lucas Hilbert-space
  combinatorics. `[exact]`
- These are **different models**: the golden chain flows to the **N=1** `c=7/10` tricritical Ising; the FS `M_k`
  series is **N=2**. So the FS model is *not* claimed to share the golden chain's IR — it shows that the
  Fibonacci combinatorics *admits* exact SUSY, while the golden chain realises SUSY only emergently. (Whether any
  lattice model has the golden chain's exact N=1 `c=7/10` IR is left open — `do not assert`.)

## Where this points (one-way, firewalled in S040)
"Where does the missing structure come from externally?" Act II makes it concrete: the golden chain's SUSY is not
in its own lattice operators — it **emerges from the collective/IR limit** (the multiplicity = the interaction),
and an *exact* supercharge requires a **different (external) algebraic structure** (the FS fermions/grading). The
fermions and the exact `Q` are external to the anyon chain. (Firewalled reading: `speculations/S040`.)

## Honest status / tiers
- golden chain: no conserved τ-parity → emergent-only SUSY: **`[TESTED-NEGATIVE]`** (robust, `‖·‖≈0.97`).
- FS sibling: `Q²=0`, `H={Q,Q†}`, `[H,(−1)^F]=0`, `E_gs=0`, integer `W`: **`[exact]`** (machine precision).
- physics classical (Fendley–Schoutens–de Boer 2003; Huijse–Schoutens). **Novelty UNCHECKED.**

## Reproduction
- `python lattice_susy.py` (pyenv) — the golden-chain parity test + the FS exact-SUSY data.
- `tests/test_b223_golden_chain_lattice_susy.py` — the negative + the exact FS locks.

## Net
The golden chain's emergent SUSY (B221/B222) is **IR-only** — there is no exact lattice supercharge — while exact
lattice SUSY lives on the Fendley–Schoutens sibling of the same Fibonacci Hilbert space. The supersymmetry is a
*collective/external* feature, not an on-site one. (`B221 → B222 → B223`; firewalled reading `S040`.)
