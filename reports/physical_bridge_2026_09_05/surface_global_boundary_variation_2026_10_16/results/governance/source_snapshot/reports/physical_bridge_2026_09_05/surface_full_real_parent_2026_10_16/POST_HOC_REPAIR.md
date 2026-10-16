# First failed gate: declared gauge-frame convention, not a physical no-go

The first sealed run at890ef12ddc9ff5e98cec1ea274f1a52150812855
finished100.701735s,30/37 checks. Full stdout108636bytes SHA256
4cf9b4f882f1bc4faaa9c156ee601e027b1d6c8ec9b2c528945b0e749eb2a8d4,
stderr1583bytes SHA256
d4be4ea126b53bc089a55148f0dfaf3bfca211ed93b3d308746d602baf8e171e,
receipt and all97 frozen sources retained in results/first_run.
97pins/13,403tracked contents/index unchanged. Reference was not launched
after the failed native gate. No independent or complete-model acceptance.

Positive checks included unit signed time weights, full D moment/Gaussian,
all chiral auxiliary metrics, internal gauge covariance and the complete
normal potential. Seven gates failed: ordered fermion equality, external
YM, four external gauge covariances and the full named Clifford map.
The full raw ordered residual is retained, not overwritten: its16 terms
are exclusively gaugino--external-vector words. The Clifford-map failure
is SEPARATE and is not explained away by repairing those16 terms.

## Gauge-frame diagnosis from transformation, not target Clifford fitting

AGW hep-th/0101233v2 Section2.3 and3.2 were personally re-read online
2026-10-16 (HTML equations34/48). Their convention is

 G -> h^-1 G barh^-1,  C -> h^-1(C-sqrt2 partial)h,

with h chiral and barh antichiral. For THIS transformation, define
Omega_alpha=G D_alpha G^-1. The product rule gives exactly

 Omega' = h^-1 Omega h + h^-1 D_alpha h,

since D_alpha barh=0. Chiral projection kills the last term: barD^2
D_alpha h=0, and barD h=0. Hence barD^2 Omega transforms in the SAME
chiral adjoint as C. The first design instead explicitly declared
G^-1 D_alpha G, which is the other gauge frame. It is not compatible
with that K density and that transformation. This was OUR supplied
convention error; no error of AGW or of the whole programme is inferred.

Correct the declared projector to W_alpha=+barD^2(G D_alpha G^-1)/4.
The plus keeps its linear W=-barD^2(DV)/4 unchanged; it changes the
non-Abelian completion. No K/F coefficient, kinetic normalization,
physical-coordinate dictionary or canonical target is adjusted. Add
actual barD(W)=0 controls and preserve all24 dictionary rejection reasons
and matrix witnesses in the complete output. The old full-map criterion
remains exactly as sealed; a failed map still means not earned in the
tested class, not an arbitrary-unitary or programme-wide exclusion.

This is a POST-HOC SCIENTIFIC CONVENTION CORRECTION, not a syntax-only
instrument repair. Original DESIGN/PROOF are preserved in the first-run
source snapshot. Corrected code/clarifications are resealed/published
BEFORE the second leaf. No successful result is asserted in advance.

Source: https://arxiv.org/html/hep-th/0101233v2 . The paper does not
explicitly print our W projector; the gauge-frame conclusion above is
an authored algebraic derivation from its stated transformation.
