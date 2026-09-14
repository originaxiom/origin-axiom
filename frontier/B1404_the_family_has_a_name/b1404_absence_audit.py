"""
B1404 part 5 -- the absence audit, WITH a homonym filter, at a PINNED REVISION.

Two design points, both learned the hard way while writing this file:

  1. MEASURE AT A PINNED REVISION, not the working tree.  This arc writes
     "Minsky", "Epstein-Penner" and "kappa = -2" onto eight doc surfaces; run
     against the working tree afterwards, the audit finds its own report and
     declares nothing absent.  BASE is the commit the arc started from.

  2. FILTER HOMONYMS, in both directions.  A bare grep counts SPELLINGS, and
     this corpus contains an unrelated Epstein (the zeta function) and an
     unrelated hyphenated "-end" (Eisenstein-end, E8-end).  Every raw line of
     both was READ before the filter was written; a filter nobody checked is
     just a way of getting the answer you wanted.
"""
import json, os, re, subprocess, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = "d08d1f98"                      # the commit this arc started from
PATHS = ["*.md", "*.py", "*.json", "*.tex"]
ARC = "frontier/B1404_the_family_has_a_name/"

# NOTE: NOT raw strings -- these need the unicode escapes to be unicode.
MINUS = "−"                       # the Unicode minus the docs use
KAPPA = "κ"                       # the Greek kappa the docs use

# term -> regexes that DISQUALIFY a line (a different object, same spelling)
HOMONYM = {
    # all raw Epstein lines were READ: every one is the Epstein ZETA FUNCTION
    # (B737's KMS/lattice cells; K027's list of RH-analogue control objects).
    "Epstein":       [r"zeta", r"bessel", r"eisenstein", r"davenport",
                      r"epstein sum", r"lattice"],
    # likewise: every "-end invariant" here is Eisenstein-end or E8-end,
    # a hyphenated prefix, not Thurston's ends of a hyperbolic 3-manifold.
    "end invariant": [r"[A-Za-z0-9₀-₉]-end"],
}

TERMS = [
    ("Minsky",                "the classification of punctured-torus groups (1999)"),
    ("Epstein",               "Epstein-Penner canonical decomposition"),
    ("Penner",                "Epstein-Penner canonical decomposition"),
    ("Marden",                "the Marden conjecture / tameness"),
    ("Maskit",                "Kleinian-group combination theorems"),
    ("Bromberg",              "the ending lamination theorem, general case"),
    ("ending lamination",     "Thurston's end invariant"),
    ("end invariant",         "Thurston's end invariant"),
    ("punctured.torus group", "the family's NAME as a technical term"),
    ("Lackenby",              "the canonical decomposition of once-punctured torus bundles"),
    ("Gu.ritaud",             "punctured-torus-bundle geometry via the Farey triangulation"),
    ("Futer",                 "Gueritaud-Futer"),
    ("Floyd",                 "Floyd-Hatcher, incompressible surfaces"),
    ("Hatcher",               "Floyd-Hatcher, incompressible surfaces"),
    ("J.rgensen",             "the inequality; once-punctured tori"),
    ("Farey",                 "the tessellation all four views share"),
]

SCALE = [
    ("Markov", "Markov", "the surface x^2+y^2+z^2 = xyz, which IS the kappa = -2 locus"),
    # Written as four FULL alternatives rather than one character class:
    # [-U+2212] is a class of BYTES in a non-UTF-8 locale, which matched any of
    # e2/88/92 followed by "2" and doubled the count from 215 to 442.  The locale
    # is also pinned below.  Representation again -- see the arc's cost line.
    ("kappa = -2",
     "|".join(k + " ?= ?" + d + "2" for k in ("kappa", KAPPA) for d in ("-", MINUS)),
     "the family's defining condition, banked as a computed value. ALL spellings: "
     "ASCII and Greek kappa, ASCII hyphen and Unicode minus, with and without spaces"),
]


def grep(pattern):
    """git grep at BASE, so the audit cannot read its own report."""
    cmd = ["git", "grep", "-I", "-n", "-E", "-i", "--", pattern, BASE, "--", *PATHS]
    # pinned, not inherited: the same bracket expression returns 215 under
    # LC_ALL=C and 442 under C.UTF-8 (see the arc's cost line, E75 #11)
    env = {k: v for k, v in os.environ.items() if k not in ("LC_ALL", "LC_CTYPE", "LANG")}
    env["LC_ALL"] = "C.UTF-8"
    out = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=env).stdout
    rows = []
    for line in out.splitlines():
        parts = line.split(":", 3)                  # rev : path : lineno : text
        if len(parts) < 4 or parts[1].startswith(ARC):
            continue
        rows.append((parts[1], parts[3]))
    return rows


print(f"  measured at {BASE} (before this arc wrote about any of it)\n")
rows = []
for term, why in TERMS:
    raw = grep(term)
    pats = [re.compile(p, re.I) for p in HOMONYM.get(term, [])]
    real = [r for r in raw if not any(p.search(r[1]) for p in pats)]
    files = sorted({f for f, _ in real})
    rows.append({"term": term, "role": why, "raw_lines": len(raw),
                 "after_homonym_filter": len(real), "files": len(files),
                 "present": bool(real), "sample_files": files[:4]})
    flag = "  <-- ABSENT" if not real else ""
    masked = "  (homonym-masked)" if raw and not real else ""
    print(f"  {term:24s} raw {len(raw):4d}  real {len(real):4d}  files {len(files):3d}"
          f"{flag}{masked}   [{why}]")

print()
scale = []
for name, rx, why in SCALE:
    hits = grep(rx)
    files = {f for f, _ in hits}
    scale.append({"term": name, "rev": BASE, "lines": len(hits), "files": len(files),
                  "role": why})
    print(f"  SCALE  {name:12s} {len(hits):5d} lines across {len(files):4d} files")

absent = [r["term"] for r in rows if not r["present"]]
masked = [r["term"] for r in rows if r["raw_lines"] and not r["after_homonym_filter"]]
print(f"\n  GENUINELY ABSENT: {absent}")
print(f"  ABSENT BUT MASKED BY A HOMONYM (a bare grep reports presence): {masked}")

out = pathlib.Path(__file__).with_name("absence_audit.json")
out.write_text(json.dumps({"base": BASE, "rows": rows, "scale": scale,
                           "absent": absent, "homonym_masked": masked}, indent=1))
print(f"  wrote {out.name}")
