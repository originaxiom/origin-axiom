# Later publication precheck and auxiliary reader correction

The staged publication subsequently committed as 1a2f0dbcd received
the ordinary full governance precheck: exit one after 37.991668
seconds, 29 PASS and the unchanged seal-provenance FAIL. All 643
unresolved paths remain, including five explicit historical violations.
The complete local before/after inventories contain 18,347 files and
the original nine source pins; their bytes are identical, SHA256
1e7b0e1ea3a48971d26a7fcb2a1983fbab019606ebd404f4f0314711d871b0c7.
The staged index SHA256 is
f357434f10e9c7f333e735a2ff8e38954e788cd87c1f33e2175e9b6578555614.
Full original captures remain in the persistent task workspace under
the prospective-publication before, governance and after stems. These
are separate from the published 472be2a2a test envelope.

An auxiliary one-off report reader initially failed on a US-ASCII
regular-expression scan of the UTF-8 governance log. The tool reported
ArgumentError, invalid byte sequence in US-ASCII, exit one. Commit
and push were separate tool calls and still proceeded; the reader's
failure must not be described as a passing precommit check. The full
governance process and before/after captures had already completed.
The corrected reader used explicit UTF-8, exited zero and confirmed
29 PASS, one FAIL, 562 unclassified entries, 76 missing-field design
candidates and five historical violations, plus the unchanged envelope.
This happened after commit, not retrospectively before it.

This is a faithful note of the tool-observed reader failure and its
timing, not a reconstructed original process log or a new receipt.
Future orchestration must stop dependent publication calls on a failed
validation result. No scientific source, original captured output or
governance criterion was changed by this correction.
