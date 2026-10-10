# Preserved first native failure and reporting-only repair

Initial seal bc0685973f7557a0ce4d1b05bb7de1f16f1f38c7 was pushed and
server-checked before the first scientific run. The native producer
exited 1 while constructing its output, before its final all-predicates
assertion: sum(facts.values()) attempted to add a SymPy BooleanAtom.

    TypeError: BooleanAtom not allowed in this context.

The original 850-byte traceback is retained unchanged in the durable
local raw capture, sha256
3288fb0d005319c6f56128d7f2c25746c974214d9cdfee1f516135c66c0abf5b,
2.437917 seconds, no signal. This privacy-safe excerpt is NOT the raw
traceback; its private absolute paths are not committed. The initial
producer remains byte-recoverable at bc0685973. No failure was overwritten.

The separate reference exited 0: 23 exact predicates, all sixteen slots.
Raw output: 1629 bytes, sha256
f86cc00bc422e15ba04d085ec2fbb5a1f1f60ee85ca9d2554a8c6f6bf1e11afe,
3.141027 seconds, no signal. This does not certify the native run.

Repair: convert each already-computed exact predicate to Python bool
before counting/JSON serialization. No mathematical expression, source,
component convention, equality, threshold or opposing control changes.
PRESEAL_REPAIR.json fixes the revised producer before the rerun.
Initial PRESEAL.json is retained and never relabeled as the revised hash.
