#!/usr/bin/env python3
"""THE VERIFICATION PACKAGE of THE PAPER -- build the manifest.

For every load-bearing claim of papers/P3_THE_PAPER/main.tex (the same list the generated provenance appendix is
built from, scripts/checks/paper_provenance.py::CLAIMS) this writes, per establishing record:
  the record's directory, its verdict, its one-line claim, every seal file (sha256 of a DESIGN / PREREGISTRATION written
  before the computation) with the sealed file's current hash, every verification script and result file it ships,
  and every test lock under tests/ that names it.
Nothing here is asserted by hand: the manifest is regenerated from the repository and a stale manifest is a test failure.

    python3 build_manifest.py            # writes MANIFEST.json and MANIFEST.md beside this file
"""
import datetime, hashlib, importlib.util, json, pathlib, platform, re, subprocess, sys
HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT))
spec = importlib.util.spec_from_file_location("paper_provenance", ROOT / "scripts" / "checks" / "paper_provenance.py")
prov = importlib.util.module_from_spec(spec); spec.loader.exec_module(prov)

def sha256(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def arc_dir(aid):
    hits = sorted(d for d in (ROOT / "frontier").glob(f"{aid}_*") if d.is_dir())
    return hits[0] if hits else None

def seals(d):
    out = []
    for s in sorted(d.glob("*.sha256")):
        recorded = s.read_text(encoding="utf-8").strip().splitlines()
        target = s.with_suffix(".md")
        cur = sha256(target) if target.exists() else None
        out.append(dict(seal_file=str(s.relative_to(ROOT)), sealed_file=str(target.relative_to(ROOT)) if target.exists() else None,
                        recorded=recorded, current_sha256=cur,
                        matches=any(cur and cur in line for line in recorded if not line.lstrip().startswith('#'))))   # comment lines (old seals kept for the record) do not count
    return out

def locks(aid):
    """all test files naming the record; primary_locks() are the ones named FOR it (test_b<number>_*.py)."""
    pat = re.compile(rf"\b{aid}\b")
    return sorted(str(t.relative_to(ROOT)) for t in (ROOT / "tests").glob("test_*.py") if pat.search(t.read_text(encoding="utf-8", errors="ignore")))

def primary_locks(aid):
    return sorted(str(t.relative_to(ROOT)) for t in (ROOT / "tests").glob(f"test_{aid.lower()}_*.py"))

def versions():
    out = {"python": platform.python_version(), "platform": platform.platform()}
    for mod in ("snappy", "sympy", "mpmath", "numpy", "flint"):
        try:
            m = __import__(mod); out[mod] = getattr(m, "__version__", "?")
        except Exception as e:
            out[mod] = f"not importable ({type(e).__name__})"
    try: out["git_head"] = subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    except Exception: out["git_head"] = "?"
    return out

def main(out_dir=None):
    out_dir = pathlib.Path(out_dir) if out_dir else HERE
    claims = []
    for sec, claim, arcs, support in prov.CLAIMS:
        recs = []
        for aid in arcs:
            d = arc_dir(aid)
            if d is None:
                recs.append(dict(arc=aid, error="record directory not found")); continue
            try: v = json.loads((d / "arc_verdict.json").read_text(encoding="utf-8"))
            except Exception: v = {}
            ver = d / "verification"
            recs.append(dict(arc=aid, dir=str(d.relative_to(ROOT)), verdict=v.get("verdict", "?"), claim_one_line=(v.get("claim_one_line") or "")[:300],
                             seals=seals(d), reproduce_sh=(ver / "reproduce.sh").exists(),
                             scripts=sorted(str(f.relative_to(ROOT)) for f in ver.glob("*") if f.suffix in (".py", ".sh")) if ver.exists() else [],
                             results=sorted(str(f.relative_to(ROOT)) for f in ver.glob("*") if f.suffix in (".json", ".out", ".txt")) if ver.exists() else [],
                             locks=locks(aid), primary_locks=primary_locks(aid)))
        claims.append(dict(section=sec, claim=claim, support=support, records=recs))
    manifest = dict(paper="papers/P3_THE_PAPER/main.tex", built=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    environment=versions(), claims=claims,
                    totals=dict(claims=len(claims), records=sum(len(c["records"]) for c in claims),
                                seals=sum(len(r.get("seals", [])) for c in claims for r in c["records"]),
                                locks=len({l for c in claims for r in c["records"] for l in r.get("locks", [])}),
                                records_with_a_primary_lock=sum(1 for c in claims for r in c["records"] if r.get("primary_locks"))))
    (out_dir / "MANIFEST.json").write_text(json.dumps(manifest, indent=1), encoding="utf-8")
    lines = ["# THE VERIFICATION PACKAGE — manifest (generated by `build_manifest.py`; do not hand-edit)", "",
             f"Built {manifest['built']} at commit `{manifest['environment'].get('git_head')}`; Python {manifest['environment']['python']}, "
             + ", ".join(f"{k} {manifest['environment'][k]}" for k in ("snappy", "sympy", "mpmath", "numpy", "flint")) + ".", "",
             f"{manifest['totals']['claims']} claims · {manifest['totals']['records']} establishing records · {manifest['totals']['seals']} seals · {manifest['totals']['locks']} distinct test files naming a record · {manifest['totals']['records_with_a_primary_lock']} of {manifest['totals']['records']} records with a primary lock.", "",
             "Locks: a *primary lock* is a test file named for the record (re-asserts its numbers); a *mention* is any other test naming it (traceability). Seals certify integrity, not chronology — see README.", "",
             "| # | claim | support | record | verdict | seals (match) | scripts | primary locks | mentions |", "|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(claims, 1):
        for r in c["records"]:
            if "error" in r: lines.append(f"| {i} | {c['claim']} | {c['support']} | {r['arc']} | **{r['error']}** | | | |"); continue
            sl = ", ".join(f"`{pathlib.Path(s['seal_file']).name}` ({'ok' if s['matches'] else 'MISMATCH'})" for s in r["seals"]) or "—"
            prim = r.get("primary_locks", []); ment = [l for l in r["locks"] if l not in prim]
            lines.append(f"| {i} | {c['claim']} | {c['support']} | `{r['arc']}` | {r['verdict']} | {sl} | {len(r['scripts'])} | {', '.join('`'+pathlib.Path(l).name+'`' for l in prim) or '—'} | {len(ment)} |")
    (out_dir / "MANIFEST.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"manifest: {manifest['totals']}")
    bad = [(c['claim'][:50], r['arc'], s['seal_file']) for c in claims for r in c["records"] for s in r.get("seals", []) if not s["matches"]]
    missing = [(c['claim'][:50], r['arc']) for c in claims for r in c["records"] if "error" in r or not r.get("locks")]
    print("seal mismatches:", bad); print("records without a lock or not found:", missing)
    return 0 if not bad and not missing else 1

if __name__ == "__main__":
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None   # --out DIR: write elsewhere (the currency test uses a temp dir)
    sys.exit(main(out))
