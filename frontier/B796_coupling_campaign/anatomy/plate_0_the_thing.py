r"""PLATE 0 — THE THING ITSELF, in three dimensions.

Not a spectrum. Not a chart. The space.

1. the knot that is removed          (exact parametric curve, 3D tube)
2. what "complement" means           (the knot thickened and taken out)
3. the packing, as actual spheres    (snappy horoballs, rendered in 3D)
4. the two crystals it is cut from   (the ideal tetrahedra in H^3,
                                      vertices ON the boundary plane
                                      and one at infinity)
Gate 5-Q. Visualization only.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

BG = '#0d0f14'; INK = '#e8e4dc'; AMB = '#e8a15c'; BLU = '#5a9fd4'
OUT = 'frontier/B796_coupling_campaign/anatomy'
plt.rcParams['font.family'] = 'DejaVu Sans'


def knot(t):
    """the figure-eight knot, exact parametrisation"""
    return ((2 + np.cos(2 * t)) * np.cos(3 * t),
            (2 + np.cos(2 * t)) * np.sin(3 * t),
            np.sin(4 * t))


def tube(t, rad=0.22, n=26):
    """a solid tube around the curve (Frenet frame)"""
    P = np.array(knot(t)).T
    d = np.gradient(P, axis=0)
    d /= np.linalg.norm(d, axis=1)[:, None]
    up = np.array([0., 0., 1.])
    n1 = np.cross(d, up); n1 /= np.linalg.norm(n1, axis=1)[:, None]
    n2 = np.cross(d, n1)
    th = np.linspace(0, 2 * np.pi, n)
    X = P[:, None, 0] + rad * (np.cos(th)[None, :] * n1[:, None, 0]
                               + np.sin(th)[None, :] * n2[:, None, 0])
    Y = P[:, None, 1] + rad * (np.cos(th)[None, :] * n1[:, None, 1]
                               + np.sin(th)[None, :] * n2[:, None, 1])
    Z = P[:, None, 2] + rad * (np.cos(th)[None, :] * n1[:, None, 2]
                               + np.sin(th)[None, :] * n2[:, None, 2])
    return X, Y, Z


fig = plt.figure(figsize=(16, 15), facecolor=BG)

# ---------------- 1. THE KNOT ----------------
ax = fig.add_subplot(221, projection='3d', facecolor=BG)
t = np.linspace(0, 2 * np.pi, 700)
X, Y, Z = tube(t, 0.20)
ax.plot_surface(X, Y, Z, color=AMB, shade=True, linewidth=0,
                antialiased=True, alpha=1.0, rstride=2, cstride=2)
ax.set_title('1.  the figure-eight knot\nthe simplest knot that is not a circle',
             color=INK, fontsize=12, pad=2)

# ---------------- 2. THE COMPLEMENT ----------------
ax2 = fig.add_subplot(222, projection='3d', facecolor=BG)
X2, Y2, Z2 = tube(t, 0.62, 30)
ax2.plot_surface(X2, Y2, Z2, color='#3a4a5e', shade=True, linewidth=0.0,
                 alpha=0.42, rstride=2, cstride=2)
Xk, Yk, Zk = tube(t, 0.10)
ax2.plot_surface(Xk, Yk, Zk, color=AMB, shade=True, linewidth=0, alpha=1)
u = np.linspace(0, 2 * np.pi, 40); v = np.linspace(0, np.pi, 22)
R = 3.6
ax2.plot_wireframe(R * np.outer(np.cos(u), np.sin(v)),
                   R * np.outer(np.sin(u), np.sin(v)),
                   R * np.outer(np.ones_like(u), np.cos(v)),
                   color='#46536a', linewidth=0.5, rstride=3, cstride=3)
ax2.set_title('2.  the OBJECT is everything else\nthe knot (amber) and a tube around it '
              'are DELETED;\nwhat remains inside the sphere is the space we study',
              color=INK, fontsize=12, pad=2)

# ---------------- 3. THE PACKING, IN 3D ----------------
ax3 = fig.add_subplot(223, projection='3d', facecolor=BG)
try:
    import snappy
    M = snappy.Manifold('m004')
    cn = M.cusp_neighborhood(); cn.set_displacement(cn.reach(), 0)
    hb = [h for h in cn.horoballs(0.02)]
    tau_im = 3.4641016151377544
    balls = []
    for h in hb:
        c = complex(h['center']); r = float(h['radius'])
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                balls.append((c.real + dx, c.imag + dy * tau_im, r))
    balls = [b for b in balls
             if -0.75 < b[0] < 0.75 and -0.75 < b[1] < 0.75]
    balls.sort(key=lambda b: -b[2])
    uu = np.linspace(0, 2 * np.pi, 22); vv = np.linspace(0, np.pi, 13)
    su, sv = np.meshgrid(uu, vv)
    for (cx, cy, r) in balls[:170]:
        shade = 0.35 + 0.65 * (r / 0.5) ** 0.4
        col = (0.33 + 0.55 * shade, 0.55 + 0.28 * shade, 0.80)
        ax3.plot_surface(cx + r * np.cos(su) * np.sin(sv),
                         cy + r * np.sin(su) * np.sin(sv),
                         r + r * np.cos(sv),
                         color=col, shade=True, linewidth=0,
                         alpha=0.97, rstride=1, cstride=1)
    n_drawn = min(170, len(balls))
except Exception as e:
    n_drawn = 0
    print('horoball panel failed:', e)
ax3.set_title(f'3.  the same object, seen from inside the missing knot\n'
              f'spheres resting on the horizon — {n_drawn} of them, '
              f'radii exactly 1/(2N),\nN a norm in the object\'s number field',
              color=INK, fontsize=12, pad=2)
ax3.set_zlim(0, 0.62); ax3.set_xlim(-0.62, 0.62); ax3.set_ylim(-0.62, 0.62)
ax3.set_box_aspect((1, 1, 0.5))

# ---------------- 4. THE TWO CRYSTALS ----------------
ax4 = fig.add_subplot(224, projection='3d', facecolor=BG)
z = complex(0.5, np.sqrt(3) / 2)          # the regular ideal shape
TOP = 2.3
for shift, col, alpha in [(0.0, BLU, 0.22), (0.5, AMB, 0.22)]:
    v0 = np.array([shift, 0.0]); v1 = np.array([shift + 1, 0.0])
    v2 = np.array([shift + z.real, z.imag])
    faces = []
    for (a, b) in [(v0, v1), (v1, v2), (v2, v0)]:
        faces.append([[a[0], a[1], 0], [b[0], b[1], 0],
                      [b[0], b[1], TOP], [a[0], a[1], TOP]])
    faces.append([[v0[0], v0[1], TOP], [v1[0], v1[1], TOP], [v2[0], v2[1], TOP]])
    ax4.add_collection3d(Poly3DCollection(faces, facecolor=col, alpha=alpha,
                                          edgecolor=col, linewidths=1.1))
    ax4.plot(*zip(*[(v[0], v[1], 0) for v in (v0, v1, v2, v0)]),
             color=col, lw=2.2)
    for v in (v0, v1, v2):
        ax4.scatter([v[0]], [v[1]], [0], color=col, s=36)
        ax4.plot([v[0], v[0]], [v[1], v[1]], [0, TOP], color=col,
                 lw=0.7, alpha=0.5, ls=':')
xs = np.linspace(-0.4, 2.4, 2); ys = np.linspace(-0.4, 1.3, 2)
XX, YY = np.meshgrid(xs, ys)
ax4.plot_surface(XX, YY, np.zeros_like(XX), color='#151a22', alpha=0.9)
ax4.set_title('4.  the two crystals the space is cut from\n'
              'two IDEAL tetrahedra: every corner is infinitely far away\n'
              '(three on the horizon, one straight up) — shape z = e^{iπ/3}, exactly',
              color=INK, fontsize=12, pad=2)
ax4.set_zlim(0, TOP); ax4.set_xlim(-0.3, 2.0); ax4.set_ylim(-0.3, 1.4)
ax4.set_box_aspect((1.6, 1.0, 1.5))

for a in (ax, ax2, ax3, ax4):
    a.set_axis_off()
for a in (ax, ax2):
    a.set_box_aspect((1, 1, 0.8))
ax3.set_box_aspect((1, 1, 0.5))     # spheres must look like spheres
ax4.set_box_aspect((1.6, 1.0, 1.5))
ax.view_init(28, 40); ax2.view_init(22, 35)
ax3.view_init(13, -62); ax4.view_init(16, -72)

fig.suptitle('PLATE 0 — THE THING ITSELF\n'
             'before any spectrum, any chart: this is the space',
             color=INK, fontsize=19, y=0.975)
fig.text(0.5, 0.015,
         'volume 2.0298832128…  ·  one cusp  ·  two ideal tetrahedra  ·  zero free parameters.\n'
         'panels 1–2 live in ordinary space; panels 3–4 are the same object in its own '
         'hyperbolic geometry, seen from the deleted knot looking out.',
         color='#9aa3b2', fontsize=10, ha='center')
fig.tight_layout(rect=[0.0, 0.04, 1.0, 0.935])
fig.savefig(f'{OUT}/plate_0_the_thing.png', dpi=140, facecolor=BG)
print('saved plate_0_the_thing.png')
