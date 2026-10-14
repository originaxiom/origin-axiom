"""Independent checks of T-SIGN (chat1). Own code; SnapPy 3.3.2.
 H: the b+- convention is the -W bundle: |Tor H1(b++W)| = |tr W - 2|, |Tor H1(b+-W)| = tr W + 2 (W as a product of
    L = [[1,0],[1,1]], R = [[1,1],[0,1]]), for every Lyndon word to length 12.
 A: amphichirality by symmetry_group().is_amphicheiral() for b++W and b+-W, every Lyndon word to length 10, against
    the swap-symmetry rule.
 N0x: every b+-W to length 12: geometric, orientable (the sealed N0 checked only the swap-symmetric ones).
 N1x: every swap-symmetric Lyndon word to length 18 (514): CS(b+-W) = +-pi^2/2 and CS(b++W) = 0.
 N2x: every Lyndon word to length 14: CS(b+-W) - CS(b++W) = pi^2/2 mod pi^2; Vol(b+-W) = Vol(b++W).
 D: double-cover consistency to length 8: CS(b++WW) = 2 CS(b+-W) = 2 CS(b++W) mod pi^2.
 Transient complex_volume failures are retried (up to 5 times) and counted."""
import itertools, json, math, sys, time, warnings
warnings.filterwarnings("ignore")
import snappy
PI2 = math.pi ** 2
def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y
def lyndon_upto(n):
    out = []
    for m in range(2, n + 1):
        for p in itertools.product("LR", repeat=m):
            w = "".join(p)
            if all(w < w[i:] + w[:i] for i in range(1, m)): out.append(w)
    return out
def lr(w): return min(w[i:] + w[:i] for i in range(len(w)))
def swap(w): return w.translate(str.maketrans("LR", "RL"))
def sym(w): return lr(swap(w)) in (w, lr(w[::-1]))
def trace(w):
    a, b, c, d = 1, 0, 0, 1
    for ch in w:
        if ch == "L": a, b, c, d = a + b, b, c + d, d      # right-multiply by [[1,0],[1,1]]
        else: a, b, c, d = a, a + b, c, c + d                # right-multiply by [[1,1],[0,1]]
    return a + d
retries = {"n": 0}
def cvol(M):
    for t in range(6):
        try:
            return complex(M.complex_volume())
        except ValueError:
            retries["n"] += 1
    raise RuntimeError("complex_volume failed 6 times")
out = {}; t0 = time.time()
# H
hbad = []
for w in lyndon_upto(12):
    tr = trace(w)
    for sgn, want in (("+", abs(tr - 2)), ("-", tr + 2)):
        H = snappy.Manifold("b+" + sgn + w).homology()
        tors = 1
        for e in H.elementary_divisors():
            if e != 0: tors *= e
        if H.betti_number() != 1 or tors != want: hbad.append([w, sgn, str(H), want])
out["H_convention_violations"] = hbad[:20]; out["H_n_violations"] = len(hbad)
# A
abad = []
na = {"+": 0, "-": 0}
for w in lyndon_upto(10):
    for sgn in "+-":
        M = snappy.Manifold("b+" + sgn + w)
        amph = M.symmetry_group().is_amphicheiral()
        na[sgn] += int(amph)
        if amph != sym(w): abad.append([w, sgn, amph, sym(w)])
out["A_amphichiral_counts_to10"] = na; out["A_swap_rule_count_to10"] = sum(sym(w) for w in lyndon_upto(10))
out["A_mismatches"] = abad
# N0x
n0bad = []
for w in lyndon_upto(12):
    M = snappy.Manifold("b+-" + w)
    if M.solution_type() != "all tetrahedra positively oriented" or not M.is_orientable(): n0bad.append([w, M.solution_type()])
out["N0x_minus_to12_non_geometric_or_nonorientable"] = n0bad
# N1x
W18 = lyndon_upto(18)
S18 = [w for w in W18 if sym(w)]
n1 = {"n_sym_to18": len(S18), "by_length": {}, "bad_minus": [], "bad_plus": [], "max_dev_minus": 0.0, "max_abs_plus": 0.0,
      "vol_mismatch": []}
for w in S18:
    n1["by_length"][len(w)] = n1["by_length"].get(len(w), 0) + 1
    Mm, Mp = snappy.Manifold("b+-" + w), snappy.Manifold("b++" + w)
    cm, cp = red(cvol(Mm).imag), red(cvol(Mp).imag)
    dev = abs(abs(cm) - PI2 / 2)
    n1["max_dev_minus"] = max(n1["max_dev_minus"], dev); n1["max_abs_plus"] = max(n1["max_abs_plus"], abs(cp))
    if dev > 1e-6: n1["bad_minus"].append([w, cm])
    if abs(cp) > 1e-6: n1["bad_plus"].append([w, cp])
    vm, vp = float(Mm.volume()), float(Mp.volume())
    if abs(vm - vp) > 1e-9: n1["vol_mismatch"].append([w, vp, vm])
    if Mm.solution_type() != "all tetrahedra positively oriented": n1["bad_minus"].append([w, "non-geometric"])
out["N1x"] = n1
# N2x
W14 = [w for w in W18 if len(w) <= 14]
n2 = {"n_words_to14": len(W14), "bad": [], "max_dev": 0.0, "vol_mismatch": [], "max_dvol": 0.0}
for w in W14:
    Mm, Mp = snappy.Manifold("b+-" + w), snappy.Manifold("b++" + w)
    cm, cp = red(cvol(Mm).imag), red(cvol(Mp).imag)
    dev = abs(abs(red(cm - cp)) - PI2 / 2)
    n2["max_dev"] = max(n2["max_dev"], dev)
    if dev > 1e-6: n2["bad"].append([w, cp, cm])
    dv = abs(float(Mm.volume()) - float(Mp.volume())); n2["max_dvol"] = max(n2["max_dvol"], dv)
    if dv > 1e-9: n2["vol_mismatch"].append([w, dv])
out["N2x"] = {k: (v[:20] if isinstance(v, list) else v) for k, v in n2.items()}
out["N2x"]["n_bad"] = len(n2["bad"])
# D
dbad = []; dmax = 0.0
for w in lyndon_upto(8):
    c2 = red(cvol(snappy.Manifold("b++" + w + w)).imag)
    cp = red(cvol(snappy.Manifold("b++" + w)).imag); cm = red(cvol(snappy.Manifold("b+-" + w)).imag)
    e1, e2 = abs(red(c2 - 2 * cp)), abs(red(c2 - 2 * cm))
    dmax = max(dmax, e1, e2)
    if e1 > 1e-6 or e2 > 1e-6: dbad.append([w, c2, cp, cm])
out["D_double_cover"] = {"n_words_to8": len(lyndon_upto(8)), "violations": dbad, "max_dev": dmax}
out["complex_volume_retries"] = retries["n"]; out["seconds"] = round(time.time() - t0, 1)
json.dump(out, open(sys.argv[1], "w"), indent=1, default=str)
print(json.dumps(out, indent=1, default=str)[:6000])
