r"""PLATE H — THE 12-FOLD COVER.

m004 (the figure-eight knot complement) is a degree-12 cover of the
Bianchi orbifold PSL(2,O_3)\H^3.  This plate makes "inherited vs its own"
a picture, from computed data only:

  (1) the TRUE Schreier coset graph of the 12 sheets, computed by exact
      arithmetic in SL(2, Z[w]/4) — group orders 3840 / 320, index 12 —
      reusing frontier/B792_maass_m004_eigenvalues/mod4_trace_law_proof.py.
  (2) the mod-2 inset: the image is D_5 (order 10) inside
      PSL(2,F_4) = A_5 (order 60), index 6 — why the level is exactly 4.
  (3) the spectral consequence: the parent's 4 tones sit inside the
      child's 43, from the certified B792 eigenvalue files.

Nothing here is drawn by hand.  Every node, edge and tick is computed.
Gate 5-Q.  Visualization only; no claim.
"""
import contextlib
import io
import json
import sys
from collections import deque

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Wedge  # noqa: E402

B792 = 'frontier/B792_maass_m004_eigenvalues'
OUT = 'frontier/B796_coupling_campaign/anatomy'
sys.path.insert(0, B792)

# reuse the certified exact Z[w]/4 arithmetic (its module body prints a
# proof transcript on import; swallow it, we only want the groups)
with contextlib.redirect_stdout(io.StringIO()):
    import mod4_trace_law_proof as M  # noqa: E402

plt.rcParams['font.family'] = 'DejaVu Sans'
BG = '#0d0f14'
INK = '#e8e4dc'
AMB = '#e8a15c'
BLU = '#4a90c4'
RED = '#d64545'
MUT = '#9aa3b2'
GRD = '#3a4150'
PALE = '#f2ede3'

# ============================================================ (1) the cover
G, H = M.G, M.H
ZERO, ONE, W = M.ZERO, M.ONE, M.W
IDM = M.mat([[ONE, ZERO], [ZERO, ONE]])
# E = diag(w, w^-1): the order-3 unit rotation stabilising the cusp
E = M.mat([[W, ZERO], [ZERO, M.rmul(W, W)]])
assert E in G, 'unit rotation not in the mod-4 image'

print(f"|SL(2,Z[w]/4)| = {len(G)}   |H mod 4| = {len(H)}   "
      f"index = {len(G) // len(H)}", flush=True)
assert len(G) == 3840 and len(H) == 320


def coset(g):
    return frozenset(M.mmul(h, g) for h in H)


reps, keys, seen = [], [], {}
for g in G:
    k = coset(g)
    if k not in seen:
        seen[k] = len(reps)
        reps.append(g)
        keys.append(k)
NC = len(reps)
assert NC == 12, NC
lookup = {g: i for i, k in enumerate(keys) for g in k}


def perm(s):
    return [lookup[M.mmul(reps[i], s)] for i in range(NC)]


pT, pU, pS, pE = perm(M.T), perm(M.U), perm(M.S), perm(E)
ID = lookup[IDM]


def orbit(start, ps):
    o, q = {start}, deque([start])
    while q:
        x = q.popleft()
        for p in ps:
            if p[x] not in o:
                o.add(p[x])
                q.append(p[x])
    return o


assert len(orbit(ID, [pT, pU, pS])) == 12, 'cover not connected'
CUSP = len(orbit(ID, [pT, pU, pE]))
print(f"  cusp subgroup <T,U,E> orbit = {CUSP}  (m004 has 1 cusp, "
      f"degree {CUSP})", flush=True)


def cycles(p):
    s, out = set(), []
    for i in range(len(p)):
        if i in s:
            continue
        c, j = [i], p[i]
        s.add(i)
        while j != i:
            c.append(j)
            s.add(j)
            j = p[j]
        out.append(c)
    return out


# --- layout: 3 translation-blocks of 4, cycled by the unit rotation E ---
blocks_raw = []
todo = set(range(NC))
while todo:
    b = orbit(min(todo), [pT, pU])
    blocks_raw.append(b)
    todo -= b
assert sorted(len(b) for b in blocks_raw) == [4, 4, 4], blocks_raw
b0 = next(b for b in blocks_raw if ID in b)
# order the identity block by whichever translation is a 4-cycle on it
ring = None
for p in (pU, pT):
    walk, x = [ID], pU[ID] if p is pU else pT[ID]
    while x != ID and len(walk) < 5:
        walk.append(x)
        x = p[x]
    if len(walk) == 4 and set(walk) == b0:
        ring = walk
        break
if ring is None:                       # deterministic fallback
    ring = [ID] + sorted(b0 - {ID})
order = list(ring)
for _ in range(2):
    order += [pE[x] for x in order[-4:]]
assert sorted(order) == list(range(12)), order
pos = {c: i for i, c in enumerate(order)}


def xy(i, r=1.0):
    a = np.pi / 2 - 2 * np.pi * i / 12
    return r * np.cos(a), r * np.sin(a)


fig = plt.figure(figsize=(15.2, 12.8), facecolor=BG)
gs = fig.add_gridspec(2, 3, height_ratios=[1.50, 1.02],
                      width_ratios=[1.0, 1.0, 0.86],
                      left=0.035, right=0.972, top=0.892, bottom=0.128,
                      wspace=0.22, hspace=0.34)

ax = fig.add_subplot(gs[0, 0:2])
ax.set_facecolor(BG)
ax.set_aspect('equal')
ax.set_xlim(-1.72, 1.72)
ax.set_ylim(-1.95, 1.52)
ax.axis('off')

# faint wedges = the three translation blocks (sheets over the rotation)
GAP = 6.0
for k in range(3):
    a1 = 90 - (4 * k + 3.5) * 30 + GAP / 2
    ax.add_patch(Wedge((0, 0), 1.255, a1, a1 + 120 - GAP,
                       facecolor='#191f2d', edgecolor='none', zorder=0))
    am = np.deg2rad(a1 + (120 - GAP) / 2)
    ax.text(1.30 * np.cos(am), 1.30 * np.sin(am),
            f'block {k + 1}', color='#6a7383', fontsize=8.4, ha='center',
            va='center', zorder=1)

# E (order-3 unit rotation): faint chords, p -> p+4
for i in range(12):
    x1, y1 = xy(i)
    x2, y2 = xy((i + 4) % 12)
    ax.plot([x1, x2], [y1, y2], color='#586274', lw=0.9, ls=':',
            zorder=1, alpha=0.9)


def edge(i, j, col, rad, lw=1.7, z=3):
    if i == j:                                   # fixed sheet: self-loop
        x, y = xy(i)
        ux, uy = x / np.hypot(x, y), y / np.hypot(x, y)
        cx, cy = x + 0.125 * ux, y + 0.125 * uy
        ax.add_patch(plt.Circle((cx, cy), 0.072, fill=False, lw=lw * 0.8,
                                edgecolor=col, zorder=z, alpha=0.9))
        return
    ax.add_patch(FancyArrowPatch(xy(i), xy(j), color=col, lw=lw,
                                 arrowstyle='-|>', mutation_scale=11,
                                 shrinkA=9.5, shrinkB=9.5, alpha=0.92,
                                 connectionstyle=f'arc3,rad={rad}', zorder=z))


for c in range(12):
    edge(pos[c], pos[pT[c]], AMB, 0.30)
    edge(pos[c], pos[pU[c]], BLU, -0.30)
done = set()
for c in range(12):
    k = frozenset((pos[c], pos[pS[c]]))
    if k in done:
        continue
    done.add(k)
    x1, y1 = xy(pos[c])
    x2, y2 = xy(pos[pS[c]])
    ax.plot([x1, x2], [y1, y2], color=RED, lw=1.5, alpha=0.85, zorder=2)

for c in range(12):
    i = pos[c]
    x, y = xy(i)
    home = (c == ID)
    ax.add_patch(plt.Circle((x, y), 0.088, facecolor='#141822',
                            edgecolor=AMB if home else INK,
                            lw=2.4 if home else 1.2, zorder=6))
    ax.text(x, y, str(i + 1), color=AMB if home else INK, fontsize=9.5,
            ha='center', va='center', zorder=7,
            fontweight='bold' if home else 'normal')
x0, y0 = xy(0)
ax.annotate('sheet 1 = Γ₄₁ itself\n(the identity coset)',
            xy=(x0, y0 + 0.10), xytext=(x0 + 0.10, 1.30), color=AMB,
            fontsize=9.4, ha='left', va='bottom',
            arrowprops=dict(arrowstyle='-', color=AMB, lw=0.9))

hs = [plt.Line2D([], [], color=AMB, lw=2, label='T : z ↦ z+1'),
      plt.Line2D([], [], color=BLU, lw=2, label='U : z ↦ z+ω'),
      plt.Line2D([], [], color=RED, lw=2, label='S : z ↦ −1/z'),
      plt.Line2D([], [], color='#586274', lw=1, ls=':',
                 label='E : z ↦ ωz   (order 3)')]
fig.legend(handles=hs, frameon=False, fontsize=9.8, labelcolor='#c8cfda',
           loc='center', bbox_to_anchor=(0.415, 0.498), ncol=4,
           handlelength=2.3, columnspacing=3.0)
ax.set_title('(1)  THE COVER — the twelve sheets, and how the parent\'s '
             'symmetries move between them',
             color=INK, fontsize=13, pad=8, loc='left')
ax.text(0.0, -1.52,
        'exact Schreier graph of Γ₄₁\\PSL(2,O₃), computed in SL(2,ℤ[ω]/4):   '
        '|G| = 3840,   |H| = 320,   index = 12.\n'
        'the three shaded blocks are the translation-blocks; the dotted E '
        'rotates them into one another (a true 3-fold symmetry of this picture),\n'
        'so the object\'s single cusp wraps the parent\'s cusp 12-to-1.',
        color=MUT, fontsize=8.6, va='top', ha='center', linespacing=1.5)

# ==================================================== (2) the mod-2 inset
ax2 = fig.add_subplot(gs[0, 2])
ax2.set_facecolor(BG)
ax2.set_aspect('equal')
ax2.axis('off')


def red2(m):
    return tuple(tuple((x[0] % 2, x[1] % 2) for x in r) for r in m)


H2 = {red2(m) for m in H}
G2 = {red2(m) for m in G}
print(f"  mod 2: |H| = {len(H2)} (D₅) inside |SL(2,F₄)| = {len(G2)} (A₅), "
      f"index {len(G2) // len(H2)}", flush=True)
reps2, keys2, seen2 = [], [], {}
for g in G2:
    k = frozenset(red2(M.mmul(h, g)) for h in H2)
    if k not in seen2:
        seen2[k] = len(reps2)
        reps2.append(g)
        keys2.append(k)
NC2 = len(reps2)
assert NC2 == 6, NC2
lk2 = {g: i for i, k in enumerate(keys2) for g in k}
q = {nm: [lk2[red2(M.mmul(reps2[i], red2(s)))] for i in range(NC2)]
     for nm, s in (('T', M.T), ('U', M.U), ('S', M.S))}
ID2 = lk2[red2(IDM)]


def xy2(i, r=1.0):
    a = np.pi / 2 - 2 * np.pi * i / NC2
    return r * np.cos(a), r * np.sin(a)


# deterministic least-crossing layout: identity on top, brute-force the
# remaining 5! orderings for minimum total edge length
from itertools import permutations  # noqa: E402
rest = [i for i in range(NC2) if i != ID2]
best, bord = None, None
for pm in permutations(rest):
    o = [ID2] + list(pm)
    p2 = {c: i for i, c in enumerate(o)}
    tot = sum(np.hypot(*(np.subtract(xy2(p2[c]), xy2(p2[q[nm][c]]))))
              for nm in q for c in range(NC2))
    if best is None or tot < best - 1e-12:
        best, bord = tot, o
ord2 = bord
pos2 = {c: i for i, c in enumerate(ord2)}


for nm, col, rad in (('T', AMB, 0.28), ('U', BLU, -0.28), ('S', RED, 0.0)):
    drawn = set()
    for c in range(NC2):
        i, j = pos2[c], pos2[q[nm][c]]
        if i == j:
            x, y = xy2(i)
            u = np.hypot(x, y)
            ax2.add_patch(plt.Circle((x + 0.15 * x / u, y + 0.15 * y / u),
                                     0.085, fill=False, lw=1.2,
                                     edgecolor=col, alpha=0.9, zorder=3))
            continue
        if nm == 'S':
            if frozenset((i, j)) in drawn:
                continue
            drawn.add(frozenset((i, j)))
            ax2.plot(*zip(xy2(i), xy2(j)), color=col, lw=1.4, alpha=0.85,
                     zorder=2)
            continue
        ax2.add_patch(FancyArrowPatch(xy2(i), xy2(j), color=col, lw=1.5,
                                      arrowstyle='-|>', mutation_scale=9,
                                      shrinkA=8, shrinkB=8, alpha=0.9,
                                      connectionstyle=f'arc3,rad={rad}',
                                      zorder=3))
for c in range(NC2):
    i = pos2[c]
    x, y = xy2(i)
    home = (c == ID2)
    ax2.add_patch(plt.Circle((x, y), 0.10, facecolor='#141822',
                             edgecolor=AMB if home else INK,
                             lw=2.2 if home else 1.1, zorder=6))
    ax2.text(x, y, str(i + 1), color=AMB if home else INK, fontsize=8.5,
             ha='center', va='center', zorder=7)
ax2.set_xlim(-1.55, 1.55)
ax2.set_ylim(-2.35, 1.45)
ax2.set_title('(3)  WHY LEVEL 4, NOT 2', color=INK, fontsize=13, pad=8,
              loc='left')
ax2.text(0, -1.42,
         'reduce mod 2 instead and the group\ncollapses to only  6  sheets:\n\n'
         f'   image = D₅ , order {len(H2)}\n'
         f'   inside PSL(2,𝔽₄) ≅ A₅ , order {len(G2)}\n'
         f'   index {len(G2) // len(H2)}  ≠  12\n\n'
         'so mod 2 is too coarse to see Γ₄₁.\nthe congruence level is exactly 4.',
         color=MUT, fontsize=8.9, ha='center', va='top', linespacing=1.45)

# ============================================== (2) the spectral consequence
evs = []
for fn in ('eigenvalues_final.json', 'scanD_refined.json',
           'scanE_refined.json'):
    d = json.load(open(f'{B792}/{fn}'))
    for e in d['eigenvalues']:
        if e.get('stable', True):
            evs.append((e['r'], e.get('multiplicity', 1),
                        e.get('type', 'NEW')))
sn, uniq = set(), []
for r, m, t in sorted(evs):
    if round(r, 6) not in sn:
        sn.add(round(r, 6))
        uniq.append((r, m, t))
old = [(r, m) for r, m, t in uniq if str(t).startswith('OLD')]
new = [(r, m) for r, m, t in uniq if not str(t).startswith('OLD')]
print(f"  spectrum: {len(uniq)} tones = {len(old)} inherited + {len(new)} own",
      flush=True)
assert len(uniq) == 43 and len(old) == 4

ax3 = fig.add_subplot(gs[1, :])
ax3.set_facecolor(BG)
LO, HI = 3.35, 13.95
PY0, PY1 = 2.28, 2.86           # parent row
for r, m in old:                       # the inheritance drop-lines
    ax3.vlines(r, 1.04, PY0, color='#59616f', lw=0.8, ls=(0, (3, 4)),
               zorder=1)
ax3.hlines(PY0 - 0.13, LO, HI, color=GRD, lw=0.8)
for r, m in old:                       # parent row
    ax3.vlines(r, PY0, PY1, color=PALE, lw=3.0, zorder=4)
    ax3.annotate(f'r = {r:.6f}\nλ = {1 + r * r:.4f}', xy=(r, PY1 + 0.06),
                 color=PALE, fontsize=7.6, ha='center', va='bottom',
                 rotation=90, zorder=5)
for r, m in new:                       # child row, its own
    ax3.vlines(r, 0, 1.00 if m == 1 else 1.46, color=AMB, lw=1.5,
               alpha=0.85, zorder=3)
for r, m in old:                       # child row, inherited
    ax3.vlines(r, 0, 1.56, color=PALE, lw=3.0, zorder=4)
MASK = dict(facecolor=BG, edgecolor='none', pad=2.2)
ax3.text(LO + 0.07, PY1 - 0.05,
         'THE PARENT   PSL(2,O₃)\\H³   —   its 4 tones below r = 13.5',
         color=PALE, fontsize=10.5, va='top', bbox=MASK, zorder=6)
ax3.text(LO + 0.07, 2.07,
         'THE OBJECT   m004   —   all 43 tones     '
         'pale = the 4 it inherited  ·  amber = the 39 that are its own '
         '(raised = doubled)',
         color=AMB, fontsize=10.5, va='top', bbox=MASK, zorder=6)
ax3.set_ylim(-0.10, 4.10)
ax3.set_xlim(LO, HI)
ax3.set_yticks([])
ax3.set_xlabel('r        (the tone is λ = 1 + r²)', color=MUT, fontsize=10)
ax3.tick_params(colors='#5a6272', labelsize=8.5)
for s in ax3.spines.values():
    s.set_color(GRD)
ax3.set_title('(2)  THE SPECTRAL CONSEQUENCE — a cover hears everything its '
              'parent hears, and more',
              color=INK, fontsize=13, pad=9, loc='left')

fig.text(0.5, 0.968, 'PLATE H — THE 12-FOLD COVER',
         color=INK, fontsize=19, ha='center', va='top')
fig.text(0.5, 0.934,
         'the object is a twelve-sheeted unwrapping of one small parent shape '
         '— and four of its forty-three tones are the parent\'s',
         color='#c8cfda', fontsize=11.5, ha='center', va='top')
fig.text(0.5, 0.072,
         'left: the twelve sheets are not a metaphor — they are the twelve cosets, '
         'computed exactly, and the coloured arrows are the parent\'s three motions '
         'shuffling one sheet into the next.\n'
         'bottom: every tone the parent can sing, the object sings too (pale); '
         'the other thirty-nine (amber) are sounds the parent cannot make. '
         'that is what a cover IS.\n'
         'independent check: vol(m004) / vol(parent) = 2.0298832128 / 0.1691569344 '
         '= 12.0000000 — the group index and the geometry agree.',
         color=MUT, fontsize=9.6, ha='center', va='top', linespacing=1.7)

fig.savefig(f'{OUT}/plate_H_cover.png', dpi=145, facecolor=BG)
plt.close(fig)
print("saved plate H", flush=True)
