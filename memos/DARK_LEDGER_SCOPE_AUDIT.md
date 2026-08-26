# Memo 56: exact E6 coupling hypergraph, not yet a dark sector

## Reproduced algebra

For the fixed \(D_5\times U(1)\) frame,

\[
27=16_{1}\oplus10_{-2}\oplus1_{4}.
\]

The 45 nonzero supports of the normalized E6 cubic split exactly into

\[
40\,(16,16,10)\quad+\quad5\,(10,10,1).
\]

Consequently no single cubic monomial contains both a 16 and the singlet;
the support hypergraph connects those sectors only by two cubic steps through
the 10.  The parity \((-1)^q\), negative on the 16 and positive on
\(10\oplus1\), is conserved on all 45 supports.

For the separately selected bridge A1, the class-by-weight table also
reproduces:

| D5 class | -1 | 0 | +1 |
|---|---:|---:|---:|
| 16 | 5 | 10 | 1 |
| 10 | 0 | 5 | 5 |
| 1 | 1 | 0 | 0 |

The two diagonal parities are neither equal nor global negatives.

## Required corrections

1. The charges \(16_1+10_{-2}+1_4\) are conventionally the
   \(E_6\to SO(10)\times U(1)_\psi\) grading, not \(U(1)_\chi\).
2. “Portal” is only a label for the cubic support hypergraph.  A physical
   portal requires realized four-dimensional fields, kinetic terms, a vacuum,
   masses and dynamics; none occurs here.
3. The \(D_5\) frame is explicitly observer-paid.  The bridge A1 is also a
   selected branch whose canonical uniqueness was refuted in OA-C1087.
   Therefore the bridge lock cannot yet be called unconditionally
   object-paid.
4. Cubic parity conservation alone does not prove exact symmetry of the full
   action, nonperturbative survival, stability of the singlet, relic abundance
   or any dark-matter observable.

## Ledger result

This is a new narrow `PROVED` representation-theory row and a useful
refinement of OA-C0014: the allowed E6 cubic supports and the mismatch of two
chosen gradings are exact.  OA-C0014 remains `EXTERNAL_BLOCKER`, because no
vacuum lifts the exotics or realizes a stable dark particle.

## Certificate

`certificates/r012_dark_ledger_scope.py` is file-relative and reuses the
branch-local exact E6/27 construction from R006.  It does not rely on the
outside seat's stored output.
