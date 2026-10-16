# Execution-only successor, before regression collection

The first attempt at published 076b05bef3598a2e2cf5f87db866d14ccdce9a9a
is retained, not replaced. Its selected regression exited 4 during
collection: the chosen runtime could not import SciPy. No selected test
ran. The metadata inventory completed, but its payload INVENTORY.json
collided with capture receipt inventory.json on a case-insensitive
filesystem; the capture wrapper exited 1 without a valid receipt for
that job. The payload is not a process receipt.

BANKED IDENTITY: this is an execution repair of the already-published
maintenance design, not a new scientific design or a changed test.
All sixteen INPUTS.json source pins must still match. The successor
uses an existing Python environment in which metadata lookup locates
SciPy, NumPy, SymPy and pytest. No package is installed, and no tolerance,
producer, expected mathematical result or selection changes.

PRIOR ART: DESIGN.md and INPUTS.json remain byte-identical. The first
attempt's focused, vacuity, relay and governance captures, failed
inventory capture and full metadata payload are retained. Raw originals
and complete before/after tree inventories remain in the private
capture directory; the published custody manifest distinguishes
path-normalized presentations from their original byte hashes.

## Successor and adversarial author review

execute.rb accepts the existing Python executable, a new empty scratch
directory and an already-published, server-confirmed source commit.
It clears the previous dependency overlay, checks all original pins,
checks disjoint output names case-insensitively before any test imports,
records package metadata, and runs the same twelve selected tests and
four diagnostic jobs. The metadata payload now has a distinct name
from every process receipt. Each process's actual exit is preserved;
the full tracked tree, source pins and index must agree before/after.

Author review specifically checks: the old failed attempt cannot be
overwritten; the payload cannot impersonate a receipt; absent SciPy is
not a mathematical failure; an expected failure in the remaining three
governance categories cannot masquerade as an all-green repository;
and package/environment substitution cannot silently alter the sealed
sixteen sources. Tests still have to pass and reject their corrupted
controls. Package versions are recorded, not assumed identical to the
first runtime. This is author review, not non-author acceptance. The
maintenance design has no empirical or phenomenological predicate.

Publish this repair and its instrument, verify the remote head, then
run. The scientific design and original source manifest are not
retroactively resealed. This note is the pre-successor execution
disclosure; no independent, full-suite, recipient or physical acceptance
is claimed. Attribution, provenance typing/history and relay debt remain
open regardless of the selected regression's outcome.
