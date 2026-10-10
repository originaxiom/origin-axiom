# Preserved first run and exact-equality repair

The initial science seal3d37ab670 was pushed before the two instruments
ran. Native exited1: only covariant_IBP_keeps_surface was false. Reference
exited0 with23/23 predicates. A separate captured diagnostic found

    integrated: 48
    surface: 40 - 2*i*(1+2*i) + 2*i*(1-2*i)
    structural equality: false
    exact expanded difference: 0
    pointwise covariant IBP difference: 0

SymPy expression-structure equality is not mathematical equality of the
two polynomial values. The repair compares their exact expanded
difference with zero. No action, boundary, fixture, scientific target,
predicate roster or success condition changes. The old source remains
recoverable at the first seal and the original failed stdout is retained
locally with hash/byte custody in RECEIPTS. The public first-failure copy
is explicitly path-normalized, NOT byte-identical raw stdout. The tiny
diagnostic log is published literally. Changed science is resealed and
pushed before authoritative reruns. This is an instrument defect, not a
physical negative, and the first run is not relabeled as success.
