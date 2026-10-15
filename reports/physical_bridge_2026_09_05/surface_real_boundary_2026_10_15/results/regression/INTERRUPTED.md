# Interrupted validation, not a scientific verdict

The regression started after science checkpoint906ef5866. The invoking
turn was interrupted by the goal-continuation handoff. On resumption
the recorded process handle6834 was missing. A read-only process query
for this packet, its pytest command and parent-dictionary child found
no matching process (exit1, no matches). Thus no live job is being
restarted solely because an observation timed out.

Only before.json exists from the capture. There is no child exit code,
stdout/stderr or after-snapshot to report. The interrupted run is neither
a test pass nor evidence of a mathematical failure. Its original
before.json is preserved unchanged. No science source, test criterion,
input pin or first-science record was changed.

The post-science validation helper now accepts a separately named
capture directory. The SAME nine test files will run under mode
regression into regression_retry, without overwriting this directory.
This is a validation-custody change, not a scientific post-hoc repair.
