#!/usr/bin/env python3
"""B452 — the FROZEN comparison registry + typed-gate machinery (Ethogram EZ).

Frozen at the E0 commit. Changes after this commit are prohibited (a change = a new campaign).

Signature type (the EZ-1/EZ-2 bridge, the FATAL fix): every catalog behavior reduces to
    Signature = (kind: str, ints: tuple[int,...], discs: tuple[int,...], values: tuple[float,...])
EZ-1 compares whole signatures against null-ensemble catalogs (frequency).
EZ-2 feeds ONLY the numeric parts (ints as exact ratios, values) to the B322/B398 machinery.
"""
from collections import Counter

import numpy as np

# ---------------- the frozen numeric registry (B398's 20, 1-sigma) ----------------
NUMERIC_TARGETS = [
    ("pmns_s12", 0.307, 0.013), ("pmns_s23", 0.545, 0.023), ("pmns_s13", 0.0220, 0.0007),
    ("weinberg_MZ", 0.23122, 0.00004), ("alpha", 0.0072974, 0.0000001),
    ("alpha_s_MZ", 0.1179, 0.0009), ("ckm_lambda", 0.2250, 0.0007),
    ("ckm_A", 0.826, 0.012), ("ckm_rhobar", 0.159, 0.010), ("ckm_etabar", 0.348, 0.010),
    ("mmu_mtau", 0.05946, 0.00005), ("me_mmu", 0.004836, 0.000001),
    ("mc_mt", 0.0074, 0.0004), ("ms_mb", 0.022, 0.002), ("mu_md", 0.47, 0.06),
    ("mb_mt", 0.0243, 0.0005), ("mtau_mt", 0.01027, 0.00005),
    ("md_ms", 0.050, 0.004), ("theta_c_sin2", 0.0506, 0.0003), ("jcp_ckm_e5", 0.3, 0.01),
]

P_BINDING = 0.01          # the B398 gate
NULL_DRAWS = 2000         # the B322 ensemble size
RNG_SEED = 20260708


# ---------------- signatures ----------------
def signature(kind, ints=(), discs=(), values=()):
    return (str(kind), tuple(int(i) for i in ints), tuple(int(d) for d in discs),
            tuple(round(float(v), 12) for v in values))


def numeric_parts(sigs):
    """EZ-2 input: all values + all ratios of positive int pairs in (0,1)."""
    out = []
    for _, ints, _, values in sigs:
        out.extend(v for v in values if 0 < v < 1)
        pos = [i for i in ints if i > 0]
        for a in pos:
            for b in pos:
                if a < b:
                    out.append(a / b)
    return sorted(set(out))


# ---------------- EZ-1: specificity (behavior vs behavior) ----------------
def ez1_specificity(object_sigs, null_catalogs, licensed=True):
    """p1 per object signature = frequency among null catalogs. p-values only if licensed
    (word channel, n>=1000); otherwise adjudication is forced/laundered, never p."""
    n = len(null_catalogs)
    counts = Counter()
    for cat in null_catalogs:
        seen = set(cat)
        for s in object_sigs:
            if s in seen:
                counts[s] += 1
    out = {}
    for s in object_sigs:
        p1 = counts[s] / n if n else 1.0
        out[s] = dict(p1=p1, fires=bool(licensed and n >= 100 and p1 < P_BINDING))
    return out


# ---------------- EZ-2: correspondence (number vs number; B322/B398 machinery) ----------------
def match_count(targets, numberset, use_sigma=True, tol=0.01):
    ns = np.asarray(sorted(numberset))
    c = 0
    for name, center, sigma in targets:
        w = sigma if use_sigma else abs(center) * tol
        i = np.searchsorted(ns, center - w, side="left")
        j = np.searchsorted(ns, center + w, side="right")
        c += (j > i)
    return c


def ez2_correspondence(object_sigs, seed=RNG_SEED, draws=NULL_DRAWS):
    ns = numeric_parts(object_sigs)
    if not ns:
        return dict(hits=0, p=1.0, fires=False, n_numbers=0)
    hits = match_count(NUMERIC_TARGETS, ns)
    rng = np.random.default_rng(seed)
    lo, hi = np.log(1e-3), np.log(1.0)
    null = []
    for _ in range(draws):
        fake_targets = [(f"r{k}", float(np.exp(rng.uniform(lo, hi))), 0.0)
                        for k in range(len(NUMERIC_TARGETS))]
        # null: random targets with matched RELATIVE windows (sigma/center preserved)
        fake = [(n_, c_, c_ * (t[2] / t[1])) for (n_, c_, _), t in zip(fake_targets, NUMERIC_TARGETS)]
        null.append(match_count(fake, ns))
    null = np.array(null)
    p = float((null >= hits).mean())
    return dict(hits=hits, null_mean=float(null.mean()),
                null_p99=float(np.percentile(null, 99)), p=p,
                fires=bool(p < P_BINDING), n_numbers=len(ns))


# ---------------- the structural predicates (frozen; can never fire H1 alone) ----------------
def p_gen3(object_sigs, null_catalogs):
    has3 = any(3 in s[1] for s in object_sigs)
    in_null = any(any(3 in s[1] for s in cat) for cat in null_catalogs)
    return has3 and not in_null


def p_gauge(object_sigs, null_catalogs):
    def has(cat):
        return any(set([8, 3, 1]) <= set(s[1]) or set([3, 2, 1]) <= set(s[1]) for s in cat)
    return has(object_sigs) and not any(has(c) for c in null_catalogs)


def p_cp(object_sigs, null_catalogs):
    # a sign-definite parity-odd invariant: kind 'chirality' with a single nonzero value,
    # object-specific. (Expected FAIL: the banked heartbeat oscillates, B448.)
    def has(cat):
        return any(s[0] == "chirality-definite" for s in cat)
    return has(object_sigs) and not any(has(c) for c in null_catalogs)


STRUCTURAL = [("P_GEN3", p_gen3), ("P_GAUGE", p_gauge), ("P_CP", p_cp)]


def structural_joint(object_sigs, null_catalogs):
    k = sum(1 for _, f in STRUCTURAL if f(object_sigs, null_catalogs))
    return dict(satisfied=k, can_fire_alone=False)   # frozen: never fires H1 alone
