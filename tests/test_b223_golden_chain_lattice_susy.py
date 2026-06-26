"""B223 / Act II -- where the SUSY lives: emergent on the golden chain, lattice-exact on the FS sibling.
Nothing to CLAIMS.md.

Load-bearing locks:
  (A) the golden chain has NO conserved tau-parity (||[H,(-1)^F]|| bounded away from 0) -> its SUSY is
      emergent/IR-only, no exact lattice grading. (TESTED-NEGATIVE)
  (B) the Fendley-Schoutens N=2 model on the SAME Lucas Hilbert space has EXACT lattice SUSY:
      Q^2=0, H_FS={Q,Q†}, [H_FS,(-1)^F]=0 (all machine precision), E_gs=0 (unbroken), integer Witten index.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "frontier", "B223_golden_chain_lattice_susy"))
from lattice_susy import golden_parity_conserved, fs_data, fs_basis, golden_basis  # noqa: E402


def test_same_lucas_hilbert_space():
    # both the golden chain and the FS sibling have Lucas dimension L_N (different constraint, same count)
    lucas = {6: 18, 9: 76, 12: 322}
    for N, L in lucas.items():
        assert len(golden_basis(N)) == L
        assert len(fs_basis(N)) == L


def test_golden_chain_no_lattice_grading():
    # tau-parity is NOT conserved -> the golden chain's SUSY is emergent-only (no exact lattice supercharge)
    for N in (8, 10, 12):
        assert golden_parity_conserved(N) > 0.5


def test_fendley_schoutens_exact_lattice_susy():
    for L in (6, 9, 12):
        d = fs_data(L)
        assert d["Q2"] < 1e-10                 # Q nilpotent: Q^2 = 0
        assert d["HF_comm"] < 1e-10            # [H_FS, (-1)^F] = 0 (graded)
        assert abs(d["Egs"]) < 1e-9            # E_gs = 0 -> unbroken SUSY
        assert abs(d["witten"] - round(d["witten"])) < 1e-9 and abs(d["witten"]) >= 1  # integer, nonzero


if __name__ == "__main__":
    for name, fn in sorted(globals().items()):
        if name.startswith("test_"):
            fn(); print(f"{name}  PASS")
    print("ALL CHECKS PASS")
