#!/usr/bin/env python3
"""T5 sweep: find every consumer of orientation in the corpus.

Coverage (stated honestly):
  SWEPT : frontier/*/FINDINGS.md (all that exist), docs/*.md (top level),
          docs/anatomy|atlas|audits|dossiers|handoffs|progress|views/**/*.md,
          papers/**/*.tex and papers/**/*.md
  SKIPPED: reports/ (evaluation-seat output, not object record), legacy/,
          story/, speculations/, knowledge/, src/, core/, scripts/, tests/
          (tests read separately by hand for the genesis-fork check),
          frontier files other than FINDINGS.md (RESULTS.json, compute.py etc.
          are the computations behind the FINDINGS; the FINDINGS is the banked
          claim surface this audit classifies).

Output: sweep_hits.tsv  (file<TAB>term<TAB>lineno<TAB>line)
        sweep_summary.txt (per-file term counts, plus bite-control check)
"""
import os, re, sys, json, collections

ROOT = "/home/user/origin-axiom"
OUT = os.path.dirname(os.path.abspath(__file__))

TERMS = {
    "orientation":      re.compile(r"orientation", re.I),
    "orientable":       re.compile(r"orientable", re.I),
    "orient-reversing": re.compile(r"orientation[- ]reversing", re.I),
    "amphichiral":      re.compile(r"amphichir", re.I),
    "chern-simons":     re.compile(r"chern[-_ ]?simons|\bCS\b", re.I),
    "spin":             re.compile(r"spin[- ]structure|spin[- ]lift|\bPin\b|Pin[⁻-]", re.I),
    "det-minus-1":      re.compile(r"det\s*=?\s*[−-]\s*1|det\s*[−-]1", re.I),
    "gieseking":        re.compile(r"gieseking", re.I),
    "m000":             re.compile(r"\bm000\b"),
    "double-cover":     re.compile(r"double[- ]cover", re.I),
    "complex-volume":   re.compile(r"complex volume", re.I),
    "sl2c-lift":        re.compile(r"SL\(2,\s*[CℂC]\)|PSL\(2", re.I),
    "knot-in-s3":       re.compile(r"knot complement|Reid", re.I),
}

def files():
    fr = sorted(
        os.path.join(ROOT, "frontier", d, "FINDINGS.md")
        for d in os.listdir(os.path.join(ROOT, "frontier"))
        if os.path.isfile(os.path.join(ROOT, "frontier", d, "FINDINGS.md")))
    dc = []
    ddir = os.path.join(ROOT, "docs")
    for f in sorted(os.listdir(ddir)):
        p = os.path.join(ddir, f)
        if f.endswith(".md") and os.path.isfile(p):
            dc.append(p)
    for sub in ["anatomy","atlas","audits","dossiers","handoffs","progress","views"]:
        for dirpath, _, names in os.walk(os.path.join(ddir, sub)):
            for n in sorted(names):
                if n.endswith(".md"):
                    dc.append(os.path.join(dirpath, n))
    pp = []
    for dirpath, _, names in os.walk(os.path.join(ROOT, "papers")):
        for n in sorted(names):
            if n.endswith((".tex", ".md")):
                pp.append(os.path.join(dirpath, n))
    return fr + dc + pp

def main():
    hits = []
    per_file = collections.defaultdict(collections.Counter)
    fl = files()
    for path in fl:
        try:
            text = open(path, encoding="utf-8", errors="replace").read()
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), 1):
            for term, rx in TERMS.items():
                if rx.search(line):
                    rel = os.path.relpath(path, ROOT)
                    hits.append((rel, term, i, line.strip()[:240]))
                    per_file[rel][term] += 1

    with open(os.path.join(OUT, "sweep_hits.tsv"), "w") as f:
        for rel, term, i, line in hits:
            f.write(f"{rel}\t{term}\t{i}\t{line}\n")

    # bite control: the KNOWN orientation-consumers must appear
    bite = {
        "chern-simons in corpus":  any(h[1] == "chern-simons" for h in hits),
        "B1141 spin payment":      any("B1141" in h[0] for h in hits),
        "complex volume":          any(h[1] == "complex-volume" for h in hits),
        "Reid / knot-in-S3":       any(h[1] == "knot-in-s3" for h in hits),
        "Gieseking":               any(h[1] == "gieseking" for h in hits),
    }
    with open(os.path.join(OUT, "sweep_summary.txt"), "w") as f:
        f.write(f"files swept: {len(fl)}\n")
        f.write(f"files with >=1 hit: {len(per_file)}\n")
        f.write(f"total hit lines: {len(hits)}\n\nBITE CONTROL:\n")
        for k, v in bite.items():
            f.write(f"  {k}: {'PRESENT' if v else 'ABSENT -> SWEEP FAILED'}\n")
        f.write("\nTOP 60 FILES BY HIT COUNT:\n")
        ranked = sorted(per_file.items(), key=lambda kv: -sum(kv[1].values()))
        for rel, c in ranked[:60]:
            f.write(f"  {sum(c.values()):4d}  {rel}  {dict(c)}\n")
    print(f"files swept: {len(fl)}; files with hits: {len(per_file)}; hit lines: {len(hits)}")
    print("BITE:", json.dumps(bite))
    if not all(bite.values()):
        print("SWEEP FAILED BITE CONTROL", file=sys.stderr)
        sys.exit(2)

if __name__ == "__main__":
    main()
