# Execution receipts for boundary variation and branch checks

All science runs below exited zero. None is a full-repository suite or
independent analytic certificate. Commands ran with LC_ALL=C, LANG=C
and PYTHONDONTWRITEBYTECODE=1 under Python 3.12.1. Shell pipelines used
pipefail and tee, so captured logs did not mask producer exit codes.
Scientific sources were unchanged during each native and focused run.

## Seals

| Scope | Commit before execution |
|---|---|
| Original variation design, proof, producer, tests and input manifest | 63d151454785816e70c4bae81440917566ccdc87 |
| Post-native degree-zero closure follow-up and frozen native input | a6d8dc15ba8670582c80291e3a835e1494d603a3 |
| R87 replay and latest readout diagnostic | 07396164ac71ca943d11dd483d6da52eecc80e24 |

[ARTIFACT_HASHES.txt](ARTIFACT_HASHES.txt),
[INPUT_HASHES.txt](INPUT_HASHES.txt),
[CLOSURE_HASHES.txt](CLOSURE_HASHES.txt) and
[CROSS_SEAT_HASHES.txt](CROSS_SEAT_HASHES.txt) were checked unchanged.
The closure follow-up was explicitly designed after the first native
result, then sealed before its own import or execution. It is not
represented as part of the first preregistration.

## Local execution

From repository root, the producers were invoked as
`python3.12 reports/silver_boundary_variation_2026_10_04/verify.py`,
then the separately sealed `closure.py` and `readout_probe.py` at that
same path. Tests used `python3.12 -m pytest -q -p no:cacheprovider
--import-mode=importlib` and the explicit files below.

| Capture | Scope and result | Exit |
|---|---|---:|
| NATIVE_FIRST.jsonl | Original controls and all four actual members PASS | 0 |
| FOCUSED_FIRST.txt | test_verify.py and preceding tensor test_structural.py; 10 passed in 59.10 seconds | 0 |
| CLOSURE_FIRST.jsonl | Two-sided closure controls and all four actual members PASS | 0 |
| FOCUSED_SECOND.txt | test_verify.py, test_closure.py and preceding tensor test_structural.py; 13 passed in 81.18 seconds | 0 |
| READOUT_FIRST.jsonl | Eight synthetic cases and nine expected diagnostic behaviors reproduced | 0 |

The diagnostic's successful exit means that the suspected current
coverage risks reproduced together with the opposite controls. It is
NOT a pass of the affected population-certification logic. In particular,
no actual cover population or puncture cohomology is computed by it.

## R87 execution

The seven native/reference sources and two test files were extracted
with git archive from d18fae3dafec9160ffe30a2cb43e4c0412547020 into an
isolated temporary directory. No foreign branch or scientific source was
modified. The native command invokes parent_gluing_character.py. The
reference command invokes parent_gluing_character_reference.py with our
fresh native capture as its sole argument. Focused pytest uses the same
flags as above, with test_physical_bridge_parent_gluing_character.py
and test_physical_bridge_gluing_freedom.py in that extracted snapshot.

| Capture | Result | Exit |
|---|---|---:|
| R87_NATIVE_FIRST.jsonl | 145 of 145 exact predicates | 0 |
| R87_REFERENCE_FIRST.jsonl | 209 of 209 modular witness predicates | 0 |
| R87_FOCUSED_FIRST.txt | 12 tests passed in 69.60 seconds | 0 |

The native capture is 31839 bytes and the reference capture 8170 bytes.
Both match the published receipt's SHA256 AND its complete saved stdout
byte-for-byte. All three native characters have degree two and nonzero
derivative at X=1. The modular verifier is the source author's separately
coded instrument, not a second exact number-field proof. This replay
does not independently prove the global PDE admission theorem.

Pinned source hashes, under reports/physical_bridge_2026_09_05:

```text
57d52d0268cc8562522560029727026d5d0cc80e88bd0f464aee704858911731  cross_branch_positives.py
f1d6bfb9e998a3306ddb41757c9356f4e99757a93ebbfc474e84be9d49bee4c7  joined_background.py
22e41effc4acf899172e4bd95c196c11542ebd58580d14ea9e20dbce49eae869  joined_background_reference.py
501b3c87400f198035360dc760f19937a97c3d3bf6fd7801cecf325ae20f27f9  gluing_freedom.py
b66e0584e780686295e8501e9e14d5f717f62202f5797b8fcaab52432b4df80c  gluing_freedom_reference.py
2d01c892b75acac30355aefed48af400e9e4376510c02033811d7d9c2048a0c9  parent_gluing_character.py
f7608983681f6ba96ff2d985de0406e442615f8ca526c134c7e821b082d61ba9  parent_gluing_character_reference.py
```

## Capture hashes

```text
7707379c4796577ccc397cb01c76e79385c232152f5fb4ed9e22cf74688aee3c  NATIVE_FIRST.jsonl
2bafb0b55f8e359117c96086c252570b30dba88f37116655a7128b9715aba380  FOCUSED_FIRST.txt
1f7a73a91277bffb8780e70201e02b4c5530baad607653f2278e32c2e7a104f0  CLOSURE_FIRST.jsonl
61096dace033ccef5e6bc8a2c668032929c1bffccfc35369defa5d7a77c9ffba  FOCUSED_SECOND.txt
d5e2f16378687e0973dd7403df8f6e80a35a95d33c9b5ac505fe4b015e9eaf04  READOUT_FIRST.jsonl
dd2ff948345e13956dcd4614c4120602f7ded7829bf339a82e995a522e829fc7  R87_NATIVE_FIRST.jsonl
5ec29325164f90796386395d8585ca3b4010c13087231ff1f18453b5aa2d2907  R87_REFERENCE_FIRST.jsonl
7bcb941dfbd93f79abc2458f426de55126ab09517fe01679fccefe5bb76aa87a  R87_FOCUSED_FIRST.txt
```

Long tool displays truncated some witness matrices; complete tee captures
are present and were parsed. No scientific rerun or overwrite was used
to conceal a failure. Two fetch attempts failed authentication before
the scoped HTTPS override succeeded. An initially guessed relay path
returned no file; the exact path was then obtained from the commit's
file list and read. Neither issue became an absence claim.

This packet is local research on audit/fork-2026-09-20, not shared-bank
adoption. No full-suite certificate, push, merge, nonauthor acceptance
or physical chirality is claimed. Unrelated untracked work was preserved.
