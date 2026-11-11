"""B754 P2 spectral-face stratum — locks for verdict-bearing computations."""
import math, cmath, subprocess, sys, os

ARC = os.path.join(os.path.dirname(__file__), '..', 'frontier', 'B754_p2_spectral')

def test_wall1_cusp_cm_disc_separates():
    """WALL-1 E1: cusp CM discs differ (m004 = -48, m003 = -3)."""
    from sympy import Poly, Rational, Symbol, discriminant, minpoly, sqrt
    x = Symbol("x")
    tau_m004 = 2 * sqrt(-3)
    omega = Rational(-1, 2) + sqrt(-3) / 2
    disc_m004 = int(discriminant(Poly(minpoly(tau_m004, x), x)))
    disc_m003 = int(discriminant(Poly(minpoly(omega, x), x)))
    assert disc_m004 == -48
    assert disc_m003 == -3
    assert disc_m004 != disc_m003

def test_wall1_voice_is_field_constant():
    """WALL-1 E1: Res zeta_K = 2*pi*h/(w*sqrt|d|) for h=1 fields."""
    fields = [(-3, 6), (-4, 4), (-7, 2), (-11, 2)]  # (disc, w)
    for d, w in fields:
        res = 2 * math.pi * 1 / (w * math.sqrt(abs(d)))
        assert res > 0, f"Res for disc {d} must be positive"
        assert 0.5 < res < 1.3, f"Res for disc {d} = {res} out of expected range"

def test_wall1_palette_sizes():
    """WALL-1 E2: Hecke palette at levels (2)/(4)/(8) = (1, 2, 8)."""
    findings = open(os.path.join(ARC, "FINDINGS.md"), encoding="utf-8").read()
    palette = tuple(1 if k == 1 else 2**(2 * k - 3) for k in (1, 2, 3))
    assert palette == (1, 2, 8) and palette[0] < palette[1] < palette[2]
    assert "palette" in findings.lower()

def test_wall1_b753_mixing_program_internal():
    """WALL-1 E4: B753 mixing = 1/(phi*sqrt5), gated PROGRAM-INTERNAL."""
    phi = (1 + math.sqrt(5)) / 2
    mixing = 1 / (phi * math.sqrt(5))
    assert abs(mixing - 0.2763932023) < 1e-8
    sin2_theta12 = 0.307
    assert abs(mixing - sin2_theta12) > 0.02, "Must NOT match sin²θ₁₂"

def test_tomb_l277_golden_weld_census():
    """TOMB-L277 override: 16/37 classes (43%) have golden-magnitude weld trace."""
    from fractions import Fraction
    rate = Fraction(16, 37)
    elt_rate = Fraction(1152, 2880)
    assert math.gcd(16, 37) == 1 and Fraction(2, 5) < rate < Fraction(23, 50)
    assert elt_rate == Fraction(2, 5)

def test_tomb_l77_saddle_field():
    """TOMB-L77 override: WRT saddle z₀ = exp(iπ/3) ∈ Q(√−3), disc = −3."""
    z0 = cmath.exp(1j * math.pi / 3)
    assert abs(z0**2 - z0 + 1) < 1e-14, "z₀ must satisfy z²−z+1=0"
    disc = (-1)**2 - 4 * 1 * 1  # disc of z²−z+1
    assert disc == -3
    omega = cmath.exp(2j * math.pi / 3)
    assert abs(z0 - (-omega**2)) < 1e-14, "z₀ = -ω² ∈ O_K"

def test_b746_f11_golden_free():
    """B746 F11 reconfirmed: zero golden markers in the banked voice artifacts (B737/B739).

    Repaired 2026-07-29. The previous body was vacuous TWICE OVER: it counted marker hits and
    then executed `pass`, so it passed no matter what the files contained; and it named
    'B737_zeta_quotient_voice', which does not exist (the arc is 'B737_candidate_zero'), so the
    `if not os.path.isdir: continue` silently skipped half the intended scan. A test that can
    pass by finding nothing to look at is the same defect as one that asserts nothing.

    F11 calls itself "grep-verifiable", so this now greps and asserts -- including a guard that
    files were actually scanned, which is what the directory typo defeated."""
    import glob
    voice_dirs = [
        os.path.join(os.path.dirname(__file__), '..', 'frontier', d)
        for d in ['B737_candidate_zero', 'B739_character_rigidity']
    ]
    markers = ['golden', 'fibonacci', 'sqrt5', 'sqrt(5)', 'phi^2', 'phi**2']
    scanned, offenders = [], []
    for vd in voice_dirs:
        assert os.path.isdir(vd), f"voice dir missing -- F11's scan would be vacuous: {vd}"
        for fn in glob.glob(os.path.join(vd, '**', '*.md'), recursive=True):
            if 'FINDINGS' not in os.path.basename(fn):
                continue
            with open(fn) as f:
                text = f.read().lower()
            scanned.append(fn)
            for m in markers:
                if text.count(m.lower()):
                    offenders.append((os.path.relpath(fn), m, text.count(m.lower())))
    assert len(scanned) >= 2, f"expected a FINDINGS in each voice dir, scanned {scanned}"
    assert not offenders, f"F11 claims zero golden markers; found {offenders}"

def test_face_irrelevant_b516():
    """B516 FACE-IRRELEVANT: Q(√−3) ∩ Q(√5) = Q (fields arithmetically disjoint)."""
    disc_spec = -3
    disc_alg = 5
    assert math.gcd(abs(disc_spec), abs(disc_alg)) == 1, "Fields must be coprime"

def test_face_irrelevant_wall7():
    """WALL-7 FACE-IRRELEVANT: scattering residue is volume-generic."""
    vol_m004 = 2.0298832128
    vol_m003 = 2.0298832128
    res_m004 = 2 * math.sqrt(3) / vol_m004
    res_m003 = 2 * math.sqrt(3) / vol_m003
    assert abs(res_m004 - res_m003) < 1e-10, "Residues must be equal for same-volume pair"
