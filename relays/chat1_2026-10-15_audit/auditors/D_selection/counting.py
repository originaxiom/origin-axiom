import json, math
P = "<repo>/relays/chat1_2026-10-14_the_scale/"
th = json.load(open(P + "t_root_fixed_threads.json"))
Ln = {int(a): b for a, b in json.load(open(P + "t_root_fixed.json"))["L_of_n"].items()}
canon = lambda s: min(s[i:] + s[:i] for i in range(len(s)))
rev = lambda s: canon(s[::-1]); mir = lambda s: canon(s.translate(str.maketrans("LR", "RL")))
def wt(word, s):
    n = len(word); return {"A": 2.0 ** -n, "B": 3.0 ** -n, "C": 1.0 / (n * (n - 1) * Ln[n])}[s]
for c in (6.0,):
    for s in "ABC":
        res = {}
        for mode in ("words", "oriented (W~revW)", "unoriented (Klein orbit)"):
            seen, Z, root = set(), 0.0, 0.0
            for w, (v, cs) in th.items():
                if mode == "words": key = w
                elif mode.startswith("oriented"): key = min(w, rev(w))
                else: key = min(w, rev(w), mir(w), mir(rev(w)))
                if key in seen: continue
                seen.add(key)
                x = wt(w, s) * math.exp(-c * v / (6 * math.pi)); Z += x
                if key == "LR": root = x
            res[mode] = round(root / Z, 3)
        print(f"c={c} weight {s}: root share", res)
