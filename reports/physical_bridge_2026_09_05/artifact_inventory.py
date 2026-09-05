"""Read-only search for the precise evidence paths behind the five suite failures.

Scope: current clone, fetched remote refs, reachable git history at these paths,
and matching basenames in the reachable object listing. Not a claim that no copy
exists in untracked local files, external uploads, or unpublished branches.
"""
import argparse
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[2]


def git(*args):
    return subprocess.run(["git",*args],cwd=ROOT,capture_output=True,text=True,
                          check=True).stdout


def inventory():
    targets = [f"frontier/B1062_bridge_cell/{name}.log" for name in (
        "b1062_v2_block1", "b1062_v2_block3", "b1062_verify_battery",
        "b1062_v2_block2n", "b1062_v1_v3")]
    targets += ["frontier/B1063_refresh_verdict/refresh_windows.log",
                "frontier/B1137_regulator_probe/results/real_grid.jsonl",
                "frontier/B1137_regulator_probe/results/null_grid.jsonl",
                "frontier/B675_hcusp_sweep/ADDENDUM_2026-09-03_B1242.md",
                "frontier/B715_native_gauge/ADDENDUM_2026-09-03_B1242.md"]
    packet = ROOT/"frontier/B646_wave2_integration/cc2_packets"
    expected = {}
    for line in (packet/"ORIGINALS_MANIFEST.txt").read_text().splitlines():
        if line.startswith("#") or not line.strip():
            continue
        sha, rel = line.split(None,1)
        path = packet/rel
        if not path.exists():
            key = str(path.relative_to(ROOT))
            targets.append(key)
            expected[key] = sha
    refs = [line.split(" ",1) for line in git("for-each-ref",
            "--format=%(refname:short) %(objectname)","refs/remotes/origin").splitlines()]
    objects = git("rev-list","--objects","--all").splitlines()
    basename_hits = {}
    names = {Path(path).name for path in targets}
    for line in objects:
        parts = line.split(" ",1)
        if len(parts)==2 and Path(parts[1]).name in names:
            basename_hits.setdefault(Path(parts[1]).name,[]).append(line)
    rows = []
    for path in targets:
        history = git("log","--all","--full-history","--format=%H","--",path).splitlines()
        ignore = subprocess.run(["git","check-ignore","-v","--no-index",path],
                                cwd=ROOT,capture_output=True,text=True)
        if ignore.returncode not in (0,1):
            raise RuntimeError(ignore.stderr)
        rows.append({"path":path, "present_in_worktree":(ROOT/path).exists(),
                     "expected_sha256_if_manifested":expected.get(path),
                     "reachable_history_commits_at_exact_path":history,
                     "reachable_object_listing_basename_hits":basename_hits.get(Path(path).name,[]),
                     "ignore_rule":ignore.stdout.strip() or None})
    return {"main_sha":git("rev-parse","origin/main").strip(), "remote_refs":refs,
            "scope":__doc__.strip(), "targets":rows}


if __name__ == "__main__":
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    if args.output.exists():
        parser.error("choose a new output filename")
    result=inventory()
    payload=json.dumps(result,indent=2)
    with args.output.open("x") as handle:
        handle.write(payload+"\n")
    for row in result["targets"]:
        print(row["path"], "present=",row["present_in_worktree"],
              "exact-history=",len(row["reachable_history_commits_at_exact_path"]),
              "basename-hits=",len(row["reachable_object_listing_basename_hits"]),
              "ignored=",bool(row["ignore_rule"]))
