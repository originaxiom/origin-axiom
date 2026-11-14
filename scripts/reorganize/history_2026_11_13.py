"""The third physical move under GOVERNANCE section 12 (docs/REORGANIZATIONS.md, its third entry): the record's
historical folders move under docs/archive/, and ten copies of notes between sessions kept inside arcs' folders and in
outside_bench/ leave the tree, 2026-11-13. The building session's card C18, approved by main (its M28 to the builder).

Moved, each with its name: legacy/, story/, paths/, speculations/ and philosophy/, to docs/archive/<name>/. The foundation's
three paths into philosophy/ change by a version of the foundation (1.68), written by its own script in the same patch.
Removed: ten copies of notes between sessions; git's history keeps them, and the last commit that holds every moved and
removed file at its old path is LAST. The living pages of LIVING have
their paths into the moved folders written again. Kept where it is: outside_bench/ (side work, read by four checks of the harvest),
knowledge/, core/, src/, packaging/.

    python3 scripts/reorganize/history_2026_11_13.py          # make the move, once
    python3 scripts/reorganize/history_2026_11_13.py --check  # say whether the tree is as the move leaves it"""
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
LAST = "fe146ca49b090f1e55dbc845c31f049073adec1e"
MOVES = [(d + "/", "docs/archive/" + d + "/") for d in ("legacy", "story", "paths", "speculations", "philosophy")]
REMOVE = (
    "frontier/B702_metallic_hearing_law/CC2_TO_CC_2026-07-19_EQ_results.md",
    "frontier/B1297_the_spectral_cover_index/CC_TO_ALL_SEATS_2026-09-08_HARVEST_NUMBERING.md",
    "frontier/B1303_the_sm_closings_z_prime/CC_TO_CHAT1_2026-09-08_B1303_DISPOSITIONS_HELD.md",
    "frontier/B1303_the_sm_closings_z_prime/CHAT1_TO_CC_2026-09-08_SESSION_RELAY.md",
    "frontier/B1305_the_cloud_156_178/CC_TO_CLOUD_2026-09-08_Q1_ANSWERED_AND_SHARPENED_HELD.md",
    "frontier/B1306_the_older_debt/CC_TO_CHAT1_2026-09-09_HANDOFF_BANKED_HELD.md",
    "frontier/B1306_the_older_debt/CC_TO_SM_2026-09-09_THE_TOWER_HARVESTED_AND_THE_RANGES_HELD.md",
    "frontier/B1306_the_older_debt/inputs/chat1_handoff_2026-09-08/CHAT1_TO_CC_2026-09-08_HANDOFF_ARROW_CHIRALITY.md",
    "frontier/B1454_genesis_v1_verified_and_adopted/received/SM_TO_CC_2026-10-02_GENESIS_V1.md",
    "outside_bench/CLOUD_TO_CC_2026-09-08_Q1_THE_QUANTUM_FACE.md",
)


# The living pages whose paths into the moved folders are written again (dated records, ledgers and the foundation's
# version log keep theirs; the foundation's own paths change by its version 1.68, B1930). Only a path that names a file now
# under docs/archive/ is written again
# (a folder's bare name only in backticks).
LIVING = ("ARCHITECTURE.md", "CLAIMS.md", "GOVERNANCE.md", "METHOD.md", "PROVENANCE.md", "REPRODUCIBILITY.md", "ROADMAP.md",
          "WORKING_RULES.md", "docs/ARCHIVE.md", "docs/BANKING_PROTOCOL.md", "docs/INDEX.md", "docs/PRACTICES.md", "docs/THE_BAR.md",
          "docs/THE_COMPLETION_MAP.md", "docs/THE_PROGRAMME_IN_SHORT.md", "docs/atlas/AUDITOR_GUIDE.md", "docs/atlas/FAILURE_ATLAS.md",
          "docs/atlas/GLOSSARY.md", "docs/atlas/INTEGRATION_MANIFEST.md", "docs/atlas/README.md", "docs/atlas/RESEARCH_TREE.md",
          "docs/atlas/SUCCESS_ATLAS.md")
OLD_PATH = re.compile(r"(?<![\w/.-])((?:legacy|story|paths|speculations|philosophy)/[\w./-]*)")


def references(text):
    """the paths of a page that name a moved file or folder at its old place, and the text with each written again"""
    found = []

    def again(m):
        old = m.group(1).rstrip(".")
        if old.endswith("/") and not (m.start() and m.string[m.start() - 1] == "`"):
            return m.group(1)              # a folder's bare name in prose is a word of the text; in backticks it is a path
        if (ROOT / "docs" / "archive" / old).exists():
            found.append(old)
            return "docs/archive/" + m.group(1)
        return m.group(1)
    return found, OLD_PATH.sub(again, text)


def git(*a):
    return subprocess.run(["git", "-C", str(ROOT), *a], check=True, capture_output=True, text=True).stdout


def tracked(prefix, rev=None):
    args = ["ls-tree", "-r", "--name-only", rev, "--", prefix] if rev else ["ls-files", "--", prefix]
    return [p for p in git(*args).split("\n") if p]


def check():
    bad = []
    for old, new in MOVES:
        if tracked(old):
            bad.append("still at its old place: " + old)
        if not tracked(new):
            bad.append("not at its new place: " + new)
        elif sorted(p[len(new):] for p in tracked(new)) != sorted(p[len(old):] for p in tracked(old, LAST)):
            bad.append("the files under %s are not those of %s at %s" % (new, old, LAST[:9]))
    bad += ["still in the tree: " + p for p in REMOVE if tracked(p)]
    for page in LIVING:
        found, _ = references((ROOT / page).read_text(encoding="utf-8"))
        bad += ["%s names %s at its old place" % (page, f) for f in found]
    return bad


if __name__ == "__main__":
    if "--check" in sys.argv:
        bad = check()
        print("as moved" if not bad else "not as moved: %d, e.g. %s" % (len(bad), bad[:3]))
        sys.exit(1 if bad else 0)
    for old, new in MOVES:
        if tracked(old):
            (ROOT / new).parent.mkdir(parents=True, exist_ok=True)
            git("mv", old.rstrip("/"), new.rstrip("/"))
    rm = [p for p in REMOVE if tracked(p)]
    if rm:
        git("rm", "-q", "--", *rm)
    written = 0
    for page in LIVING:
        found, new = references((ROOT / page).read_text(encoding="utf-8"))
        if found:
            (ROOT / page).write_text(new, encoding="utf-8"); written += len(found)
    bad = check()
    print("moved %d folders; removed %d files; wrote %d paths of living pages again; %s" % (len(MOVES), len(rm), written,
          "as moved" if not bad else "INCOMPLETE: %s" % bad[:3]))
    sys.exit(1 if bad else 0)
