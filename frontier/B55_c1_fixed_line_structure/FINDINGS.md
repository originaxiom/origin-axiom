# B55 Findings

> Logged observation, not a claim (`../../GOVERNANCE.md` §5).

## Verdict

```text
PRODUCES-PROOF-MODULE
```

The `c=1` fixed-line sector structure is settled for **all** `m`, completing the
`c=1` row that B54 had only for `m=1`.

## Exact Results

**Symmetric sector (mod 4).** Proved per residue class with `m` symbolic:

```text
m = 1, 3 (mod 4): (t-1)(t+1)(t^2 - t + 1)   Phi_6  (Eisenstein, disc -3)
m = 2     (mod 4): (t-1)(t+1)(t^2 + 1)        Phi_4  (Gaussian)
m = 0     (mod 4): (t-1)^3 (t+1)              degenerate (parabolic)
```

So the earlier "odd -> Phi_6, even -> Phi_4" reading is corrected: the structure
is **mod 4**, and `m = 0 (mod 4)` degenerates to a parabolic `(t-1)^2` factor
rather than `Phi_4`.

**Antisymmetric sector (all m).**

```text
(t-1)(t+1)(t^2 - m t - 1)
```

`char(M) = t^2 - m t - 1` appears for every residue class -- the universal `c=1`
antisymmetric factor.

## Mechanism

At `c=1` the derivative recurrence has characteristic equation `(r-1)(r^2+1)=0`,
roots `{1, i, -i}`. The constant forcing `(e_x1 - e_x4)` resonates with `r=1`,
producing one linear-in-k term (slope `L=(1/2,0,0,-1/2,0,0,0,0)`, supported on
the `x1, x4` coordinates) plus a period-4 part:

```text
dtau_k = k*L + Q(k mod 4),     dtau(k+4) = dtau(k) + 4L.
```

The period-4 part yields the mod-4 cyclotomic symmetric sector; the linear term
(`x1, x4` only) yields the `m`-linear `char(M)` in the antisymmetric sector. This
is verified symbolically (per residue class) and numerically (`m = 1..12`); `m=1`
reproduces B54's Eisenstein/golden twins.

## Impact On PC12

B55 upgrades PC12's `c=1` content from a single `m=1` example (B54) to a complete
general-`m` description of both sectors, with a clean structural proof. No
selector, no physics dictionary, no new claim. The figure-eight resemblance of
the `c=1` Eisenstein factor is a coincidence, controlled in `frontier/B56`.
