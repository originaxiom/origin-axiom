#!/usr/bin/env python3
"""B447 (Thermodynamic Campaign D2) — the m-scan harness.

Five warm observables across the metallic family m=1..6 + periodic/random controls,
with the leave-golden-out exceptionality classifier (see PREREGISTRATION.md).

Run:  python3 harness.py    (~10 min; results printed + mscan_results.json)
"""
import json
import math
import numpy as np

rng = np.random.default_rng(20260707)

MS = [1, 2, 3, 4, 5, 6]
TARGET_N = 1500
V_LIST = [0.5, 1.0, 2.0, 4.0]


def metallic_word(m, target=TARGET_N):
    """Substitution a -> a^m b, b -> a; return the letter array (0=a, 1=b)."""
    w = [0]
    while len(w) < target:
        nxt = []
        for c in w:
            nxt.extend([0] * m + [1] if c == 0 else [0])
        w = nxt
    return np.array(w[:], dtype=int)


def lam(m):
    return (m + math.sqrt(m * m + 4)) / 2


def theta(m):
    """The b-letter frequency = the gap-label module generator (the trap: NOT (sqrt(m^2+4)-m)/2)."""
    return 1.0 / (1.0 + lam(m))


def hamiltonian(word, V):
    N = len(word)
    H = np.zeros((N, N))
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = 1.0
    H[np.arange(N), np.arange(N)] = V * np.where(word == 0, 1.0, -1.0)
    return H


def spectrum(word, V):
    return np.linalg.eigvalsh(hamiltonian(word, V))


# ---------- observable 1: specific heat C(T) (canonical, single-particle) ----------
def specific_heat(E, Tgrid):
    E = E - E.min()
    C = []
    for T in Tgrid:
        w = np.exp(-E / T)
        Z = w.sum()
        e1 = (E * w).sum() / Z
        e2 = (E * E * w).sum() / Z
        C.append((e2 - e1 * e1) / T / T)
    return np.array(C)


def count_peaks(C):
    return int(np.sum((C[1:-1] > C[:-2]) & (C[1:-1] > C[2:])))


# ---------- observable 2: transport exponent beta ----------
def transport_beta(word, V):
    N = len(word)
    H = hamiltonian(word, V)
    E, U = np.linalg.eigh(H)
    c = N // 2
    psi0 = U.conj().T[:, c]                       # <n|psi0> in eigenbasis
    x = np.arange(N) - c
    ts = np.unique(np.round(np.logspace(0.3, math.log10(N), 40)).astype(int))
    x2, tt = [], []
    for t in ts:
        amp = U @ (np.exp(-1j * E * t) * psi0)
        p = np.abs(amp) ** 2
        if p[:5].sum() + p[-5:].sum() > 1e-8:      # boundary guard
            break
        x2.append(float((p * x * x).sum()))
        tt.append(t)
    tt, x2 = np.array(tt, float), np.array(x2)
    sel = x2 > 4.0                                 # skip the ballistic-onset transient
    if sel.sum() < 6:
        sel = np.ones(len(tt), bool)
    s = np.polyfit(np.log(tt[sel]), np.log(x2[sel]), 1)[0]
    return 0.5 * float(s), len(tt)


# ---------- observable 3: box-counting D_q of the spectrum ----------
def dq_spectrum(E, qs=(-2, -1, 0, 1, 2, 3, 4), jrange=(4, 9)):
    """Generalized dimensions D_q of the spectrum (counting measure), box method.

    D_0 = slope of log N_box vs log(1/eps)  (positive by construction);
    D_1 = slope of the box entropy vs log(1/eps);
    D_q = (1/(q-1)) * slope of log(sum p^q) vs log(eps)  [note: log eps, not log 1/eps].
    """
    E = np.sort(E)
    span = E[-1] - E[0]
    out = {}
    js = list(range(jrange[0], jrange[1] + 1))
    log_inv_eps = np.array([j * math.log(2) for j in js])   # log(1/eps) + const
    for q in qs:
        ys = []
        for j in js:
            eps = span / 2 ** j
            idx = np.floor((E - E[0]) / eps).astype(int)
            counts = np.bincount(idx)
            p = counts[counts > 0] / len(E)
            if q == 0:
                ys.append(math.log(len(p)))                 # log N_box
            elif q == 1:
                ys.append(-(p * np.log(p)).sum())           # box entropy
            else:
                ys.append(math.log((p ** q).sum()))         # log sum p^q
        slope = np.polyfit(log_inv_eps, ys, 1)[0]
        if q in (0, 1):
            out[q] = float(slope)
        else:
            # d log(sum p^q) / d log(eps) = -slope ;  D_q = that / (q-1)
            out[q] = float(-slope / (q - 1))
    return out


# ---------- observable 4: gap-label realization ----------
def gap_labels(E, th, n_top=10):
    E = np.sort(E)
    N = len(E)
    d = np.diff(E)
    thr = 8 * np.median(d)
    labels = []
    for i in np.argsort(d)[::-1]:
        if d[i] <= thr or len(labels) >= n_top:
            break
        ids = (i + 1) / N
        best = None
        for q in range(-30, 31):
            p = round(ids - q * th)
            err = abs(p + q * th - ids)
            if best is None or err < best[2]:
                best = (p, q, err)
        labels.append(dict(ids=round(float(ids), 6), p=best[0], q=best[1],
                           resid=round(float(best[2]), 6), width=round(float(d[i]), 6)))
    return labels


# ---------- observable 5: Lyapunov gamma(E) on/off spectrum ----------
def lyapunov(word, V, Es):
    out = []
    for E in Es:
        M = np.eye(2)
        acc = 0.0
        for n in range(len(word)):
            v = V * (1.0 if word[n] == 0 else -1.0)
            M = np.array([[E - v, -1.0], [1.0, 0.0]]) @ M
            nm = np.linalg.norm(M)
            if nm > 1e12:
                acc += math.log(nm)
                M /= nm
        acc += math.log(max(np.linalg.norm(M), 1e-300))
        out.append(acc / len(word))
    return np.array(out)


def loo_errors(vals):
    """Self-calibrated leave-one-out errors: for each m_i, fit a quadratic in log(lam)
    on the OTHER five and predict m_i. Returns the six absolute errors.
    Golden is flagged only if |e_1| > 3*median(|e_2..6|) AND |e_1| > 5% of the spread —
    this avoids the tiny-residual blowup of a naive (error/fit-RMS) score."""
    x = np.array([math.log(lam(m)) for m in MS])
    y = np.array(vals, float)
    errs = []
    for i in range(len(MS)):
        sel = np.arange(len(MS)) != i
        coef = np.polyfit(x[sel], y[sel], 2)
        errs.append(abs(float(y[i] - np.polyval(coef, x[i]))))
    return errs


def classify(vals):
    errs = loo_errors(vals)
    e1, rest = errs[0], errs[1:]
    med = float(np.median(rest))
    spread = float(np.max(vals) - np.min(vals))
    flag = (e1 > 3 * med) and (e1 > 0.05 * max(spread, 1e-9))
    return dict(loo_errors=[round(e, 4) for e in errs], e1_over_med=round(e1 / max(med, 1e-12), 2),
                spread=round(spread, 4), flag=bool(flag))


def main():
    res = dict(meta=dict(probe="B447", date="2026-07-07"))
    words = {m: metallic_word(m) for m in MS}
    # controls
    per = np.tile([0, 1], TARGET_N // 2)[:TARGET_N]
    rnd = rng.integers(0, 2, TARGET_N)
    Tgrid = np.logspace(-2, 1, 240)

    print("=" * 76)
    print("B447 D2 — controls first (gates)")
    print("=" * 76)
    ctrl = {}
    for name, w in [("periodic", per), ("random", rnd)]:
        E = spectrum(w, 1.0)
        b, npts = transport_beta(w, 1.0)
        dq = dq_spectrum(E)
        C = specific_heat(E, Tgrid)
        ctrl[name] = dict(beta=round(b, 3), D0=round(dq[0], 3), n_C_peaks=count_peaks(C))
        print(f"  {name:9s}: beta={b:.3f}  D0={dq[0]:.3f}  C-peaks={count_peaks(C)}")
    res['controls'] = ctrl

    print("\n" + "=" * 76)
    print("B447 D2 — the m-scan (V=1 for C/D_q/labels/gamma; beta at V in " + str(V_LIST) + ")")
    print("=" * 76)
    scan = {}
    for m in MS:
        w = words[m]
        E1 = spectrum(w, 1.0)
        row = dict(lam=round(lam(m), 6), theta=round(theta(m), 6),
                   sq_kernel=int([5, 2, 13, 5, 29, 10][m - 1]))
        # C(T)
        C = specific_heat(E1, Tgrid)
        row['C_peaks'] = count_peaks(C)
        row['C_peak_T'] = round(float(Tgrid[int(np.argmax(C))]), 4)
        # D_q at V=1
        dq = dq_spectrum(E1)
        row['Dq_V1'] = {str(q): round(v, 4) for q, v in dq.items()}
        # transport across V
        row['beta'] = {}
        for V in V_LIST:
            b, npts = transport_beta(w, V)
            row['beta'][str(V)] = round(b, 4)
        # D0 across V (for the NEW-MATH family-law question)
        row['D0_V'] = {}
        for V in V_LIST:
            row['D0_V'][str(V)] = round(dq_spectrum(spectrum(w, V), qs=(0,))[0], 4)
        # gap labels
        row['gap_labels'] = gap_labels(E1, theta(m), n_top=8)
        row['label_resid_max'] = max(g['resid'] for g in row['gap_labels'])
        # gamma on/off spectrum
        Eon = E1[np.linspace(10, len(E1) - 10, 12).astype(int)]
        d = np.diff(np.sort(E1))
        i = int(np.argmax(d))
        Eoff = [float(np.sort(E1)[i] + d[i] / 2), float(E1.max() + 1.0)]
        gon = lyapunov(w, 1.0, Eon)
        goff = lyapunov(w, 1.0, np.array(Eoff))
        row['gamma_on_mean'] = round(float(gon.mean()), 4)
        row['gamma_off_gap'] = round(float(goff[0]), 4)
        row['gamma_off_out'] = round(float(goff[1]), 4)
        scan[m] = row
        print(f"  m={m}: lam={row['lam']:.4f} th={row['theta']:.4f} "
              f"C-peaks={row['C_peaks']} peakT={row['C_peak_T']} D0={row['Dq_V1']['0']} "
              f"beta(1)={row['beta']['1.0']} gam_on={row['gamma_on_mean']} "
              f"gam_gap={row['gamma_off_gap']} labres={row['label_resid_max']}")
    res['scan'] = scan

    print("\n" + "=" * 76)
    print("B447 D2 — the leave-golden-out classifier (score = (O(1)-pred)/fit-RMS)")
    print("=" * 76)
    cls = {}
    for key, getter in [
        ("D0_V1", lambda m: scan[m]['Dq_V1']['0']),
        ("D0_V2", lambda m: scan[m]['D0_V']['2.0']),
        ("beta_V1", lambda m: scan[m]['beta']['1.0']),
        ("beta_V2", lambda m: scan[m]['beta']['2.0']),
        ("C_peak_T", lambda m: scan[m]['C_peak_T']),
        ("gamma_on", lambda m: scan[m]['gamma_on_mean']),
    ]:
        vals = [getter(m) for m in MS]
        c = classify(vals)
        c['values'] = [round(v, 4) for v in vals]
        cls[key] = c
        print(f"  {key:9s}: O(m)={c['values']}  |e1|/med(|e|)={c['e1_over_med']} "
              f"spread={c['spread']}  {'FLAG' if c['flag'] else 'smooth'}")
    res['classifier'] = cls

    # internal scaling-window consistency gate (replaces the mis-attributed B186 anchor;
    # see FINDINGS: the prereg's "B163 0.91/0.77" numbers are B186's TRACE-MAP box dims,
    # a different object — documented as a prereg correction)
    print("\n  size-consistency gate (D0 at N~1000 vs N~2500, golden & silver, V=1):")
    gate = {}
    for m in (1, 2):
        d0 = {}
        for tgt in (1000, 2500):
            wl = metallic_word(m, tgt)
            d0[tgt] = round(dq_spectrum(spectrum(wl, 1.0), qs=(0,))[0], 4)
        gate[m] = d0
        print(f"    m={m}: D0(N~1000)={d0[1000]}  D0(N~2500)={d0[2500]}  drift={abs(d0[1000]-d0[2500]):.3f}")
    res['d0_size_gate'] = gate

    with open('mscan_results.json', 'w') as f:
        json.dump(res, f, indent=1)
    print("\n[mscan_results.json written]")


if __name__ == '__main__':
    main()
