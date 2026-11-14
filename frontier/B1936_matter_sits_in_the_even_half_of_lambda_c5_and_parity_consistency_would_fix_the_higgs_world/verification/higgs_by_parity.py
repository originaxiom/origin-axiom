"""If the frame's holomorphic objects are exactly one degree-parity class of Lambda*(C^5) (matter's kernels are
holomorphic; conjugation flips both holomorphy and degree parity), which Higgs reading follows, under both signs of the
hypercharge convention? Each sector's coupling needs its degrees to sum to 0 mod 5, which fixes the Higgs degree the
sector needs; the holomorphic Higgs S is the one in matter's parity class."""
Y6 = {"Q": 1, "u": -4, "d": 2, "L": -3, "e": 6}
SECT = {"up": ("Q", "u"), "down": ("Q", "d"), "lep": ("L", "e")}
for sign in (+1, -1):
    k = {f: (2 * sign * y) % 5 for f, y in Y6.items()}
    par = {k[f] % 2 for f in k}
    assert len(par) == 1, "matter is not in one parity class"
    mp = par.pop()
    world = {}
    for s, (a, b) in SECT.items():
        kh = (-(k[a] + k[b])) % 5                     # the Higgs degree the sector needs
        world[s] = "S" if kh % 2 == mp else "S~"
    print("hypercharge sign %+d: matter's degrees %s (all %s); the sector Higgs degrees -> readings %s" % (
        sign, sorted(set(k.values())), "even" if mp == 0 else "odd", world))
