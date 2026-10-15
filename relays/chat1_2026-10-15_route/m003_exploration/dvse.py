# down vs lepton twisted coupling vectors: proportional channel by channel (d = e) at N = 5, distinct at N = 7?
import mpmath as mp
exec(open("closure_law.py").read().split("random.seed")[0])
tau = mp.mpc(0.13, 1.07)
for N, (a, b) in ((5, (1, 3)), (7, (1, 4)), (7, (1, 6)), (9, (1, 3)), (8, (1, 3)), (10, (1, 3))):
    vec = {}
    for name, (qL, qR) in (("down", (1, 2)), ("lepton", (-3, 6)), ("up", (1, -4))):
        ub, de = ((qL+qR)*b/N, (qL+qR)*a/N), ((qL-qR)*b/N, (qL-qR)*a/N)
        vec[name] = quat(tau, ub, de)
    rat = [vec["lepton"][s] / vec["down"][s] for s in range(1, 4)]
    spread = max(abs(abs(r) - abs(rat[0])) for r in rat) / abs(rat[0])
    print(f"N={N} line ({a},{b}): |lepton_s/down_s| over i,j,k = {[mp.nstr(abs(r), 6) for r in rat]}  relative spread {mp.nstr(spread, 3)}")
print("phases of lepton_s/down_s (units of pi) at N = 5, 8, 10, two tau:")
for tau in (mp.mpc(0.13, 1.07), mp.mpc(-0.31, 0.95)):
    for N, (a, b) in ((5, (1, 3)), (5, (2, 1)), (8, (1, 3)), (10, (1, 3))):
        vec = {}
        for name, (qL, qR) in (("down", (1, 2)), ("lepton", (-3, 6))):
            ub, de = ((qL+qR)*b/N, (qL+qR)*a/N), ((qL-qR)*b/N, (qL-qR)*a/N)
            vec[name] = quat(tau, ub, de)
        print(f"  tau={mp.nstr(tau,3)} N={N} ({a},{b}):", [mp.nstr(mp.arg(vec['lepton'][s]/vec['down'][s])/mp.pi, 5) for s in range(1, 4)])
