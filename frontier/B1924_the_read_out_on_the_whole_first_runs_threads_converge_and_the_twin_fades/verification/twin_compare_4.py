"""The fourth run's comparisons (expectations in whole_average_4.py's docstring, written before the run).
Per number (48), |z| against pure noise (median 0.67, 5 % above 2). Structure only is printed."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
D = {}
for f in ("whole_average_3.json", "whole_average_4.json"):
    D.update(json.loads((HERE / f).read_text()))


def stats(z):
    z = np.asarray(z)
    return "median |z| %.2f, share above 2: %.0f%%, largest %.2f (%d numbers)" % (np.median(z), 100 * np.mean(z > 2), z.max(), len(z))


def between(a, b):
    z = []
    for k in D[a]["R"]:
        r1, r2 = np.array(D[a]["R"][k]), np.array(D[b]["R"][k]); s1, s2 = np.array(D[a]["se"][k]), np.array(D[b]["se"][k])
        z += list(np.abs(r1 - r2) / np.sqrt(s1 ** 2 + s2 ** 2))
    return z


def pooled(a, b):
    """the inverse-variance pool of two independent samples"""
    R, se = {}, {}
    for k in D[a]["R"]:
        r1, r2 = np.array(D[a]["R"][k]), np.array(D[b]["R"][k]); s1, s2 = np.array(D[a]["se"][k]), np.array(D[b]["se"][k])
        w1, w2 = 1 / s1 ** 2, 1 / s2 ** 2
        R[k] = (w1 * r1 + w2 * r2) / (w1 + w2); se[k] = 1 / np.sqrt(w1 + w2)
    return {"R": R, "se": se}


def paired(label):
    rm, rt = D["%s mark" % label]["rows"], D["%s twin" % label]["rows"]
    assert [r["word"] for r in rm] == [r["word"] for r in rt]
    w = np.array([r["length"] for r in rm]); zp = []
    for k in rm[0]["A"]:
        d = np.array([np.array(a["A"][k]) - np.array(b["A"][k]) for a, b in zip(rm, rt)])
        mean = (w[:, None] * d).sum(0) / w.sum()
        jk = np.array([(np.delete(w, i)[:, None] * np.delete(d, i, 0)).sum(0) / np.delete(w, i).sum() for i in range(len(w))])
        se = np.sqrt((len(w) - 1) * np.mean((jk - mean) ** 2, 0))
        zp += list(np.abs(mean) / se)
    return zp


if __name__ == "__main__":
    print("pure noise: median |z| 0.67, share above 2: 5%")
    for name in ("mark", "twin"):
        print("(a) n = 22, the two independent samples, %s: %s" % (name, stats(between("22 %s" % name, "22b %s" % name))))
    for name in ("mark", "twin"):
        D["22p %s" % name] = pooled("22 %s" % name, "22b %s" % name)
        print("(b) n = 22 pooled against n = 28, %s: %s" % (name, stats(between("22p %s" % name, "28 %s" % name))))
    print("(c) n = 28, the mark against its twin, paired: %s" % stats(paired("28")))
    print("    n = 22 (second sample), the mark against its twin, paired: %s" % stats(paired("22b")))
