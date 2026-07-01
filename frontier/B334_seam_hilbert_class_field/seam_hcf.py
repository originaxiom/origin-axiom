"""B334 -- the seam's Hilbert class field IS the two-ended compositum (Chat handoff, verified).

Reconciles B333. B333: Q(sqrt-15)'s INTRINSIC invariants are generic (h=2 shared by many; units +-1)
-> no value in the field. B334: its RELATIONAL structure is exact and lovely --

  H(Q(sqrt-15)) = Q(sqrt5, sqrt-3).

The seam field Q(sqrt-15) has class number 2: its arithmetic is INCOMPLETE (not a UFD). Its Hilbert
class field -- the minimal extension where every ideal becomes principal -- is exactly the two-ended
compositum Q(sqrt5, sqrt-3). So the two ends (sqrt5 -> E8, sqrt-3 -> E6) are the arithmetic COMPLETION
of the seam; the object, touching both ends, IS the completion of its own seam. (This is genus theory:
disc -15 = -3*5 has 2 ramified primes, genus field degree 2^(2-1) = 2 = h, so genus field = HCF =
Q(sqrt of the prime discriminants) = Q(sqrt-3, sqrt5).)

VERIFIED (prime splitting): a split prime p of Q(sqrt-15) is PRINCIPAL <=> it splits completely in
Q(sqrt5,sqrt-3) <=> (5|p)=(-3|p)=+1 <=> p = 1,4 mod 15; NON-principal <=> both = -1 <=> p = 2,8 mod 15.
Cross-checked against the principal binary form x^2+xy+4y^2 (0 mismatches).

The class group Z/2 = the arithmetic partition: principal ('self-contained' in the seam) vs
non-principal ('needs both ends to factor'). [LEAP] structure vs value.

NULL (137, killed): 137 = 2 mod 15 -> non-principal -- but ~0.556 of split primes are non-principal
(that is what h=2 MEANS), a coin flip. No SM content from which class a single number lands in. DEAD.

Correction: 'unique because disc = 3*5' is TRUE but nearly tautological (the field is defined by its
primes); the genuine content is RELATIONAL (HCF = the two ends), consistent with B333's generic
intrinsic invariants. The value is still not in the field. Firewalled; nothing to CLAIMS.
"""
import sympy as sp
from sympy.functions.combinatorial.numbers import jacobi_symbol as leg


def prime_class(p):
    """among primes splitting in Q(sqrt-15): 'principal' iff (5|p)=(-3|p)=+1 (splits in the compositum)."""
    return "principal" if (leg(5, p) == 1 and leg(-3, p) == 1) else "non-principal"


def split_primes(hi=400):
    return [p for p in sp.primerange(7, hi) if p not in (3, 5) and leg(-15, p) == 1]


def splitting_law(hi=400):
    """return (principal residues mod 15, non-principal residues mod 15) -- expect {1,4} and {2,8}."""
    ps = split_primes(hi)
    prin = sorted({p % 15 for p in ps if prime_class(p) == "principal"})
    nonp = sorted({p % 15 for p in ps if prime_class(p) == "non-principal"})
    return prin, nonp


def form_cross_check(hi=400, B=60):
    """principal <=> represented by the principal form x^2+xy+4y^2 (disc -15). Return #mismatches."""
    def repr_by(a, b, c, p):
        return any(a*x*x + b*x*y + c*y*y == p for x in range(-B, B) for y in range(-B, B))
    return sum(1 for p in split_primes(hi) if repr_by(1, 1, 4, p) != (prime_class(p) == "principal"))


def null_137(hi=400):
    """137 is non-principal, but the non-principal fraction ~ 1/2 -> dead as a prediction."""
    ps = split_primes(hi)
    frac = sum(1 for p in ps if prime_class(p) == "non-principal") / len(ps)
    return prime_class(137), round(frac, 3)


if __name__ == "__main__":
    prin, nonp = splitting_law()
    print("splitting law: principal p mod 15 in", prin, " non-principal in", nonp, "(expect {1,4} / {2,8})")
    print("form cross-check mismatches:", form_cross_check(), "(0 = HCF = compositum confirmed)")
    cls137, frac = null_137()
    print(f"137 -> {cls137};  non-principal fraction = {frac} (~1/2, coin flip) -> 137 DEAD as prediction")
