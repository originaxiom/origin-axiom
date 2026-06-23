"""B193 -- SL(3) sealing / field-content scouts (V188). Fast locks.

L8: chirality (cyclic-palindrome block seq, B128/B134) and the SU(2)_k eigenvalue field (B132) are INDEPENDENT --
all four (chirality, field) combinations occur; field = quantum mod-4 spin-content, not chirality. L10: the SU(2)_k
field reaches the compositum Q(zeta12)=Q(sqrt-3,i) (quantum), while the classical seed trace-fields Q(sqrt-3),Q(i)
are disjoint (intersection Q, exact). Full version in sealing_scouts.py.
"""
import numpy as np
import sympy as sp


def _S(k):
    n = k + 1
    return np.array([[np.sqrt(2/(k+2))*np.sin(np.pi*(a+1)*(b+1)/(k+2)) for b in range(n)] for a in range(n)], dtype=complex)
def _T(k): return np.diag([np.exp(2j*np.pi*(a*(a+2)/(4*(k+2)))) for a in range(k+1)])
def _rho_word(word, k):
    S = _S(k); T = _T(k); R = T; L = S @ T @ np.linalg.inv(S)
    rep = np.eye(k+1, dtype=complex)
    for ch in word: rep = rep @ (R if ch == "R" else L)
    return rep
def _seq_word(seq): return "".join("R"*m + "L"*m for m in seq)
def _order(lam, maxn=240):
    for n in range(1, maxn+1):
        if abs(lam**n - 1) < 1e-7: return n
    return None
def _field(seq, k=4):
    s = {_order(e) for e in np.linalg.eigvals(_rho_word(_seq_word(list(seq)), k))} - {None}
    has6 = any(o in (3, 6) for o in s); has4 = any(o == 4 for o in s)
    return "Q(zeta12)" if has6 and has4 else "Q(i)" if has4 else "Q(sqrt-3)" if has6 else "Q (rational)"
def _chir(seq):
    seq = tuple(seq); rev = tuple(reversed(seq))
    return "amphi" if rev in {seq[i:] + seq[:i] for i in range(len(seq))} else "chiral"


def test_chirality_and_field_independent():
    seqs = [(1,), (2,), (1, 2, 1), (1, 2, 3), (1, 2, 3, 4)]
    tab = {s: (_chir(s), _field(s)) for s in seqs}
    amphi_fields = {f for (c, f) in tab.values() if c == "amphi"}
    qs3_chir = {c for (c, f) in tab.values() if f == "Q(sqrt-3)"}
    assert len(amphi_fields) >= 2            # fixed chirality (amphi), field varies
    assert qs3_chir == {"amphi", "chiral"}   # fixed field Q(sqrt-3), chirality varies


def test_quantum_fusion_vs_classical_disjoint():
    assert _field((2,)) == "Q(zeta12)"       # SU(2)_4 reaches the compositum (quantum fusion)
    x = sp.Symbol('x')
    assert sp.degree(sp.minimal_polynomial(sp.sqrt(-3), x)) == 2   # classical golden field, degree 2
    assert sp.degree(sp.minimal_polynomial(sp.I, x)) == 2          # classical silver field, degree 2
    assert sp.degree(sp.minimal_polynomial(sp.exp(2*sp.pi*sp.I/12), x)) == 4  # compositum degree 4 => intersection Q
