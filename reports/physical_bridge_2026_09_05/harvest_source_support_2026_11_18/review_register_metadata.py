"""Read fixed Git blobs and check paragraph custody, never mathematical code.

Unit splitting follows the documented register format. Matching its hashes
checks source identity, not independent extraction correctness or proof truth.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
MAIN = "c34a926a2f796dff76f2f781bdf3d69d0fcc0e8f"
SOURCE = "8d5c9103272393ccf1bdc0c3a7fd5a8a054f5bb3"
BASE = "frontier/B1957_the_seats_claims_register/verification/"


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def tag(path):
    parts = path.split("/")
    stem = parts[-1][:-3]
    if parts[0] == "relays" and len(parts) == 2:
        return stem
    return "/".join(parts[1:-1] + [stem]) if parts[0] in ("relays", "reports") else path[:-3]


def paragraphs(text):
    # Custody adaptation of the reviewed extract.py unit format; no imports.
    bullet = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+\S")
    row = re.compile(r"^\s*\|.*\|\s*$")
    sep = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
    current, fenced, out = None, False, {}
    def close():
        nonlocal current
        if current:
            out[current[0]] = re.sub(r"\s+", " ", current[1])
        current = None
    for number, line in enumerate(text.split("\n"), 1):
        if line.strip().startswith("```"):
            fenced = not fenced
            if current:
                current[1] += "\n" + line
            continue
        if fenced:
            if current:
                current[1] += "\n" + line
            continue
        if not line.strip() or line.lstrip().startswith("#") or sep.match(line):
            close()
            continue
        if row.match(line):
            close(); current = [number, line.strip()]; close(); continue
        if bullet.match(line):
            close(); current = [number, line.strip()]; continue
        if current is None:
            current = [number, line.strip()]
        else:
            current[1] += " " + line.strip()
    close()
    return out


def main():
    units = json.loads(git("show", MAIN + ":" + BASE + "UNITS.json"))
    sources = {}
    for item in units["files"]:
        if item["lane"] == "physical":
            text = git("show", SOURCE + ":" + item["file"]).decode()
            sources[tag(item["file"])] = (item["file"], paragraphs(text))
    names = git("ls-tree", "-r", "--name-only", MAIN, BASE + "records/").decode().splitlines()
    verdicts = {}
    for path in names:
        if not path.rsplit("/", 1)[-1].startswith("physical-"):
            continue
        record = json.loads(git("show", MAIN + ":" + path))
        for uid in record.get("units", []):
            prior = verdicts.get(uid)
            if prior and prior[0] != record["verdict"]:
                raise ValueError((uid, prior, record["verdict"]))
            verdicts[uid] = (record["verdict"], record["id"])
    count, mismatches, flags = 0, [], []
    pattern = re.compile(r"complete.{0,55}(inverse|domain|kernel|spectrum)|bounded.{0,15}inverse|"
                         r"not independently|unreviewed|actual.{0,40}(operator|fields)", re.I)
    for uid, form, kind, expected in units["units"]:
        lane, key, number = uid.split(":")
        if lane != "physical":
            continue
        path, ps = sources[key]
        text = ps.get(int(number), "")
        observed = hashlib.sha1(text.encode()).hexdigest()[:10]
        count += 1
        if observed != expected:
            mismatches.append({"id": uid, "expected": expected, "observed": observed})
        verdict, record = verdicts.get(uid, ("PENDING", None))
        if verdict == "VERIFIED" and pattern.search(text):
            flags.append({"id": uid, "path": path, "line": int(number), "record": record,
                          "text": text, "meaning": "Reading candidate only; keyword match is not a defect"})
    result = {"method": "Fixed-source paragraph hashes and keyword reading candidates only",
              "main_head": MAIN, "source_head": SOURCE, "physical_units_checked": count,
              "source_hash_mismatches": mismatches, "reading_candidates": flags,
              "scientific_execution_count": 0, "proof_verification": False}
    (HERE / "M9_PARAGRAPH_CUSTODY.json").write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"units": count, "hash_mismatches": len(mismatches),
                      "reading_candidates": len(flags)}))
    if mismatches:
        raise ValueError("Paragraph custody mismatch")


if __name__ == "__main__":
    main()
