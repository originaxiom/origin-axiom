"""Inventory committed artifacts only; never import or run scientific sources."""

import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[3]
PREFIX = "reports/physical_bridge_2026_09_05/"
TARGET = "8d5c9103272393ccf1bdc0c3a7fd5a8a054f5bb3"
MAIN = "5dec726d6468b0834f3fcdbb4650195e57bbfc42"
HERE = Path(__file__).resolve().parent


def git(*arguments):
    return subprocess.check_output(["git", *arguments], cwd=ROOT)


def content(path):
    return git("show", TARGET + ":" + path)


def category(path, data):
    name = Path(path).name
    if not data:
        return "empty preserved stream"
    if name in {"independent_checks.py", "check_boundary_law.py", "checks.py"}:
        return "mathematical checker source"
    if name == "result.json":
        return "historical mathematical output"
    if name in {"engineering_checks.py", "run_checks.py"}:
        return "execution infrastructure source"
    if "/engineering_results/" in path:
        return "engineering-only receipt or output"
    if name == "collect_source_metadata.py":
        return "custody-only source"
    if name == "OWN_GRAM_CHECK_REPAIR.diff":
        return "proposed unexecuted checker repair"
    return "provenance, specification, or source-quotation metadata"


def main():
    initial = json.loads(content(PREFIX + "all_seats_dependency_plan_2026_11_17/"
                                 "M7_NON_MARKDOWN_INTAKE.json"))
    original = {item["path"] for item in initial["candidates"]}
    changed = git("diff", "--name-only", "1aa76251", TARGET,
                  "--", "reports/physical_bridge_2026_09_05", "relays").decode().splitlines()
    paths = sorted(p for p in changed if not p.endswith(".md"))
    missing_original = sorted(original - set(paths))
    if missing_original:
        raise ValueError("Previously listed paths disappeared: " + repr(missing_original))
    register = json.loads(git("show", MAIN + ":frontier/B1957_the_seats_claims_register/"
                             "verification/UNITS.json"))
    entries = []
    for path in paths:
        data = content(path)
        item = {"path": path, "bytes": len(data), "lines": len(data.splitlines()),
                "sha256": hashlib.sha256(data).hexdigest(),
                "category": category(path, data), "in_original_intake": path in original}
        if path.endswith(".json"):
            obj = json.loads(data)
            item["json_shape"] = list(obj) if isinstance(obj, dict) else {"list_length": len(obj)}
        if path.endswith(".py"):
            tree = ast.parse(data, filename=path)
            item["top_level_functions"] = [n.name for n in tree.body if isinstance(n, ast.FunctionDef)]
            item["test_methods"] = [c.name + "." + n.name for c in tree.body
                                    if isinstance(c, ast.ClassDef) for n in c.body
                                    if isinstance(n, ast.FunctionDef) and n.name.startswith("test_")]
        entries.append(item)
    output_checks = []
    for folder, checker in (("agy_exp_endgame_review_2026_11_15", "independent_checks.py"),
                            ("relative_register_boundary_law_2026_11_15", "check_boundary_law.py")):
        base = PREFIX + folder + "/"
        result = json.loads(content(base + "run01/result.json"))
        observed = hashlib.sha256(content(base + checker)).hexdigest()
        output_checks.append({"output": base + "run01/result.json",
                              "source_sha256_matches": result["source_sha256"] == observed,
                              "recorded_completed": result["completed"],
                              "recorded_groups": list(result["checks"]),
                              "execution_in_this_collection": False})
    result = {
        "method": "Git blob inventory, JSON reading and AST inspection only; no scientific execution",
        "base": "1aa76251", "source_head": TARGET, "main_register_head": MAIN,
        "original_candidates": len(original), "expanded_candidates": len(entries),
        "new_paths": sorted(set(paths) - original),
        "counts_by_category": dict(Counter(e["category"] for e in entries)),
        "historical_output_source_identity": output_checks,
        "registered_companion_files": [f for f in register["files"] if f["lane"] == "physical"
                                        and any(s in f["file"] for s in
                                                ("agy_exp_endgame_review_2026_11_15/REVIEW.md",
                                                 "relative_register_boundary_law_2026_11_15/FINDINGS.md",
                                                 "registered_domain_index_join_2026_11_16/PROOF.md",
                                                 "registered_domain_index_join_2026_11_16/ACTUAL_SLOT_VERTEX_AND_HIGHER_MASS.md",
                                                 "registered_domain_index_join_2026_11_16/NORMALIZED_WILSON_CROSSING_VERTEX.md",
                                                 "registered_domain_index_join_2026_11_16/verification/DESIGN.md"))],
        "limits": "Inventory and coverage, not independent acceptance; quotation metadata retains its original reading limits",
        "entries": entries,
    }
    (HERE / "NON_MARKDOWN_COVERAGE.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: result[k] for k in ("expanded_candidates", "counts_by_category",
                                            "historical_output_source_identity")}, indent=2))


if __name__ == "__main__":
    main()
