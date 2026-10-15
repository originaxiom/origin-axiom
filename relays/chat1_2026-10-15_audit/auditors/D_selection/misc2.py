import json, math
P = "/home/claude/origin-axiom/relays/"
tf = json.load(open(P + "chat1_2026-10-14_selection/thread_frame.json"))
per = tf["readouts"]["per thread"]
print("12-thread m1/m2 range:", min(p["m1/m2"] for p in per.values()), max(p["m1/m2"] for p in per.values()))
print("data (m1/m3, m2/m3):", tf["readouts"]["data"])
hy = json.load(open(P + "chat1_2026-10-14_selection/post_hoc_hybrid.json"))
print("hybrid keys:", list(hy.keys())[:8])
th = json.load(open(P + "chat1_2026-10-14_the_scale/t_root_fixed_threads.json"))
for w in ["LLLRLRR", "LLLRRLR", "LLRRRLR", "LLRLRRR", "LLRLRR", "LLRRLR", "LR", "LLRR"]:
    print(w, "Vol %.6f CS %.6f" % tuple(th[w]))
