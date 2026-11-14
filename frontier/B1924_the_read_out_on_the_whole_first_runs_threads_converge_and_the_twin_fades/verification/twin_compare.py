"""B1924's comparisons, from the three runs' json files (structure only is printed; no value of R).

Per component (48 numbers: the frame's 20 outputs at both ends and both covariant readings, 2 or 3 numbers each), |z| = |difference| / its sampling error, against pure noise (a standard
normal: median |z| 0.674, share above 2 4.6 %). Two kinds of comparison:
 - between n (different words, independent samples): error sqrt(se1^2 + se2^2), each se a jackknife over words;
 - mark against twin at one n (THE SAME words, so the two are correlated): the PAIRED jackknife, the jackknife of the
   difference itself, word by word. The unpaired error is also printed, to show how much the pairing matters.
The components are not independent of one another (one sample of words feeds all 48), so the shares are indicative."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
D = {}
for f in ("whole_average_2.json", "whole_average_3.json"):
    D.update(json.loads((HERE / f).read_text()))


def stats(z):
    z = np.asarray(z)
    return "median |z| %.2f, share above 2: %.0f%%, largest %.2f (%d components)" % (np.median(z), 100 * np.mean(z > 2), z.max(), len(z))


def between(a, b):
    z = []
    for k in D[a]["R"]:
        r1, r2 = np.array(D[a]["R"][k]), np.array(D[b]["R"][k])
        s1, s2 = np.array(D[a]["se"][k]), np.array(D[b]["se"][k])
        z += list(np.abs(r1 - r2) / np.sqrt(s1 ** 2 + s2 ** 2))
    return z


def paired(n):
    rm, rt = D["%d mark" % n]["rows"], D["%d twin" % n]["rows"]
    assert [r["word"] for r in rm] == [r["word"] for r in rt], "the twins were not read on the same words"
    w = np.array([r["length"] for r in rm])
    zp, zu = [], []
    for k in rm[0]["A"]:
        d = np.array([np.array(a["A"][k]) - np.array(b["A"][k]) for a, b in zip(rm, rt)])     # words x components
        mean = (w[:, None] * d).sum(0) / w.sum()
        jk = np.array([(np.delete(w, i)[:, None] * np.delete(d, i, 0)).sum(0) / np.delete(w, i).sum() for i in range(len(w))])
        se = np.sqrt((len(w) - 1) * np.mean((jk - mean) ** 2, 0))
        zp += list(np.abs(mean) / se)
        s1, s2 = np.array(D["%d mark" % n]["se"][k]), np.array(D["%d twin" % n]["se"][k])
        zu += list(np.abs(mean) / np.sqrt(s1 ** 2 + s2 ** 2))
    return zp, zu


if __name__ == "__main__":
    print("pure noise: median |z| 0.67, share above 2: 5%")
    for a, b in (("10 mark", "16 mark"), ("16 mark", "22 mark"), ("10 twin", "16 twin"), ("16 twin", "22 twin")):
        print("%s against %s (independent words): %s" % (a, b, stats(between(a, b))))
    for n in (10, 16, 22):
        zp, zu = paired(n)
        print("n = %d, the mark against its twin, PAIRED: %s" % (n, stats(zp)))
        print("n = %d, the mark against its twin, unpaired (for comparison): %s" % (n, stats(zu)))
