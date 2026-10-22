"""B1722, after the read (labelled; the completion map's C4, P-286): is the pull-back walk's limit a uniform random word?
The walk on SL(2, Z) steps L, R with probability (1 - p)/2 each and L^-1, R^-1 with p/2 each (B1663). Its limit point's
continued-fraction digits are read from the two columns of the product, keeping the digits on which they agree. If the
digits are i.i.d. with P(k) = 2^-k, the limit is a uniform random infinite word in L, R, and a thread read from it is
drawn from the weave's uniform measure (B1722's W1), which gives every primitive class of one length the same weight.
Importing computes nothing.
    python3 -B walk_digits.py      # writes walk_digits.json beside itself"""
import collections, json, pathlib, random
HERE = pathlib.Path(__file__).resolve().parent
L, R, Li, Ri = ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((1, 0), (-1, 1)), ((1, -1), (0, 1))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def cf(p, q, kmax=60):
    out = []
    while q and len(out) < kmax:
        a, r = divmod(p, q); out.append(a); p, q = q, r
    return out


def run(p, n_walks, steps, seed):
    rng = random.Random(seed); marg = collections.Counter(); pair = collections.Counter()
    for _ in range(n_walks):
        M = ((1, 0), (0, 1))
        for _ in range(steps):
            u = rng.random()
            M = mul(M, L if u < (1 - p) / 2 else R if u < 1 - p else Li if u < 1 - p / 2 else Ri)
        (a, b), (c, d) = M
        if c == 0 or d == 0: continue
        x, y = cf(a, c), cf(b, d); k = 0
        while k < min(len(x), len(y)) - 1 and x[k] == y[k]: k += 1
        dig = [t for t in x[1:k - 1] if t > 0]      # the integer part and the last agreeing digit dropped
        marg.update(min(t, 5) for t in dig); pair.update((min(s, 3), min(t, 3)) for s, t in zip(dig, dig[1:]))
    nd, npair = sum(marg.values()), sum(pair.values())
    q = lambda k: 2.0 ** -k if k < 3 else 0.25
    return {"p": p, "walks": n_walks, "steps": steps, "digits": nd,
            "marginals_1_to_4_and_5plus": [marg[k] / nd for k in range(1, 6)],
            "max_pair_deviation_from_independent_geometric": max(abs(pair[(s, t)] / npair - q(s) * q(t)) for s in (1, 2, 3) for t in (1, 2, 3))}


def main():
    out = {"geometric_1_to_4_and_5plus": [0.5, 0.25, 0.125, 0.0625, 0.0625], "runs": [run(0.0, 3000, 150, 1722), run(0.5, 3000, 600, 1722)]}
    json.dump(out, open(HERE / "walk_digits.json", "w"), indent=1)
    for r in out["runs"]: print(r)


if __name__ == "__main__":
    main()
