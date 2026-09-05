# Failures retained, not rewritten as successful runs

## B1098 live-test loader

The original test failed before checking the triple because the executed
certificate prefix lacked `__file__`. The failure and original source hash
are in EXTENSION_1.md. The corrected loader, with unchanged mathematical
assertions, passed in the combined run: **27 passed in 40.76 s**.

## R3 first execution: output serialization, not a model verdict

Instrument sealed at commit `c9a7ad69`; `mass_match.py` SHA-256
`f73d07ef7df14c2111283bf04d05d669351ac786750127e9597dc45b12b1c56e`.
The mathematical checks ran, but serializing a NumPy boolean failed:

```text
  File "mass_match.py", line 189, in main
    json.dump(result, handle, indent=2, allow_nan=False)
TypeError: Object of type bool is not JSON serializable
```

The original **incomplete** `mass_results_first_run.json` is retained byte for
byte. It is intentionally not valid JSON and is not a successful result.
No numerical verdict is taken from this run.

Post-hoc repair, before the rerun: convert bound results to native floats,
add a JSON round-trip regression, and serialize the entire payload before
opening the destination. The rerun uses a new output name. The pre-repair
source remains in git and both output artifacts remain on disk.
