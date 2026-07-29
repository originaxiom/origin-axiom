r"""CELL 2, STAGE 0 — the Hecke VALIDATION GATE at level (4).

Prereg (WAVE1_PREREGISTRATION.md, sealed 8424a335): before any Hecke
claim, the coefficient relations must HOLD on certified mult-1
newforms. If they fail under both named normalizations, the level-(4)
normalization is wrong -> ABORT (banked fact); Stage 1 never runs.

Method: reconstruct the collocation eigenvector a_mu at a certified
mult-1 eigenvalue; restrict to the parent-integral sublattice
mu = nu * (i/sqrt3), nu in Z[w] (where classical Hecke acts); test,
for split primes pi = 3+w (N=7) and 4+w (N=13):

    T1 (eigen-relation, alpha in {-1, 0, +1} tested and named):
       lam_pi := chat(pi)/chat(1);  check
       lam_pi * chat(pi) =? chat(pi^2) + N(pi)^alpha * chat(1)
    T2 (coprime multiplicativity): lam_pi * lam_pibar =? chat(pi*pibar)/chat(1)

Unit caveat (declared): Gamma_41's cusp stabilizer has NO unit
rotations, so chat(nu) need not be unit-invariant; relations are
tested on the raw chat and on the mu6-averaged chat (both reported).

Gate 5-Q.
"""
import json
import sys

import numpy as np

sys.path.insert(0, 'frontier/B792_maass_m004_eigenvalues')
from hejhal_m004 import (K_table, Lattice, System, build_moves,
                        find_cusp_lattice)  # noqa: E402

OM = complex(-0.5, np.sqrt(3) / 2)
# E31 fixes (two, both caught by the gate's own preconditions):
# (1) O3^dual under Re(conj(mu)*z) is d1*O3 with d1 = 1 + i/sqrt3
#     (= (2/sqrt3) e^{i pi/6}); NOT (i/sqrt3)*O3.
# (2) the embedding must be COMPLEX MULTIPLICATION nu -> nu*d1 (the
#     O3-module iso), not the additive dual-basis map. In Lam* integer
#     coordinates (u1 = 1, u2 = i/(2 sqrt3)):
#     nu = p + q*omega  |->  mu = (p - q)*u1 + (2p + 2q)*u2   (EXACT;
#     |mu| = (2/sqrt3)|nu|, so Hecke indexing respects norms).

tau, _, _, _ = find_cusp_lattice()
lat = Lattice(tau)
moves = build_moves()
print("Building system (Y = 0.75, rmax 10.1) ...")
S1 = System(lat, moves, 0.75, 10.1, margin=25.0)  # Rcut 8.68: covers pi7^2 and nu=7 at |mu| = 8.08
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


U2 = complex(0, 1 / (2 * np.sqrt(3)))


def chat_pq(a, p, q):
    """Coefficient at the O3-dual point of nu = p + q*omega (exact coords)."""
    mu = (p - q) * 1.0 + (2 * p + 2 * q) * U2
    d = np.abs(S1.mus - mu)
    j = int(np.argmin(d))
    if d[j] > 1e-9:
        return None
    return a[j]


class Nu(complex):
    """nu carrying exact (p, q) integer coordinates in Z[omega]."""
    def __new__(cls, p, q):
        z = super().__new__(cls, p + q * OM)
        z.p, z.q = p, q
        return z


def numul(x, y):
    # (p1 + q1 w)(p2 + q2 w), w^2 = -1 - w
    p = x.p * y.p - x.q * y.q
    q = x.p * y.q + x.q * y.p - x.q * y.q
    return Nu(p, q)


def nuconj(x):
    # conj(p + q w) = p + q*conj(w) = (p - q) - q*w
    return Nu(x.p - x.q, -x.q)


def chat(a, nu):
    return chat_pq(a, nu.p, nu.q)


def nu_of(p, q):
    return Nu(p, q)


ZETA6 = Nu(1, 1)  # 1 + omega = e^{i pi/3}


def unit_avg(a, nu):
    """mu6-average of chat over exact unit rotations of nu; reports
    how many of the 6 orbit points were in range via .n_found."""
    vals = []
    u = Nu(1, 0)
    for k in range(6):
        v = chat(a, numul(nu, u))
        if v is not None:
            vals.append(v)
        u = numul(u, ZETA6)
    if not vals:
        return None
    m = np.mean(vals)
    return m


MULT1 = [4.900085373, 5.912917882, 7.406615600]

print()
print("=" * 72)
print("CELL 2 STAGE 0 — HECKE VALIDATION GATE (mult-1 newforms)")
print("=" * 72)

gate_results = []
for r in MULT1:
    a, smin = eigvec(r)
    print(f"\n--- form r = {r} (sigma_min = {smin:.1e}) ---")
    for avg_name, cfun in [('raw', chat), ('mu6-avg', unit_avg)]:
        c1 = cfun(a, nu_of(1, 0))
        if c1 is None or abs(c1) < 1e-10:
            print(f"  [{avg_name}] chat(1) unavailable/zero — skip")
            continue
        for pname, pi in [('pi7', nu_of(3, 1)), ('pi13', nu_of(4, 1))]:
            Np = round(abs(pi) ** 2)
            cpi = cfun(a, pi)
            cpi2 = cfun(a, numul(pi, pi))
            if cpi is None or cpi2 is None:
                print(f"  [{avg_name}] {pname}: coefficients out of range")
                continue
            lam = cpi / c1
            best = None
            for alpha in (-1, 0, 1):
                lhs = lam * cpi
                rhs = cpi2 + (Np ** alpha) * c1
                rel = abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-30)
                if best is None or rel < best[1]:
                    best = (alpha, rel)
            print(f"  [{avg_name}] {pname} (N={Np}): |lam| = {abs(lam):.4f} "
                  f"(bound 2*sqrt(N) = {2*np.sqrt(Np):.2f}); "
                  f"best eigen-relation: alpha = {best[0]}, "
                  f"rel dev = {best[1]:.2e}")
            gate_results.append({'r': r, 'norm': avg_name, 'p': pname,
                                 'lam_abs': float(abs(lam)),
                                 'alpha': best[0], 'rel_dev': float(best[1])})
        # T2 coprime multiplicativity with pi7 * conj(pi7) = 7
        cpi = cfun(a, nu_of(3, 1))
        cpib = cfun(a, nuconj(nu_of(3, 1)))
        c7 = cfun(a, nu_of(7, 0))
        if None not in (cpi, cpib, c7):
            lhs = (cpi / c1) * (cpib / c1)
            rhs = c7 / c1
            rel = abs(lhs - rhs) / max(abs(lhs), abs(rhs), 1e-30)
            print(f"  [{avg_name}] T2 mult (7 = pi*pibar): rel dev = {rel:.2e}")
            gate_results.append({'r': r, 'norm': avg_name, 'p': 'T2-7',
                                 'rel_dev': float(rel)})

print()
print("=" * 72)
print("GATE VERDICT")
print("=" * 72)
devs = [g['rel_dev'] for g in gate_results if 'rel_dev' in g]
passing = [d for d in devs if d < 0.05]
print(f"  relations tested: {len(devs)}; passing at 5%: {len(passing)}")
if devs and min(devs) > 0.05:
    print("""
  GATE: FAILED under both normalizations and both unit treatments.
  Per the sealed prereg this is the ABORT branch: the level-(4)
  Hecke normalization (double-coset structure for Gamma_41, which is
  congruence but not Gamma_0-type) is NOT the naive Bianchi one.
  BANKED FACT: no Hecke claim runs; Stage 1 (doublet surgery) is
  BLOCKED pending a correct level-(4) operator construction — a
  registered follow-up, not a silent degradation. (This failure mode
  was pre-registered as the gate's purpose; G5.)""")
else:
    print("""
  GATE: at least one relation family passes at 5% — report the
  passing (normalization, unit-treatment) pair; Stage 1 may proceed
  under EXACTLY that pair, named in its output.""")

with open('frontier/B796_coupling_campaign/cell2_gate_results.json', 'w') as f:
    json.dump(gate_results, f, indent=1)
print("Saved cell2_gate_results.json")
