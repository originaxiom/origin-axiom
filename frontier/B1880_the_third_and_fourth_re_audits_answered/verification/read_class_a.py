"""B1880 -- the seven files under lists with other names whose sealed content was on main and has changed since: what changed.

A mechanical reading, not a judgement by eye: each file is compared with the version that had the recorded hash, after the
substitutions that a path repair and the attribution rule's redaction make.  If the two are then equal, nothing but a path or
a redacted name changed.  Reads all_hash_lists.json (written by measure_all_hash_lists.py) and the commit graph.
"""
import difflib
import importlib.util
import json
import pathlib
import re
import sys
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
HERE = pathlib.Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("gates_b1880_read", ROOT / "scripts" / "gates" / "gates.py")
G = importlib.util.module_from_spec(spec)
spec.loader.exec_module(G)

HOME = "/" + "Users" + "/" + r"[A-Za-z0-9_]+" + "/"                     # a local home folder, spelt in pieces
REPO_DIR = HOME + r"origin-axiom"
SEAT_DIR = HOME + r"oa-seat-[a-z0-9]+"


def norm(text):
    out = []
    for line in text.split("\n"):
        st = line.strip()
        if st == "import os" or st.startswith("_REPO = "):
            continue                                                   # the two lines a path repair adds
        line = re.sub(r"_REPO \+ (['\"])", r"\1<repo>", line)             # the repaired form ...
        line = re.sub(r"(['\"])" + REPO_DIR, r"\1<repo>", line)           # ... and the form it replaced
        line = re.sub(REPO_DIR, "<repo>", line)
        line = re.sub(SEAT_DIR, "<seat>", line)
        line = re.sub(HOME, "", line)                                   # a local home folder dropped from a path
        line = line.replace("<cc2-seat>", "<seat>").replace("[machine-path]", "<seat>")     # the two placeholders the redactions wrote
        line = G._VENDOR_RE.sub("[redacted-model]", line)
        line = re.sub(r"\[redacted-model\]-\d+", "[redacted-model]", line)
        line = re.sub(r'("model":\s*)"[^"]*"', r'\1"<a model name>"', line)
        out.append(line)
    return "\n".join(out)


def main():
    data = json.loads((HERE / "all_hash_lists.json").read_text(encoding="utf-8"))
    rows, out = data["other_names_not_verifying"]["class_A"] + data["other_names_not_verifying"]["class_B"], []
    P = lambda *a: (out.append(" ".join(str(x) for x in a)), print(*a))
    P("THE FILES OF CLASSES A AND B UNDER LISTS WITH OTHER NAMES (SEVEN AND TWO): THE SEALED VERSION AGAINST TODAY'S")
    equal = 0
    for r in rows:
        path, c = r["file"], r["sealed_content_last_at"]
        old = subprocess.run(["git", "-C", str(ROOT), "show", f"{c}:{path}"], capture_output=True, text=True).stdout
        new = (ROOT / path).read_text(encoding="utf-8", errors="replace")
        d = [l for l in difflib.unified_diff(old.split("\n"), new.split("\n"), lineterm="", n=0) if l[:1] in "+-" and l[:3] not in ("+++", "---")]
        changed = "-%d +%d" % (sum(l[0] == "-" for l in d), sum(l[0] == "+" for l in d))
        commits = subprocess.run(["git", "-C", str(ROOT), "log", "--format=%h %cs", f"{c}..HEAD", "--", path], capture_output=True, text=True).stdout.split("\n")
        same = norm(old) == norm(new)
        equal += same
        P("  %s" % path)
        P("     sealed content last at %s (%s); changed by %s; lines removed and added %s; equal after the path and attribution substitutions: %s" % (
            c, r["date"], ", ".join(x for x in commits if x), changed, same))
    P("")
    P("files: %d; equal to their sealed version after the substitutions: %d" % (len(rows), equal))
    if equal == len(rows):
        P("so in none of them did a line of mathematics, a threshold or a datum change: a local path was made relative, or a name was redacted.")
    else:
        P("NOT ALL EQUAL: the files that differ beyond a path or a redacted name are to be read by hand.")
    # CORRECTED 2026-11-12 (Review 79's second round).  This line wrote the tracked run file at every call, and the arc's lock
    # calls main() at every test run: a run of the suite rewrote a tracked file, with lines of git's log in it that move when
    # any of the nine files is touched.  It is written only when asked for now.
    if "--write" in sys.argv:
        (HERE / "read_class_a_run.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    return equal == len(rows)


if __name__ == "__main__":
    raise SystemExit(0 if main() else 1)
