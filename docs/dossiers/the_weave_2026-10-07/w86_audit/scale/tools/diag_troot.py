"""Diagnostic: the T-ROOT measuring loop (same words, same order, same calls), each SnapPy call wrapped separately,
recording the exception type and message, and which call raised. Also records all values for comparison."""
import json, math, sys, time, traceback, warnings
warnings.filterwarnings("ignore")
import snappy
PI2 = math.pi ** 2
def red(x):
    y = math.fmod(x, PI2)
    if y > PI2 / 2: y -= PI2
    if y <= -PI2 / 2: y += PI2
    return y
def lyndon(n, alphabet="LR"):
    k = len(alphabet); w = [-1]
    while w:
        w[-1] += 1
        m = len(w)
        yield "".join(alphabet[i] for i in w)
        while len(w) < n:
            w.append(w[len(w) - m])
        while w and w[-1] == k - 1:
            w.pop()
words = [w for w in lyndon(18) if len(w) >= 2]
words.sort(key=lambda w: (len(w), w))
events, vals = [], {}
t0 = time.time()
for i, w in enumerate(words):
    M = snappy.Manifold("b++" + w)
    rec = {}
    for name, f in (("volume", lambda: float(M.volume())), ("complex_volume", lambda: complex(M.complex_volume())),
                    ("solution_type", lambda: M.solution_type())):
        try:
            rec[name] = f()
        except BaseException as e:
            events.append({"i": i, "word": w, "call": name, "type": type(e).__name__, "msg": str(e)[:300],
                           "tb": traceback.format_exc()[-600:]})
            rec[name] = None
    vals[w] = [rec["volume"], None if rec["complex_volume"] is None else red(rec["complex_volume"].imag), rec["solution_type"]]
out = {"n": len(words), "events": events, "seconds": round(time.time() - t0, 1)}
json.dump({"meta": out, "vals": vals}, open(sys.argv[1], "w"))
print(json.dumps(out, indent=1)[:5000])
