# Preserved timeout and exact phase-algebra performance repair

First seal67fdfb45e624acddf2855e54e73b49f747c82c67 was pushed and
server-confirmed before first execution. Native reached the declared
1200-second limit: exit124,1200.027036601s, stdout/stderr both zero
bytes. Reference was correctly NOT launched. First-run RECEIPT and all
38 pinned source snapshots are retained verbatim.12,948 tracked files,
all38pins and index unchanged; fingerprint
f372b4efc542b16f412a7bd9629951481473d38ff76242cbd67499a7bd7e39d8.
This is an INCOMPLETE COMPUTATION, not a mathematical negative or pass.

A one-second external process profile showed active Python arithmetic,
not an idle external wait. It does not identify the precise expression
or prove a specific simplifier defect. Repeated generic complex/trig
simplification is a plausible cost; the first instrument supplied no
intermediate stage log, so do not claim that diagnosis as established.

Repair BEFORE rerun: reduce the declared half-integral theta harmonics
as rational Laurent functions of formal nonzero t=exp(i theta/2).
sin(a theta+b)=(exp(ib)t^(2a)-exp(-ib)t^(-2a))/(2i), similarly cos.
Exact rational cancellation tests all theta, NOT one angle or a grid.
The phase is substituted back before later derivatives/monodromy checks.
Any unexpected harmonic raises instead of being silently projected out.
Other independent constant-angle trig identities remain symbolic.

Add three two-sided instrument checks: the universal circle identity,
sin(theta) nonidentity DESPITE vanishing at theta0, and preservation of
half-monodromy/derivative. Add flushed per-check diagnostic stderr lines
so any later incomplete run retains completed stages. Nonempty stderr
is therefore expected diagnostics, not an error or a hidden clean run.

No old mathematical criterion, field, sign, parameter, angle quantifier,
local/global scope, source-action fence or positive/negative comparator
is weakened. No earlier partial assertion is banked. Proof unchanged.
SOURCE_CHECK adds the independently viewed PDF/HTML equation-label map,
not altered source coefficients. Renew manifest/ledger, commit/push and
terminal server-confirm BEFORE a new result leaf is executed. This is
an explicitly post-timeout instrument repair, not original preregistration.
