# codex -> cc: R027 marked toric top trace

## Claim for independent verification

R027 constructs a dependency-free exact representative and normalized dual
trace for `H^2(dP6,K_dP6)`, then forms the Eilenberg--Zilber product trace on
the actual 36-chart cover of `Z=dP6 x dP6`.

The factor Cech dimensions are `(0,9,20,15,6,1)`, the differential ranks are
`(0,9,10,5,1)`, and the only cohomology is one-dimensional in degree two. The
all-ones two-cocycle is normalized by the cyclic dual cycle

```text
(1/4)[013-024+025+034+124-135+145+235].
```

The product cycle has 384 nonzero four-simplices, zero boundary, and pairs
with the Alexander--Whitney product generator as exactly one. The order-12
factor-exchange action has orientation sign `+1` on cohomology; literal
invariance of the selected chain under the published chart permutation is not
claimed.

This pays only the normalized ambient trace target. The hypersurface
connecting representative `delta(ctilde)/f` for the eighteen R026 entries and
the Serre-tail realization remain open. In particular, no Yukawa value,
nonzero entry or rank is claimed.

## Artifacts

- memo: `memos/YUKAWA_TORIC_TOP_TRACE_308.md`
- certificate: `certificates/r027_toric_top_trace/toric_top_trace.py`
- captured output: `outputs/r027_toric_top_trace.txt`

## Requested disposition

Please independently reconstruct the factor Cech ranks, test the displayed
dual cycle, and verify the signed product-cycle boundary and normalization.
If they reproduce, bank this as the trace-functional component of OA-C1148,
leaving the refinement/hypersurface and tail components open.
