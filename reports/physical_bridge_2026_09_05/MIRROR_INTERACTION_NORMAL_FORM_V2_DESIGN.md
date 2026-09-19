# R33 normal-form control v2 — mutation fixture repair, before execution

2026-09-19. The first normal-form-control native run at seal 878f6866
HALTED before producing a verdict: mass.copy() preserves SymPy's
ImmutableDenseMatrix type, so the negative fixture cannot change an
entry. Its traceback and all three original control files are preserved.
The original control's six-test and expanded runs are NOT RUN because
the native instrument halted; they are not counted as successful.

The ONLY scientific-source difference in v2 is explicit construction
of a MutableDenseMatrix for the deliberate wrong-mass fixture.
The six test definitions are reused verbatim except the imported
v2 producer filename and module name. No mathematical criterion,
original R33 producer or original failing assertion is changed.

All quantifiers, priors and positive/rejecting controls of
MIRROR_INTERACTION_NORMAL_FORM_DESIGN.md are retained. Seal, commit,
push and remote-confirm this design and the two v2 files before use.
Run the v2 native producer, then its six tests, then the original
five-file R33 focused population followed by the v2 test file.
This is six files, NOT the whole repository or the halted v1 tests.
The original two structural-comparison failures are expected to remain.
Accept the diagnosis only if the exact residual and symbolic family
pass AND the altered mass and noncollinear vector fail the gap identity.
