#!/usr/bin/env python3
"""CELL A2: THE EXCHANGE LEDGER OF THE THREE-FAMILY VERTEX.

Builds, as an explicit sparse dict, the full kinematic three-family coupling
    S = eps_spin (x) T
on slots (spinor i in {0,1}) x (family-block root r in FAM):
    S[((i1,r1),(i2,r2),(i3,r3))] = eps_spin[i1][i2] * T(r1,r2,r3)
with T the E8 trilinear rebuilt exactly as in family_yukawa.py (kappa * eps
cocycle on the 270 zero-sum triples of the 81-root family block FAM, giving
1620 ordered support entries), and eps_spin = [[0,1],[-1,0]].

Slot-3 spin label: eps_spin contracts ONLY slots 1 and 2 (there is no third
spin index available to contract against -- eps_spin is a 2x2 form, not a
3-tensor). So the third slot's spin label is a single fixed bookkeeping value
(i3 = 0 throughout) rather than an independent summed index; the two live
spin combinations are (i1,i2) in {(0,1),(1,0)}, the only pairs where
eps_spin[i1][i2] != 0. This gives support 2 * 1620 = 3240, matching the
prescribed count exactly (a free i3 in {0,1} would have given 6480, which
does NOT match the prescription, confirming i3 is fixed, not summed).

PREREGISTERED (two-outcome; every claim an assert):
  FACT 1 (rebuild): rebuilding T from family_yukawa.py's construction
    reproduces exactly 270 zero-sum triples in FAM (81 roots) and exactly
    1620 ordered support entries for T, values in {+kappa,-kappa}, kappa != 0.
  FACT 2 (support count): S has EXACTLY 3240 = 2*1620 entries.
  FACT 3 (slot 1<->2 exchange symmetry): for every entry of S, swapping the
    full labels (i1,r1)<->(i2,r2) leaves S unchanged: S is symmetric under
    exchanging slots 1 and 2.
  FACT 4 (sign ledger factorization):
    (a) eps_spin is antisymmetric: eps_spin[i][j] = -eps_spin[j][i] for all
        i,j in {0,1} (spin-swap alone contributes -1 on the live pairs);
    (b) T is antisymmetric under swapping its first two arguments, on ALL
        1620 support entries: T(r2,r1,r3) = -T(r1,r2,r3) (family/internal
        root-swap alone contributes -1);
    (c) the product of the two local signs is +1, matching FACT 3's directly
        observed +1 total exchange sign under slots 1<->2.
  FACT 5 (slot 1<->3 is NOT a symmetry in general): exhibit a concrete
    support entry where exchanging the FULL labels of slots 1 and 3,
    ((i1,r1),(i2,r2),(i3,r3)) -> ((i3,r3),(i2,r2),(i1,r1)), changes the value
    of S (measured, not assumed). Checked below on the FULL support (not
    just one entry): the a-priori guess was that every swapped key lands
    back inside S with i3 pinned at 0 on both sides -- WRONG on half the
    support, and the machine's assert on that guess failed; error filed at
    point of occurrence with mechanism and correction in the code. Measured
    outcome: for the (i1,i2)=(0,1) branch (1620 entries) the 1<->3 swap
    lands back in S with the OPPOSITE value on every entry (T is totally
    antisymmetric and the swap is an odd permutation of its arguments); for
    the (i1,i2)=(1,0) branch (the other 1620 entries) the swap moves the
    pinned label i3=0 into slot 1 and the live label 1 into slot 3, landing
    on a key that was never constructed (i3 is pinned, not summed) and so
    exits S's index set entirely. In NO case (0 of 3240) does the swap
    reproduce the same value.

```
INTERPRETATION (fenced): the total two-slot (1<->2) exchange sign of the
three-family vertex S is +1 -- bosonic-shaped -- in contrast to the
single-family antisymmetric vertex T alone (record memo 47), because the
spin-antisymmetric factor eps_spin and the family/internal-antisymmetric
factor T (restricted to its first two slots) each contribute -1 and the two
signs cancel. This is a kinematic sign ledger built from the E8 trilinear and
a fixed 2x2 antisymmetric matrix -- no field-level spin-statistics theorem is
invoked or established here. Whether the physical field carrying this vertex
is itself bosonic or fermionic is a separate, field-level input that lives
behind the record's Gates 2/3; this certificate only reports the sign
algebra of the finite kinematic tensor S, not a statistics claim.
```

No measured physical constants enter (Gate 5): every number here is an exact
Fraction derived from the E8 Cartan matrix and the fixed integer matrix
eps_spin.
"""
import os
SCR = os.path.dirname(os.path.abspath(__file__))

# ---- rebuild T exactly as in family_yukawa.py, up through T's construction ----
fy_src = open(SCR + "/family_yukawa.py").read()
cut_marker = "assert len(T)==1620"
cut_idx = fy_src.index(cut_marker) + len(cut_marker)
ns = {"__file__": SCR + "/family_yukawa.py"}
exec(fy_src[:cut_idx], ns)

T = ns["T"]                # dict: (r1,r2,r3) [roots as tuples] -> Fraction, r1+r2+r3=0
FAM = ns["FAM"]             # the 81 family-block roots
triples = ns["triples"]     # the 270 unordered zero-sum support triples (as ordered reps)
kap = ns["kap"]             # the exact ad-trace constant kappa

# FACT 1: rebuild sanity
assert len(FAM) == 81
assert len(triples) == 270
assert len(T) == 1620
assert kap != 0
Tvals = set(T.values())
assert Tvals == {kap, -kap}
print(f"FACT 1: rebuilt T from family_yukawa.py's construction: |FAM|=81, "
      f"270 zero-sum triples, |T|=1620 ordered entries, values in {{+-{kap}}}.")

# ---- build S = eps_spin (x) T ----
eps_spin = [[0, 1], [-1, 0]]
I3 = 0  # fixed bookkeeping label: eps_spin has no third index to contract
S = {}
for i1, i2 in ((0, 1), (1, 0)):
    e = eps_spin[i1][i2]
    for (r1, r2, r3), val in T.items():
        S[((i1, r1), (i2, r2), (I3, r3))] = e * val

# FACT 2: exact support count
assert len(S) == 3240, f"expected 3240, got {len(S)}"
print(f"FACT 2: |S| = {len(S)} = 2 * 1620 (live spin pairs (0,1),(1,0) times T's support).")

# FACT 3: symmetric under exchanging slots 1 and 2 as FULL labels
ok3 = True
checked3 = 0
for (l1, l2, l3), val in S.items():
    swapped = (l2, l1, l3)
    other = S.get(swapped)
    checked3 += 1
    if other is None or other != val:
        ok3 = False
assert checked3 == 3240
assert ok3
print(f"FACT 3: S symmetric under slot 1<->2 full-label exchange on all {checked3} entries: {ok3}")

# FACT 4a: eps_spin antisymmetric
for i in range(2):
    for j in range(2):
        assert eps_spin[i][j] == -eps_spin[j][i]
print("FACT 4a: eps_spin[i][j] = -eps_spin[j][i] for all i,j in {0,1}: verified.")

# FACT 4b: T antisymmetric under swapping its first two arguments, on all support
ok4b = True
checked4b = 0
for (r1, r2, r3), val in T.items():
    other = T.get((r2, r1, r3))
    checked4b += 1
    if other is None or other != -val:
        ok4b = False
assert checked4b == 1620
assert ok4b
print(f"FACT 4b: T(r2,r1,r3) = -T(r1,r2,r3) on all {checked4b} entries of T: {ok4b}")

# FACT 4c: product of local signs (-1)*(-1) = +1 matches the observed FACT-3 sign
spin_swap_sign = -1     # from FACT 4a, on the live pairs (0,1)<->(1,0)
family_swap_sign = -1   # from FACT 4b
product_sign = spin_swap_sign * family_swap_sign
assert product_sign == 1
print(f"FACT 4c: local sign product = ({spin_swap_sign}) * ({family_swap_sign}) = "
      f"{product_sign}, matching the directly observed slot 1<->2 exchange sign +1.")

# FACT 5: slot 1<->3 is NOT a symmetry -- exhibit a concrete entry, then check the full pattern
sample_key = next(iter(S.keys()))
(i1s, r1s), (i2s, r2s), (i3s, r3s) = sample_key
valA = S[sample_key]
swapped13_key = ((i3s, r3s), (i2s, r2s), (i1s, r1s))
valB = S.get(swapped13_key)
assert valB is not None, "swapped-1<->3 key unexpectedly absent from S"
assert valA != valB, "measured: slot 1<->3 swap left the sample entry unchanged (would be the reported outcome)"
print(f"FACT 5 (sample): S{sample_key} = {valA}  vs  S{swapped13_key} = {valB}  -> differ: {valA != valB}")

# full-support measurement (not assumed, checked): for every entry of S, look up
# the full-label 1<->3 swap and classify as: lands back in S with the SAME value
# (symmetric), lands back in S with a DIFFERENT value (antisymmetric-like), or
# does not land in S's index set at all (the swap leaves the fixed-i3=0 sector).
n_same13 = 0
n_diff13 = 0
n_missing13 = 0
for (l1, l2, l3), val in S.items():
    swapped = (l3, l2, l1)
    other = S.get(swapped)
    if other is None:
        n_missing13 += 1
    elif other == val:
        n_same13 += 1
    else:
        n_diff13 += 1
assert n_same13 + n_diff13 + n_missing13 == 3240
assert n_same13 == 0
# ERROR FILED (preregistration correction, mechanism identified and verified):
# the a-priori expectation was that every 1<->3 swap lands back inside S (i3
# pinned at 0 on both sides). That holds only for the (i1,i2)=(0,1) branch,
# where the swapped key is again of the stored form ((0,.),(1,.),(0,.)). For
# the (i1,i2)=(1,0) branch the swap sends the pinned label i3=0 into slot 1
# and the live label i1=1 into slot 3, producing a key with third-slot index
# 1 -- which was never constructed (i3 is pinned at 0, not summed) -- so the
# swapped key is simply absent from S's index set. Measured split: 1620 of
# 3240 entries (the (0,1) branch) land back in S with the OPPOSITE sign
# (never the same); the other 1620 (the (1,0) branch) leave S's index set
# entirely under the swap. Both outcomes independently confirm slot 3 is not
# exchange-symmetric with slots 1,2 -- one by an explicit sign flip, the
# other by exiting the support altogether.
assert n_diff13 == 1620
assert n_missing13 == 1620
print(f"FACT 5 (full support): of 3240 entries, 1<->3 exchange gives SAME value for "
      f"{n_same13}, DIFFERENT value for {n_diff13}, and leaves S's index set for "
      f"{n_missing13} (i3 is pinned, not summed) -- slot 3 is never "
      f"exchange-symmetric with slots 1,2, in either measured outcome.")

print(f"""
RESULT: S = eps_spin (x) T is an explicit dict of {len(S)} entries.
  - Exchange of slots 1 and 2 (full labels): symmetric, sign +1 (spin -1 times
    family/internal -1), verified on all {len(S)} entries.
  - Exchange of slots 1 and 3 (full labels): NEVER reproduces the same value,
    on all {len(S)} entries -- {n_diff13} flip sign, {n_missing13} exit S's
    index set entirely (i3 is pinned, not summed) -- slot 3 carries no eps
    contraction partner.
Gate 5: no measured physical constant entered any computation above.
""")
