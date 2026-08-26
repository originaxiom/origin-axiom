# R019 — the in-frame hypercharge theorem and the selection fence

## Narrow result

Outside memo 70's exact computation reproduces.  In the selected trinification `A2^3` frame,
the `27` contains SM-shaped 15-state assignments whose rank-three Cartan charge direction obeys
the four standard anomaly equations.  Every accepted direction has

```text
(Yu, Yd, Yl, Ye) / Yq = (-4, 2, -3, 6)
```

up to exchanging the two antitriplet labels, and is unique up to overall scale.  R019 extends the
source's two-frame control to all three choices of color slot; each gives 36 accepted assignments,
zero non-SM ratios and zero multidimensional linear solution spaces.

## The discriminating scope fact

The charge ratios are not special to E6.  Once a left-handed SM-shaped 15-plet and the usual
anomaly equations are assumed, the three linear conditions give

```text
Yl = -3 Yq,  Ye = 6 Yq,  Yu + Yd = -2 Yq,
```

and the cubic condition factors as

```text
-18 (Yu/Yq - 2) (Yu/Yq + 4) = 0.
```

Thus the ratios follow universally from the assumed multiplet content.  The object-side content
of memo 70 is narrower but real: the chosen `27`-derived trinification complement realizes those
directions for every enumerated assignment and weak-root choice.

## What remains unpaid

- The object does not select the trinification frame, color orientation or weak root.
- The computation presupposes an SM-shaped 15-state subset and does not prove that the other
  twelve states of the `27` are absent, vectorlike or massive in a four-dimensional spectrum.
- It does not execute B892's distinct centralizer frame.
- It does not construct a physically gauged U(1), a gauge field, kinetic normalization or coupling.
- `Yq=1/6` is an overall normalization convention in this calculation, not a derived measured
  parameter.

Therefore memo 70 earns a narrow proved child row.  It does not reverse OA-C0013's failed strong
selector or close OA-C1118's complete-spectrum/declared-sector computation.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r019_hypercharge/hypercharge_trinification_scope.py
```

The certificate is file-relative and reuses the byte-identical exact E6/27 stack already shipped
in R006.
