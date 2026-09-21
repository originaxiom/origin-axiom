# R42-V2: preregistered diagnostic of the first Ricci comparison failure

2026-09-21. Original science pin
ecd6e70eaaa5012e0b1879892909da3e6ebc30b1 remains unchanged.
This successor is written AFTER the first R42 failure, but is itself
sealed, committed, pushed and remote-verified BEFORE execution.

The original native command exited zero while reporting ricci=false;
an exit code alone is not a scientific pass. The first new suite had
24 passes and one failure, test_generic_tensor_identity[ricci]. The
seventeen-file focused population had 276 passes and five failures:
the four existing IDs plus this new one. Both first logs are preserved.
No test is removed or its result counted as a pass retroactively.

P0: distinguish equality of the two generic n=3 Ricci polynomials from
structural equality of their SymPy expression trees. The original
producer compares clean(ric) to -2 Id+clean(gram), without normalizing
the difference; its separately normalized Ricci/Psi residual passes.
The prior is that this is a comparison defect, not a false curvature
identity. This is only a hypothesis until the successor runs. It is
the same error family that earlier normal-form controls warned about;
the first R42 verifier did not consistently apply that lesson.

The authored contraction, with C symmetric and sum_i C_iik=0, is

    sum_i R(i,j)^i_k = -2 delta_jk
       - sum_i,a (C_iia C_jak-C_jia C_iak)
       = -2 delta_jk+sum_i,a C_jia C_kia.

No geometric hypothesis, tensor sign, coefficient or expected identity
is changed. Recompute that same contraction from the frozen producer.
Check all nine polynomial residuals BOTH by rational normalization
and by expansion to zero polynomials. Independently check the quadric
specialization and two exact nonzero rational cubic specializations.

Failable controls: reversing the constant curvature contribution
must produce -4 Id, and reversing the cubic Gram contribution must
give a generically nonzero residual. A nonzero constant matrix must
fail the polynomial-zero instrument. Recheck all other native groups
from the unchanged original producer, but report the old structural
flag separately; do not silently set it to true.

Pass: every correct residual is zero, the altered controls are nonzero,
and the unchanged native groups still pass. Then adjudicate the original
failure as a representation-sensitive comparison bug. Otherwise retain
the analytic identity as disputed and diagnose without overwriting.
The corrected native reporter must exit nonzero for any failed check.

Execute this new native producer and its five tests, then the exact
previous seventeen-file population PLUS this successor test file.
Expect the original five failed IDs to persist; that does not make the
suite green. No finite test certifies the all-dimensional global proof,
physical spectrum, dynamical base selection or quantum theory.
