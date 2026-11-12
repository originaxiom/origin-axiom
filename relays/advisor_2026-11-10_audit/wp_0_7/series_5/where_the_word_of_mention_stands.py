"""for every phrase the sweep excuses today by a word of mention: how far the nearest such word stands from the phrase"""
import importlib.util, os, re, sys
root = os.path.abspath(sys.argv[1])
spec = importlib.util.spec_from_file_location("rs", os.path.join(root, "scripts/checks/retraction_sweep.py"))
rs = importlib.util.module_from_spec(spec); spec.loader.exec_module(rs)
phrases = [(p, re.compile(re.escape(p), re.I)) for p in rs._phrases()]
rows = []
for rel in rs._tracked_md():
    if rel in rs.EXEMPT_FILES or rel.startswith(rs.EXEMPT_PREFIXES) or os.path.basename(rel) in rs.EXEMPT_BASENAMES:
        continue
    try:
        body = open(os.path.join(root, rel), encoding="utf-8", errors="ignore").read()
    except OSError:
        continue
    flat_body = rs._flatten(body).lower()
    live = [(p, rx) for p, rx in phrases if p.lower() in flat_body]
    for n, line in enumerate(body.split("\n"), 1):
        flat = rs._flatten(line)
        in_flat, in_raw = list(rs.MENTION_CUES.finditer(flat)), list(rs.MENTION_CUES.finditer(line))
        if not (in_flat or in_raw):
            continue
        for p, rx in live:
            for m in rx.finditer(flat):
                gaps = [max(0, c.start() - m.end(), m.start() - c.end()) for c in in_flat]
                table = line.lstrip().startswith("|")
                own_cell = None
                if table:
                    # the cell of the flattened row that holds the phrase
                    a = flat.rfind("|", 0, m.start()) + 1; b = flat.find("|", m.end()); b = len(flat) if b < 0 else b
                    own_cell = bool(rs.MENTION_CUES.search(flat[a:b]))
                rows.append((min(gaps) if gaps else None, rel, n, p, len(flat), table, own_cell, bool(in_raw) and not in_flat))
print("phrase occurrences on a line that carries a word of mention:", len(rows))
print("  in a table row:", sum(1 for r in rows if r[5]), "-- with the word in the phrase's own cell:", sum(1 for r in rows if r[5] and r[6]))
print("  word found only before the markup is taken off (a strike-through):", sum(1 for r in rows if r[7]))
d = sorted(r[0] for r in rows if r[0] is not None)
print("  distance from the phrase to the nearest word, in characters of the flattened line:")
for cut in (0, 20, 40, 80, 120, 160, 200, 300, 500, 1000, 5000):
    print("     within %5d: %d" % (cut, sum(1 for x in d if x <= cut)))
print("\nthe farthest:")
for r in sorted(rows, key=lambda r: -(r[0] or 0))[:14]:
    print("  %5s chars  %s:%d  [%s]  (line of %d chars%s)" % (r[0], r[1], r[2], r[3][:50], r[4], ", table row" if r[5] else ""))
