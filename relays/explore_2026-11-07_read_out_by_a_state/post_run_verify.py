"""The explore seat, 2026-11-07: THE READ-OUT BY A STATE -- second methods and one POST HOC completion, written AFTER
reading read_out_by_a_state_out.txt (committed unread at 56fd9f7e5).

  P1  invisibility: this seat's mod-5 test against the web seat's own LA.invisible (line) and exact E = +-I mod 5 (rung)
  P2  the 'unresolved' flags of section D: E mod 5 is periodic in each gap with period 20, so a pattern with no invisible
      member at gaps 0..40 has none at any gap
  P3  uniqueness by the matrix method (closed approximants, k = 30): the deepest rotation and its multiplicity
  P4  the read-out by the sinc-DVR eigenvector (second discretisation of the read-out, not only of the energy)
  P5  HS7's two failed length spectra, retried (randomised triangulations; the alternative algorithm if present)
  P6  POST HOC (the volume action was pre-registered only for the leaders, as HS6v): the least excess volume among
      line-invisible departures with a unique lightest state, RANGE-SCOPED -- the web seat's space (m <= 6, runs <= 6;
      m = 7, 8, runs <= 3) and up to 3 non-1 runs <= 6 with gaps 0..12; k = 10 (k = 12 for the leaders)
    python3 post_run_verify.py
"""
import importlib.util
import itertools
import math
import pathlib
import sys

import mpmath as mp
import numpy as np
from scipy.linalg import eigh

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sp = importlib.util.spec_from_file_location("read_out_by_a_state_check", HERE / "read_out_by_a_state_check.py")
C = importlib.util.module_from_spec(sp)
sys.modules["read_out_by_a_state_check"] = C
sp.loader.exec_module(C)
LA, D0 = C.LA, C.D0


def rung_exact(runs):
    E = D0.mul(LA.mat(runs), D0.inv(LA.mat([1] * len(runs))))
    return C.mod5(E) in (C.I5, C.NEGI5)


def d_range(gmax):
    for K in range(1, 4):
        for rs in itertools.product(range(2, 7), repeat=K):
            for gaps in itertools.product(range(gmax + 1), repeat=K - 1):
                yield C.build(rs, gaps), rs, gaps


def unique_matrix(runs, k=30):
    seq = C.closed(runs, k)
    hs = [C.axis_height(seq, i) for i in range(len(seq))]
    top = max(hs)
    mult = sum(1 for x in hs if abs(x - top) < mp.mpf(10) ** -30)
    return top, mult, hs.index(top)


if __name__ == "__main__":
    print("THE READ-OUT BY A STATE -- post-run verification (the explore seat, 2026-11-07; written after the read)")

    print("\nP1. invisibility, two implementations, on section D's 1809 departures (gaps 0..40, Lemma C patterns)")
    XMAX = 2 * mp.log(C.Q_exact((6,))) + mp.mpf("0.01")
    n, mis_l, mis_r = 0, 0, 0
    for runs, rs, gaps in d_range(40):
        if 2 * mp.log(C.B_bound(rs)) > XMAX:
            continue
        n += 1
        E = C.E5(runs)
        mis_l += C.line_inv(E) != LA.invisible(runs)
        mis_r += C.rung_inv(E) != rung_exact(runs)
    print("  departures %d; line mismatches %d; rung mismatches %d" % (n, mis_l, mis_r))

    print("\nP2. periodicity of E mod 5 in the gaps, and the invisible residues of the flagged patterns")
    per_ok = True
    for rs in ((2, 3), (3, 2), (2, 2)):
        for g in range(0, 21):
            per_ok &= C.E5(C.build(rs, (g,))) == C.E5(C.build(rs, (g + 20,)))
    for g, h in itertools.product(range(0, 21), repeat=2):
        per_ok &= C.E5(C.build((2, 2, 2), (g, h))) == C.E5(C.build((2, 2, 2), (g + 20, h))) == C.E5(C.build((2, 2, 2), (g, h + 20)))
    print("  E5 periodic with period 20 in each gap (patterns (2,3), (3,2), (2,2), (2,2,2)): %s" % per_ok)
    for rs in ((2, 3), (3, 2)):
        li = [g for g in range(20) if C.line_inv(C.E5(C.build(rs, (g,))))]
        ri = [g for g in range(20) if C.rung_inv(C.E5(C.build(rs, (g,))))]
        print("  %s: line-invisible residues %s; rung-invisible residues %s" % (rs, li, ri))
    li3 = [(g, h) for g, h in itertools.product(range(20), repeat=2) if C.line_inv(C.E5(C.build((2, 2, 2), (g, h))))]
    ri3 = [(g, h) for g, h in itertools.product(range(20), repeat=2) if C.rung_inv(C.E5(C.build((2, 2, 2), (g, h))))]
    print("  (2,2,2): line-invisible residue pairs %d (first %s); rung-invisible %d" % (len(li3), li3[:6], len(ri3)))

    print("\nP3. uniqueness of the deepest class by the matrix method (closed approximants, k = 30)")
    for runs in [(6,), (2, 1, 1, 1, 2), (2, 1, 2, 1, 2), C.build((2, 2), (13,)), C.build((2, 2, 2), (1, 11)),
                 C.build((2, 2, 2), (11, 1)), C.build((2, 2, 2), (1, 21))]:
        top, mult, at = unique_matrix(runs)
        lam, order, gap = C.deepest(runs)
        print("  %-34s matrix: deepest %.12f multiplicity %d at run %d | lambda/2 %.12f gap %s" % (
            runs if len(runs) < 12 else "(%d runs) %s" % (len(runs), [r for r in runs if r > 1]),
            float(top), mult, at, float(lam[order[0]] / 2), mp.nstr(gap, 3)))

    print("\nP4. the read-out by the sinc-DVR eigenvector (H* = sqrt5 phi)")
    H = float(C.HSTAR)
    for A in (1e-2, 1.0, 2 * math.pi):
        q = C.qof(A, H)
        w, U = C.window(q)
        nn = 801
        u = np.linspace(-U, U, nn)
        hh = u[1] - u[0]
        i = np.arange(nn)
        Dd = i[:, None] - i[None, :]
        Dn = np.where(Dd == 0, 1, Dd)
        T = np.where(Dd == 0, np.pi ** 2 / 3, 2.0 * (-1.0) ** np.abs(Dd) / Dn ** 2) / hh ** 2
        val, vec = eigh(T + np.diag(q * np.cosh(2 * u)), subset_by_index=[0, 0])
        P = vec[:, 0] ** 2
        P /= P.sum()
        dvr = float((P / np.cosh(2 * u)).sum())
        fd = C.readout(q)["h_ratio"]
        print("  A = %-8.5g <Im>/H*: DVR %.10f, FD %.10f; difference %.1e" % (A, dvr, fd, abs(dvr - fd)))

    print("\nP5. HS7's failed length spectra, retried")
    try:
        import snappy
        for word in ("LLRLRLLRLRLR", "LLRLLRLLRLRLR"):
            got = None
            for attempt in range(8):
                M = snappy.Manifold("b++" + word)
                for _ in range(attempt):
                    M.randomize()
                try:
                    spec = M.length_spectrum(2.5)
                    got = ("length_spectrum after %d randomizations" % attempt,
                           [(float(x.length.real()), int(x.multiplicity)) for x in spec[:4]])
                    break
                except Exception:
                    continue
            if got is None and hasattr(snappy.Manifold("m004"), "length_spectrum_alt"):
                try:
                    M = snappy.Manifold("b++" + word)
                    rows = M.length_spectrum_alt(count=6)
                    got = ("length_spectrum_alt", [(float(x.length.real()), None) for x in rows])
                except Exception as exc:
                    got = ("length_spectrum_alt failed", repr(exc))
            print("  b++%-16s %s" % (word, got))
    except Exception as exc:
        print("  P5 failed: %r" % (exc,))

    print("\nP6. POST HOC, RANGE-SCOPED: the volume action over line-invisible departures with a unique lightest state")
    import snappy
    VOL4 = float(snappy.ManifoldHP("m004").volume())

    def letters(runs, k):
        st = "".join(("L" if j % 2 == 0 else "R") * r for j, r in enumerate(runs))
        return st + ("R" if len(runs) % 2 else "") + "LR" * k

    def dV(runs, k=10):
        M = snappy.Manifold("b++" + letters(runs, k))
        st = M.solution_type()
        return float(M.volume()) - (k + (len(runs) + 1) // 2) * VOL4, st

    space = set(LA.space())
    for runs, rs, gaps in d_range(12):
        space.add(runs)
    rows, bad, nline = [], [], 0
    for runs in sorted(space, key=lambda r: (len(r), r)):
        E = C.E5(runs)
        li, ri = C.line_inv(E), C.rung_inv(E)
        if not li:
            continue
        nline += 1
        lam, order, gap = C.deepest(runs)
        uq = gap > mp.mpf(10) ** -30
        v, st = dV(runs)
        if st != "all tetrahedra positively oriented":
            bad.append((runs, st))
            continue
        rows.append((v, runs, uq, ri, float(lam[order[0]] / 2)))
    rows.sort()
    print("  departures in range: %d; line-invisible: %d; volumes with a degenerate solution: %d %s" % (
        len(space), nline, len(bad), bad[:3]))
    print("  the 10 least excess volumes among line-invisible departures (any lightest state):")
    for v, runs, uq, ri, Hd in rows[:10]:
        print("    %-34s dV %.10f  unique lightest %-5s rung-invisible %-5s depth %.6f" % (
            runs if len(runs) < 12 else "(%d runs) %s" % (len(runs), [r for r in runs if r > 1]), v, uq, ri, Hd))
    uq_rows = [t for t in rows if t[2]]
    print("  the 8 least among those with a UNIQUE lightest state:")
    for v, runs, uq, ri, Hd in uq_rows[:8]:
        v12, _ = dV(runs, 12)
        print("    %-34s dV(k=10) %.10f  dV(k=12) %.10f  rung-invisible %-5s depth %.6f" % (
            runs if len(runs) < 12 else "(%d runs) %s" % (len(runs), [r for r in runs if r > 1]), v, v12, ri, Hd))
    if len(uq_rows) > 1:
        print("  least unique: %s; gap to the next %.6f; is it (6): %s" % (
            uq_rows[0][1], uq_rows[1][0] - uq_rows[0][0], uq_rows[0][1] == (6,)))
    print("\npost_run_verify exit 0")
