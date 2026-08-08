r"""PLATE E — THE BODY.

The actual shape of m004 (the figure-eight knot complement).

  (1) the horoball packing of the MAXIMAL cusp, drawn in the cusp
      lattice Lambda = Z + Z*2sqrt(-3), with a zoom into one gap so the
      cascade of smaller balls is visible.  Source: snappy's
      CuspNeighborhood.horoballs() at maximal displacement.
  (2) the two ideal tetrahedra, as the shape-parameter triangle
      (0, 1, z) in the plane.  Source: M.tetrahedra_shapes('rect').

Everything drawn is computed.  Cross-check: the horoball centres and
radii are re-derived independently from the B792 Riley holonomy group
Gamma_41 = <A, B> that the Maass solver actually uses (hejhal_m004), by
enumerating the cusp points a/c of its group elements.  The two agree
EXACTLY -- same radii 1/(2N), same centres, no fitted offset -- for
every N = |c|^2 <= 4.

NOTE ON A FIXED BUG.  An earlier version of this script reported the
cross-check as FAILING.  That was a torus boundary-identification bug,
not a real disagreement: the two sides reduced points onto the cusp
torus with different conventions, so a centre sitting on the seam was
counted once as x = 0 and once as x = 1 (likewise y = 0 vs y = 2sqrt3).
Identifying the seam -- which is what "torus" means -- makes the two
point sets literally equal.  See CHECK below.

Gate 5-Q.  Visualization only; no claim.
"""
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import mpmath
import numpy as np
import snappy
from matplotlib.collections import EllipseCollection
from matplotlib.colors import LinearSegmentedColormap, Normalize

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import build_moves, find_cusp_lattice, reduced_words, wmat  # noqa: E402

OUT = 'frontier/B796_coupling_campaign/anatomy'
plt.rcParams['font.family'] = 'DejaVu Sans'
BG = '#0d0f14'
INK = '#e8e4dc'
AMBER = '#e8a15c'
BLUE = '#4a90c4'
RED = '#d64545'
MUTED = '#9aa3b2'
GRID = '#3a4150'

# small balls sink toward the background, big balls burn amber
BALL = LinearSegmentedColormap.from_list(
    'ball', ['#151b28', '#1d3253', '#2f6fa8', '#4a90c4', '#8fbcda', '#e8a15c'])

CUT_MAIN = 0.010        # smallest radius drawn in the wide view
CUT_ZOOM = 0.004        # smallest radius drawn in the zoom (~20 s to fetch)
TOL = 1e-6

# ---------------------------------------------------------------- data
M = snappy.Manifold('m004')
VOL = M.volume()
SHAPES = M.tetrahedra_shapes('rect')
print(f'm004: vol={VOL}  ntet={M.num_tetrahedra()}  cusps={M.num_cusps()}',
      flush=True)
print(f'  solution type: {M.solution_type()}', flush=True)
print(f'  shapes: {SHAPES}', flush=True)

cn = M.cusp_neighborhood()
cn.set_displacement(cn.reach(), 0)          # the MAXIMAL cusp
tr = cn.translations(0)
print(f'  maximal cusp: translations {tr}  area {cn.volume(0)*2}', flush=True)

# snappy hands back the cusp with meridian = i and longitude = 2sqrt3
# (real).  Multiplying the plane by i turns that into exactly the lattice
# used everywhere else in this campaign: Lambda = Z + Z*2sqrt(-3).
TAU, _, _, BAD = find_cusp_lattice()        # from the Maass solver
T2 = TAU.imag                               # 2*sqrt(3) = 3.4641016151
assert BAD == 0
assert abs(abs(complex(tr[0])) - 1.0) < 1e-12
assert abs(float(tr[1].real) - T2) < 1e-9, (tr[1], T2)
assert abs(T2 - 2 * np.sqrt(3)) < 1e-12


def fetch(cut):
    hb = cn.horoballs(cut)
    c = np.array([1j * complex(h['center']) for h in hb])
    r = np.array([float(h['radius']) for h in hb])
    return np.mod(c.real, 1.0), np.mod(c.imag, T2), r, len(hb)


CX, CY, RAD, NMAIN = fetch(CUT_MAIN)
print(f'  {NMAIN} horoballs with r >= {CUT_MAIN};  r_max = {RAD.max()}',
      flush=True)
ZX, ZY, ZR, NZOOM = fetch(CUT_ZOOM)
print(f'  {NZOOM} horoballs with r >= {CUT_ZOOM} (for the zoom)', flush=True)


def tile(cx, cy, rad, xlo, xhi, ylo, yhi):
    """Lattice-translate the fundamental-domain balls over a window.

    The copy range must be wide enough that any ball whose DISC meets
    the window is included -- the largest radius is 1/2, so centres up
    to 1/2 outside the window still put ink in it.  Too narrow a range
    leaves unfilled shelves at the edges.
    """
    pad = rad.max() + 1e-9
    m0, m1 = int(np.floor(xlo - pad)) - 1, int(np.ceil(xhi + pad)) + 1
    k0, k1 = int(np.floor((ylo - pad) / T2)) - 1, int(np.ceil((yhi + pad) / T2)) + 1
    px, py, pr = [], [], []
    for m in range(m0, m1 + 1):
        for k in range(k0, k1 + 1):
            X, Y = cx + m, cy + k * T2
            keep = ((X + rad > xlo) & (X - rad < xhi)
                    & (Y + rad > ylo) & (Y - rad < yhi))
            px.append(X[keep])
            py.append(Y[keep])
            pr.append(rad[keep])
    px, py, pr = (np.concatenate(a) for a in (px, py, pr))
    o = np.argsort(pr)          # ascending: big balls drawn last, on top
    return px[o], py[o], pr[o]


# ---- independent re-derivation from the B792 group -------------------
# The horoball at the cusp point a/c is the image of the horoball at
# infinity under an element [[a, b], [c, d]] of Gamma_41, and has
# Euclidean radius 1/(2|c|^2).  So: enumerate the group's cusp points.
#
# Both sides are reduced onto the cusp torus with the SAME convention,
# including the seam: a coordinate within TOL of the period is snapped
# to 0.  Without that, points on the seam are double-counted and the
# comparison spuriously fails.

def key(p):
    x = float(np.mod(p.real, 1.0))
    y = float(np.mod(p.imag, T2))
    if min(x, 1.0 - x) < TOL:
        x = 0.0
    if min(y, T2 - y) < TOL:
        y = 0.0
    return (round(x, 6), round(y, 6))


def group_cusps(maxlen, cmax=2.3):
    d = {}
    for w in reduced_words(maxlen):
        Mx = wmat(w)
        c = Mx[1, 0]
        if abs(c) < 1e-12 or abs(c) > cmax:
            continue
        d.setdefault(int(round(abs(c) ** 2)), set()).add(key(complex(Mx[0, 0] / c)))
    return d


snap = {}
for x, y, r in zip(CX, CY, RAD):
    snap.setdefault(int(round(1.0 / (2.0 * r))), set()).add(key(complex(x, y)))

GRP = group_cusps(6)                       # words of length <= 6
NS = [1, 3, 4]                             # the norms with |c| <= 2.2
CHECK = []
for n in NS:
    g, s = GRP.get(n, set()), snap.get(n, set())
    CHECK.append((n, len(s), len(g), g == s))
    print(f'  N=|c|^2={n}: radius 1/{2*n}  snappy {len(s)} centres, '
          f'group {len(g)} centres, identical={g == s}', flush=True)
ALL_OK = all(c[3] for c in CHECK)

# the solver's OWN move list (words of length <= 5) is an exact subset:
# word-length truncation finds only 8 of the 12 norm-4 cusps.
bm = {}
for Mx in build_moves():
    a, _ = Mx[0]
    c, _ = Mx[1]
    bm.setdefault(int(round(abs(c) ** 2)), set()).add(key(complex(a / c)))
BM = [(n, len(bm.get(n, set()))) for n in NS]
BM_SUB = all(bm.get(n, set()) <= snap.get(n, set()) for n in NS)
print(f'  build_moves() (|w|<=5): {BM}  exact subset of snappy: {BM_SUB}',
      flush=True)

# every radius is 1/(2N) for N an Eisenstein norm a^2 - ab + b^2
EIS = {a * a - a * b + b * b for a in range(-80, 81) for b in range(-80, 81)}
uradii = sorted(set(np.round(RAD, 12)))[::-1]
NORMS = [int(round(1 / (2 * r))) for r in uradii]
assert all(abs(1 / (2 * r) - round(1 / (2 * r))) < 1e-7 for r in uradii)
assert all(n in EIS for n in NORMS)
print(f'  {len(uradii)} distinct radii, all of the form 1/(2N) with N an '
      f'Eisenstein norm; N up to {max(NORMS)}', flush=True)

# the regular ideal tetrahedron: z = exp(i pi/3), vol = Cl_2(pi/3)
Z_REG = np.exp(1j * np.pi / 3)
assert all(abs(complex(z) - Z_REG) < 1e-9 for z in SHAPES)
CL2 = float(mpmath.clsin(2, mpmath.pi / 3))                 # 1.0149416064...
LOB = float(3 * (mpmath.clsin(2, 2 * mpmath.pi / 3) / 2))   # 3*Lambda(pi/3)
assert abs(CL2 - LOB) < 1e-12, (CL2, LOB)
assert abs(2 * CL2 - VOL) < 1e-9, (2 * CL2, VOL)
print(f'  Cl2(pi/3) = {CL2!r}   2*Cl2(pi/3) = {2*CL2!r}   snappy vol = {VOL}',
      flush=True)

# ---- the gap we zoom into --------------------------------------------
# Three radius-1/2 balls at (0,0), (1/2, sqrt3/2), (-1/2, sqrt3/2) are
# mutually tangent, and the radius-1/6 ball at (0, 1/sqrt3) is inscribed
# in the curvilinear triangle they leave.  Horoballs at p1, p2 with
# radii r1, r2 are tangent exactly when |p1 - p2|^2 = 4 r1 r2 (NOT
# r1 + r2 -- which is why small discs may sit inside big ones' shadows).
# The zoom strip holds TWO such gaps: the up-pointing triangle cut by
# (0,0), (1/2, sqrt3/2), (-1/2, sqrt3/2) with the r=1/6 ball at
# (0, 1/sqrt3), and the down-pointing one cut by (1/2, sqrt3/2),
# (-1/2, sqrt3/2), (0, sqrt3) with the r=1/6 ball at (0, 2/sqrt3).
TRI = [([(0.0, 0.0), (0.5, T2 / 4), (-0.5, T2 / 4)], (0.0, 1 / np.sqrt(3))),
       ([(0.5, T2 / 4), (-0.5, T2 / 4), (0.0, T2 / 2)], (0.0, 2 / np.sqrt(3)))]
for big, ins in TRI:
    for i, p in enumerate(big):
        for q in big[i + 1:]:
            d2 = (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2
            assert abs(d2 - 4 * 0.5 * 0.5) < 1e-9, (p, q, d2)
        d2 = (p[0] - ins[0]) ** 2 + (p[1] - ins[1]) ** 2
        assert abs(d2 - 4 * 0.5 * (1 / 6)) < 1e-9, (p, ins, d2)
    # the inscribed ball must really be one of snappy's r=1/6 horoballs
    assert key(complex(*ins)) in snap[3], ins
print('  gap geometry verified: 2 triangles of mutually tangent r=1/2 balls, '
      'each with an r=1/6 ball inscribed (and present in snappy\'s list)',
      flush=True)

# a tall strip containing both triangles
ZXL, ZXH = -0.30, 0.30
ZYL, ZYH = 0.30, 1.44

# ------------------------------------------------------------- figure
XLO, XHI = -1.0, 2.0
YLO, YHI = 0.0, T2
px, py, pr = tile(CX, CY, RAD, XLO, XHI, YLO, YHI)
qx, qy, qr = tile(ZX, ZY, ZR, ZXL, ZXH, ZYL, ZYH)
print(f'  drawing {len(pr)} discs (wide) + {len(qr)} discs (zoom)', flush=True)

fig = plt.figure(figsize=(17.0, 9.9), facecolor=BG)
gs = fig.add_gridspec(2, 3, width_ratios=[1.0, 0.50, 1.28],
                      height_ratios=[1.0, 0.58],
                      left=0.045, right=0.985, top=0.845, bottom=0.150,
                      wspace=0.11, hspace=0.17)

NRM = Normalize(np.log10(CUT_ZOOM), np.log10(0.5))


def draw_outlines(axis, bx, by, br):
    """Every horoball as a bare circle -- including the hidden ones.

    At the MAXIMAL cusp the shadows of the r >= 1/6 balls already cover
    essentially the whole plane (4 x pi/4 + 8 x pi/36 = 3.84 against a
    torus of area 2sqrt3 = 3.46), so the filled, occlusion-correct view
    cannot show anything smaller: the cascade is really there, it is
    just underneath.  Drawing boundary circles instead of fills is the
    usual horoball-diagram convention and exposes it.  This panel is a
    diagram of the SET of horoballs, not a photograph of it.
    """
    axis.add_collection(EllipseCollection(
        2 * br, 2 * br, np.zeros_like(br), units='xy',
        offsets=np.column_stack([bx, by]), offset_transform=axis.transData,
        facecolors='none', edgecolors=BALL(NRM(np.log10(br))),
        linewidths=0.45, alpha=0.9))


def draw_balls(axis, bx, by, br, rim_above):
    """Fill discs in ascending radius so big ones occlude small ones.

    Edges must ride on the SAME collection as the fill: a separate rim
    pass would paint outlines of hidden balls through the discs in
    front of them.
    """
    colr = BALL(NRM(np.log10(br)))
    sel_small = br <= rim_above
    for sel, ec, lw in ((sel_small, 'none', 0.0), (~sel_small, '#0d0f14', 0.7)):
        if not sel.any():
            continue
        axis.add_collection(EllipseCollection(
            2 * br[sel], 2 * br[sel], np.zeros_like(br[sel]), units='xy',
            offsets=np.column_stack([bx[sel], by[sel]]),
            offset_transform=axis.transData, facecolors=colr[sel],
            edgecolors=ec, linewidths=lw))


# ---------------- (1) THE HOROBALL PACKING ----------------
ax = fig.add_subplot(gs[:, 0])
ax.set_facecolor(BG)
draw_balls(ax, px, py, pr, 0.045)

ax.add_patch(plt.Rectangle((0, 0), 1, T2, fill=False, ec='#f2ede3', lw=1.35,
                           ls=(0, (5, 3)), zorder=7, alpha=0.92))
ax.annotate('one cusp torus\nΛ = ℤ + ℤ·2√−3', xy=(0.5, T2 - 0.30),
            color='#f2ede3', fontsize=9.0, ha='center', va='center', zorder=8,
            bbox=dict(boxstyle='round,pad=0.32', fc='#0d0f14', ec='#f2ede3',
                      lw=0.7, alpha=0.9))
ax.annotate('r = ½\n(N = 1)', xy=(0.5, T2 / 4), color='#20130a', fontsize=8.6,
            ha='center', va='center', zorder=9, weight='bold')

ax.set_xlim(XLO, XHI)
ax.set_ylim(YLO, YHI)
ax.set_aspect('equal')
ax.set_xticks([-1, 0, 1, 2])
ax.set_yticks([0, T2 / 4, T2 / 2, 3 * T2 / 4, T2])
ax.set_yticklabels(['0', '√3/2', '√3', '3√3/2', '2√3'])
ax.tick_params(colors='#5a6272', labelsize=8)
for s in ax.spines.values():
    s.set_color(GRID)
ax.set_title('THE HOROBALL PACKING — the maximal cusp, seen from infinity\n'
             f'{NMAIN} balls of radius ≥ {CUT_MAIN} per torus, tiled 3×',
             color=INK, fontsize=11.5, pad=9, loc='left')

# mark on the wide view where the zoom panel comes from
ax.add_patch(plt.Rectangle((ZXL, ZYL), ZXH - ZXL, ZYH - ZYL, fill=False,
                           ec='#8fbcda', lw=1.1, zorder=8))

# ---------------- THE ZOOM ----------------
axz = fig.add_subplot(gs[0, 1])
axz.set_facecolor(BG)
draw_outlines(axz, qx, qy, qr)
for _, ins in TRI:
    axz.annotate('⅙', xy=ins, color='#8fbcda', fontsize=9.5, ha='center',
                 va='center', weight='bold', zorder=9)
axz.set_xlim(ZXL, ZXH)
axz.set_ylim(ZYL, ZYH)
axz.set_aspect('equal')
axz.set_xticks([])
axz.set_yticks([])
for s in axz.spines.values():
    s.set_color('#8fbcda')
    s.set_linewidth(1.1)
axz.set_title('THE GAP, MAGNIFIED\n'
              f'outlines — incl. hidden balls, to r = {CUT_ZOOM}',
              color='#8fbcda', fontsize=9.4, pad=8, loc='left')

cax = fig.add_axes([0.052, 0.118, 0.235, 0.0125])
sm = plt.cm.ScalarMappable(norm=NRM, cmap=BALL)
cb = fig.colorbar(sm, cax=cax, orientation='horizontal')
cb.set_ticks(np.log10([0.5, 1 / 6, 1 / 8, 1 / 14, 0.03, CUT_MAIN, CUT_ZOOM]))
cb.set_ticklabels(['½', '⅙', '⅛', '1/14', '.03', f'{CUT_MAIN}', f'{CUT_ZOOM}'])
cb.ax.tick_params(colors='#5a6272', labelsize=7.2, length=2)
cb.outline.set_edgecolor(GRID)
cb.set_label('horoball radius = 1/2N,  N an Eisenstein norm a²−ab+b²',
             color=MUTED, fontsize=8.2, labelpad=3)

# ---------------- (2) THE TWO IDEAL TETRAHEDRA ----------------
axt = fig.add_subplot(gs[0, 2])
axt.set_facecolor(BG)
for j, (z, dx) in enumerate([(complex(SHAPES[0]), 0.0),
                             (complex(SHAPES[1]), 1.72)]):
    xs = np.array([0.0, 1.0, z.real]) + dx
    ys = np.array([0.0, 0.0, z.imag])
    axt.fill(xs, ys, color=AMBER, alpha=0.14, zorder=1)
    axt.plot(np.append(xs, xs[0]), np.append(ys, ys[0]), color=AMBER,
             lw=1.7, zorder=3)
    axt.scatter(xs, ys, s=48, facecolors=BG, edgecolors=INK, linewidths=1.2,
                zorder=5)
    for xx, yy, lab, va, off in [(xs[0], ys[0], '0', 'top', -10),
                                 (xs[1], ys[1], '1', 'top', -10),
                                 (xs[2], ys[2], 'z', 'bottom', 8)]:
        axt.annotate(lab, (xx, yy), color=INK, fontsize=11, ha='center',
                     va=va, xytext=(0, off), textcoords='offset points')
    # the three interior angles of (0, 1, z) = the dihedral angles
    a0 = np.degrees(np.angle(z))
    a1 = np.degrees(np.pi - np.angle(z - 1))
    a2 = 180.0 - a0 - a1
    for xx, yy, ang, ox, oy in [(xs[0], ys[0], a0, 21, 10),
                                (xs[1], ys[1], a1, -21, 10),
                                (xs[2], ys[2], a2, 0, -25)]:
        axt.annotate(f'{ang:.0f}°', (xx, yy), color=BLUE, fontsize=8.6,
                     ha='center', va='center', xytext=(ox, oy),
                     textcoords='offset points')
    axt.annotate(f'tetrahedron {j}\nz = {z.real:.9f} + {z.imag:.9f} i',
                 (dx + 0.5, -0.26), color=MUTED, fontsize=8.4, ha='center',
                 va='top')
axt.annotate('≡', (1.36, 0.40), color=INK, fontsize=21, ha='center',
             va='center')
axt.set_xlim(-0.36, 3.10)
axt.set_ylim(-0.60, 1.16)
axt.set_aspect('equal')
axt.set_xticks([])
axt.set_yticks([])
for s in axt.spines.values():
    s.set_color(GRID)
axt.set_title('THE TWO IDEAL TETRAHEDRA — the whole manifold, unglued\n'
              'each drawn as its shape parameter: the triangle (0, 1, z)',
              color=INK, fontsize=11.5, pad=9, loc='left')

# ---------------- the numbers ----------------
axn = fig.add_subplot(gs[1, 1:])
axn.set_facecolor(BG)
axn.set_xticks([])
axn.set_yticks([])
for s in axn.spines.values():
    s.set_color(GRID)

y = [0.935]


def line(txt, c=INK, fs=9.0, dy=0.098, x=0.022, mono=False):
    axn.text(x, y[0], txt, color=c, fontsize=fs, transform=axn.transAxes,
             va='top', family='DejaVu Sans Mono' if mono else 'DejaVu Sans')
    y[0] -= dy


# line budget: the dy's below must sum to well under 1.0 or the last
# lines fall out of the panel box.
line('z₀ = z₁ = e^(iπ/3) = (1 + i√3)/2 = 1 + ω   —   a UNIT in the Eisenstein '
     'integers ℤ[ω];  all six dihedral angles exactly 60°', AMBER, 9.4, 0.098)
line(f'vol = Cl₂(π/3) = {CL2:.10f}    ×2 = {2*CL2:.10f} = vol(m004)   '
     f'[snappy: {VOL}]', INK, 8.8, 0.088)
line('horoballs are tangent when |p₁−p₂|² = 4r₁r₂ (not r₁+r₂) — which is why a '
     'small disc can sit inside a big one\'s shadow', MUTED, 8.4, 0.115)
line('CROSS-CHECK — snappy\'s horoballs vs the B792 group Γ₄₁ = ⟨A, B⟩, via its '
     'cusp points a/c', BLUE, 9.2, 0.092)
line('   N = |c|²                 ' + '  '.join(f'{c[0]:>7d}' for c in CHECK),
     MUTED, 8.6, 0.072, mono=True)
line('   radius 1/2N              ' + '  '.join(f'{"1/%d" % (2*c[0]):>7s}'
                                                for c in CHECK),
     MUTED, 8.6, 0.072, mono=True)
line('   snappy horoballs/torus   ' + '  '.join(f'{c[1]:>7d}' for c in CHECK),
     MUTED, 8.6, 0.072, mono=True)
line('   Γ₄₁ cusp points, |w|≤6   ' + '  '.join(f'{c[2]:>7d}' for c in CHECK),
     MUTED, 8.6, 0.072, mono=True)
line('   centres identical?       ' + '  '.join(
    f'{("yes" if c[3] else "NO"):>7s}' for c in CHECK),
    '#7fb2d6' if ALL_OK else RED, 8.6, 0.092, mono=True)
line('the two agree EXACTLY — same radii, same centres, no fitted offset.'
     if ALL_OK else 'MISMATCH — see stdout', '#7fb2d6' if ALL_OK else RED,
     8.8, 0.078)
line(f'(the solver\'s own move list, words |w|≤5, finds '
     f'{"/".join(str(b[1]) for b in BM)} of {"/".join(str(c[1]) for c in CHECK)}'
     f' — an exact subset: {"yes" if BM_SUB else "no"}. word-length truncation,'
     ' not a discrepancy.)', MUTED, 8.0, 0.0)

fig.suptitle('PLATE E — THE BODY\n'
             'the shape of the absence: how the missing knot packs against '
             'itself, and the two identical bricks the whole space is cut from',
             color=INK, fontsize=17, y=0.972, ha='center')
fig.text(0.5, 0.012,
         'left: looking straight down the knot\'s missing thread. each disc is a '
         'ball of "the part of the space that runs off to infinity" — drawn as an '
         'eye at infinity would see it, the big ones hiding the rest.\n'
         'middle: the same region in outline, so the hidden ones show — between '
         'any three balls that touch there are infinitely many smaller ones, '
         'their sizes locked to a number pattern.\n'
         'right: cut m004 along its two pieces and you get two copies of the '
         'single most symmetric shape hyperbolic space allows — nothing was '
         'chosen, the geometry forces it.',
         color=MUTED, fontsize=9.0, ha='center', va='bottom')

fig.savefig(f'{OUT}/plate_E_body.png', dpi=145, facecolor=BG)
plt.close(fig)
print('saved plate E', flush=True)
