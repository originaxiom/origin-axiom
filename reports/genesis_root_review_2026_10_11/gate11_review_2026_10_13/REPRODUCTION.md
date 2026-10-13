# Gate 11 archive review reproduction record

The review used `/Users/dri/.pyenv/versions/3.12.1/bin/python3` in fresh copies under `/private/tmp/oa-gate11-review-Nmb5QHdI`. The original extraction is `/private/tmp/oa-through-gate11-read-qrhkm68c/Origin_Axiom_Banking_Seat_2026_10_13`. No original extracted file changed during replay.

`replay_review_as_executed.py` is the preserved driver as executed, with its original absolute source/scratch paths. SHA256 before execution was `5b67025e18146d35e344d3c82238f4f0f2caffb03e7e938578cf79b565e2c05f`. It copies the selected gate directories, runs their unchanged producers and compares JSON while ignoring only `elapsed_seconds`. It is an execution record, not a location-independent CLI. Reproduction elsewhere requires new source/scratch locations and a separately recorded driver; the original is not overwritten.

The ten producers all exited zero. The strict aggregate comparison exited one because four Gate11 W10 floating residuals differ. They are preserved in the original/replayed JSON and the diff. All Boolean predicates and all other non-timing result fields agree. No second run or relaxed comparator was substituted for the first outcome.

| W10 residual | Archived | Replayed |
| --- | ---: | ---: |
| Based commutator identity | 1.3334236103572998e-15 | 1.3327193038905524e-15 |
| Braid relation | 5.670926147281867e-16 | 8.989550626504553e-16 |
| Delta fourth power minus identity | 9.226380847435024e-16 | 1.5632082117998628e-15 |
| Sign squared minus identity | 2.2610626239330836e-16 | 4.460365043975677e-16 |

The source reference tests each of these against 1e-10. Both sets satisfy that unchanged threshold. They are numerical consistency evidence, not certified intervals. The exact normal-form central signs and extra ruled-metaplectic controls use integer phase/rotation arithmetic.

`REPLAY_RECEIPT.json` contains process exits, timings and source/output hashes. `outputs/` preserves the eleven replayed result JSON files, the archived Gate11 reference comparison, and each producer's first stdout/stderr. `CUSTODY.json` identifies the supplied archive, its eight original package hashes and the older baseline. `REMOTE_HEADS.txt` is a local remote-tracking snapshot after an all-head fetch, using public role aliases under the attribution rule; retained historical refs need not be currently advertised branches.

An initial attempt to run the system `shasum` before execution failed because the inherited C.UTF-8 locale is unsupported by its Perl runtime. Setting LC_ALL=C and LANG=C made the hash command succeed. This was an operational pre-execution failure, not a failed scientific trial. The driver uses that explicit locale for all subprocesses.

The paper used for the unique-continuation check is Sampson, *Some properties and applications of harmonic mappings* (1978), DOI 10.24033/asens.1344. Only the relevant theorem/proof pages212-213 were checked here, including rendered pages; no full-paper reading claim is made. The noncompact theorem statements were checked in Wu-Zhang arXiv2109.01776v1. The external papers and the user's complete attachment are not republished in this packet.

No new scientific producer or existing test was modified. No shared B-number is allocated. Repository-wide gates, full-suite status and independent analytic acceptance are distinct from these successful local replays; publication scope is recorded separately.
