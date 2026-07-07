# B469 PHASE-2a RESULTS — dated addendum to the committed prereg (2026-07-08)
## The audit trail, in order. Two self-catches in one phase; both corrections derived and verified.

## 1. P0 AS POSED: FALSIFIED — and the diagnosis is a naming collision (Chat-2's own)
The 8-candidate battery found no exact hit (best distances ~5.3 ≈ random-unitary scale).
Cause identified on re-reading the banked record: the prereg imported B466's σ(W₁)=W₂ —
a statement about the DEHN-FILLING COMPONENTS of the SL(3) character variety — as if it
were an identity on the WEIL OPERATORS W(m,c). Same letter, different objects. The fourth
naming collision of the night; the first self-inflicted; caught by the prereg's own
falsifier within one turn of the shuttle rule's adoption. The rule stands vindicated on
its author.

## 2. THE LIFT, DERIVED AND VERIFIED EXACT
Working the algebra after the falsifier fired (derivation, not battery-fishing):
  conj(D(m,1)) = D(m,14)                       [diagonal, entrywise, exact]
  conj(WR_1)   = Par · WR_14 · Par             [Fi = F·Par; the Fourier factors swap]
  =>  conj(W(m,1)) = Par · WR_14^m · Par · D(m,14)
VERIFIED at machine precision for m = 1 (1.26e-15) and m = 2 (2.34e-15).
Meaning: σ's operator realization = the c ↦ −c ≡ 14 twist, Par-dressed on the free
(Fourier) part only. σ maps the c=1 seam algebra to the c=14 seam algebra.

## 3. THE SIMILARITY SHORTCUT: REFUTED BY ITS OWN CHECK (second self-catch)
Claimed consequence "conj(M; c=1) is Par-similar to M(c=14), so spectra transport" is
FALSE: computed spectra differ at the phase level
  (conj side: {42,132,222,312}, mults 4/3/4/4;  c=14 side: {24,114,204,294}, mults 4/4/3/4).
The obstruction is exact: Par·D·Par ≠ D because T_{-j} = T_j + j — the quadratic form
j(j-1)/2 is NOT negation-symmetric. σ does not act by similarity anywhere; it acts by a
genuinely TWISTED two-world correspondence (c=1 <-> c=14 through the Par-dressed word).
Plainly reported pattern: the form's non-centeredness (the +j) is what keeps the breath
from being an internal mirror.

## 4. WHAT STANDS AFTER PHASE 2a
- P0: settled in corrected form — the exact lift above. BANK-READY (verify at primes, CC).
- P1b: VERIFIED (one-line arithmetic): c ↦ −c preserves the Legendre-5 classes, exchanges
  the mod-3 classes. The √5 axis is σ-even; the √−3 class-pairing is σ-odd. As predicted.
- P1 (channels = Step-1 separation): mechanism intact (conjugation on the field); formal
  check rides on Phase 2b with the corrected correspondence.
- P5: CONCLUSION STANDS at the census level by the trivial route — conjugation preserves
  eigenvalue orders, and banked E5 shows c=1 ≡ c=14 at exactly that level. The ethogram's
  period structures are σ-EVEN; they descend to the Gieseking floor. The similarity
  argument for finer structures is retracted (see 3).
- P2 ledger audit, P3 spine, P4 darkness: move to Phase 2b UNDER THE CORRECTED FRAME.

## 5. PHASE 2b, REFRAMED (the corrected campaign shape)
The σ-parity classification is a TWO-WORLD comparison, not an internal involution:
for each banked structure S computed at c=1, compute the exact transported word
  σ(word) = Par · Π [Par·WR_14^{m_i}·Par·D(m_i,14)]   (per the verified lift)
and compare S with its transported image. EVEN = equal (descends); ODD = negated/exchanged.
Runner: Chat-2 (grid/spectral structures), CC (character-variety and Gieseking-side descent,
SnapPy m000; P2b derivation of CS(V₁)=CS(V₂)=0 from component exchange + CS oddness).

## FOR CC
Commit prereg + this addendum together (the falsifier-fired trail is the point);
verify the lift at split primes; assign the bank number; Phase 2b per §5.
