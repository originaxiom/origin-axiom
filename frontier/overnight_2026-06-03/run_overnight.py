"""Overnight exploratory queue runner (2026-06-03).

Sequential, per-job HARD timeout (subprocess), continue on error/timeout, gate Job 5
on Job 2 == GO. Writes only inside this directory; commits nothing. One job can never
eat the queue: on timeout/error a status stub is merged into the job's JSON (preserving
any partial state it checkpointed) and the runner moves on.
"""

import json
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOG = HERE / "_run.log"
PY = sys.executable

JOBS = [
    ("run_job1.py", "time_reversal.json",      60 * 60),
    ("run_job2.py", "sl3_apoly_go_nogo.json",  45 * 60),
    ("run_job3.py", "cross_m_silver.json",     60 * 60),
    ("run_job4.py", "sl7_partial.json",        75 * 60),
    ("run_job5.py", "sl3_apoly_full.json",    100 * 60),
]


def log(msg):
    line = f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {msg}"
    print(line, flush=True)
    with open(LOG, "a") as f:
        f.write(line + "\n")


def read_json(p):
    try:
        return json.loads(Path(p).read_text())
    except Exception:
        return None


def merge_stub(out, **kw):
    cur = read_json(out) or {}
    for k, v in kw.items():
        cur.setdefault(k, v)
    cur.update({k: v for k, v in kw.items() if k == "status"})  # always set status
    Path(out).write_text(json.dumps(cur, indent=2, default=str))


def main():
    log(f"=== overnight queue start (python {sys.version.split()[0]}) ===")
    for script, outname, timeout in JOBS:
        out = HERE / outname
        if script == "run_job5.py":
            go = read_json(HERE / "sl3_apoly_go_nogo.json") or {}
            if go.get("verdict") != "GO":
                out.write_text(json.dumps(
                    {"skipped": "Job 2 not GO", "job2_verdict": go.get("verdict"),
                     "job2_nullity_summary": go.get("nullity_summary")}, indent=2, default=str))
                log(f"SKIP {script}: Job 2 verdict = {go.get('verdict')} (gate requires GO)")
                continue
        log(f"START {script} (timeout {timeout // 60} min)")
        t0 = time.time()
        try:
            r = subprocess.run([PY, str(HERE / script)], cwd=str(HERE),
                               timeout=timeout, capture_output=True, text=True)
            dt = time.time() - t0
            if r.returncode == 0:
                log(f"DONE  {script} in {dt:.0f}s  | {(r.stdout or '').strip().splitlines()[-1] if r.stdout.strip() else 'ok'}")
            else:
                log(f"ERROR {script} exit {r.returncode} in {dt:.0f}s | {(r.stderr or '')[-200:].strip()}")
                merge_stub(out, status="error", exit_code=r.returncode,
                           stderr_tail=(r.stderr or "")[-1500:])
        except subprocess.TimeoutExpired:
            dt = time.time() - t0
            log(f"TIMEOUT {script} after {dt:.0f}s (limit {timeout}s)")
            merge_stub(out, status="timeout", timeout_seconds=timeout)
        except Exception as e:
            dt = time.time() - t0
            log(f"RUNNER-EXC {script} after {dt:.0f}s: {e!r}")
            merge_stub(out, status="runner_exception", error=repr(e))
    log("=== overnight queue done ===")


if __name__ == "__main__":
    main()
