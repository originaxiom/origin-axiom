# Cell 2 — Observer-Flow Closure and Protocol Dependence

## Repository baseline

```text
383d20f97f83c1453103e38797a2b2690d9b1135
```

The general operation of iterating derived sequences is classical. Cell 2
therefore addresses the exact behavior of this substitution and whether the
B540 graph is intrinsic.

No repository files were modified.

---

# 1. Exact certification method

A long fixed prefix is used only to discover candidate return words. Each edge
is then certified independently of that finite prefix.

For source substitution S, prefix u, return words R_i, coding Theta(i)=R_i,
and candidate return substitution rho, the program checks:

1. every R_i u contains u exactly at positions 0 and |R_i|;
2. S(R_i)=Theta(rho(i)) exactly as words;
3. S and rho are primitive;
4. both are prolongable on their initial symbols.

Hence the fixed point y of rho satisfies

S(Theta(y)) = Theta(rho(y)) = Theta(y).

It is therefore the unique source fixed point beginning with the prolongable
letter. The proper return boundaries prove the return-word list is complete.

Every certified edge is exact; graph closure no longer depends on assumed
finite-prefix saturation.

---

# 2. One-letter prefix protocol

For the protocol “derive every system with respect to its prefix of length
one,” the seven seed systems close on exactly twelve canonical systems.

The graph has:

- three fixed points;
- one nontrivial cycle;
- cycle length two;
- both cycle nodes of type q=2.

Thus B540 is upgraded to

\[
\boxed{12\text{ exact nodes},\ 3\text{ fixed points},\
1\text{ exact }q=2\text{ two-cycle}.}
\]

**Status:** `PROVED EXACTLY WITHIN THE PREFIX-1 PROTOCOL`

---

# 3. Protocol independence is refuted

Changing only the prefix length changes the exact graph.

With prefix length two:

- twelve nodes;
- two fixed points;
- two distinct two-cycles;
- both cycles are q=1;
- sigma belongs to a two-cycle instead of being fixed.

With prefix length three:

- eleven nodes;
- three fixed points;
- two distinct two-cycles;
- sigma again belongs to a two-cycle.

Therefore

\[
\boxed{
\text{the 12-node graph, self-fixed sigma, and unique double clock
are not intrinsic to sigma.}
}
\]

They are properties of the pair

\[
(\sigma,\text{selected prefix-observation protocol}).
\]

**Status:** `REFUTED AS PROTOCOL-INDEPENDENT`

---

# 4. Exact prefix-scale census

| prefix k | nodes | fixed | nontrivial cycles | sigma cycle |
|---:|---:|---:|---|---:|
| 1 | 12 | 3 | 2 | 1 |
| 2 | 12 | 2 | 2, 2 | 2 |
| 3 | 11 | 3 | 2, 2 | 2 |
| 4 | 10 | 4 | 2 | 1 |
| 5 | 12 | 3 | 3 | 1 |
| 6 | 10 | 4 | none | 1 |
| 7 | 12 | 3 | 4 | fixed after one transient |
| 8 | 11 | 1 | 2, 2, 3 | 2 |
| 9 | 12 | 1 | 2, 2, 3 | 2 |
| 10 | 12 | 1 | 2, 2, 3 | 2 |
| 11 | 12 | 2 | 2, 3 | 2 |
| 12 | 11 | 1 | 2, 2, 2 | 2 |

Across k=1,...,12, exact cycle lengths are

\[
\boxed{1,2,3,4}.
\]

The clock is forced after the observation scale is specified, but the object
does not select one observation scale.

The proper classification is:

\[
\boxed{
\text{forced conditional dynamics}
=
\text{object}+\text{observation protocol}.
}
\]

---

# 5. Incidence arithmetic cannot predict the target

The nodes S_a=sigma and S_B have:

- alphabet size four;
- q=1;
- identical characteristic polynomial;
- identical determinant;
- identical Smith group coker(I-A)=Z/11;
- integrally conjugate incidence matrices.

An explicit conjugator is

\[
X=
\begin{pmatrix}
0&-5&-3&-5\\
0&-3&-2&-3\\
-5&-3&0&0\\
-3&-2&0&0
\end{pmatrix},
\qquad \det X=-1,
\]

with

\[
A_{S_a}X=XA_{S_B}.
\]

Their mod-2 incidence systems are therefore also conjugate.

Nevertheless, under prefix length one,

\[
S_a\mapsto S_a,
\qquad
S_B\mapsto K1\_N0.
\]

So the packet

\[
(q,\mathbb F_2\text{ class},\mathbb Z/11\text{ charge},
\operatorname{SNF},\mathrm{GL}(\mathbb Z)\text{ class})
\]

does not determine the observer-flow target.

The missing data are ordered language structure and selected prefix—not
incidence arithmetic.

**Status:** `REFUTED BY EXACT GL(Z)-CONJUGATE COLLISION`

---

# 6. Physics and repo interpretation

Not justified:

> The object intrinsically recognizes itself as a fixed observer and possesses
> one intrinsic double clock.

Justified:

> Under one-letter prefix observation, the object is self-fixed and the only
> nontrivial derived-system cycle is the q=2 two-cycle.

Different observation windows yield different exact effective clocks. The
substrate constrains possible responses, while the coarse-graining selects
which temporal pattern is observed. Sigma does not choose that observable.

Repo contribution:

- B540 prefix-1 closure upgraded to exact edge-by-edge certificates;
- graph renamed conceptually as a **prefix-conditioned derived-system flow**;
- “self-recognition” and “double clock” must carry explicit prefix-1 scope.

---

# Verdict

```text
PREFIX-1 12-NODE CLOSURE               PROVED EXACTLY
PREFIX-1 THREE FIXED POINTS             PROVED EXACTLY
PREFIX-1 UNIQUE q=2 TWO-CYCLE           PROVED EXACTLY
INTRINSIC 12-NODE GRAPH                 REFUTED
INTRINSIC SELF-FIXED SIGMA              REFUTED
INTRINSIC UNIQUE DOUBLE CLOCK           REFUTED
PREFIX LENGTHS TESTED                   1..12
EXACT CYCLE LENGTHS                     1, 2, 3, 4
ARITHMETIC PACKET PREDICTS TARGET       REFUTED
FINAL CLASSIFICATION                    CONDITIONED ON OBSERVATION PROTOCOL
REPOSITORY WRITES                       NONE
```

The governed campaign now advances to **Cell 3: Complete Fixed-Character
Scheme**.
