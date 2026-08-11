"""B1035 — the shadow library, and the orphaned core.

The code sweep's second return. Three sweeps over frontier/ (1,686 .py files) produced one
correction to a premise this refresh had been carrying, one measured adoption debt, and one
methodological finding about independence between arcs.

Everything is counted here, not quoted from a report. Counts are DISTINCT FILES (rg -l style),
never match counts.
"""
import json
import os
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[2]
SELF = "B1035"
R = {"checks": {}}


def chk(name, ok, **d):
    R["checks"][name] = {"pass": bool(ok), **d}
    return ok


def py_files(sub="frontier"):
    out = []
    for dirpath, _, names in os.walk(ROOT / sub):
        for n in names:
            if n.endswith(".py"):
                out.append(pathlib.Path(dirpath) / n)
    return out


FRONTIER = py_files()
# This arc's own files are excluded from every count. EIGHTH instance of one hazard in seven arcs
# — and the first predicted in advance: verify.py imports origin_axiom to check the core, which
# would have made it the 7th importer of the thing whose 6 importers are the finding.
OTHERS = [p for p in FRONTIER if SELF not in str(p)]


def files_matching(pattern, paths=None, flags=0):
    rx = re.compile(pattern, flags)
    hits = []
    for p in (paths if paths is not None else OTHERS):
        try:
            if rx.search(p.read_text(encoding="utf-8", errors="ignore")):
                hits.append(p)
        except OSError:
            continue
    return hits


chk("the_frontier_is_the_size_the_sweeps_reported", len(FRONTIER) > 1600, n=len(FRONTIER))

# ---------------------------------------------------------- 1. THE SHADOW LIBRARY EXISTS
syspath = files_matching(r"sys\.path")
chk("hundreds_of_frontier_files_manipulate_sys_path", len(syspath) > 200, n=len(syspath))

HUBS = {"cyclo_engine": "frontier/B358_seam_certification/cyclo_engine.py",
        "step0_exact_matrices": "frontier/B367_value_map/step0_exact_matrices.py"}
hub_counts = {}
for name, path in HUBS.items():
    hub_counts[name] = {"importers": len(files_matching(re.escape(name))),
                        "exists": (ROOT / path).is_file(), "path": path}
chk("two_arc_directories_are_load_bearing_infrastructure",
    all(v["exists"] for v in hub_counts.values())
    and hub_counts["cyclo_engine"]["importers"] > 40
    and hub_counts["step0_exact_matrices"]["importers"] > 30,
    hubs=hub_counts)

# They are filed as ordinary research arcs — each carries a verdict like any other cell.
chk("and_both_are_filed_as_ordinary_research_arcs",
    (ROOT / "frontier/B358_seam_certification/arc_verdict.json").is_file()
    and (ROOT / "frontier/B367_value_map/arc_verdict.json").is_file())

# ------------------------------------------------------------ 2. THE CERTIFIED CORE IS ORPHANED
core_importers = files_matching(r"(?:^|\s)(?:import|from)\s+origin_axiom")
core_names = sorted(p.relative_to(ROOT).parts[1] for p in core_importers)
chk("almost_nothing_imports_the_certified_core",
    len(core_importers) < 10, n=len(core_importers), arcs=core_names)
# ...and its consumers are the FIVE ORIGINAL PROBES. Nothing since B9 until B1034.
chk("its_only_consumers_are_the_original_probes_and_one_new_arc",
    all(re.match(r"B[159]_|B[68]_|B1034_", a) for a in core_names), arcs=core_names)

LRA = r"\[\[1, ?1\], ?\[0, ?1\]\]|\[\[1, ?0\], ?\[1, ?1\]\]|\[\[2, ?1\], ?\[1, ?1\]\]"
redefiners = files_matching(LRA)
overlap = [p for p in redefiners if p in set(core_importers)]
chk("the_founding_matrices_are_redefined_inline_in_hundreds_of_files",
    len(redefiners) > 150, n=len(redefiners))
chk("and_NOT_ONE_of_them_imports_the_core_that_has_held_them_all_along",
    overlap == [], n_overlap=len(overlap),
    core_has_them="src/origin_axiom/algebra.py defines L, R, A = L*R")

# The core really does define them — this is adoption debt, not missing code.
alg = (ROOT / "src/origin_axiom/algebra.py").read_text(encoding="utf-8")
chk("the_core_defines_L_R_and_A", all(s in alg for s in ("L = sp.Matrix", "R = sp.Matrix",
                                                         "A = L * R")))

# ------------------------------------------- 3. THE TRACE MAP HAS NO CANONICAL HOME ANYWHERE
TM = r"x\*z ?- ?y|2\*x\*z ?- ?y|Fricke|Vogt"
tm_frontier = files_matching(TM)
tm_src = files_matching(TM, paths=py_files("src"))
chk("the_trace_map_is_re_derived_across_the_corpus", len(tm_frontier) > 50, n=len(tm_frontier))
chk("and_it_has_NO_home_in_the_certified_core", tm_src == [], n_src=len(tm_src))

# --------------------- 4. SHARED KERNELS WEAKEN THE INDEPENDENCE OF "INDEPENDENT" ARCS
def defs(path):
    try:
        src = (ROOT / path).read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return {}
    out, cur, buf = {}, None, []
    for ln in src.splitlines():
        m = re.match(r"def (\w+)\(", ln)
        if m:
            if cur:
                out[cur] = "\n".join(buf)
            cur, buf = m.group(1), [ln]
        elif cur is not None:
            buf.append(ln)
    if cur:
        out[cur] = "\n".join(buf)
    return out


PAIR = ("frontier/B930_overlap_matrix/overlap.py", "frontier/B935_composition_hunt/compose.py")
a, b = defs(PAIR[0]), defs(PAIR[1])
shared = [k for k in a if k in b and a[k] == b[k] and a[k].count("\n") > 2]
chk("two_arcs_in_the_dense_band_share_a_byte_identical_kernel",
    len(shared) > 30, n_shared_functions=len(shared), pair=list(PAIR),
    shared_lines=sum(a[k].count("\n") + 1 for k in shared))
chk("so_agreement_between_them_is_not_independent_evidence", len(shared) > 30,
    note="a bug in the shared kernel reproduces identically in both rather than being caught "
         "by disagreement")

# ------------------------------------------------------- 5. THE INSTRUMENT INDEX FROZE AT B370
TOOLBOX = (ROOT / "docs/TOOLBOX.md").read_text(encoding="utf-8")
tb_max = max(int(x[1:]) for x in re.findall(r"\bB\d+\b", TOOLBOX))
chk("the_toolbox_index_stops_far_short_of_the_corpus", tb_max < 500, highest_arc_cited=tb_max)
chk("and_it_omits_the_repos_most_precise_instrument",
    "branch_cell9" not in TOOLBOX and "B878" not in TOOLBOX)
chk("while_that_instrument_is_real_and_on_main",
    (ROOT / "frontier/B878_maass_upper_window/branch_cell9_rung1_v2.py").is_file())

# ------------- 6. A NON-FINDING, RECORDED SO THE NEXT GREP DOES NOT RE-RAISE IT
unresolvable = files_matching(r"sys\.path\.insert\([^)]*(?:/Users/|<seat-workdir>)")
harvest_arcs = sorted({p.relative_to(ROOT).parts[1] for p in unresolvable})
chk("some_files_carry_sys_path_inserts_that_cannot_resolve_here",
    len(unresolvable) > 20, n=len(unresolvable), arcs=harvest_arcs)
chk("BUT_they_are_all_inside_verbatim_preserved_harvest_packets",
    all(re.match(r"B(646|651|656|663|670)_", x) for x in harvest_arcs), arcs=harvest_arcs)
b646 = (ROOT / "frontier/B646_wave2_integration/FINDINGS.md").read_text(encoding="utf-8")
chk("and_the_harvest_arc_states_the_policy_and_how_it_reran_them",
    "ORIGINALS_MANIFEST.txt = sha256 of every" in b646
    and "their pipeline, packet-local imports" in b646)
chk("SO_THIS_IS_NOT_A_DEFECT__recorded_to_stop_the_next_sweep_reflagging_it", True,
    reason="the packets are hash-manifested as received; editing the paths would break the "
           "manifest, and the reruns were done with packet-local imports")

R["numbers"] = {
    "frontier_py_files": len(FRONTIER),
    "sys_path_manipulators": len(syspath),
    "hub_importers": {k: v["importers"] for k, v in hub_counts.items()},
    "core_importers": len(core_importers), "core_importer_arcs": core_names,
    "inline_LRA_redefiners": len(redefiners), "of_which_import_the_core": len(overlap),
    "trace_map_files": len(tm_frontier), "trace_map_in_src": len(tm_src),
    "toolbox_highest_arc": tb_max,
    "unresolvable_syspath_files": len(unresolvable), "harvest_arcs": harvest_arcs,
}
R["all_pass"] = all(v["pass"] for v in R["checks"].values())

if __name__ == "__main__":
    (pathlib.Path(__file__).parent / "results.json").write_text(
        json.dumps(R, indent=1, ensure_ascii=False))
    for k, v in R["checks"].items():
        print(("PASS " if v["pass"] else "FAIL ") + k)
    print("\nALL PASS:", R["all_pass"])
