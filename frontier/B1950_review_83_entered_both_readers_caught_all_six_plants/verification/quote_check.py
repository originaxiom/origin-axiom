"""Review 83: the readers' quotations checked by machine against the reading copy review-83/read at b35eac607 (main,
2026-11-17). For each finding of a reading file, every back-quoted or fenced quotation of 25 characters or more is
searched, whitespace-normalised, in the reading commit's tracked text files of the window's arcs and docs. Usage:
python3 quote_check.py READING.md [READING.md ...]; prints per file: findings, quotations parsed, quotations found."""
import re, subprocess, sys, pathlib
READ = "b35eac607"
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
names = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "-r", "--name-only", READ], capture_output=True, text=True).stdout.split("\n")
keep = [n for n in names if n.endswith((".md", ".py", ".json", ".txt")) and (re.match(r"frontier/B19[0-4]\d_", n) or n.startswith(("docs/", "tests/", "scripts/")) or n in ("GENESIS.md", "README.md"))]
norm = lambda s: re.sub(r"\s+", " ", s).strip()
blob = {}
for n in keep:
    r = subprocess.run(["git", "-C", str(ROOT), "show", "%s:%s" % (READ, n)], capture_output=True)
    try: blob[n] = norm(r.stdout.decode("utf-8"))
    except UnicodeDecodeError: pass
corpus = "\n".join(blob.values())
for path in sys.argv[1:]:
    t = pathlib.Path(path).read_text()
    parts = re.split(r"(?m)^#{3,4} (?:Finding )?`?(?:F-)?R83-\d+`?", t)[1:]
    heads = re.findall(r"(?m)^#{3,4} (?:Finding )?`?((?:F-)?R83-\d+)`?", t)
    nq = nf = 0; missing = []
    for h, body in zip(heads, parts):
        qs = re.findall(r"\*\*Verbatim quotation[^:]*:\*\*\s*`\"?(.+?)\"?`", body) + re.findall(r"(?s)```(?:\w+)?\n(.+?)```", body)
        for q in qs:
            q = norm(q.strip('"'))
            if len(q) < 25: continue
            nq += 1
            if q in corpus: nf += 1
            else: missing.append((h, q[:90]))
    print("%s: %d findings; %d quotations parsed; %d found exactly in the reading commit" % (pathlib.Path(path).name, len(heads), nq, nf))
    for h, q in missing[:12]: print("   not found:", h, "|", q)
