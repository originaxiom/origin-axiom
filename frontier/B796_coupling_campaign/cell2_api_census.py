r"""D3 — the a_pi CENSUS (Cell 2's CM-vs-construction discriminator).

GO: masterplan v6 (cc, 2026-08-06). Registered follow-up of the
sealed Wave-1 Cell-2 gate (WAVE1_FINDINGS: "the a_pi census is the
next Cell-2 computation").

QUESTION: the Cell-2 gate found a STRUCTURED ZERO of the naive
coefficient proxy at the split prime pi_7 on two mult-1 newforms.
CM forms vanish at a DENSITY-1/2 set of primes (those inert in the
CM field, tracked by a quadratic character); a wrong double-coset
construction produces diffuse errors, not character-tracking zeros.

PRE-STATED FORK (before compute):
  (i)  zeros at ~half the primes AND the zero-set matches a quadratic
       character pattern -> CM reading STRENGTHENED (goes to cc);
  (ii) zero at pi_7 ONLY -> isolated, neither reading; banked as an
       unexplained support fact;
  (iii) zeros at essentially all primes (or none) -> support artifact
       of the naive proxy -> construction reading; the zero carries
       no CM information.
The proxy is the SAME naive coefficient-at-dual-point used by the
gate — the census tests the PATTERN of the proxy's zeros, which is
exactly what the gate's finding was about. No Hecke claim is made
(the gate's ABORT stands).

Nine split primes (norm p = 1 mod 3), nu = p + q*omega with
N(nu) = p^2 - pq + q^2:
  7 = N(3+w), 13 = N(4+w), 19 = N(5+2w), 31 = N(6+w), 37 = N(7+3w),
  43 = N(7+w), 61 = N(9+4w), 67 = N(9+2w), 73 = N(9+w)
(2, 5, 11, ... inert — excluded; 3 ramified — excluded.)

ZERO CRITERION (pre-stated): |c(nu)| / median(|c| over the mode disk)
< 1e-6 -> ZERO; > 1e-2 -> NONZERO; between -> AMBIGUOUS (reported).

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (K_table, Lattice, System, build_moves,
                        find_cusp_lattice)  # noqa: E402

OM = complex(-0.5, np.sqrt(3) / 2)
U2 = complex(0, 1 / (2 * np.sqrt(3)))
OUT = 'frontier/B796_coupling_campaign'

PRIMES = [(7, (3, 1)), (13, (4, 1)), (19, (5, 2)), (31, (6, 1)),
          (37, (7, 3)), (43, (7, 1)), (61, (9, 4)), (67, (9, 2)),
          (73, (9, 1))]
MULT1 = [4.900085373, 5.912917882, 7.406615600, 7.687671168,
         9.027421524, 9.080648624]  # all certified mult-1 newforms

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
print("Building system (Y = 0.75, rmax 10.1, margin 40 — dual disk to "
      "N = 73 at |mu| = 9.86) ...")
S1 = System(lat, moves, 0.75, 10.1, margin=40.0)
print(f"  {len(S1.mus)} modes / {len(S1.zs)} pts", flush=True)


def eigvec(r):
    KT = K_table(S1.args, S1.ts, S1.wts, [r], [])
    KT = KT.reshape(len(S1.norms), len(S1.heights))
    V = ((S1.Y * KT[S1.nrm_idx, 0])[None, :] * S1.P0
         - (S1.tstar[:, None] * KT[S1.nrm_idx, 1:].T) * S1.P1)
    cn = np.linalg.norm(V, axis=0)
    cn[cn == 0] = 1
    _, sv, Vh = np.linalg.svd(V / cn[None, :])
    return Vh[-1].conj() / cn, sv[-1]


def c_at(a, p, q):
    """Naive coefficient at the O3-dual point of nu = p + q*omega
    (module map: integer Lam* coords (p - q, 2p + 2q))."""
    mu = (p - q) * 1.0 + (2 * p + 2 * q) * U2
    d = np.abs(S1.mus - mu)
    j = int(np.argmin(d))
    if d[j] > 1e-9:
        return None
    return a[j]


results = {}
print()
print(f"{'form r':>13} | " + " ".join(f"{p:>7}" for p, _ in PRIMES))
for r in MULT1:
    a, smin = eigvec(r)
    med = np.median(np.abs(a[np.abs(a) > 0]))
    row = []
    for (p, (pp, qq)) in PRIMES:
        c = c_at(a, pp, qq)
        if c is None:
            row.append('OOR')
            continue
        ratio = abs(c) / med
        row.append('ZERO' if ratio < 1e-6 else
                   ('nz' if ratio > 1e-2 else f'~{ratio:.0e}'))
    results[r] = {'sigma_min': float(smin), 'median': float(med),
                  'row': dict(zip([p for p, _ in PRIMES], row))}
    print(f"{r:>13} | " + " ".join(f"{s:>7}" for s in row), flush=True)

print()
print("=" * 72)
print("CENSUS VERDICT (pre-stated fork)")
print("=" * 72)
for r, d in results.items():
    zeros = [p for p, s in d['row'].items() if s == 'ZERO']
    nz = [p for p, s in d['row'].items() if s == 'nz']
    n_test = len(zeros) + len(nz)
    frac = len(zeros) / n_test if n_test else float('nan')
    if n_test and len(zeros) == 0:
        verdict = 'no zeros — the pi_7 gate-zero not reproduced here OR fork (iii)'
    elif frac > 0.85:
        verdict = 'fork (iii): zeros ~everywhere — support artifact; construction reading'
    elif zeros == [7]:
        verdict = 'fork (ii): pi_7 only — isolated; unexplained support fact'
    elif 0.3 <= frac <= 0.7:
        verdict = ('fork (i) CANDIDATE: ~half zero — check character '
                   'pattern; goes to cc if it tracks a discriminant')
    else:
        verdict = f'mixed ({len(zeros)}/{n_test} zero) — report as-is'
    print(f"  r = {r}: zeros at {zeros} -> {verdict}")

with open(f'{OUT}/cell2_api_census.json', 'w') as f:
    json.dump(results, f, indent=1)
print("Saved cell2_api_census.json")
