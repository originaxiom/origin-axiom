# R007 — omega-one parity is redundant for integral E6 characteristics

## Claim

Let `c=A t` be the weighted-Dynkin labels of an integral E6 coroot-lattice characteristic.  If
all entries of `c` are even, then all entries of `t` are even and every weight of the minuscule 27,
including `omega_1`, has even grade.

The proof is immediate once the lattice hypothesis is made explicit: `det(A)=3`, so the E6 Cartan
matrix is invertible modulo two.  Therefore

```text
A t = c = 0 mod 2  =>  t = 0 mod 2.
```

Every integral weight pairs integrally with the simple coroots, so its pairing with an even `t` is
even.

## Exact finite check

The dependency-free certificate also copies and recomputes the locked 20 accepted characteristics.
Exactly nine are projective/even, and they are exactly the nine rows whose weighted-Dynkin labels
are all even.  It then checks all 64 label vectors `c=2d`, finding 24 that satisfy the necessary
integrality condition; every one has even `t` and an even 27-spectrum.

The integrality hypothesis cannot be dropped.  The arbitrary even vector
`c=(2,0,0,0,0,0)` has `t_1=8/3` and lies outside the characteristic lattice.

## Scope

This closes the redundancy theorem OA-C1070.  It does not independently prove that the inherited
20-row nilpotent-orbit census is complete; that remains conditional in OA-C1058.  It also does not
select one projective stratum or supply a physical fermion construction.

Certificate SHA-256:
`04425da77220542cd4aa58ceaf58a3b632401e8b5b58e503762c330a1d5fbf2d`.
