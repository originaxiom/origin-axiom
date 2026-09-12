# B1335 — the vanishing is not formal, now EXHIBITED: a non-zero index over `F_p`, and its refutation in characteristic zero

**Verdict: NEGATIVE** (the falsifier does not fire) **with a positive structural finding**: no proof
of the vanishing can come from the index identities and the domain conditions alone, because over a
finite field those conditions permit `I != 0`.

**This does NOT fire falsifier 6.** Read §3 before quoting anything here.

## 1. The exhibit: `I != 0` over `F_7` and `F_13`, in domain `D`

Scanning one-cusped census manifolds with honest `SL2(F_p)` representations (enumerated and filtered
by the relators), twisted by cusp-trivial characters:

On **`m010`** — chiral, `H_1 = Z/6 + Z`, `H_1/<peripheral> = Z/6`, volume 2.6667 — there are sectors with

```
Sym^3 (x) chi,  chi cusp-trivial of order 6:   a_0 = a_0* = 0,  t_0 = t_0* = 1,  r_1 = 0,  I = +1
                                                                                 r_1 = 2,  I = -1
```

Checked exhaustively with **independently written, self-contained code** (`verify_m010.py`):

- relators evaluate to `+I`, so odd `Sym^3` is valid — **not** the `-I` trap that produced this
  bench's last false positive (B1330 add. 2);
- `mu` and `lam` commute and are genuinely unipotent (`mu - I` nilpotent), so the cusp sits in a
  one-parameter unipotent group — the domain's cusp condition;
- the four identities all hold: `r_1 + r_1* = t_1` (0+2=2), `t_1 = t_0 + t_0*` (1+1=2),
  `I = (a_0 - a_0*) + t_0* - r_1`, `I(V*) = -I(V)`;
- `a_0 = a_0*` and `t_0 = t_0*`, so the sector is **in domain `D`**, and `I = t_0 - r_1` as `D` requires;
- no theorem forbids it: T2 needs `M` closed, T3 needs `V` self-dual (it is not), T4 needs rank one,
  T5 needs `t_0 = 0`.

**It is not a single-prime accident.** The cusp-trivial character group is `Z/6`, so such characters
exist only for `p = 1 mod 6`. Of the primes scanned, exactly those admit them, and exactly those
show the phenomenon:

| `p` | reps | unipotent + irreducible | cusp-trivial chars | in-domain sectors | **non-zero** |
|---|---|---|---|---|---|
| 5 | 480 | 0 | 1 | 0 | 0 |
| **7** | 4704 | 1344 | 5 | 18816 | **2688** |
| 11 | 21120 | 0 | 1 | 0 | 0 |
| **13** | — | — | 5 | — | **yes** |

## 2. The refutation in characteristic zero

The `SL2(F_p)` reps above are **not** the geometric holonomy, and the parabolic `SL2(C)` character
variety of a one-cusped manifold is finite, so most of them have no characteristic-zero counterpart.
The one that matters is `rho_geo`. Computed at 60 digits:

```
m010 rho_geo:  relator -> +I  (|rho(r) - I| = 5.7e-50)
               tr(mu) = tr(lam) = -2      <- NOT +2
```

`rho_geo(mu)` is `-(unipotent)`. So `Sym^odd(rho_geo(mu))` has every eigenvalue `-1`, giving
`t_0 = 0` and `I = 0` by T5 — **odd germs are trivially zero on the geometric holonomy, and the
mod-`p` hits at `Sym^3` live on the trace-`+2` component, which `rho_geo` is not in.**

With the valid (even) germs, every cusp-trivial character, in characteristic zero:

| germ | characters | result |
|---|---|---|
| `Sym^2`, `Sym^4` | all 5 non-trivial cusp-trivial | `a_0 = 0, a_1 = 1, t_0 = 1, r_1 = 1`, **`I = 0`** (10 of 10) |

Every numerical rank is reported with its singular-value gap; they run **`1e45` to `1e50`**, so the
rank determinations are not close calls.

## 3. What this does and does not establish

**Does not.** Falsifier 6 asks for a non-zero index *on an unprotected twist sector of a chiral cover
of the object*. `m010` is not a cover of `m004`; the reps are not the geometric holonomy; and the
hits do not survive to characteristic zero. **The trigger does not fire, and the programme's
vanishing is untouched.**

**Does.** B1329 argued the vanishing is *not formal*. This exhibits it:

> **The index identities and the domain conditions do not imply `I = 0`.** Over `F_7` and `F_13`
> they are all satisfied and the index is `+-1`. So no proof of the vanishing can be assembled from
> them alone — any proof must use something specific to characteristic zero, or to the geometric
> component of the character variety.

That closes off a whole class of attempted proofs, and it explains why purely formal manipulation of
B1297's four identities has never produced one: **there is nothing there to find.**

## 4. A methodological caution this bench now owes itself

Mod-`p` scanning over **arbitrary** `SL2(F_p)` representations can produce in-domain non-zero
indices that do not exist in characteristic zero. Earlier scans that used mod-`p` arithmetic on
*non-geometric* representations inherit this caveat, and a mod-`p` non-zero must be confirmed on a
characteristic-zero representation before it counts as anything — which is the rule B1333 stated and
this arc is the first case where it actually bit.

Two further practical notes:

- **A peripheral trace of `-2` kills every odd germ** by T5, on any manifold. Worth checking before
  spending a scan on odd powers.
- The domain's cusp condition is on the *representation*, and a random `SL2(F_p)` rep can satisfy it
  while lying on a component with no geometric point. Domain membership is necessary, not sufficient.

Reproduce: `verification/broad.py` (the census scan), `verification/primescan.py` (across primes,
with the unipotent + irreducible filters), `verification/verify_m010.py` (one sector, self-contained
independent recomputation), `verification/char0.py` (the characteristic-zero computation on
`rho_geo`, with singular-value gaps). Logs in `verification/logs/`.
