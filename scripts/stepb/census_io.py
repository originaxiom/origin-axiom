"""STEP B's generator, the census loader (data-free; the second review's storage conditions).

- Refuses any file whose sha256 differs from the manifest (the manifest is committed and pushed before any read).
- Reads the refined census's per-line gzip JSONL: per record {"line": [a, b], "order": N, "tau": [re, im], "rows": [[dir, radius,
  reading, up, down, lepton, V, J, V defined], ...]} or {"error": ...}; error configurations are kept as a list (excluded
  identically for data and null).
- The reading label (B1821's evaluator) is per sector (up, down, lepton) "S" or "S~"; its index is 4u + 2d + l, S~ = 1.
- The directions are B1810's thirteen (B1821's DIRS); a0 (index 1) and F_-2 (index 6) are one direction (B1824): the loader
  keeps a0's rows and drops F_-2's after checking, per configuration, that the two agree at the census's precision
  (dup_disagreement: within 1e-9 absolutely, or both below the roundoff floor, or within 1e-6 in log10; the moduli and |J|
  where both define the mixing); `dup_tol` bounds what remains.
- The mirror (B1821): the census covers Re tau in [0, 1/2]; the configuration (-x + i y, (a, -b)) is (x + i y, (a, b)) with
  J -> -J.  `mirror_partner` gives each line's partner class in the menu, for the tau mixture over the whole band."""
from __future__ import annotations

import gzip, hashlib, json, math, pathlib
from fractions import Fraction as Fr

import numpy as np

import stepb_core as C

A0, FM2 = 1, 6
DUP_TOL = 1e-6          # log10: the identity's agreement for values well above the precision limit
DUP_FLOOR = 1e-12       # the roundoff floor (cells.FLOOR): below it an output is a structural zero (or exact 0)
DUP_ABS = 1e-9          # the double-precision limit of a ratio of singular values: Weyl's bound gives an absolute error of
                        # order c eps, c up to ~1e6 where F_-2's components span e^(pi Im tau)/4 ~ 7e4 at Im tau = 4 (the
                        # S279 diagnostic: 2184 physical disagreements, all m1/m3 at Im 3.5-4, at most 3.3e-5 in log10)


def dup_disagreement(x: float, y: float) -> float:
    """0 when an a0 value and its F_-2 twin agree at the census's precision (B1824: one direction), else their |log10|
    difference (inf for a physical value paired with a structural zero).  They agree when they differ by at most DUP_ABS,
    or both lie below the floor (two roundoff values, or exact zeros), or their log10 difference is at most DUP_TOL."""
    if abs(x - y) <= DUP_ABS:
        return 0.0
    xb, yb = x < DUP_FLOOR, y < DUP_FLOOR
    if xb and yb:
        return 0.0
    if xb != yb:
        return math.inf
    d = abs(math.log10(x) - math.log10(y))
    return 0.0 if d <= DUP_TOL else d


def sha256(path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def verify(directory, manifest: dict) -> None:
    d = pathlib.Path(directory)
    names = sorted(p.name for p in d.glob("*.jsonl.gz"))
    if sorted(manifest) != names:
        raise ValueError("the files do not match the manifest's list: %d files, %d in the manifest" % (len(names), len(manifest)))
    bad = [n for n in names if sha256(d / n) != manifest[n]]
    if bad:
        raise ValueError("sha256 mismatch, refused: %s" % bad[:5])


def reading_index(label: str) -> int:
    parts, i = [], 0
    while i < len(label):
        if label[i] != "S":
            raise ValueError(label)
        if i + 1 < len(label) and label[i + 1] == "~":
            parts.append(1); i += 2
        else:
            parts.append(0); i += 1
    if len(parts) != 3:
        raise ValueError(label)
    return 4 * parts[0] + 2 * parts[1] + parts[2]


def line_key(a: str, b: str):
    A, B = Fr(a), Fr(b)
    return min((A, B), ((-A) % 1, (-B) % 1))


def mirror_partner(key):
    a, b = key
    return line_key(str(a), str((-b) % 1))


def load(directory, manifest: dict, dup_tol: float = 1e-6):
    """returns (Census, info): every row except F_-2's, after the duplicate check; info has the configurations' lines and tau,
    the error configurations, and the largest a0/F_-2 difference in log10"""
    verify(directory, manifest)
    cfg_l, cfg_t, errors = [], [], []
    cols = {k: [] for k in ("cfg", "d", "r", "k", "m", "v", "J", "vdef")}
    worst_dup = 0.0
    for path in sorted(pathlib.Path(directory).glob("*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                rec = json.loads(line)
                key = line_key(*rec["line"]); tau = tuple(rec["tau"])
                if "error" in rec:
                    errors.append((key, tau, rec["error"])); continue
                ci = len(cfg_l); cfg_l.append(key); cfg_t.append(tau)
                by = {}
                for row in rec["rows"]:
                    d, r, lab, up, dn, lp, V, J, vd = row
                    by[(d, r, lab)] = row
                for (d, r, lab), row in by.items():
                    if d == FM2:
                        twin = by[(A0, r, lab)]
                        both_v = bool(row[8]) and bool(twin[8])          # |V| is compared only where both define it
                        for x, y in zip(_flat(row, both_v), _flat(twin, both_v)):
                            worst_dup = max(worst_dup, dup_disagreement(x, y))
                        continue
                    _, _, _, up, dn, lp, V, J, vd = row
                    cols["cfg"].append(ci); cols["d"].append(d); cols["r"].append(r); cols["k"].append(reading_index(lab))
                    cols["m"].append([up, dn, lp]); cols["v"].append(V); cols["J"].append(J); cols["vdef"].append(bool(vd))
    if worst_dup > dup_tol:
        raise ValueError("a0 and F_-2 disagree beyond the census's precision (%.3g in log10; B1824 says they are one direction)" % worst_dup)
    cen = C.Census(cfg=np.array(cols["cfg"]), d=np.array(cols["d"]), r=np.array(cols["r"]), k=np.array(cols["k"]),
                   m=np.array(cols["m"], float), v=np.array(cols["v"], float), J=np.array(cols["J"], float),
                   vdef=np.array(cols["vdef"]), lines=cfg_l, tau=np.array(cfg_t, float))
    return cen, {"errors": errors, "worst_a0_Fm2_log10": worst_dup, "n_cfg": len(cfg_l)}


def _flat(row, with_v: bool):
    _, _, _, up, dn, lp, V, J, _ = row
    return list(up) + list(dn) + list(lp) + ((list(V) + [abs(J)]) if with_v else [])


# ---- the streaming loader (the fourth review's F7): compact arrays, no per-row Python containers ----
from dataclasses import dataclass as _dc


@_dc
class CompactCensus:
    """the census as compact arrays: F (n, 10) float32 natural-log features (stepb_core.features' order), J (n,) float32 SIGNED
    (the interpolant's tenth coordinate, cells.py), cfg int32, d / r / k int8, vdef bool; lines and tau per configuration.
    Same attribute names as stepb_core.Census for the downstream code."""
    F: np.ndarray
    J: np.ndarray
    cfg: np.ndarray
    d: np.ndarray
    r: np.ndarray
    k: np.ndarray
    vdef: np.ndarray
    lines: list
    tau: np.ndarray


ROWS_KEPT_PER_CFG = 13 * 2 * 8 - 2 * 8          # 208 rows, less F_-2's 16


def _row_features(rows) -> tuple:
    """(F (n, 10) float32, d, r, k, vdef, J signed float32) for one configuration's rows without F_-2; logs of the (m2/m3,
    m1/m3) per sector, the three moduli and |J|; -inf where an output is not positive"""
    d = np.array([x[0] for x in rows], np.int8); r = np.array([x[1] for x in rows], np.int8)
    k = np.array([reading_index(x[2]) for x in rows], np.int8)
    up = np.array([x[3] for x in rows], float); dn = np.array([x[4] for x in rows], float); lp = np.array([x[5] for x in rows], float)
    V = np.array([x[6] for x in rows], float); Js = np.array([x[7] for x in rows], float); J = np.abs(Js)
    vd = np.array([bool(x[8]) for x in rows])
    raw = np.stack([up[:, 1], up[:, 0], dn[:, 1], dn[:, 0], lp[:, 1], lp[:, 0], V[:, 0], V[:, 1], V[:, 2], J], axis=1)
    with np.errstate(divide="ignore", invalid="ignore"):
        F = np.where(raw > 0, np.log(raw), -np.inf).astype(np.float32)
    return F, d, r, k, vd, Js.astype(np.float32)


def load_compact(directory, manifest: dict, n_cfg_expected: int, dup_tol: float = 1e-6):
    """stream every file into preallocated arrays (n_cfg_expected x 192 rows); the a0/F_-2 check as load() does it"""
    verify(directory, manifest)
    n = n_cfg_expected * ROWS_KEPT_PER_CFG
    F = np.empty((n, 10), np.float32); Jsg = np.empty(n, np.float32); cfg = np.empty(n, np.int32)
    d = np.empty(n, np.int8); r = np.empty(n, np.int8); k = np.empty(n, np.int8); vdef = np.empty(n, bool)
    lines, taus, errors = [], [], []; pos = 0; worst = 0.0
    for path in sorted(pathlib.Path(directory).glob("*.jsonl.gz")):
        with gzip.open(path, "rt", encoding="utf-8") as fh:
            for line in fh:
                rec = json.loads(line)
                key = line_key(*rec["line"]); tau = tuple(rec["tau"])
                if "error" in rec:
                    errors.append((key, tau, rec["error"])); continue
                by = {(x[0], x[1], x[2]): x for x in rec["rows"]}
                for (dd, rr, lab), x in by.items():
                    if dd == FM2:
                        y = by[(A0, rr, lab)]; both_v = bool(x[8]) and bool(y[8])
                        for a, b in zip(_flat(x, both_v), _flat(y, both_v)):
                            worst = max(worst, dup_disagreement(a, b))
                keep = [x for x in rec["rows"] if x[0] != FM2]
                assert len(keep) == ROWS_KEPT_PER_CFG, len(keep)
                Fi, di, ri, ki, vi, Ji = _row_features(keep)
                ci = len(lines); lines.append(key); taus.append(tau)
                sl = slice(pos, pos + len(keep))
                F[sl], d[sl], r[sl], k[sl], vdef[sl], cfg[sl], Jsg[sl] = Fi, di, ri, ki, vi, ci, Ji
                pos += len(keep)
    if worst > dup_tol:
        raise ValueError("a0 and F_-2 disagree beyond the census's precision (%.3g in log10; B1824 says they are one direction)" % worst)
    if pos != n:
        raise ValueError("row count %d differs from the expected %d (%d error configurations)" % (pos, n, len(errors)))
    return CompactCensus(F=F, J=Jsg, cfg=cfg, d=d, r=r, k=k, vdef=vdef, lines=lines, tau=np.array(taus, float)), \
        {"errors": errors, "worst_a0_Fm2_log10": worst, "n_cfg": len(lines), "bytes_per_row": (F.nbytes + Jsg.nbytes + cfg.nbytes + d.nbytes + r.nbytes + k.nbytes + vdef.nbytes) / n}
