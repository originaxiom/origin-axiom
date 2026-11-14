"""Do the frame's level-5 charges sort the fields into exterior degrees of C^5 (main, 2026-11-14 night)? Expectation
written before the run: k = 2 * (6Y) mod 5 gives Q, u, e -> 2 (the 10), d, L -> 4 (the 5bar), the right-handed neutrino
-> 0, the Higgs -> 1 (the 5); conjugates go to 5 - k. Any miss refutes it. Also: the Hodge pairing k <-> 5 - k flips the
degree's parity because 5 is odd."""
Y6 = {"Q": 1, "u (u^c)": -4, "d (d^c)": 2, "L": -3, "e (e^c)": 6, "nu^c": 0, "H": 3}
expect = {"Q": 2, "u (u^c)": 2, "d (d^c)": 4, "L": 4, "e (e^c)": 2, "nu^c": 0, "H": 1}
ok = True
for f, y in Y6.items():
    k = (2 * y) % 5; kc = (2 * (-y)) % 5
    ok &= (k == expect[f]) and (kc == (5 - expect[f]) % 5)
    print("%-9s 6Y = %+d  ->  degree k = %d (%s), its conjugate -> %d" % (f, y, k, "even" if k % 2 == 0 else "odd", kc))
print("expectation met for every field and its conjugate:", ok)
print("Hodge pairing k <-> 5 - k flips parity for every k:", all((k % 2) != ((5 - k) % 2) for k in range(6)))
print("dimensions: even half", sum(__import__('math').comb(5, k) for k in (0, 2, 4)), "odd half", sum(__import__('math').comb(5, k) for k in (1, 3, 5)))
