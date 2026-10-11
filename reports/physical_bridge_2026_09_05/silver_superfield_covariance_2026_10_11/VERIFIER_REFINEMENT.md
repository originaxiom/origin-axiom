# Exact-log control scope refinement, after the first successful runs

Initial pushed seal4cc9a13ce73d113e456cdf9de302e82d2d465ea6 gave
41/41 native,24/24 reference,8 focused and40 five-packet regression PASS.
Literal first logs and all receipts are retained; original code remains
in that commit. No mathematical failure is concealed or relabeled.

Self-review caught a wording ambiguity in DESIGN: the false rule
delta V=delta G/2 fails the full canonical nonabelian exponential variation,
but can still leave the forbidden WZ slots zero. It must not be described
as necessarily failing that slot-only test. This is distinct from the
wrong-sign and frozen-normal-compensator controls, which DO test forbidden
slots. The original inequality predicate was correct; its scope needed
this explicit qualification.

DESIGN and PROOF now state the distinction. Each algorithm adds a positive
control that the false rule can pass forbidden-slot recovery; focused
tests require both the exact-variation failure AND that surviving property.
Every previous equation, fixture, transformation and criterion remains.
This makes the verifier harder to overread, not the mathematics weaker.

Updated seven-file science envelope is sealed and pushed BEFORE replay.
All first logs remain byte-faithful, with their earlier successful counts.
Outside review and the full physical multiplet/SM/TOE remain unearned.
