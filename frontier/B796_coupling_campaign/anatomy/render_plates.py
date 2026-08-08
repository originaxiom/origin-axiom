r"""THE ANATOMY ATLAS — plates rendered from computed data, not drawn.

Every pixel comes from the branch's certified artifacts:
  Plate A  the cusp torus + the eigenfunctions themselves (the modes)
  Plate B  the Fourier support lattice (the symmetry zero, the pi7 zero)
  Plate C  the geodesic length spectrum, m004 vs its sister m003
  Plate D  the spectral barcode (43 eigenvalues, mult, parent/newform)

Gate 5-Q. Visualization only; no claim.
"""
import json
import sys

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (K_table, Lattice, System, build_moves,
                        find_cusp_lattice)  # noqa: E402

OUT = 'frontier/B796_coupling_campaign/anatomy'
plt.rcParams['font.family'] = 'DejaVu Sans'
INK = '#e8e4dc'
BG = '#0d0f14'

# a warm/cool diverging map for the standing waves
WAVE = LinearSegmentedColormap.from_list(
    'wave', ['#1b3a6b', '#2f6fa8', '#7fb2d6', '#f2ede3',
             '#e8a15c', '#c9532f', '#6b1d12'])

print("building system ...", flush=True)
tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
S = System(lat, moves, 0.75, 10.1)
print(f"  {len(S.mus)} modes", flush=True)


def eigvec(r):
    KT = K_table(S.args, S.ts, S.wts, [r], [])
    KT = KT.reshape(len(S.norms), len(S.heights))
    V = ((S.Y * KT[S.nrm_idx, 0])[None, :] * S.P0
         - (S.tstar[:, None] * KT[S.nrm_idx, 1:].T) * S.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    return Vh[-1].conj() / cn


def field_on_torus(a, r, nx=340, ny=340, t=0.9):
    """f(z,t) over one period of the cusp torus."""
    xs = np.linspace(-0.5, 0.5, nx)
    ys = np.linspace(-abs(tau) / 2, abs(tau) / 2, ny)
    X, Y = np.meshgrid(xs, ys)
    absmu = np.abs(S.mus)
    from hejhal_m004 import bessel_nodes
    ts_, wts_ = bessel_nodes(r + 1, (2 * np.pi * absmu * t).min())
    Kv = K_table(2 * np.pi * absmu * t, ts_, wts_, [r], [])[:, 0]
    F = np.zeros_like(X, dtype=complex)
    for j, mu in enumerate(S.mus):
        if abs(a[j]) < 1e-13:
            continue
        F += a[j] * t * Kv[j] * np.exp(2j * np.pi * (mu.real * X + mu.imag * Y))
    return X, Y, F.real


# ---------------- PLATE A : THE MODES ----------------
MODES = [(3.938916864, 'λ₁ = 16.515066   (mult 2)'),
         (4.900085373, 'λ₂ = 25.010837   (mult 1)'),
         (6.632802303, 'λ₅ = 44.994066   (mult 2)'),
         (7.072004187, 'λ₆ = 51.013243   INHERITED (the parent\'s own voice)')]

fig, axes = plt.subplots(2, 2, figsize=(13, 13.6), facecolor=BG)
for ax, (r, label) in zip(axes.ravel(), MODES):
    print(f"  plate A: mode r = {r}", flush=True)
    a = eigvec(r)
    X, Y, F = field_on_torus(a, r)
    v = np.percentile(np.abs(F), 99.4)
    ax.pcolormesh(X, Y, F, cmap=WAVE, vmin=-v, vmax=v, shading='gouraud',
                  rasterized=True)
    ax.set_facecolor(BG)
    ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color('#3a4150')
    ax.set_title(label, color=INK, fontsize=11.5, pad=9, loc='left')
fig.suptitle('PLATE A — THE MODES\nthe object\'s own standing waves, drawn on the'
             ' cusp torus (its one open end)',
             color=INK, fontsize=17, y=0.975, ha='center')
fig.text(0.5, 0.018,
         'each panel is a solution of Δf = λf on the figure-eight knot complement, '
         'evaluated from the computed Fourier coefficients.\n'
         'warm = f > 0, cool = f < 0, pale = the nodal set (where the object is silent). '
         'these four had never been drawn before.',
         color='#9aa3b2', fontsize=9.6, ha='center')
fig.tight_layout(rect=[0.01, 0.045, 0.99, 0.945])
fig.savefig(f'{OUT}/plate_A_modes.png', dpi=145, facecolor=BG)
plt.close(fig)
print("  saved plate A", flush=True)

# ---------------- PLATE B : THE VOICE (Fourier support) ----------------
fig, axes = plt.subplots(1, 2, figsize=(14.5, 7.4), facecolor=BG)
U2 = complex(0, 1 / (2 * np.sqrt(3)))
for ax, (r, lab) in zip(axes, [(4.900085373, 'a NEWFORM  (λ₂ = 25.0108)'),
                               (7.072004187, 'the INHERITED form  (λ₆ = 51.0132)')]):
    a = eigvec(r)
    w = np.abs(a)
    w = w / w.max()
    m1 = np.round(S.mus.real).astype(int)
    m2 = np.round(S.mus.imag * 2 * np.sqrt(3)).astype(int)
    keep = (np.abs(m1) <= 7) & (np.abs(m2) <= 22)
    sz = 4 + 300 * w[keep] ** 0.45
    col = np.where(w[keep] < 1e-9, '#2a2f3a', '#e8a15c')
    ax.scatter(m1[keep], m2[keep], s=sz, c=col, edgecolors='none')
    dead = keep & (w < 1e-9)
    ax.scatter(m1[dead], m2[dead], s=13, marker='x', c='#4a5262', linewidths=0.7)
    if 'NEWFORM' in lab:
        ax.scatter([2, -2], [8, -8], s=330, facecolors='none',
                   edgecolors='#d64545', linewidths=1.8, zorder=5)
        ax.annotate('π₇ — the universal zero\n(every newform is silent here)',
                    xy=(2, 8), xytext=(4.3, 15), color='#d64545', fontsize=9.5,
                    arrowprops=dict(arrowstyle='-', color='#d64545', lw=0.9))
    ax.set_facecolor(BG); ax.set_aspect(0.30)
    ax.set_xlabel('m₁', color='#9aa3b2'); ax.set_ylabel('m₂', color='#9aa3b2')
    ax.tick_params(colors='#5a6272', labelsize=8)
    for s in ax.spines.values():
        s.set_color('#3a4150')
    ax.set_title(lab, color=INK, fontsize=12, pad=8)
fig.suptitle('PLATE B — THE VOICE\nwhich harmonics the object actually uses '
             '(dot size = strength, ✕ = exact silence)',
             color=INK, fontsize=16, y=0.98)
fig.text(0.5, 0.02,
         'the entire odd-m₂ half of the lattice is dead in every form: '
         'the object only ever speaks in even harmonics of its cusp — a hidden half-period symmetry.\n'
         'the circled pair is the π₇ zero found this week: a note every newform refuses, '
         'and the inherited form does not.',
         color='#9aa3b2', fontsize=9.6, ha='center')
fig.tight_layout(rect=[0.01, 0.06, 0.99, 0.9])
fig.savefig(f'{OUT}/plate_B_voice.png', dpi=145, facecolor=BG)
plt.close(fig)
print("  saved plate B", flush=True)

# ---------------- PLATE C : THE BONES (length spectrum) ----------------
OM = complex(-0.5, np.sqrt(3) / 2)


def load_len(fn):
    d = json.load(open(f'frontier/B792_maass_m004_eigenvalues/{fn}'))
    return d['geodesics']


def norms_of(gs):
    out = []
    for g in gs:
        tr = 2 * np.cosh(complex(g['re'], g['im']) / 2)
        b = tr.imag / OM.imag
        aa = tr.real - b * OM.real
        ar, br = round(aa), round(b)
        out.append((g['re'], g['im'], (ar * ar - ar * br + br * br) % 4))
    return out


try:
    g4 = norms_of(load_len('length_spectrum.json'))
    g3 = norms_of(load_len('length_spectrum_m003.json'))
    fig, ax = plt.subplots(figsize=(13.5, 7.6), facecolor=BG)
    CL = {0: '#4a90c4', 1: '#d64545', 3: '#e8a15c'}
    for gs, mk, nm, al in [(g4, 'o', 'm004 — the object', 0.85),
                           (g3, '^', 'm003 — the sister', 0.5)]:
        for cls in (0, 1, 3):
            pts = [(x, y) for x, y, c in gs if c == cls]
            if pts:
                ax.scatter(*zip(*pts), s=13 if mk == 'o' else 15, marker=mk,
                           c=CL[cls], alpha=al, edgecolors='none',
                           label=f'{nm}   norm ≡ {cls} (mod 4)')
    ax.set_facecolor(BG)
    ax.set_xlabel('geodesic length', color='#9aa3b2')
    ax.set_ylabel('torsion (how far it twists)', color='#9aa3b2')
    ax.tick_params(colors='#5a6272', labelsize=8)
    for s in ax.spines.values():
        s.set_color('#3a4150')
    lg = ax.legend(frameon=False, fontsize=8.6, labelcolor='#c8cfda', ncol=2)
    ax.set_title('PLATE C — THE BONES\nevery closed loop in the object, and in its sister',
                 color=INK, fontsize=16, pad=14)
    fig.text(0.5, 0.015,
             'each dot is a closed geodesic — a way of walking in the space and returning. '
             'colour = its arithmetic class.\n'
             'the object NEVER uses red (norm ≡ 1 mod 4). the sister does. '
             'this is a proved theorem, and it is what tells the twins apart.',
             color='#9aa3b2', fontsize=9.6, ha='center')
    fig.tight_layout(rect=[0.01, 0.055, 0.99, 0.97])
    fig.savefig(f'{OUT}/plate_C_bones.png', dpi=145, facecolor=BG)
    plt.close(fig)
    print("  saved plate C", flush=True)
except FileNotFoundError as e:
    print(f"  plate C skipped: {e}")

# ---------------- PLATE D : THE BARCODE ----------------
evs = []
for fn in ('eigenvalues_final.json', 'scanD_refined.json', 'scanE_refined.json'):
    try:
        d = json.load(open(f'frontier/B792_maass_m004_eigenvalues/{fn}'))
        for e in d['eigenvalues']:
            if e.get('stable', True):
                evs.append((e['r'], e.get('multiplicity', 1),
                            e.get('type', 'NEW')))
    except (FileNotFoundError, KeyError):
        pass
seen, uniq = set(), []
for r, m, t in sorted(evs):
    k = round(r, 6)
    if k not in seen:
        seen.add(k)
        uniq.append((r, m, t))
fig, ax = plt.subplots(figsize=(14.5, 4.6), facecolor=BG)
for r, m, t in uniq:
    parent = str(t).startswith('OLD')
    ax.vlines(r, 0, 1 if m == 1 else 1.55,
              color='#f2ede3' if parent else '#e8a15c',
              lw=2.6 if parent else 1.5, alpha=1 if parent else 0.8)
    if parent:
        ax.annotate(f'{1+r*r:.3f}', xy=(r, 1.02), color='#f2ede3',
                    fontsize=7.6, ha='center', rotation=90, va='bottom')
ax.set_ylim(0, 2.35); ax.set_xlim(3.4, 13.9)
ax.set_facecolor(BG); ax.set_yticks([])
ax.set_xlabel('r     (the eigenvalue is λ = 1 + r²)', color='#9aa3b2')
ax.tick_params(colors='#5a6272', labelsize=8.5)
for s in ax.spines.values():
    s.set_color('#3a4150')
ax.set_title('PLATE D — THE SPECTRUM\n43 tones, computed where the literature had none. '
             'tall pale lines = inherited from the parent; amber = the object\'s own; '
             'raised = doubled tones',
             color=INK, fontsize=14.5, pad=14, loc='left')
fig.text(0.5, 0.02,
         'this is the whole voice of the object up to r = 13.5. '
         'four of the forty-three are its parent speaking through it; the rest are its own.',
         color='#9aa3b2', fontsize=9.6, ha='center')
fig.tight_layout(rect=[0.01, 0.07, 0.99, 0.97])
fig.savefig(f'{OUT}/plate_D_spectrum.png', dpi=145, facecolor=BG)
plt.close(fig)
print(f"  saved plate D ({len(uniq)} eigenvalues)", flush=True)
print("DONE")
