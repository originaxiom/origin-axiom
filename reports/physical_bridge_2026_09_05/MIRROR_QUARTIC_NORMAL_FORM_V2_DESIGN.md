# R34 normal-form v2: exact-input guard before simplification

2026-09-19. Seal fce21ad79597d80188ee1e0aec022250a461a049 remains
unchanged. V1 native passes its algebraic controls; nine tests return
8 pass / 1 fail because residual(Float(1),Integer(1)) subtracts to
exact zero before the float guard runs. The eight-file focused run
was started in the same orchestration as the returned test status,
before its failure was inspected: 134 pass / 4 fail. This scheduling
did not alter files or erase failures, but it was not a halt-on-first-
control-failure sequence. No contrary procedural claim is made.

V2 changes only this guard: sympify and inspect BOTH operands before
subtraction. All scientific expressions and every original file stay.
Its nine tests are the same population and assertions against v2;
the wrong-coefficient, rational-identity, floating-input and stable/
unstable-domain controls are all retained. No new physical claim.

Seal this design, v2 producer and v2 test file; commit, push and
remote-confirm BEFORE native and test execution. Inspect each exit
before the next scientific command. Then execute the original seven
whole files plus BOTH the v1 and v2 control test files: nine files.
The v1 failed guard is not deselected. Expected focused outcome is
the same four failed IDs with nine additional passing instances;
report the observed count, not this expectation as evidence.
