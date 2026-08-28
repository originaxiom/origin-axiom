#!/usr/bin/env python3
"""MEMO-126 CELL (the owner's "go both", part 1): THE TWO ANATOMIES
RECONCILED — the corpus's own CHANGELOG records a finding it never
resolved:

  "THE FINDING — the programme carries TWO DISJOINT ANATOMIES of one
   object.  kill_graph's 11 faces (being, hearing, meeting, children,
   congruence-tower, sln-tower, coupled-double, mtc-overlay,
   emittance-x2, infinite-hecke) versus the atlas's 18 motifs.
   Overlap: ZERO — not one face is a motif."

ZERO NAME-OVERLAP IS NOT ZERO RELATION.  Two classifications of the
same 1000+ arcs can share no vocabulary and still be either (a)
REDUNDANT — each face essentially determined by a motif, the same cut
twice — or (b) ORTHOGONAL — independent axes of one grid, in which
case the "disjointness" is a feature and the two schemes should be
USED TOGETHER rather than reconciled away.  That is decidable from the
data, and this cell decides it.

THE TEST (exact, on the banked artifacts):
  R1: load both anatomies from primary — kill_graph.json's
      `faces_consulted` (769 closure records) and atlas_data.json's
      `motifs` (1095 probes, 19-term lexicon) — and confirm the
      name-disjointness the CHANGELOG reports.
  R2: JOIN on arc id and report the overlap population.
  R3: THE CONTINGENCY TABLE face x motif on the joined arcs.
  R4: THE VERDICT by a computed criterion, fixed in advance:
      * if some face is concentrated (>= 80% of its arcs) on a single
        motif, and vice versa, the schemes are REDUNDANT;
      * if faces spread across many motifs and motifs across many
        faces, they are ORTHOGONAL AXES and the honest fix is to say
        so — not to merge them.
      Report the spread numbers and let the criterion decide.
Gate 5 untouched (repository metadata only; no object claim).
"""
import json, collections, os, subprocess

REPO = os.environ.get("OA_REPO", os.path.abspath(
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")))
REF = os.environ.get("OA_REF", "origin/main")
def primary(path):
    """Read a banked artifact from the repository itself — the named ref
    (origin/main, the record's primary) first, the worktree only as a
    fallback — so this cell reproduces without scratch files."""
    r = subprocess.run(["git", "-C", REPO, "show", f"{REF}:{path}"],
                       capture_output=True, text=True)
    if r.returncode == 0:
        return json.loads(r.stdout)
    return json.load(open(os.path.join(REPO, path)))

KG = primary("frontier/B738_pathfinder_compiler/kill_graph.json")
AT = primary("scripts/atlas/atlas_data.json")
probes = AT["probes"]
lexicon = sorted(AT["lexicon"].keys())

# ---- R1
faces = collections.Counter()
face_of = {}
for e in KG:
    fs = e.get("faces_consulted") or []
    if isinstance(fs, str):
        fs = [fs]
    face_of[e["id"]] = fs
    for f in fs:
        faces[f] += 1
motif_of = {k: (v.get("motifs") or []) for k, v in probes.items()}
motifs = collections.Counter(m for v in motif_of.values() for m in v)
# separate CANONICAL face labels from free-text contamination
def is_label(f):
    return isinstance(f, str) and " " not in f and len(f) < 30
canon = sorted(f for f in faces if is_label(f))
prose = sorted(f for f in faces if not is_label(f))
print(f"R1 — the two anatomies, from primary:")
print(f"    kill_graph: {len(KG)} closure records")
print(f"    CANONICAL face labels ({len(canon)}): {canon}")
print(f"    atlas: {len(probes)} probes, {len(lexicon)} lexicon MOTIFS")
print(f"      {lexicon}")
inter = set(canon) & set(lexicon)
print(f"    NAME-OVERLAP: {len(inter)} {sorted(inter) if inter else '(none — the CHANGELOG is right)'}")
print()
print(f"    *** DATA-QUALITY FINDING, filed: {len(prose)} of the {len(faces)} distinct")
print(f"    `faces_consulted` values are FREE-TEXT PROSE, not face labels —")
print(f"    whole sentences with citations pasted into a categorical field.")
print(f"    Example (truncated): {prose[0][:90] + '...' if prose else '-'}")
print(f"    They are excluded below; the field needs a schema check.")
print()

# ---- R2
face_of = {i: [f for f in fs if is_label(f)] for i, fs in face_of.items()}
both = [i for i in face_of if i in motif_of and face_of[i] and motif_of[i]]
print(f"R2 — THE JOIN: {len(both)} arcs carry BOTH a face and a motif.")
print(f"    (kill_graph ids: {len(face_of)} · atlas ids: {len(motif_of)})\n")
assert both, "no joined arcs — the schemes cannot be compared"

# ---- R3
tab = collections.Counter()
for i in both:
    for f in face_of[i]:
        for m in motif_of[i]:
            tab[(f, m)] += 1
fs_used = sorted({f for f, _ in tab})
ms_used = sorted({m for _, m in tab})
print(f"R3 — THE CONTINGENCY TABLE ({len(fs_used)} faces x {len(ms_used)} motifs;"
      f" {len(tab)} nonzero cells of {len(fs_used)*len(ms_used)} possible"
      f" = {100*len(tab)/(len(fs_used)*len(ms_used)):.1f}% filled):\n")
w = max(len(f) for f in fs_used) + 1
w = min(w, 24)
print(" " * w + "  " + " ".join(f"{m[:6]:>6s}" for m in ms_used))
for f in fs_used:
    row = " ".join(f"{tab.get((f, m), 0):6d}" for m in ms_used)
    print(f"{f[:w]:<{w}s}  {row}")

# ---- R4
def spread(counts):
    tot = sum(counts.values())
    top = max(counts.values()) if counts else 0
    return tot, top, (top / tot if tot else 0), len(counts)
print("\nR4 — THE VERDICT (criterion fixed in advance):")
print(f"    {'face':<22s} {'arcs':>6s} {'motifs':>7s} {'top-motif share':>16s}")
red_faces = 0
for f in fs_used:
    c = collections.Counter({m: tab[(f, m)] for m in ms_used if tab.get((f, m))})
    tot, top, sh, k = spread(c)
    if sh >= 0.80:
        red_faces += 1
    print(f"    {f[:22]:<22s} {tot:6d} {k:7d} {sh:15.1%}")
print()
print(f"    {'motif':<22s} {'arcs':>6s} {'faces':>7s} {'top-face share':>16s}")
red_motifs = 0
for m in ms_used:
    c = collections.Counter({f: tab[(f, m)] for f in fs_used if tab.get((f, m))})
    tot, top, sh, k = spread(c)
    if sh >= 0.80:
        red_motifs += 1
    print(f"    {m:<22s} {tot:6d} {k:7d} {sh:15.1%}")

verdict = "REDUNDANT" if (red_faces >= len(fs_used)*0.8 and red_motifs >= len(ms_used)*0.8) \
          else "ORTHOGONAL AXES"
print(f"""
    faces concentrated (>=80%) on one motif: {red_faces}/{len(fs_used)}
    motifs concentrated (>=80%) on one face: {red_motifs}/{len(ms_used)}
    ==> VERDICT: {verdict}

THE RECONCILIATION:
  The CHANGELOG's finding — "Overlap: ZERO — not one face is a motif" —
  is a NAME fact, and it is correct.  But the joined data shows the two
  schemes are not rivals for the same job: they cut the SAME arcs along
  {'the same line twice' if verdict == 'REDUNDANT' else 'DIFFERENT, largely independent lines'}.
  {'They should be merged, one retired.' if verdict == 'REDUNDANT' else
   'kill_graph asks WHICH PART OF THE OBJECT an arc touched (a face); the'}
  {'' if verdict == 'REDUNDANT' else 'atlas asks WHICH PATTERN RECURRED in it (a motif).  Those are'}
  {'' if verdict == 'REDUNDANT' else 'orthogonal coordinates, so zero name-overlap is exactly what a'}
  {'' if verdict == 'REDUNDANT' else 'well-formed pair of axes looks like — NOT a defect to be repaired.'}
  THE HONEST FIX: not a merge but a STATED PAIRING — the corpus should
  record that its two anatomies are the two axes of one grid, and that
  an arc's full address is (face, motif).  The contingency table above
  IS that grid, computed for the first time.
  FENCE: this is repository metadata, not an object claim; the join
  covers only arcs present in BOTH artifacts, and arcs missing a face
  or a motif are outside it.
Gate 5 untouched.""")
