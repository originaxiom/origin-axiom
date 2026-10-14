# Local pre-execution seal, remote publication delayed

The exact source/criteria/hash ledger were committed at
9d234b06850633abfa04a8b9d96aec7adbeeb480 BEFORE the first scientific
import/execution. INPUTS pins match before and after both first runs.
No scientific source or criterion was changed after those outcomes.

However, the attempted pre-execution push failed with exit1:

    error: RPC failed; HTTP 408 curl 22 The requested URL returned error: 408
    send-pack: unexpected disconnect while reading sideband packet
    fatal: the remote end hung up unexpectedly
    Everything up-to-date

The server read still showed a3e744d99b4a7247c33fb2b5412dc92e39f3e75b.
The scientific run had already been launched before these yielded
results were observed. This is a sequencing error: the intended
server-confirmation gate was not reached before execution. It is NOT
a remotely published preregistration or a push-before-run certificate.
The failed operation is not described as a scientific failure or repaired
by changing the already committed seal.

A later retry, without modifying any scientific files, succeeded and
published a3e744d99..9d234b068 on the same dedicated audit branch.
Remote verification follows that retry. It does not change the initial
timing. The first26/21 PASS outputs and receipt remain byte-faithful.
The valid evidence is a LOCAL COMMITTED pre-execution seal plus disclosed
post-execution remote publication. No blind/outside acceptance is claimed.

Future runs that require pre-execution remote publication must wait for
the push's actual terminal success AND completed server read, not merely
start those operations. Frozen first results are preserved, not replaced
by a rerun presented as the first execution.
