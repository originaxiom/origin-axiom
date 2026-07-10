# B507 FINDINGS — the β-function, first pass (2026-07-10): the negative branch computed; the κ>0 gap named
**Computed (2 seeds agreeing, F-equilibrated leaf averages):** on κ ∈ [−1.9, 0]:
**g_M(κ) ≈ −1.05 to −1.25** (monotone-ish, strongly negative) and g_D(κ) ≈ −2.6 to −2.7.
**Meaning:** the B506 emergent drift has its SOURCE here — on the negative-κ leaves (the Markov side,
where the object lives) the measurement verb is NOT marginal leaf-wise: it contracts at ≈ e⁻¹ per
event. Haar-marginality (Q1b, ∫g_M dHaar = 0, PROVED) forces a compensating POSITIVE branch at κ > 0
— the zero of g_M lies in (0, 2): a genuine attractor structure, not uniform criticality.
**Named gap (honest):** the κ > 0 half is UNSAMPLED — Haar rejection at tol 0.02 found <50 pairs per
leaf there (itself a datum: the Haar κ-density is heavily negative-skewed). Fix priced: DIRECT leaf
parametrization (angles (a,b,u) with κ(a,b,u) solved for u — no rejection), then the zero-set cell,
the g(2)=0 gate, and the B506-d consistency lock. Prereg gates stand; nothing banked beyond the
negative branch + the density observation. Firewalled; form-level only.

---

## THE COMPLETE CURVE + THE ZERO (2026-07-10, approved run; 6M Haar samples, measure-correct binning)
**Both exact gates PASS at 4 decimals:** E_Haar[g_M] = 0.0003 (theorem: 0, Q1b); E_Haar[g_D] = −1.9995
(theorem: −2, Q1a) — the method is certified by the proved ledger.
**The curve:** g_M monotone increasing, −2.88 (κ=−1.9) → +0.39 (κ=1.5) → bending to the proved
marginal 0 at κ=2. g_D likewise (−8.5 → −0.29), everywhere negative (decimation always contracts).
**THE ZERO: κ\* = 0.001 ≈ 0.** The flow reading (w=κ−2, |w|′=e^{g}|w|): g_M<0 below zero pushes κ UP
toward 0; g_M>0 on (0,2) pushes κ DOWN toward 0 — **κ=0 is the ATTRACTOR of the slow measurement
flow.** And κ=0 is precisely the POINTER LEAF: the decree map's decoherence-proof irreducible point
(1,1,1) (order-6 torsion) lives there, and D maps it within the same leaf to the order-3 point. The
two independent computations — the decree map's fixed-point analysis and the β-function's zero —
select THE SAME LOCUS. "What survives measurement is the discrete" is now the zero of an emergent,
gate-certified β-function. (Via the anchor: λ\*² = (κ\*−2)/4 < 0 — the attractor is INSIDE the
spectral window, not a real-coupling fixed point; form-level, firewalled.) Consistency lock vs
B506's d and the exact κ\*=0 identity (is g_M(0)=0 provable? the pointer state suggests yes):
queued as the campaign's proof obligation.
