"""B342 -- abstract discrete-symmetry facts: the Z/3 IS the trimaximal symmetry (+ the honest data comparison).

FIREWALL: this probe banks ONLY standard, abstract group theory + an HONEST observation about data. It
is NOT a derivation, NOT a continuous-value fit, and makes NO claim that the object's geometric Z/3 is
the physical lepton flavor symmetry -- that identification is [LEAP], firewalled to speculations/S048.
Nothing to CLAIMS.

The verified group theory (standard, Harrison-Perkins-Scott / textbook):
  1. The Z/3 cyclic mixing -> the DFT (Fourier) matrix F[j,k] = omega^{jk}/sqrt3 is DEMOCRATIC:
     |F[j,k]|^2 = 1/3 for all j,k.
  2. (1,1,1)/sqrt3 is the Z/3-INVARIANT eigenvector (trivial rep) and equals TBM's MIDDLE column.
  3. TM2 (trimaximal-2, preserving the middle column) forces |U_e2|^2 = 1/3, i.e. the correlation
     sin^2 theta_12 = 1/(3 cos^2 theta_13)  ->  theta_12 = 35.7 deg (at theta_13 = 8.57 deg).

The HONEST data comparison (the check that must accompany any such statement):
  observed theta_12 = 33.4 deg.  TM2 -> 35.7 deg (off 2.3).  TM1 (preserve the FIRST column) -> 34.3
  deg (off 0.9).  => CURRENT DATA FAVOURS TM1 over TM2. So the object's would-be pattern (TM2, via its
  Z/3 preserving the middle/magic column) is FALSIFIABLE and currently DISFAVOURED.

VERDICT: the object's Z/3 *is* the trimaximal symmetry (a math fact); IF one identified it with lepton
flavor (a [LEAP], firewalled), it would select TM2 -- which current data disfavours vs TM1. Symmetry
yes, continuous value no. Firewalled; nothing to CLAIMS.
"""
import numpy as np

THETA13_DEG = 8.57       # PDG global-fit central value (used only for the correlation, not a derivation)
THETA12_OBS = 33.4       # observed


def z3_dft_is_democratic():
    w = np.exp(2j * np.pi / 3)
    F = np.array([[w**(j * k) for k in range(3)] for j in range(3)]) / np.sqrt(3)
    return np.allclose(np.abs(F)**2, 1 / 3)


def magic_column_is_z3_invariant():
    """(1,1,1)/sqrt3 is fixed by the cyclic Z/3 = TBM's middle column."""
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]]); v = np.ones(3) / np.sqrt(3)
    U_TBM_mid = np.array([1, 1, 1]) / np.sqrt(3)
    return np.allclose(P @ v, v) and np.allclose(np.abs(U_TBM_mid), v)


def theta12_from(scheme):
    """TM2: sin^2 th12 = 1/(3 cos^2 th13). TM1: cos^2 th12 cos^2 th13 = 2/3."""
    c13sq = np.cos(np.radians(THETA13_DEG))**2
    if scheme == 'TM2':
        s12sq = 1 / (3 * c13sq)
    elif scheme == 'TM1':
        s12sq = 1 - 2 / (3 * c13sq)
    return np.degrees(np.arcsin(np.sqrt(s12sq)))


def data_favours_tm1():
    """the honest comparison: |TM1 - obs| < |TM2 - obs| (current data favours TM1)."""
    d_tm2 = abs(theta12_from('TM2') - THETA12_OBS)
    d_tm1 = abs(theta12_from('TM1') - THETA12_OBS)
    return d_tm1 < d_tm2, round(theta12_from('TM1'), 2), round(theta12_from('TM2'), 2)


if __name__ == "__main__":
    print("1. Z/3 -> DFT democratic (|entry|^2=1/3):", z3_dft_is_democratic())
    print("2. (1,1,1)/sqrt3 = Z/3-invariant = TBM middle column:", magic_column_is_z3_invariant())
    print(f"3. TM2 correlation: theta_12 = {theta12_from('TM2'):.2f} deg (vs obs {THETA12_OBS})")
    fav, tm1, tm2 = data_favours_tm1()
    print(f"   HONEST: TM1 -> {tm1} deg, TM2 -> {tm2} deg, obs {THETA12_OBS} -> data favours TM1: {fav}")
    print("=> the object's Z/3 IS the trimaximal symmetry (math); the lepton-flavor identification is")
    print("   [LEAP] (firewalled, S048), and its TM2 selection is currently DISFAVOURED vs TM1.")
