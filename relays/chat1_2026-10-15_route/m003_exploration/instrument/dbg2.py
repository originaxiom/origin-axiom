exec(open("twisted_explore.py").read().split('if __name__ == "__main__":')[0])
w = "L" + "R"*25
rd = raw(w, 512, (0, 1), (1, 2), 5); rl = raw(w, 512, (0, 1), (-3, 6), 5)
for key in ("Y1", "Y2x", "Y3x"):
    A_, B_ = rd[key], rl[key]
    print(key, "finite:", np.isfinite(A_).all(), np.isfinite(B_).all(), " max|lep - down| / max|down|:", f"{np.max(np.abs(B_ - A_)) / np.max(np.abs(A_)):.2e}")
cd_, cl = cells(rd), cells(rl)
for n in cd_:
    if cd_[n] is None: continue
    print(n, "down", np.round(cd_[n]["s"] / cd_[n]["s"][0], 8), "lepton", np.round(cl[n]["s"] / cl[n]["s"][0], 8))
