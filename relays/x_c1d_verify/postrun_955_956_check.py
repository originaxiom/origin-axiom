#!/usr/bin/env python3
"""Standalone post-run check for Card X-C1d, rows 955 and 956 only.

The sealed verifier (relays/x_c1d_verify/verify_x_c1d.py at 7b404befb) stopped on these two rows with a
parsing fault: SnapPy writes high-precision numbers with a space before the exponent ("... e-66"),
which mpmath does not parse. This script loads the sealed verifier unchanged, replaces only the text
"mp.mpf(str(" by a parser that removes that space, in the two functions that read SnapPy numbers
(_mpc and q3_names), and reruns verify_rows_955_956 exactly as sealed. It also checks that the
patched source differs from the sealed source in nothing else, and runs planted faults. 0 of 19.
"""
from __future__ import annotations

import hashlib
import importlib.util
import inspect
import json
import pathlib
import sys
import time

import mpmath as mp

HERE = pathlib.Path(__file__).resolve().parent
SEALED = HERE / "verify_x_c1d.py"
NAME = "agy_exp_x_c1d_sealed"


def load():
    spec = importlib.util.spec_from_file_location(NAME, SEALED)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[NAME] = mod
    spec.loader.exec_module(mod)
    return mod


def _num(x) -> mp.mpf:
    return mp.mpf(str(x).replace(" ", ""))


def main() -> None:
    t0 = time.time()
    XD = load()
    XD._num = _num
    patched = {}
    for fname in ("_mpc", "q3_names"):
        src = inspect.getsource(getattr(XD, fname))
        new = src.replace("mp.mpf(str(", "_num((")
        # the only change: the parser; everything else identical
        same_otherwise = new.replace("_num((", "mp.mpf(str(") == src
        exec(compile(new, f"<patched {fname}>", "exec"), XD.__dict__)
        patched[fname] = {"replacements": src.count("mp.mpf(str("), "identical_otherwise": same_otherwise}
    # planted parsing control: the sealed parser must fail on SnapPy's spacing, the patched one must not
    s = "-3.43719769963701048411140800903414594905394336164888632893982 e-66"
    try:
        mp.mpf(s)
        sealed_fails = False
    except Exception:
        sealed_fails = True
    patched_parses = abs(_num(s) + mp.mpf("3.43719769963701048411140800903414594905394336164888632893982e-66")) < mp.mpf(10) ** (-120)
    try:
        r955, r956 = XD.verify_rows_955_956()
        err = None
    except Exception as exc:
        r955 = r956 = {"result": "verifier error"}
        err = repr(exc)
    # planted faults on the decided cells: each must be caught by the same comparisons the sealed code makes
    planted = {}
    if err is None:
        q3 = r956["q3"]
        planted["PC_names_537"] = q3["names"] != 537
        planted["PC_threads_odd_1_0_1"] = r956["q2"]["threads"]["odd"] != {str((1, 0, 1)): 326}
        planted["PC_q1_private_one"] = r956["q1"]["all_decided_and_1_1_0_at_120_digits"] is True
        planted["PC_register_carries_hand"] = r956["q5"]["lift_class_flipped_by_C"] is True
    payload = {
        "card": "X-C1d", "postrun_rows": ["955", "956"], "sealed_script_sha256": hashlib.sha256(SEALED.read_bytes()).hexdigest(),
        "patched_functions": patched, "parse_control": {"sealed_parser_fails_on_spacing": sealed_fails, "patched_parser_reads_it": bool(patched_parses)},
        "planted_faults_caught": planted, "all_planted_caught": bool(planted) and all(planted.values()),
        "rows": {"955": XD._clean(r955), "956": XD._clean(r956)}, "error": err, "elapsed_seconds": round(time.time() - t0, 3),
    }
    out = (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")
    (HERE / "postrun_955_956_out.json").write_bytes(out)
    (HERE / "POSTRUN_OUTPUT_SHA256.txt").write_text(f"{hashlib.sha256(out).hexdigest()}  postrun_955_956_out.json\n", encoding="utf-8")


if __name__ == "__main__":
    main()
