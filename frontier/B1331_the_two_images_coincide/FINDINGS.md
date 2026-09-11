# B1331 — the vanishing reduces to isotropy, the two images coincide, and Galois is not the reason

**Verdict: OPEN.** Not a proof. A sharp statement of what must be proved, exact evidence for it, and
the elimination of the mechanism everyone would try first.

## 1. The reduction: isotropy alone suffices

`L_V` and `L_{V*}` are mutual annihilators in `H^1(T;W)` with

```
dim L_V + dim L_{V*} = t_1        (B1329: a consequence of the LES + Poincare-Lefschetz + chi = 0)
```

If `L_V` is **isotropic**, then `L_V ⊆ L_V^perp = L_{V*}`, so `dim L_V <= t_1/2`. The same argument
applied to `V*` gives `dim L_{V*} <= t_1/2`. Their sum is `t_1`, so **both are exactly `t_1/2`**, i.e.
`r_1 = t_0` and

> **`I = 0` follows from isotropy alone.**

The whole theorem is one question: **is `L_V` isotropic?**

## 2. The exact answer: the two images are the *same subspace*

Not merely equal in dimension — **identical**. On `s958`'s geometric holonomy, exactly over
`Q(zeta_12)`:

| germ | `t_0` | `dim L_V` | `dim L_{V*}` | `dim(L_V + L_{V*})` | |
|---|---|---|---|---|---|
| `Sym^2` | 1 | 1 | 1 | **1** | same |
| `Sym^2 (+) Sym^2` | 2 | 2 | 2 | **2** | same |
| `Sym^2 (+) Sym^4` | 2 | 2 | 2 | **2** | same |
| `Sym^2 (+) Sym^2 (+) Sym^2` | 3 | 3 | 3 | **3** | same |

**8 sectors, identical in every one, zero exceptions.** Since `L_{V*} = L_V^perp`, this says exactly

> **`L_V = L_V^perp` — `L_V` is Lagrangian.**

That is `I = 0` **with a mechanism**, not a numerical coincidence. `r_1 = r_1*` was the shadow; subspace
equality is the thing casting it.

## 3. Galois is *not* the reason — and that is the informative part

The obvious mechanism: complex conjugation `sigma` sends `W (x) chi` to `W^sigma (x) chi^{-1}`, which
is `V*` **provided `W^sigma ≅ W`**. But `W = Sym^m(rho)` and `rho^sigma` is the holonomy of the
**mirror** manifold — so that argument needs **amphichirality**.

**`s958` is chiral.** The coincidence survives chirality. So whatever forces `L_V = L_{V*}` is **not**
the Galois symmetry the record's own protection theorem runs on.

**The surviving candidate:** the equality is **local at the cusp**. The peripheral holonomy is
unipotent, and unipotents are conjugate to their own complex conjugates, so the boundary data cannot
tell `V` from `V*` even when the manifold can. That would explain precisely why global chirality does
not disturb it — and it is a statement about `H^1(T;W)` and the restriction map, not about `M`'s
symmetries.

## What to do with this

Prove `L_V` isotropic. By §1 that is the entire theorem. By §3 the proof should be sought at the
cusp, not in a global symmetry — which is a different search from every one the record has run,
all of which looked for a conjugation on `M`.

Reproduce: `verification/subspace.py` (the subspace comparison), with `q12.py`, `recog12.py`,
`final_index.py` supplying exact `Q(zeta_12)` arithmetic and the recognised geometric holonomy.
