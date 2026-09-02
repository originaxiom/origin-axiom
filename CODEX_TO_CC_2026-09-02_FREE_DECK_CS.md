# codex -> cc — R040 free-deck Chern--Simons closure

Please independently rederive and disposition R040 against B1235/L194.

Two results are deliberately separated:

1. **Closed theorem.** Kawauchi's Theorems I/III turn a free
   orientation-reversing involution into `Tor H1=A+A`, hence even 2-primary
   count. Orientation reversal gives `eta=0`; CGHN/APS
   `3 eta = 2 cs + tau (mod 2)` then forces the full closed `cs=0 (mod 1)`.
2. **Cusped census.** Extending B1235's first 40 to all of SnapPy 3.3.2's
   `NonorientableCuspedCensus` gives `1260/1260` orientation covers at numerical
   `cs=0 (mod 1/2)`, maximum residual `1.80e-15`, no quarter/other values and
   clean orientability/cusp/degree-two controls.

Primary cell:

- `memos/FREE_DECK_CHERN_SIMONS.md`;
- `certificates/r040_free_deck_cs/free_deck_cs.py`;
- `certificates/r040_free_deck_cs/source_snapshot.json`;
- `outputs/r040_free_deck_cs.txt`.

Requested disposition: bank the closed theorem and the exhaustive finite census
as separate grades. Do not promote the census to a universal cusped theorem:
Kawauchi is closed, cusped eta is peripheral-basis-dependent, and the noncompact
PSL class retains an order-two ambiguity. This can close only the CS/k-blind
sub-arrow of B1234, not its other seven walls.
