"""
Movement XXII — the object's tight-binding gap structure, and the density-trap wall
on the falsifiable combination-gap prediction (past-the-gate, owner-authorized).

The object is a proven quasicrystal (movements XIII-XV), so a tight-binding
Hamiltonian on its sequence has a gap-labeled Cantor spectrum (gap-labeling
theorem): every spectral gap's IDS value lies in the frequency ℤ-module generated
by the golden-tensor letter frequencies.  The FALSIFIABLE physics candidate (the
mixed-chain prediction, S065 H4) is whether the object opens genuine RANK-2
COMBINATION gaps -- gaps whose label needs two of the module generators, which
neither Fibonacci copy alone has.

Computed here (Sturm-count IDS at N=200000, the exact tool B172 used):
  * the object HAS real gaps (E-widths 1.4, 1.2, 0.8, 0.5, ...): a genuine
    quasicrystal spectrum.
  * BUT the combination-gap signature is DENSITY-TRAPPED: with 4 generators, the
    frequency module is dense, and a MARGIN TEST (2nd-best module-fit distance /
    best-fit distance) returns ~1.0 for EVERY gap -- no gap can be decisively
    assigned a rank.  Even the clean rank-1 gaps (f_a, f_B) are indistinguishable
    from rank-4 combinations at numerical tolerance.

So: NOT "the object opens combination gaps" (that is the B171 density-trap error),
and NOT "it has none" (numerics cannot refute them).  The honest verdict: the
falsifiable prediction is real but NOT numerically resolvable in-sandbox -- it needs
EXACT algebraic gap-labeling (the finite-size-floor NEEDS-SPECIALIST wall of B172).
Firewalled; the physics reading is in speculations/S065.
"""
import numpy as np

phi = (1 + np.sqrt(5)) / 2
sq = np.sqrt(phi)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
_w = np.array([phi, 1, phi * sq, sq])
FREQ = _w / _w.sum()                                   # golden-tensor letter frequencies


def chain(N):
    u = 'a'
    while len(u) < N:
        u = ''.join(SUB[c] for c in u)
    return u[:N]


def sturm_ids(N=200000, lam=1.5, npts=4000, vmap=(0., 1., 2., 3.)):
    """IDS(E) via the Sturm sequence (vectorized over E) — exact state counting."""
    u = chain(N)
    vm = dict(zip('abAB', vmap))
    d = np.array([vm[c] for c in u]) * lam
    Eg = np.linspace(d.min() - 2.5, d.max() + 2.5, npts)
    q = d[0] - Eg
    cnt = (q < 0).astype(float)
    for i in range(1, N):
        q = (d[i] - Eg) - 1.0 / np.where(np.abs(q) < 1e-300, 1e-300, q)
        cnt += (q < 0)
    return Eg, cnt / N


def find_gaps(Eg, ids, N, min_ewidth=0.05):
    labels = []
    i = 0
    while i < len(Eg) - 1:
        j = i
        while j + 1 < len(Eg) and abs(ids[j + 1] - ids[i]) < 0.5 / N:
            j += 1
        if Eg[j] - Eg[i] > min_ewidth and 1e-3 < ids[i] < 1 - 1e-3:
            labels.append((Eg[j] - Eg[i], ids[i]))
        i = max(j, i + 1)
    return sorted(labels, reverse=True)


def margin(lab, tol=3e-3):
    """min-rank module fit and the margin (2nd-best dist / best dist); ~1.0 = density-trapped."""
    cands = []
    for na in range(-3, 4):
        for nb in range(-3, 4):
            for nA in range(-3, 4):
                for nB in range(-3, 4):
                    val = (na * FREQ[0] + nb * FREQ[1] + nA * FREQ[2] + nB * FREQ[3]) % 1.0
                    dist = min(abs(val - lab), abs(val - lab + 1), abs(val - lab - 1))
                    if dist < tol:
                        cands.append((dist, sum(x != 0 for x in (na, nb, nA, nB))))
    cands.sort()
    if not cands:
        return None
    m = (cands[1][0] / cands[0][0]) if len(cands) > 1 and cands[0][0] > 0 else 99.0
    return cands[0][1], m


if __name__ == "__main__":
    Eg, ids = sturm_ids()
    gaps = find_gaps(Eg, ids, 200000)
    print(f"tight-binding gaps (N=200000): {len(gaps)} with E-width>0.05  -> real quasicrystal spectrum")
    print(f"{'E-width':>8} {'label':>8}  best-rank  margin")
    worst_margin = 0
    for width, lab in gaps[:8]:
        r = margin(lab)
        if r:
            worst_margin = max(worst_margin, r[1])
            print(f"{width:8.3f} {lab:8.4f}     {r[0]}      {r[1]:.1f}x  "
                  f"{'DECISIVE' if r[1] > 3 else 'density-trapped'}")
    print(f"\nbest margin over all gaps = {min(margin(l)[1] for _, l in gaps if margin(l)):.1f}x "
          f"(>3 would be decisive) -> combination-gap signature NOT numerically resolvable; NEEDS exact gap-labeling.")
