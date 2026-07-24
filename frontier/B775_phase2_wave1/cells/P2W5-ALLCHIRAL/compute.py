"""P2W5-ALLCHIRAL (OI-122 / L83(b)) — when does an SU(3)_k stage hear all-chirally?

QUESTION (sealed): characterize WHEN a general SU(3)_k stage has tr_even = 0 for
the object's figure-eight play W = RL.  Banked context: B584 (kappa=5: tr_even=0,
tr_odd=-1/phi), B585 (LAW-O tr_odd = [4|kappa] - [5|kappa]/phi, held out 5/5;
LAW-E for the even channel FAILED its hold-out and was banked as a dead guess),
B587 (the twelve Weyl-twisted Gauss terms; the even channel = the +/- DIFFERENCE
assembly, which mixes divisor-gated terms with unit-conductor terms oscillating
as the quadratic character (kappa/5) -- "it cannot satisfy any divisibility law").

METHOD (B775 Phase-2 structural; blind/hold-out discipline):
  channel A  Kac-Peterson SU(3)_k modular data (B238 su3_data), tr_even via the
             charge-conjugation projector  tr(M(I+C)/2).
  channel A' the SAME kappa via the B585-N1 identity tr_even = (Z - Z(S^2 W))/2
             -- an independent estimator on the same stage (no projector).
  channel B  an INDEPENDENT re-implementation of the finite Weil representation
             on C[P/kappa Q] (B587 route): tr_even = (Z_+ - Z_-)/2 over the
             +/-Weyl cosets.  Different mathematics, different code path.
  TRAIN on kappa = 4..43, then PREDICT the held-out kappa = 44..70.
  A decoy (B585's dead LAW-E) is pushed through the SAME machinery to certify
  that the failure branch can actually fire (MB12 anti-vacuity).

Verdict branches (all can FIRE and FAIL): RESOLVED-A (clean criterion on kappa,
validated held-out), RESOLVED-B (no clean condition at the swept range),
UNRESOLVED (gates fail / partial-fit ambiguity).

Run: python3 compute.py   (pyenv python3, numpy only, ~3 min).  Nothing to CLAIMS.md.
"""
import itertools
import json
import os
import time

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
HERE = os.path.dirname(os.path.abspath(__file__))
TOL = 1e-7

# ---------------------------------------------------------------- channel A
PERMS = list(itertools.permutations(range(3)))
SGN = {p: (-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3)) for p in PERMS}


def su3_data(k):
    """SU(3)_k Kac-Peterson (S,T,C).  Vectorised clone of B238's su3_data(k)."""
    kap = k + 3
    wts = [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]
    idx = {w: i for i, w in enumerate(wts)}
    L = np.array([[w[0] + w[1] + 2.0, w[1] + 1.0, 0.0] for w in wts])
    s = L.sum(axis=1)
    S = np.zeros((len(wts), len(wts)), dtype=complex)
    for p in PERMS:                      # ip(u,v) = u.v - (sum u)(sum v)/3
        S += SGN[p] * np.exp(-2j * np.pi * (L[:, list(p)] @ L.T - np.outer(s, s) / 3.0) / kap)
    S = S / np.sqrt((np.abs(S) ** 2).sum(axis=0)[0])
    c = k * 8.0 / kap
    T = np.array([np.exp(2j * np.pi * (((2.0 / 3) * (a * a + a * b + b * b) + 2 * (a + b))
                                       / (2 * kap) - c / 24.0)) for (a, b) in wts])
    C = np.zeros((len(wts), len(wts)))
    for w, i in idx.items():
        C[idx[(w[1], w[0])], i] = 1.0
    return wts, S, T, C


def modular_gate(S, Tv):
    n = S.shape[0]
    T = np.diag(Tv)
    if not np.allclose(S @ S.conj().T, np.eye(n), atol=1e-8):
        return False
    if not np.allclose(S, S.T, atol=1e-8):
        return False
    S2 = S @ S
    if not np.allclose(np.abs(S2) @ np.abs(S2), np.eye(n), atol=1e-8):
        return False
    ST3 = np.linalg.matrix_power(S @ T, 3)
    i0 = np.unravel_index(np.argmax(np.abs(S2)), S2.shape)
    return np.allclose(ST3, (ST3[i0] / S2[i0]) * S2, atol=1e-6)


def channels_A(k, word="RL", gate=False):
    """(tr_even, tr_odd, Z, tr_even_N1, gate) on SU(3)_k; two independent estimators."""
    wts, S, Tv, C = su3_data(k)
    n = len(wts)
    gv = modular_gate(S, Tv) if gate else None
    Si = S.conj().T
    Rop, Lop = np.diag(Tv), Si @ np.diag(Tv.conj()) @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == "R" else Lop)
    Z = np.trace(M)
    even_proj = np.trace(M @ (np.eye(n) + C) / 2)          # projector estimator
    odd_proj = Z - even_proj
    even_N1 = (Z - np.trace((S @ S) @ M)) / 2              # B585-N1 estimator
    return even_proj, odd_proj, Z, even_N1, gv


# ---------------------------------------------------------------- channel B
_S1 = np.array([[-1, 0], [1, 1]])
_S2 = np.array([[1, 1], [0, -1]])
WEYL = []
for wd in ((), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)):
    Mw = np.eye(2, dtype=int)
    for g in wd:
        Mw = (_S1 if g == 0 else _S2) @ Mw
    WEYL.append((Mw, (-1) ** len(wd)))
U = np.array([[0, -1], [1, 2]])
UINV = np.array([[2, 1], [-1, 0]])


def _ip(u, v):
    return (2.0 * (u[..., 0] * v[..., 0] + u[..., 1] * v[..., 1])
            + (u[..., 0] * v[..., 1] + u[..., 1] * v[..., 0])) / 3.0


def channels_B(kap, word="RL"):
    """tr_even/tr_odd from the finite Weil rep on C[P/kappa Q] (independent route)."""
    reps, index = [], {}
    for c1 in range(kap):
        for c2 in range(3 * kap):
            index[(c1, c2)] = len(reps)
            reps.append(UINV @ np.array([c1, c2]))
    reps = np.array(reps)
    n = len(reps)
    Tv = np.exp(1j * np.pi * _ip(reps, reps) / kap)
    S = np.exp(-2j * np.pi * _ip(reps[:, None, :], reps[None, :, :]) / kap) / np.sqrt(n)
    assert np.allclose(S @ S.conj().T, np.eye(n), atol=1e-7), f"Weil S not unitary, kap={kap}"

    def canon(mu):
        c = U @ mu
        return (int(c[0]) % kap, int(c[1]) % (3 * kap))

    sig = {}
    for pm in (1, -1):
        for wi, (Wm, sg) in enumerate(WEYL):
            sig[(pm, wi)] = np.array([index[canon(pm * (Wm @ mu))] for mu in reps])
    par = np.zeros((n, n))
    par[sig[(-1, 0)], np.arange(n)] = 1.0
    assert np.allclose(S @ S, par, atol=1e-6), f"Weil S^2 != parity at kap={kap}"
    Sinv = S.conj().T
    Rop, Lop = np.diag(Tv), Sinv @ np.diag(Tv.conj()) @ S
    M = np.eye(n, dtype=complex)
    for ch in word:
        M = M @ (Rop if ch == "R" else Lop)
    rows = np.arange(n)
    t = {key: M[rows, s].sum() for key, s in sig.items()}   # tr(M P_w) = sum_i M[i,sigma(i)]
    Zp = sum(WEYL[wi][1] * t[(1, wi)] for wi in range(6)) / 6.0
    Zm = sum(WEYL[wi][1] * t[(-1, wi)] for wi in range(6)) / 6.0
    return (Zp - Zm) / 2, (Zp + Zm) / 2


# ---------------------------------------------------------------- candidates
def LAW_Eprime(kap):
    """the criterion fitted below (stated here so it is auditable in one line)"""
    return (1 if kap % 5 in (2, 3) else 0) - (1 if kap % 4 == 2 else 0)


def LAW_Eprime_char(kap):
    """the SAME criterion in B587's language: a quadratic CHARACTER law, not a
    divisibility law.  chi5 = Legendre(kappa|5) in {0,+-1}."""
    chi5 = 0 if kap % 5 == 0 else (1 if kap % 5 in (1, 4) else -1)
    return (1 - chi5 - (1 if kap % 5 == 0 else 0)) / 2 - ((1 if kap % 2 == 0 else 0)
                                                          - (1 if kap % 4 == 0 else 0))


def LAW_E_dead(kap):
    """B585's DEAD guess -- the decoy, run through the same machinery (MB12)"""
    if kap % 4 == 2:
        return -1
    if kap % 6 == 1 or (kap % 4 == 0 and kap >= 8):
        return 1
    return 0


# ---------------------------------------------------------------- the sweep
t0 = time.time()
KMAX_TRAIN, KMAX_ALL = 43, 70          # kappa ranges (3+ full periods of 20)
print("P2W5-ALLCHIRAL — L83(b): when does an SU(3)_k stage hear all-chirally?")
print(f"sweep kappa = 4..{KMAX_ALL}   (train 4..{KMAX_TRAIN}, HELD-OUT {KMAX_TRAIN+1}..{KMAX_ALL})\n")

even, odd, Zs, gate_ok, est_gap = {}, {}, {}, {}, {}
for kap in range(4, KMAX_ALL + 1):
    k = kap - 3
    do_gate = kap in (4, 5, 6, 9, 12, 17, 24, 31, 44, 57)      # sampled full modular gate
    e, o, Z, e2, gv = channels_A(k, "RL", gate=do_gate)
    even[kap], odd[kap], Zs[kap] = e.real, o.real, Z
    if gv is not None:
        gate_ok[kap] = bool(gv)
    est_gap[kap] = max(abs(e.imag), abs(e - e2))
print("  kappa: tr_even  tr_odd")
for row in range(4, KMAX_ALL + 1, 10):
    seg = range(row, min(row + 10, KMAX_ALL + 1))
    print("   " + " ".join(f"{kap:>3d}" for kap in seg))
    print("   " + " ".join(f"{even[kap]:+3.0f}" for kap in seg) + "   <- tr_even")
    print("   " + " ".join((f"{odd[kap]:+3.0f}" if abs(odd[kap] - round(odd[kap])) < 1e-6
                            else f"{odd[kap]:+.1f}") for kap in seg) + "   <- tr_odd")

# ---------------------------------------------------------------- gates
G = {}
G["modular_gate"] = len(gate_ok) >= 8 and all(gate_ok.values())
G["estimators_agree"] = max(est_gap.values()) < TOL          # projector vs N1, all kappa
G["tr_even_integral"] = max(abs(even[kap] - round(even[kap])) for kap in even) < TOL
G["banked_B584"] = abs(even[5]) < TOL and abs(odd[5] + 1 / PHI) < TOL
BANKED_E = {6: -1, 7: 1, 8: 1, 9: 0, 10: -1, 11: 0, 12: 1, 13: 1, 14: -1}   # B585/B587 table
G["banked_B585_even"] = all(abs(even[kap] - v) < TOL for kap, v in BANKED_E.items())
G["banked_LAW_O"] = all(abs(odd[kap] - ((1.0 if kap % 4 == 0 else 0.0)
                                        - (1 / PHI if kap % 5 == 0 else 0.0))) < TOL
                        for kap in even)
# channel B (independent Weil route) on a sub-range
wb = {}
for kap in range(4, 21):
    eb, ob = channels_B(kap, "RL")
    wb[kap] = (eb.real, ob.real)
G["channel_B_agrees"] = all(abs(wb[kap][0] - even[kap]) < 1e-6
                            and abs(wb[kap][1] - odd[kap]) < 1e-6 for kap in wb)
print("\nGATES")
for g, v in G.items():
    print(f"  {g:22s} {'PASS' if v else 'FAIL'}")
print(f"  (max |imag| / |projector - N1| over all kappa = {max(est_gap.values()):.2e};"
      f"  channel-B cross-check on kappa=4..20)")

# ---------------------------------------------------------------- fit (TRAIN only)
train = {kap: round(even[kap]) for kap in range(4, KMAX_TRAIN + 1)}
period = None
for p in range(1, 41):
    if all(train[kap] == train[kap + p] for kap in train if kap + p in train):
        period = p
        break
print(f"\nFIT (train kappa = 4..{KMAX_TRAIN}):  smallest period p <= 40 : {period}")
table = None
if period is not None:
    table = {}
    ok = True
    for kap, v in train.items():
        r = kap % period
        if r in table and table[r] != v:
            ok = False
        table[r] = v
    if not ok:
        table = None
if table is not None:
    zero_res = sorted(r for r, v in table.items() if v == 0)
    print(f"  residue table mod {period}: " + " ".join(f"{r}:{table[r]:+d}" for r in sorted(table)))
    print(f"  ZERO (all-chiral) residues: {zero_res}   ({len(zero_res)}/{period} of stages)")
    cf_ok = all(LAW_Eprime(kap) == v for kap, v in train.items())
    print(f"  closed form  tr_even = [kappa = +-2 mod 5] - [kappa = 2 mod 4]  on train: "
          f"{'MATCHES' if cf_ok else 'no'}")
else:
    cf_ok = False
    print("  no consistent residue table at any period <= 40")

# ---------------------------------------------------------------- HELD-OUT
hold = list(range(KMAX_TRAIN + 1, KMAX_ALL + 1))
hits_tab = sum(1 for kap in hold if table is not None and table.get(kap % period) == round(even[kap]))
hits_cf = sum(1 for kap in hold if LAW_Eprime(kap) == round(even[kap]))
hits_decoy = sum(1 for kap in hold if LAW_E_dead(kap) == round(even[kap]))
decoy_train = sum(1 for kap in train if LAW_E_dead(kap) == train[kap])
print(f"\nHELD-OUT kappa = {hold[0]}..{hold[-1]}  ({len(hold)} stages, > one full period)")
print(f"  residue-table criterion : {hits_tab}/{len(hold)}")
print(f"  closed form             : {hits_cf}/{len(hold)}")
print(f"  DECOY (B585 dead LAW-E) : {hits_decoy}/{len(hold)}   [train {decoy_train}/{len(train)}]"
      "  <- the failure branch is live")
for kap in hold:
    if table is not None and table.get(kap % period) != round(even[kap]):
        print(f"    MISS at kappa={kap}: table {table.get(kap % period)} vs {round(even[kap])}")

# ---------------------------------------------------------------- scope: other words
print("\nSCOPE — is the criterion word-generic?  even channel of heavier metallic words:")
scope = {}
for word in ("RRLL", "RRRLLL"):
    vals = []
    for kap in range(4, 21):
        e, o, Z, e2, _ = channels_A(kap - 3, word)
        vals.append(e.real)
    scope[word] = vals
    unit = max(abs(v - round(v)) for v in vals) < TOL and max(abs(v) for v in vals) <= 1 + TOL
    scope[word + "_unit"] = bool(unit)
    print(f"  {word:>7}: " + " ".join(f"{v:+.3f}" for v in vals))
    print(f"          {{0,+-1}}-valued: {unit}   max|.| = {max(abs(v) for v in vals):.3f}")
gold_unit = max(abs(even[kap]) for kap in even) <= 1 + TOL and G["tr_even_integral"]
print(f"       RL: {{0,+-1}}-valued: {gold_unit}   max|.| = "
      f"{max(abs(even[kap]) for kap in even):.3f}   over kappa=4..{KMAX_ALL}")
print("  => the unit {0,+-1} even chord is figure-eight-specific (B587's minimality")
print("     mechanism: det(A -+ I) = -+1x5 only for the golden word); the criterion")
print("     below is scoped to the object's own word W = RL.")

# the same criterion in B587's language: a CHARACTER law, not a divisibility law
char_ok = all(abs(LAW_Eprime_char(kap) - even[kap]) < TOL for kap in even)
print(f"\nMECHANISM READING (B587): tr_even = (1 - chi5(kappa) - [5|kappa])/2 "
      f"- ([2|kappa] - [4|kappa])")
print(f"  identity over the FULL sweep kappa=4..{KMAX_ALL}: {'EXACT' if char_ok else 'FAILS'}")
print("  -> the even channel is governed by the quadratic character mod 5 (the six")
print("     reflection Gauss sums of conductor +-5) plus the 2-adic split of the")
print("     rotation terms (d=4 vs d=16).  This is exactly why B585's LAW-E (a pure")
print("     DIVISIBILITY guess) had to die, and why a character law survives.")

# ---------------------------------------------------------------- VERDICT
gates_all = all(G.values())
if not gates_all:
    verdict, headline = "UNRESOLVED", "gate failure: the sweep is not trustworthy"
elif period is None or table is None:
    verdict = "RESOLVED-B"
    headline = f"no consistent periodic criterion at kappa <= {KMAX_ALL} (period search <= 40 empty)"
elif hits_tab == len(hold) and cf_ok and hits_cf == len(hold) and char_ok:
    verdict = "RESOLVED-A"
    headline = ("tr_even(kappa) = [kappa = +-2 mod 5] - [kappa = 2 mod 4]; all-chiral (tr_even=0) "
                "iff those two indicators AGREE — 11 of the 20 residues mod 20")
elif hits_tab == len(hold):
    verdict = "RESOLVED-A"
    headline = (f"criterion = the period-{period} residue table (100% held-out); "
                "no matching closed form")
elif hits_tab >= 0.8 * len(hold):
    verdict = "UNRESOLVED"
    headline = f"criterion fits only {hits_tab}/{len(hold)} held-out stages — partial, ambiguous"
else:
    verdict = "RESOLVED-B"
    headline = f"the fitted criterion dies held-out ({hits_tab}/{len(hold)}) — no clean condition"

allchiral = sorted(r for r, v in (table or {}).items() if v == 0)
print("\n" + "=" * 78)
print(f"VERDICT: {verdict}")
print(f"  {headline}")
if verdict == "RESOLVED-A":
    print(f"  all-chiral residues kappa mod {period}: {allchiral}")
    print("  equivalently: a stage hears the object all-chirally iff")
    print("     (kappa = +-2 mod 5)  <=>  (kappa = 2 mod 4).")
    print("  corollaries (in-cell, checked):")
    print("   - 5|kappa & kappa != 2 mod 4  =>  tr_even = 0: B584's 'the golden amplitude is")
    print(f"     entirely theta-odd' is a corollary, but it FAILS at kappa = 10 mod 20")
    print(f"     (kappa=10: tr_even={even[10]:+.0f}, kappa=30: {even[30]:+.0f}) — the golden")
    print("     stages split into all-chiral (5,15,20,25,...) and non (10,30,50,...).")
    print("   - the even channel is a UNIT chord ({0,+-1}); the odd channel is the golden")
    print("     two-tone chord (LAW-O). Chirality-defect never exceeds one unit.")
print("=" * 78)

res = {
    "cell": "P2W5-ALLCHIRAL", "lead": "OI-122 / L83(b)", "verdict": verdict,
    "headline": headline,
    "criterion": "tr_even(kappa) = [kappa == +-2 mod 5] - [kappa == 2 mod 4]",
    "allchiral_iff": "[kappa == +-2 mod 5] == [kappa == 2 mod 4]",
    "period": period, "allchiral_residues_mod20": allchiral,
    "density_allchiral": f"{len(allchiral)}/{period}" if period else None,
    "sweep": [4, KMAX_ALL], "train": [4, KMAX_TRAIN], "heldout": [hold[0], hold[-1]],
    "heldout_hits_table": hits_tab, "heldout_hits_closedform": hits_cf,
    "heldout_n": len(hold), "decoy_B585_LAW_E_heldout_hits": hits_decoy,
    "gates": {g: bool(v) for g, v in G.items()},
    "max_estimator_gap": float(max(est_gap.values())),
    "tr_even": {str(kap): int(round(even[kap])) for kap in range(4, KMAX_ALL + 1)},
    "character_form": "tr_even = (1-chi5(kappa)-[5|kappa])/2 - ([2|kappa]-[4|kappa])",
    "character_form_exact": bool(char_ok),
    "scope_word_specific": {"RL_unit": bool(gold_unit), "RRLL_unit": scope["RRLL_unit"],
                            "RRRLLL_unit": scope["RRRLLL_unit"]},
    "channels": ["KP-projector", "B585-N1-lift", "finite-Weil-rep (kappa=4..20)"],
    "firewall": "structural only; no SM values; nothing to CLAIMS.md",
    "runtime_s": round(time.time() - t0, 1),
}
with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(res, fh, separators=(",", ":"), sort_keys=True)
print(f"\nresults.json written  ({res['runtime_s']}s)")
