# Cell 1C — Exact Defect Kinematics

## Scope

Cell 1B proved that every nonzero element of \(\mathbb Z/11\) has a finite
localized carrier. Cell 1C asks what the substitution language itself permits
those carriers to do.

This is a **kinematic** calculation. It classifies legal local rewrites. It
does not insert a time evolution or Hamiltonian.

Repository head at launch:

```text
22f7ee4ab59299970ee6db454f93816982e50fce
```

No repository files were modified.

---

# 1. Exact finite census

All distinct factors of \(\sigma^{10}(a)\) were enumerated for every length

\[
7\le L\le500.
\]

For all 494 tested lengths, the exact factor counts agree between
\(\sigma^9(a)\) and \(\sigma^{10}(a)\). Since the former is a prefix of the
latter, the observed factor sets are identical at those two depths.

At length 500 there are 1,699 distinct factors.

The result is therefore an exhaustive, depth-stabilized finite-factor census,
not an asymptotic theorem about every possible length.

---

# 2. Strict carrier relocation was not found

A strict relocation witness requires:

1. one legal background factor \(x\);
2. two legal alternatives \(y,z\) with the same three-letter outer boundaries;
3. \(y\) and \(z\) each differ from \(x\) in exactly one contiguous component;
4. both components carry the same nonzero charge;
5. the components occupy different positions.

Such a triple would move one charge from one position to another without
introducing additional charged components.

No witness exists in the exhaustive stabilized census through \(L=500\):

\[
\boxed{
N_{\mathrm{strict\ motion}}(L\le500)=0.
}
\]

**Status:** `NOT OBSERVED IN AN EXHAUSTIVE FINITE CENSUS`

This is not a theorem of permanent immobility. It means that free translation
is not supplied by the smallest natural static rewrite relation.

---

# 3. Neutral pair creation and annihilation exist

A neutral pair witness is a legal factor \(y\) differing from a legal
background \(x\) in two separated components with charges

\[
q,\qquad -q.
\]

Replacing \(x\leftrightarrow y\) is a legal local creation/annihilation rewrite
with total charge zero.

Exact witnesses were found for four of the five inverse pairs:

\[
\boxed{
1+10,\quad2+9,\quad3+8,\quad4+7.
}
\]

The reversed orientation supplies both charges in each pair. Thus the
oriented charges with witnesses are

\[
1,2,3,4,7,8,9,10.
\]

Examples include:

\[
3+8=0\pmod{11}
\]

inside a length-13 legal factor, and

\[
1+10=0\pmod{11}
\]

inside a length-14 factor.

The inverse pair

\[
\boxed{5+6}
\]

was not observed through length 500.

**Status:**
- four inverse-pair channels: `PROVED BY EXPLICIT EXACT WITNESSES`;
- \(5+6\): `NOT OBSERVED THROUGH LENGTH 500`.

---

# 4. Two exact fusion/splitting channels exist

A fusion witness uses one background \(x\), a split configuration \(y\) with
two separated charged components \(q_1,q_2\), and a fused configuration \(z\)
with one component of charge \(q_1+q_2\). All three factors are legal and have
the same outer boundary.

Exactly two ordered channels were found through length 500:

\[
\boxed{3+9\longleftrightarrow1}
\]

and

\[
\boxed{10+3\longleftrightarrow2}.
\]

The reverse rewrites are exact splitting channels:

\[
1\longrightarrow3+9,
\qquad
2\longrightarrow10+3.
\]

No other ordered fusion channel was observed in the census.

**Status:** `TWO CHANNELS PROVED BY EXPLICIT EXACT WITNESSES`

---

# 5. What this means physically

The grammar permits more than static charge labels:

- finite charged carriers exist;
- four inverse pairs can be created or annihilated locally;
- two nontrivial fusion/splitting reactions are legal;
- all reactions preserve total \(\mathbb Z/11\) charge.

But it does not provide free propagation under the strict test.

The emerging picture is therefore not a gas of freely moving particles. It is
closer to:

> **charged local rearrangements with highly constrained reaction channels.**

Most importantly, \(\sigma\) is an inflation/substitution rule, not a local
time-update law. A legal rewrite does not tell us how often it occurs, in
which direction, or with what amplitude.

Thus the calculation identifies the precise missing physical input:

\[
\boxed{\text{a dynamical selection rule on the legal rewrite graph}.}
\]

That input could be:

- a classical update rule;
- a stochastic rate;
- a quantum Hamiltonian;
- an action assigning amplitudes to rewrites.

Without it, the object supplies charge sectors and reaction kinematics, but
not motion in time.

---

# 6. Contribution to the repo

This extends the prime-11 branch from a cohomological invariant to a finite
reaction algebra:

\[
\mathbb Z/11\text{ torsion}
\rightarrow
\text{observer-wide charge}
\rightarrow
\text{localized carriers}
\rightarrow
\text{pair and fusion channels}.
\]

It also closes one over-optimistic route:

> The substitution language alone does not currently yield a freely
> propagating charged excitation.

The result should be integrated as exact mathematics with the mobility
absence explicitly finite-range.

---

# 7. Next computation

Two paths now separate cleanly.

## Structural path

Return to the governed master campaign and execute **Cell 2: the observer-flow
closure theorem**.

## Physics path

Supply one minimal dynamics on the exact rewrite graph and compare controls:

1. equal-amplitude quantum adjacency;
2. energy-weighted Hamiltonian;
3. reversible stochastic rates;
4. a matched random-substitution control.

Then compute:

- charge-sector connectivity;
- dispersion or lack of it;
- bound states;
- reaction amplitudes;
- whether the absent strict motion becomes effective higher-order hopping.

That would be a conditioned physical model, not a claim that the time law was
forced by \(\sigma\).

---

# Claim ledger

```text
FACTOR LENGTHS EXHAUSTED                    7..500
DEPTH-9/DEPTH-10 STABLE LENGTHS             494/494
STRICT SAME-BACKGROUND MOTION               0 WITNESSES
ANNIHILATION PAIRS                           1+10, 2+9, 3+8, 4+7
MISSING INVERSE PAIR                         5+6
FUSION/SPLITTING                             3+9 <-> 1
                                             10+3 <-> 2
TOTAL CHARGE CONSERVATION                    EXACT
FREE PARTICLE PROPAGATION                    NOT DERIVED
CANONICAL TIME DYNAMICS                      ABSENT
```
