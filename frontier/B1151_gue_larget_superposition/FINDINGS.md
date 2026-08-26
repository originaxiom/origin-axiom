# B1151 — THE LARGE-T GUE TEST (C4): the preregistered single-GUE gate is NOT met at T=3000 — and the discriminating computation locates the deviation in the MERGE (ζ_K = ζ·L(χ₋₃) is a 2-fold GUE superposition)

**Status: banked (frontier). Verdict NEGATIVE (the preregistered single-GUE gate was not met) —
informative: the discriminating per-factor computation shows the deviation is the *superposition*,
not any per-factor departure from universality. The cloud seat's preregistered cell
`c4_gue_larget.py` (`origin/outside-bench`), run on this bench's i9 at T=3000 via `c4_finish.py`
(reused the saved ζ zeros + a 10-core parallel L(χ₋₃) scan, after the original stalled on mpmath's
slow high-n `zetazero`). Two-bench, owner-approved compute split. Gate 5 untouched. Lock
`tests/test_b1151_gue_larget.py`.**

## The preregistered gate, and the result

**Gate (the cloud's, sealed in the cert):** GUE-consistent **iff** `p_GUE > 0.01` **and**
`p_Poisson < 1e−6` **and** `D_GUE < D_Poisson`; otherwise bank the negative honestly. Density gate:
merged count vs `N(T) = (T/π)log(T√3/(2πe))` within `O(log T)`.

**Scale:** T=3000 — ζ zeros **2468** (to t=2998.96) + L(χ₋₃) zeros **2991** = **5459 merged**
(vs 108 at the T=130 down-payment). The L(χ₋₃) scan took 6098 s on 10 cores.

| test | result | gate |
|---|---|---|
| density | 5459 vs smooth **5458.0**, \|diff\|=**1.0** | O(log T)=8.0 → **PASS** |
| unfolded mean spacing | **1.000072** | within 0.01 → **PASS** |
| KS vs **GUE** Wigner surmise | D=**0.13365**, p=**2.2e−85** | needs p>0.01 → **FAIL** |
| KS vs **Poisson** | D=0.15617, p=2.0e−116 | needs p<1e−6 → pass (rejected) |

**Gate verdict: NOT MET.** GUE is *closer* than Poisson (D_GUE < D_Poisson) and Poisson is strongly
rejected — but single-GUE is **also** rejected (p ≈ 0). Banked as the preregistered negative.

## The discriminating computation — where the deviation lives

`verification/gue_analysis.py` unfolds **each L-factor separately** (its own Weyl density
ρ = (1/2π)log(cond·t/2π), cond=1 for ζ, 3 for L(χ₋₃)) and KS-tests each against the single-GUE
Wigner surmise, on the committed raw zeros:

| spectrum | spacings | KS vs GUE |
|---|---|---|
| ζ alone | 2468 | D=**0.0401**, p=6.9e−4 |
| L(χ₋₃) alone | 2990 | D=**0.0487**, p=1.4e−6 |
| **merged** ζ_K | 5459 | D=**0.13365**, p=2.2e−85 |

**The merged deviation (0.134) is ≈ 3× each factor's (0.040, 0.049).** The non-GUE-ness lives in the
**merge**, not in either factor. That is the textbook signature of a **2-fold GUE superposition**:
ζ_K = ζ·L(χ₋₃) is a *product* L-function (the Dedekind zeta of ℚ(√−3), B737 — the cusp voice's own
numerator), so its zeros are the **union of two independent GUE spectra**. Independent spectra do
**not cross-repel**, so the union has an excess of small spacings — which rejects single-GUE — while
each factor keeps its own level repulsion, so Poisson stays rejected too. The failure mode the
handoff flagged as *interesting* (the density gate) **passed exactly**; it is the **spacing** that
carries the two-spectra structure.

## Honest fences

- **Generic, not object-specific.** GUE is generic (Montgomery / Katz–Sarnak, B1142) — this certifies
  the universality *class* at scale, never object-specificity; and the superposition is likewise
  generic for *any* product of two L-functions. **No firewall crossing.**
- **The per-factor residual.** Each factor's KS still rejects at p<0.01 (D≈0.04–0.05). This is
  consistent with (a) the Wigner **surmise** being an approximation to the exact GUE/Gaudin
  nearest-neighbour distribution — detectable at ~2500 samples — and (b) the leading-order Weyl
  unfolding. It does **not** touch the located-in-the-merge conclusion (the 3× gap). A clean
  per-factor GUE confirmation (exact Gaudin distribution + higher-order unfolding) is the named
  follow-up, together with a positive test of the merged spacing against the 2-fold superposition
  surmise.
- **Gate 5 untouched** — a statistical universality statement about an arithmetic zeta, no SM value.

## Discipline

The verdict is the cert's own preregistered outcome, run at scale and reported faithfully (the
`verification/c4_verdict.txt`). The discriminating computation (`gue_analysis.py`) and the raw zeros
(`c4_zeros_{zeta,L}.txt`, the ~1.7 h scan) are committed so the location-in-the-merge is re-checkable
without re-scanning. Cloud seat credited (the preregistered cell + gate). Two-bench compute split.
