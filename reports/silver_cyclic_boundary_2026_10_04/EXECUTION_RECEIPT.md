# Execution receipt

Scientific seal: e20efaee7d769192c442154d27f6759aada6691e, committed
locally before first import or execution. Runtime: Python 3.12.1,
SymPy 1.14.0, LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1. All six sealed
hashes remain unchanged after native and test runs.

| Capture | Outcome |
|---|---|
| NATIVE_FIRST.jsonl | Exit 0; four candidates, both amplitudes; controls pass |
| READOUT_FIRST.jsonl | Exit 0; 19 cases, all 16 diagnostic predicates hold |
| FOCUSED_FIRST.txt | Exit 2; duplicate test_verify module names at collection |
| FOCUSED_SECOND.txt | Exit 0; 10 passed in 206.57 seconds |

The rerun added `--import-mode=importlib` to `python3.12 -m pytest -q`,
targeting this packet's test_verify.py and the variation packet's
test_verify.py. No source, criterion, expected value or test changed.
The raw collection failure is retained locally byte-for-byte, ignored
for path privacy. Its committed display copy redacts only the absolute
workspace prefix and is not represented as raw bytes.

Raw capture hashes:

    a916237c62b052423386b393c31f7342e92fe33d0b4f487b48b119fd59625d4b NATIVE_FIRST.jsonl
    ac3de5348ea2946924b0da4e88fe26560a64022ada32db23dc42d8ccfa9b1d76 READOUT_FIRST.jsonl
    3fa87c7fb18aaf9f27f44addbe9a500a097dc37c02fdea930fe3cdd1ab173b72 FOCUSED_FIRST.txt
    5571d55f33f1662035c27c3e7983ca49f4df9fdfec1db7a33c8b97cf79b4f235 FOCUSED_SECOND.txt

A pre-seal checksum command failed on the inherited locale; LC_ALL=C
fixed it before any manifest was authored. Two later tail requests used
an incorrect relative path; the actual log was then read. Neither was
scientific evidence. No native scientific failure occurred. Both first
science captures are complete files. The tree was read-only during runs.

Fetch used a command-local HTTPS rewrite; no saved Git configuration
changed. All eight live heads were server-confirmed. The unrelated
parent-mirror folder was untouched. Focused verification is not full-suite
certification. No push, merge or main banking is claimed.
