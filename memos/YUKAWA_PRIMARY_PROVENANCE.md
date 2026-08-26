# R017 — primary up-Yukawa derivations are branch-local

Main B1154 correctly flagged the height-308 up-Yukawa proof as single-homed in the local audit
workspace.  R017 closes that provenance debt for the two load-bearing claims:

1. At the exact height-308 point, cohomological naturality factors the full up-type tensor through
   `H^1(G_Y)=0`, while the Higgs input lifts through
   `H^1(K_1)=H^2(K_1)=0`.  Hence `mu_u=0` and its Wilson-projected `1 x 6`
   matrix has rank zero.
2. Throughout the same locally-free BCDD monad topology, the ambient injected
   `chi_0+chi_1` contains the unique audited up-type Higgs.  A helpful nonambient `chi_0` rank
   jump necessarily creates at least a second massless up-type Higgs before a new mass/mixing
   mechanism is supplied.  Coefficient variation alone therefore cannot repair the up Yukawa
   while preserving the exact one-Higgs spectrum.

The human proofs are `memos/YUKAWA_CUP_PRODUCTS_308.md` and
`memos/YUKAWA_EXACT_SPECTRUM_NO_GO.md`.  Their two Python certificates run from any checkout and
any working directory with the standard library only.  R017 does not claim to ship the separate
Sage/down-sector chain stack: the down/lepton cup-product evaluator remains open.
