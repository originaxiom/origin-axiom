# B1332 addendum 2 — the reduction needs isotropy for BOTH `V` and `V*`, with a counterexample

## The imprecision

§1 of the main findings says:

> *If `L_V` is **isotropic**, then `L_V ⊆ L_V^perp = L_{V*}`, so `dim L_V <= t_1/2`. The same
> argument applied to `V*` gives `dim L_{V*} <= t_1/2`. Their sum is `t_1`, so **both are exactly
> `t_1/2`** … **`I = 0` follows from isotropy alone.***

The first sentence is correct. **"The same argument applied to `V*`" silently assumes `L_{V*}` is
isotropic too** — which does not follow from `L_V` being isotropic. So as a *pointwise* implication,
"`L_V` isotropic ⇒ `I = 0`" is **false**.

## The counterexample

B1335's `m010` sector over `F_13` (`Sym^3 (x) chi`, `chi` cusp-trivial of order 6), recomputed here
with each module's **own** invariant forms — the `SL2`-invariant form on `Sym^m` is *not* invariant
for the dual module, and reusing it is an error this addendum first made and then caught, the
tell being a Gram that was neither symmetric nor antisymmetric:

| | `t_0` | `t_1` | `r_1` | `dim L` | invariant forms | isotropic for all of them |
|---|---|---|---|---|---|---|
| `V` | 1 | 2 | 0 | **0** | 4 | **YES** (trivially: `dim 0`) |
| `V*` | 1 | 2 | 2 | **2** | 4 | **NO** — Gram `[[0,3],[3,0]]` |

`t_1/2 = 1`. So:

- `L_V` **is** isotropic, and isotropy's bound `dim L_V <= t_1/2` holds (`0 <= 1`) — but it is not
  an equality, and `I = t_0 - r_1 = 1 - 0 = 1 != 0`;
- consistency is restored by `L_{V*}` having `dim = 2 > t_1/2`, so it **cannot** be isotropic — and
  the direct computation confirms it is not.

(The Gram is symmetric, as it must be: `m = 3` is odd, so the invariant form is alternating, and
alternating times the antisymmetric cup gives a symmetric pairing — the parity check of the main
findings §5, here serving as a check that the corrected form was the right one.)

## What survives, and what to say instead

As a statement about the **class**, the reduction is sound: if *every* `V` in the family has `L_V`
isotropic, then `V*` is in the family too, both bounds apply, and `I = 0` follows. That is the form
in which the target "prove isotropy" is still the right target for the one-cusped case.

What must not be said is the pointwise version. The correct statements are:

```
L_V isotropic                     =>  dim L_V <= t_1/2          (only an inequality)
L_V and L_{V*} both isotropic     =>  dim L_V = dim L_{V*} = t_1/2  =>  I = 0
```

This does not change any computed result — every one-cusped sector in the main findings has **both**
`L_V` and `L_{V*}` isotropic — but it changes what the record may claim from a single isotropy
computation.
