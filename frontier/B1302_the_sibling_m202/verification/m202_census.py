"""B1302: the automorphism census of pi_1(m202) on SnapPy's own holonomy (numeric, no exact rep needed): word pairs (a', b') of length <= 5
preserving the trace triple up to SL2 signs and sending the relator to +-I; classes by the H1 = Z^2 action.  fc R72b / sm:B1282: 180 pairs, 12 classes."""
import itertools, json, warnings
warnings.filterwarnings("ignore")
import numpy as np, snappy
M = snappy.Manifold("m202"); G = M.fundamental_group(); rel = G.relators()[0]
Gh = M.high_precision().fundamental_group()
def mat(w): m = Gh.SL2C(w); return np.array([[complex(m[0, 0]), complex(m[0, 1])], [complex(m[1, 0]), complex(m[1, 1])]])
An, Bn = mat("a"), mat("b"); letters = {"a": An, "b": Bn, "A": np.linalg.inv(An), "B": np.linalg.inv(Bn)}
def ev(w):
    Mx = np.eye(2, dtype=complex)
    for ch in w: Mx = Mx @ letters[ch]
    return Mx
def reduced(w):
    out = []
    for ch in w:
        if out and out[-1] == ch.swapcase(): out.pop()
        else: out.append(ch)
    return "".join(out)
def inv_str(w): return w.swapcase()[::-1]
def subst(word, ia, ib):
    out = ""
    for ch in word:
        img = ia if ch.lower() == "a" else ib
        out += img if ch.islower() else inv_str(img)
    return reduced(out)
TA, TB, TAB = np.trace(An), np.trace(Bn), np.trace(An @ Bn)
print("relator -> +-I on SnapPy's lift:", np.allclose(ev(rel), np.eye(2), atol=1e-9) or np.allclose(ev(rel), -np.eye(2), atol=1e-9), " traces", np.round(TA, 6), np.round(TB, 6), np.round(TAB, 6))
words = []
for n in range(1, 6):
    for tup in itertools.product("aAbB", repeat=n):
        w = "".join(tup)
        if reduced(w) == w: words.append(w)
def okt(w, t): x = np.trace(ev(w)); return any(abs(x - y) < 1e-9 for y in (t, -t))
ca = [w for w in words if okt(w, TA)]; cb = [w for w in words if okt(w, TB)]
def is_pm_I(Mx): return np.allclose(Mx, np.eye(2), atol=1e-8) or np.allclose(Mx, -np.eye(2), atol=1e-8)
found = []
for ia in ca:
    Ma = ev(ia)
    for ib in cb:
        if not any(abs(np.trace(Ma @ ev(ib)) - y) < 1e-9 for y in (TAB, -TAB)): continue
        if not is_pm_I(ev(subst(rel, ia, ib))): continue
        found.append((ia, ib))
def h1(ia, ib):
    e = lambda w, g: sum(1 if ch == g else -1 if ch == g.upper() else 0 for ch in w)
    return ((e(ia, "a"), e(ib, "a")), (e(ia, "b"), e(ib, "b")))
classes = {}
for ia, ib in found: classes.setdefault(h1(ia, ib), []).append((ia, ib))
print(f"census: {len(found)} word pairs (length <= 5), {len(classes)} distinct H1 actions  [fc R72b / sm:B1282: 180 / 12]")
def order(Mx):
    import numpy as np
    A_ = np.array(Mx); P = np.eye(2, dtype=int)
    for k in range(1, 13):
        P = P @ A_
        if (P == np.eye(2, dtype=int)).all(): return k
    return None
for k, v in sorted(classes.items(), key=lambda kv: (order(kv[0]) or 99, kv[0])): print(f"   H1 action {k}  order {order(k)}  count {len(v):3d}  e.g. {v[0]}")
json.dump(dict(pairs=len(found), classes=len(classes), actions=[dict(action=list(map(list, k)), order=order(k), count=len(v), rep=v[0]) for k, v in classes.items()]), open("m202_census.json", "w"))
