"""G1 — does the Weyl sign hear the discriminant? (prereg 5848c32d)
Golden word: B_w = 3I - w - w^-1 (disc 5). Silver word: B_w = 6I - w - w^-1
(disc 32). Test det(w) vs p-parity of det(B_w) on W(E6) and W(A2)."""
import sys
sys.path.insert(0, '<seat-workdir>/next_queue/n1_counting')
import numpy as np
import n1_jeffrey_terms as J

def vp(n, p):
    v = 0
    n = abs(n)
    while n and n % p == 0:
        v += 1
        n //= p
    return v

def test_group(Wmats, eps, name, dim):
    for tr_word, disc, label in ((3, 5, "golden"), (6, 32, "silver"), (5, 21, "tr5: det(A+I)=7 PREDICT v7"), (7, 45, "tr7: det(A+I)=9 PREDICT none")):
        agree = {p: 0 for p in (2, 3, 5, 7)}
        total = 0
        dets = {}
        for idx in range(len(Wmats)):
            w = Wmats[idx]
            winv = np.rint(np.linalg.inv(w)).astype(np.int64)
            B = tr_word * np.eye(dim, dtype=np.int64) - w - winv
            d = int(round(abs(np.linalg.det(B.astype(float)))))
            s = int(eps[idx])
            total += 1
            for p in agree:
                if s == (-1) ** vp(d, p):
                    agree[p] += 1
            dets[d] = dets.get(d, 0) + 1
        print(f"{name} {label} (tr={tr_word}, disc={disc}): "
              f"sign agreement: " + " ".join(f"v_{p}: {agree[p]}/{total}" for p in agree),
              flush=True)
        if label == "silver":
            print(f"   silver det multiset ({name}): {sorted(dets.items())}", flush=True)

W6, eps6 = J.weyl_group()
test_group(W6, eps6, "W(E6)", 6)
s1 = np.array([[-1, 1], [0, 1]]); s2 = np.array([[1, 0], [1, -1]])
Wa, ea = [np.eye(2, dtype=int)], [1]
frontier = [(np.eye(2, dtype=int), 1)]
seen = {tuple(np.eye(2, dtype=int).flatten())}
while frontier:
    m, s = frontier.pop()
    for g in (s1, s2):
        nm = m @ g
        k = tuple(nm.flatten())
        if k not in seen:
            seen.add(k)
            Wa.append(nm); ea.append(-s)
            frontier.append((nm, -s))
assert len(Wa) == 6
test_group(Wa, ea, "W(A2)", 2)
