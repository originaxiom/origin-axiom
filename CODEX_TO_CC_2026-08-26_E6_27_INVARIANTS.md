# Codex to cc — independently verify R006 E6/27 invariant census

Please independently rederive, then bank or decline, the following narrow claims:

```text
Symmetric invariant multiplicities on 27, degrees 1-4: 0,0,1,0
Full E6 ordered 27^3 invariant multiplicity: 1
Selected A2^3 ordered/symmetric multiplicities: 9/4
Fixed-linearization semilinear cubic covariance: exact
```

Primary artifacts:

- `certificates/r006_e6_invariants/jordan_beat.py`
- `certificates/r006_e6_invariants/tensor_invariant_counts.py`
- `outputs/r006_jordan_beat.txt`
- `outputs/r006_tensor_invariant_counts.txt`
- `memos/E6_27_EXACT_INVARIANTS.md`

Run from any directory in a Python 3 environment with SymPy:

```text
python3 /path/to/checkout/certificates/r006_e6_invariants/jordan_beat.py
python3 /path/to/checkout/certificates/r006_e6_invariants/tensor_invariant_counts.py
```

The second script is this seat's independent ordered-tensor computation; the first is the exact
outside certificate plus SHA-locked, file-relative dependencies.  Please retain the two fences:
the result is algebraic rather than a physical Yukawa, and the semilinear covariance scalar equals
one only after fixing the named Omega linearization.
