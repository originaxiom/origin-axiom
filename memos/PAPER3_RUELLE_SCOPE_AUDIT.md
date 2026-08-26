# Paper III: the M-character dictionary is exact; the gravity and n=2 upgrades are not

## What survives

With \(M\simeq SO(2)\), let \(\sigma_k\) be the one-dimensional
\(M\)-character evaluated on the holonomy component \(m_\gamma\).  Then

\[
R(s,\sigma_k)=\prod_{[\gamma]}
  \left(1-e^{ik\theta_\gamma}e^{-s\ell_\gamma}\right)
\]

in the absolute-convergence half-plane \(\Re s>2\).  At \(s=k\), each factor
is \(1-q_\gamma^k\).  The direct Euler-product identification is therefore
secure for integers \(k\ge3\), and Pfaff's finite ratio formula supplies that
same tail.

## Required corrections

1. \(\sigma_k\) is an \(M\)-character, not generally a representation of
   \(\Gamma\).  Paper III currently conflates the two definitions.
2. The displayed theorem says \(R(k,\sigma_k)\) “for \(\Re s>2\)” although
   \(s\) is absent.  It should first state \(R(s,\sigma_k)\), then substitute
   \(s=k\).
3. That substitution lies in the certified absolute domain only for
   \(k\ge3\).  \(k=2\) is exactly the boundary residue OA-C1060.
4. A finite-cutoff curve that looks smooth at \(s=2\) does not prove
   convergence, cutoff-order independence, regularity, or equality with a
   meromorphic continuation.
5. “Below the abscissa, divergence is certain” is too strong.  Leaving the
   absolute-convergence domain does not by itself exclude conditional
   convergence.
6. An infinite-product representation does not logically prove that no finite
   torsion identity exists.  The elementary telescoping product
   \(\prod_{n=2}^\infty(1-n^{-2})=1/2\) is a countercontrol to that inference.
7. Passing from finite Pfaff ratios to an infinite \(m\to\infty\) expression
   needs a separate convergence/asymptotic theorem.
8. Most importantly, the current corpus constructs a discrete geodesic
   GMY-form factor, not the gauge-fixed finite-volume cusped Einstein
   spin-2/vector/scalar determinant.  The latter remains OA-C1062.

## Ledger effect

No new endpoint row is required.  The existing dispositions remain exact:

- OA-C1059 `REFUTED`: no finite shifted Dirichlet-L Euler factorization;
- OA-C1060 `EXTERNAL_BLOCKER`: no proved \(n=2\), \(s=2\) value;
- OA-C1061 `REFUTED`: cited torsion/scattering objects do not directly equal
  the gravity determinant;
- OA-C1062 `EXTERNAL_BLOCKER`: the spin-resolved cusped one-loop construction
  is absent.

Paper III becomes sound after these definition, domain, inference and physical
scope corrections.  It cannot currently advertise the full cusped
boundary-graviton determinant as established.

## Certificate

`certificates/r011_ruelle_scope.py` is a dependency-free check of the exponent
dictionary, the \(k=2\) boundary, and the infinite-product countercontrol.
