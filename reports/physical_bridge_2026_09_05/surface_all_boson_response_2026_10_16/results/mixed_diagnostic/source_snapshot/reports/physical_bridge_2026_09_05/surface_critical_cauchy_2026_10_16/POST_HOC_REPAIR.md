# Canonical serialization after the first capture

First execution at published0d7fb504188c147a9541d5dee8bf2ee7ec9ba26e
passed all115mathematical checks in BOTH methods. Native18.437448s,
reference19.177627s. The complete-record equality gate correctly failed:
two triplet log entries were rationally equal but Sympy simplify saved
different factorizations. The full outputs, raw diagnostics, receipt and
199source snapshots remain in results/first_run. That failed receipt
is not overwritten or relabeled a pass. Original manifest/seals remain
in its source snapshot and in the pre-execution commit.

The only scientific-code change is enc: canonical cancel(expand(z))
instead of simplify(z) for serialized matrix entries. Operators,
fundamental formulas, reference integration, all acceptance criteria and
source checks remain unchanged. The new representation still undergoes
complete-record comparison; no equality criterion is weakened. This
repair is POST-HOC to the first execution, but is hashed, committed,
pushed and exact-server-confirmed BEFORE the successor capture.

The mathematical/analytic proof remains authored, not independently
accepted. Full angular integers/curved boundary/global physical theory
and foundational SM/three/gravity are not inferred from115checks.
