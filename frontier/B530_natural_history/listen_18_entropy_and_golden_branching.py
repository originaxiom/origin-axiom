"""
Movement XVI — the exact entropy and the golden branching (Path D of the
exploration-seat handoff, verified independently).

The object's information content, read exactly:

  * topological entropy h = log(beta) = 1.3019 nats = 1.8782 bits / letter
    (primitive => uniquely ergodic => metric entropy = topological entropy).

  * GOLDEN BRANCHING (exact, from the digram frequencies of the fixed point):
        P(b|a) = P(B|A) = 1/phi   exactly
        tunnels are deterministic: P(A|b) = P(a|B) = 1
    and the ternary branch after A is golden all the way down:
        after A:  B gets 1/phi ;  the remaining 1/phi^2 splits a:A in the
        BREATH ratio 1/sqrt(phi) : 1  (movement XII's |gamma|).

  * the STRUCTURAL / TUNNEL entropy split: the deciders {a,A} carry all the
    information (H = 0.96, 1.34 bits), the couriers {b,B} carry ZERO
    (deterministic).  The decider/courier split of movement III is an
    information split, not just a frequency split.

FIREWALLED FRAMING (Path A, motivation only -- NOT a claim): the handoff reads
the object as "the conversation between keep (F) and hide (M)": keep=Fibonacci
makes a:b = phi:1, hide=Thue-Morse makes a:b = 1:1, and sqrt(phi)=sqrt(phi*1) is
their geometric mean; FM != MF (FM(a)=aba, MF(a)=abba, differ by 1 letter).
These are true facts about F and M, but sqrt(phi)'s actual mechanism in the
object is the F-vs-F^2 copy-inequality (movement VII), not verb-averaging -- so
the geometric-mean reading is an interpretive rhyme, kept as motivation, not
banked as a derivation.  (Verify-don't-trust also caught a handoff sign slip:
the lifted keep-verb eigenvalues are (phi,phi,-1/phi,-1/phi), NOT +1/phi.)

No physics.
"""
import numpy as np
from collections import Counter

PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}


def entropy_facts(n=3000000):
    beta = PHI * (1 + SQ)
    h_nats = np.log(beta)
    u = 'a'
    while len(u) < n:
        u = ''.join(SUB[c] for c in u)
    u = u[:n]
    dig = Counter(u[i:i + 2] for i in range(len(u) - 1))
    uni = Counter(u[:-1])
    P = lambda x, y: dig[x + y] / uni[x]
    cond = {x: {y: P(x, y) for y in 'abAB' if dig[x + y] > 0} for x in 'abAB'}
    H = {x: -sum(p * np.log2(p) for p in row.values()) for x, row in cond.items()}
    return beta, h_nats, cond, H, P


def checks():
    beta, h_nats, cond, H, P = entropy_facts()
    r = {}
    r['h_nats'] = round(h_nats, 4)
    r['golden_branch'] = (abs(P('a', 'b') - 1 / PHI) < 1e-3 and abs(P('A', 'B') - 1 / PHI) < 1e-3)
    r['tunnels_deterministic'] = (abs(P('b', 'A') - 1) < 1e-6 and abs(P('B', 'a') - 1) < 1e-6)
    # decider/courier entropy split
    r['deciders_carry_bits'] = (H['a'] > 0.9 and H['A'] > 1.3)
    r['couriers_zero'] = (H['b'] < 1e-6 and H['B'] < 1e-6)
    # nested golden branch after A
    r['after_A_breath_split'] = (abs(P('A', 'a') / P('A', 'A') - 1 / SQ) < 3e-3)
    # Path A verb facts (with the corrected -1/phi)
    F = np.kron(np.eye(2), np.array([[1, 1], [1, 0]]))
    Mv = np.kron(np.eye(2), np.array([[1, 1], [1, 1]]))
    r['keep_eig'] = sorted(np.round(np.linalg.eigvals(F).real, 3).tolist())      # phi,phi,-1/phi,-1/phi
    r['hide_eig'] = sorted(np.round(np.linalg.eigvals(Mv).real, 3).tolist())      # 2,2,0,0
    Fs = {'a': 'ab', 'b': 'a'}
    Ms = {'a': 'ab', 'b': 'ba'}
    fm = ''.join(Fs[c] for c in Ms['a'])
    mf = ''.join(Ms[c] for c in Fs['a'])
    r['FM_neq_MF_diff'] = abs(len(fm) - len(mf))
    return r


if __name__ == "__main__":
    beta, h_nats, cond, H, P = entropy_facts()
    print(f"topological entropy h = log(beta) = {h_nats:.4f} nats = {h_nats/np.log(2):.4f} bits/letter")
    print("\nconditional branching (exact golden):")
    for x in 'abAB':
        row = ", ".join(f"{y}:{p:.4f}" for y, p in cond[x].items())
        role = 'decider' if x in 'aA' else 'tunnel '
        print(f"  after {x} ({role}): {row}   H={H[x]:.4f} bits")
    print("\nchecks:", checks())
