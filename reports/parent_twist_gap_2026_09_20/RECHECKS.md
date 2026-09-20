# F05 execution, source and scope receipt

2026-09-20. Outcomes below are transcribed command-tool results, not a
durable raw terminal capture, independent proof review or repository-wide
banking pass. No scientific source was changed while tests were running.

## Seal and first execution

Input was clean fork branch `audit/fork-2026-09-20` at `297e1dd7`.
DESIGN.md, PROOF.md, verify.py and test_verify.py were sealed in SEAL.json
and committed at `dad3bd3a` before first execution. Expected outcomes,
normalization, countercontrols and scope were disclosed beforehand.
No failed F05 revision, assertion change, parameter adjustment or retry
occurred before the result below.

Interpreter: `/Users/dri/.pyenv/versions/3.12.1/bin/python3.12`;
Python 3.12.1, SymPy 1.14.0.

```
python3.12 -m pytest -q reports/parent_twist_gap_2026_09_20/test_verify.py
```

Process 16165, final chunk `9aa3cc`, exit 0:

```
24 passed in 3.75s
```

Controls cover local BPS equations, both terms in covariant parallelism,
the Clifford mixed-term cancellation, exact positive algebraic spectra,
wrong-scale and trivial-coefficient comparators, marked geometric and
twisted relations, determinant restriction, a trace non-self-duality witness,
order-two and order-four pairing behavior, complete parent center phases,
the surviving root system, unitary transitions, shifted cusp Fourier
coercivity and the bounded perturbation threshold. A nonparallel oscillator
prevents a false universalization of geometric vanishing.

The generic closure, compactness and bounded perturbation arguments are
written proofs. Finite exact tests check their identities and controls;
they do not certify the infinite-dimensional theorems by themselves.

## Unchanged antecedents

```
python3.12 -m pytest -q --import-mode=importlib \
  reports/nonsplit_admissibility_2026_09_20/test_verify_v2.py \
  reports/complete_domain_2026_09_20/test_verify.py \
  reports/nonsplit_cusp_growth_2026_09_20/test_verify.py \
  reports/full_flag_growth_2026_09_20/test_verify.py
```

Process 16041, final chunk `8106f9`, exit 0:

```
62 passed, 1 warning in 20.38s
```

The warning concerns optional Plink tkinter GUI availability. No GUI enters
these assertions. Importlib mode distinguishes repeated test-file names.
Post-run verification (chunk `a50f3f`) found all four F05, four F04, four
F03, four F02 and seven F01-v2 seal entries unchanged: 23 digests total.
Historical F01-v1 and R16 failures remain in their existing receipts;
neither was rerun or relabeled green here.

At report finalization an additional shasum invocation failed before hashing
because the inherited C.UTF-8 locale was unavailable to Perl. Repeating only
that read-only command with command-local LC_ALL=C and LANG=C succeeded:
all four F05 hashes match SEAL.json (chunk `8b6608`). No environment setting
was changed persistently and no scientific test was rerun for this issue.

## R39 reception and reproduction

Pin: `8d2cced21cc63772828458fb842e0280513b2f29`.
Scientific seal: `ce48016a5b592f625cf71babc4f65cb3bb51543a`.
Six scientific files were unchanged between the two commits. Ten source
files were extracted to `/private/tmp/oa-r39-review.Zjt4ZR` and compared
with their exact Git bytes. Hashes are in R39_RECEPTION.json.

```
env PYTHONDONTWRITEBYTECODE=1 python3.12 -m pytest -q -p no:cacheprovider \
  /private/tmp/oa-r39-review.Zjt4ZR/tests/test_physical_bridge_parent_background.py
```

Process 7600, final chunk `65ed80`, exit 0: **16 passed in 2.08 s**.
Extraction emitted a locale warning; byte comparison succeeded. This is
reproduction of the existing implementation, not an independent one.
R39's separately reported larger focused run was not rerun here and is
not converted to a full-suite green claim.

Fresh all-ref retrieval was attempted but did not succeed: sandbox DNS
failure, then SSH public-key authentication failure. HTTPS was redirected
to SSH by existing Git configuration; a command-local override attempt
did not repair authentication. No credentials or persistent Git settings
were changed. The local pin remains usable, but current remote coverage
cannot be claimed from these attempts. No other seat was checked out,
merged, modified or executed while unsealed.

## Primary-source reading boundary

Personally read before F05 execution:

- Braun et al., [Higgs Bundles for M-theory on G2-Manifolds](https://arxiv.org/html/1812.06072v2),
  equations 2.9--2.19 and B.8--B.14, on the complete local bosonic action
  and auxiliary-field elimination.
- Menal-Ferrer--Porti, [Twisted cohomology for hyperbolic three manifolds](https://arxiv.org/html/1001.2242v2),
  introductory theorems and sections 2.1--2.2 through Lemma 2.14, including
  the compact-support argument and nontrivial coefficient restriction.

After the sealed tests passed, personally read Braun section 2.3,
equations 2.34--2.44, to confirm the fermion/coefficient-operator dictionary
before its commuting-Higgs restriction. This confirms the interpretation
of zero modes; no sealed science file or expected value was changed.
The action's factor of two in its wave equation was retained as a warning
against identifying a mathematical Q bound with a four-dimensional mass.

Selected sections were read, not both full papers anew. No agent summary
or PDF was used. Prior repository-source reading is itemized in DESIGN.md.

## Not accomplished by these checks

No independent expert proof review, complete E8 spectrum, actual numerical
mass bottom, selected Wilson character, new source solution, interacting
mirror gap, anomaly completion, full-suite/gate pass, four-dimensional
gravity calculation or empirical prediction. No push or publication.
