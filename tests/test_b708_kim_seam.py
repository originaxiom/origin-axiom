"""B708 lock — Kim x the seam: the arithmetic-CS pairing reproduces our structure."""
def legendre(a, p):
    a %= p
    return 0 if a == 0 else (1 if pow(a, (p - 1) // 2, p) == 1 else -1)
def lk(p, q): return (1 - legendre(p, q)) // 2          # Morishita mod-2 linking
def pstar(p): return ((-1) ** ((p - 1) // 2)) * p

def test_two_hands_are_linked():
    # being(3) and hearing(5) are linked (linking 1 both ways) = mutual inertness
    assert lk(3, 5) == 1 and lk(5, 3) == 1
    # a control: 3 and 13 are NOT symmetrically forced; just confirm lk is well-defined 0/1
    for p, q in [(3, 5), (5, 7), (3, 7), (5, 13)]:
        assert lk(p, q) in (0, 1)

def test_audibility_is_infinite_prime_linking():
    # audible <=> p* > 0 <=> (-1/p) = +1 <=> unlinked with the archimedean prime -1
    for p in (3, 5, 7, 11, 13):
        audible = pstar(p) > 0
        unlinked_with_inf = (legendre(-1, p) == 1)   # (-1/p)=+1 iff p=1 mod4
        assert audible == unlinked_with_inf
        assert audible == (p % 4 == 1)

def test_meeting_is_the_F2_sum():
    # being*hearing = meeting: (-3)*(5) = -15 (the cup product / F_2-addition)
    def sqfree(n):
        m = abs(n); d = 2
        while d * d <= m:
            while m % (d * d) == 0: m //= d * d
            d += 1
        return m if n > 0 else -m
    assert sqfree(pstar(3) * pstar(5)) == -15
