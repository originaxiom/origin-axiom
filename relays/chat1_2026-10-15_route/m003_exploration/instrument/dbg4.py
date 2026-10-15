exec(open("twisted_explore.py").read().split('if __name__ == "__main__":')[0])
w = "L" + "R"*25
rd = raw(w, 512, (0, 1), (1, 2), 5); rl = raw(w, 512, (0, 1), (-3, 6), 5)
du = np.max(np.abs(rl["_u"] - rd["_u"]) / np.maximum(np.abs(rd["_u"]), 1e-300))
dv = np.max(np.abs(rl["_v"] - rd["_v"]) / np.maximum(np.abs(rd["_v"]), 1e-300))
print("max relative |u_l - u_d|:", du, " |v_l - v_d|:", dv)
i = np.unravel_index(np.argmax(np.abs(rl["_v"] - rd["_v"])), rd["_v"].shape); print("worst at", i, rd["_v"][i], rl["_v"][i])
