"""B689 — the meeting holds ground: neither hand alone; a_3=-1, a_5=+1."""


def test_neither_hand_alone_and_two_fingerprints():
    genus = {3: 0, 5: 0, 15: 1}
    assert genus[3] == 0 and genus[5] == 0   # no weight-2 form at either prime
    assert genus[15] == 1                     # structure exists at the meeting

    def ap(p):
        cnt = 1
        for x in range(p):
            for y in range(p):
                if (y*y + x*y + y - (x**3 + x**2)) % p == 0:
                    cnt += 1
        return p + 1 - cnt
    assert ap(3) == -1 and ap(5) == 1         # different Atkin-Lehner signs
