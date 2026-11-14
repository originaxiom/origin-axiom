"""Comparisons of the read-out with the canonical end (expectations in canon_readout.py's docstring, written before the
run): per convention (maximal horoball L_max; length-2 horocycle L_2), n = 16 against n = 22 (independent words), and
the mark against its twin at each n (paired, the same words). Structure only is printed."""
import json, pathlib
import numpy as np
HERE = pathlib.Path(__file__).resolve().parent
D = json.loads((HERE / "canon_readout.json").read_text())


def keys(conv):
    return [k for k in D["16 mark"]["R"] if ("|%s|" % conv) in k]


def stats(z):
    z = np.asarray(z)
    return "median |z| %.2f, share above 2: %.0f%%, largest %.2f (%d numbers)" % (np.median(z), 100 * np.mean(z > 2), z.max(), len(z))


def between(a, b, conv):
    z = []
    for k in keys(conv):
        r1, r2 = np.array(D[a]["R"][k]), np.array(D[b]["R"][k]); s1, s2 = np.array(D[a]["se"][k]), np.array(D[b]["se"][k])
        z += list(np.abs(r1 - r2) / np.sqrt(s1 ** 2 + s2 ** 2))
    return z


def paired(n, conv):
    rm, rt = D["%d mark" % n]["rows"], D["%d twin" % n]["rows"]
    assert [r["word"] for r in rm] == [r["word"] for r in rt]
    w = np.array([r["length"] for r in rm]); z = []
    for k in keys(conv):
        d = np.array([np.array(a["A"][k]) - np.array(b["A"][k]) for a, b in zip(rm, rt)])
        mean = (w[:, None] * d).sum(0) / w.sum()
        jk = np.array([(np.delete(w, i)[:, None] * np.delete(d, i, 0)).sum(0) / np.delete(w, i).sum() for i in range(len(w))])
        se = np.sqrt((len(w) - 1) * np.mean((jk - mean) ** 2, 0))
        z += list(np.abs(mean) / se)
    return z


if __name__ == "__main__":
    print("pure noise: median |z| 0.67, share above 2: 5%")
    for conv in ("L_max", "L_2"):
        for name in ("mark", "twin"):
            print("%s, %s: n = 16 against n = 22: %s" % (conv, name, stats(between("16 %s" % name, "22 %s" % name, conv))))
        for n in (16, 22):
            print("%s: the mark against its twin at n = %d, paired: %s" % (conv, n, stats(paired(n, conv))))
