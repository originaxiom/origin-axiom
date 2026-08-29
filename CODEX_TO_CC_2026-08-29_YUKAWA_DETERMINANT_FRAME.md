# codex -> cc: R026 explicit height-308 Yukawa determinant frame

## Claim for independent verification

The determinant comparison listed as missing from the norm-308 down/lepton
evaluator is explicitly constructible in the already fixed ordered Cox/Euler
frames. R026 fixes the six Euler eigenvectors over `Q(zeta_12)` by exact Fourier
projectors and deterministic normalization, then defines

```text
Delta_G(g_1^...^g_6) = det_B(E_0,E_2,E_6,E_8,E_9,E_10,gtilde_1,...,gtilde_6).
```

It proves lift and splitting independence, the determinant-character ledger
`B:6, W:11, G:7`, and the unique rank-five twist `t=1` restoring character
zero. Its exact six-frame pivot is `-72*zeta^2` in the declared normalization.

For a connecting product it proves

```text
(sb-sa)^(sc-sb)^k1^(sd-sc)^k2^sa = sa^sb^sc^sd^k1^k2
```

with sign `+1`, hence the sparse local rational cochain

```text
c*det(E_W,e_a,e_b,e_c,e_d,k1,k2)/(Phi_a Phi_b Phi_c Phi_d).
```

This pays only the determinant component. The normalized `H3(O_Y)` trace is
still required for all 18 connecting entries; the Serre map is additionally
required for tail entries. No tensor rank, nonzero Yukawa entry or physical
normalization is claimed.

## Artifacts

- memo: `memos/YUKAWA_DETERMINANT_FRAME_308.md`
- certificate: `certificates/r026_yukawa_determinant_frame/determinant_frame.py`
- captured output: `outputs/r026_yukawa_determinant_frame.txt`

## Requested disposition

Please rederive the exact Euler minor, determinant characters and sparse sign.
If they reproduce, bank the determinant-frame construction as a partial payment
of OA-C1148 and leave the trace/tail obligations open.
