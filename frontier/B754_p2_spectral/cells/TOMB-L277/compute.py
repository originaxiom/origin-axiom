"""B754 P2 cell — TOMB-L277 (TOMBSTONES K-O: the golden "trace leak" tr rho_{SU(2)_3}(A) = -1/phi
as a distinguished signal — KILLED base-rate, B742-reconfirmed: 1350/2880 nonzero, 384/2880
golden-magnitude, seed class size 96, one of 4 golden classes).

P2 QUESTION: does the spectral face AS BANKED (ONLY B737, B739, B746, B753) bear on this killed
claim in a way the original kill never tested?

THE ORIGINAL KILL'S BLIND SPOT (the B' exposure note): the kill counted TRACE MAGNITUDES inside
the single rep rho_{SU(2)_3}; it never consulted any spectral quantity — it cannot exclude a
spectral fact singling out the seed's 96-elt class among the 4 golden classes.

TWO OPERATORS ARE DEFINED (Gate 5-Q Q2: discrimination is shown for each BEFORE any
verdict-bearing use):

  O(c), the face-ECHO operator on conjugacy classes c of the banked 2880 image:
    O(c) = (exact trace, eigenphase multiset (degrees, exact rationals), face-echo set), where
    the face-echo set is the subset of the frozen surface's COMPUTED golden spectral data
    matched by c:
      'B753-block-trace(+1/phi)' if tr(c) = +1/phi     [B753 output.txt L15]
      'B753-phase-pair(+-72deg)' if {+-72deg} subset of c's eigenphases  [B753 output.txt L11]
      'B746-F3-chord(v)' for v in {-phi, +1/phi, +phi^3, -phi^-3}       [B746 FINDINGS F3 + S3]
    The voice arcs (B737/B739) contribute NOTHING to the echo set — that emptiness is itself
    banked (B746 F11; B739's character-rigidity theorem) and is re-verified by value-token grep.

  B(w), the face's own object as a word map (B753's banked construction, one-hop through the
  arc's cited B238 pipeline): B(w) = U^dag C rho_{SU(3)_2}(w) U, the 2x2 theta-odd block of the
  twisted weld at the word w in {R,L}. B753 computed it at exactly ONE word (g = RL).

  Q2 comparators (the sister/census-manifold slot instantiated for an MTC-overlay claim): for O,
  generic classes of the same image — the class of rho(RRL) (the tombstone's own trace-0
  comparator hyperbolic) and the class of rho(t); for B, the tombstone's comparator words
  RRL, RLL themselves.

Q6 SPECIALNESS BUDGET: any "the face specially touches THIS claim" is charged its comparator
question in-cell — PART 6 evaluates B(w) at the tombstone's comparator words.

CONVENTIONS: SU(2)_3 side exactly as the banked kill (B742 recompute C1-C7, from B210's
dual_mckay.py conventions): S_ab = sqrt(2/5) sin(pi(a+1)(b+1)/5), T = diag e^{2pi i(h_a - c/24)},
h_a = a(a+2)/20, c = 9/5; R = t, L = s t^-1 s^-1, rho(RL) = T S T^-1 S^-1 (S^-1 = S);
BFS dedup key = entries rounded to 5 decimals. Weld side exactly as B753's compute.py:
su3_data(2) from the banked B238 pipeline (one-hop inside B753's citation), C = charge
conjugation, R = T, L = S^-1 T^-1 S, theta-odd basis u_j = (e_{(1,0)}-e_{(0,1)})/sqrt2,
(e_{(2,0)}-e_{(0,2)})/sqrt2.

Deterministic: no wall-clock, no randomness, no network. RUN-WITH plain python3 (numpy+sympy).
Gate 5: pure representation theory + file grep; no SM values anywhere. Q5: no experience
vocabulary. E23/E25: not triggered (no congruence-level statement, no integer-relation fit).
"""
import math
import os
import re
from fractions import Fraction

import numpy as np
import sympy as sp

CELL = os.path.dirname(os.path.abspath(__file__))
FRONTIER = os.path.normpath(os.path.join(CELL, "..", "..", ".."))
PHI = (1 + math.sqrt(5)) / 2
TOL = 1e-6
checks = []


def CHECK(ok, msg):
    checks.append(bool(ok))
    print(f"CHECK: [{'PASS' if ok else 'FAIL'}] {msg}")


# ============================================================================ PART 0
print("=" * 100)
print("PART 0 — the killed claim's object, exact (sympy; B742/B210 conventions)")
print("=" * 100)
n5 = 5
Ssym = sp.Matrix(4, 4, lambda i, j: sp.sqrt(sp.Rational(2, n5)) * sp.sin(sp.pi * (i + 1) * (j + 1) / n5))
hsym = [sp.Rational(a * (a + 2), 4 * n5) for a in range(4)]
Tsym = sp.diag(*[sp.exp(2 * sp.pi * sp.I * (hsym[a] - sp.Rational(9, 5) / 24)) for a in range(4)])
Tsym_inv = sp.diag(*[1 / Tsym[a, a] for a in range(4)])
assert sp.simplify(Ssym * Ssym - sp.eye(4)) == sp.zeros(4, 4)
tr_seed_exact = sp.simplify(sp.expand_complex(sp.expand(sp.trace(Tsym * Ssym * Tsym_inv * Ssym))))
CHECK(sp.simplify(tr_seed_exact - (1 - sp.sqrt(5)) / 2) == 0,
      f"tr rho_SU(2)_3(RL) = {tr_seed_exact} = -1/phi EXACT (sympy) — the killed claim's number, "
      "matches banked kill")

# ============================================================================ PART 1
print()
print("=" * 100)
print("PART 1 — the kill's ground re-established: the 2880 image, census, classes (B742 C1-C7)")
print("=" * 100)
a4 = np.arange(4)
S = np.sqrt(2 / n5) * np.sin(np.pi * np.outer(a4 + 1, a4 + 1) / n5).astype(complex)
T = np.diag(np.exp(2j * np.pi * (a4 * (a4 + 2) / 20 - (9 / 5) / 24)))
I4 = np.eye(4)
Tinv, Sinv = np.conj(T), S


def key(M):
    return tuple(np.round(M.flatten(), 5))


seen = {key(I4): 0}
elems = [I4]
frontier = [I4]
while frontier:
    nf = []
    for M in frontier:
        for g in (S, T):
            P = M @ g
            kk = key(P)
            if kk not in seen:
                seen[kk] = len(elems)
                elems.append(P)
                nf.append(P)
    frontier = nf
order = len(elems)
traces = np.array([np.trace(M) for M in elems])
abst = np.abs(traces)
n_nonzero = int(np.sum(abst > TOL))
n_golden = int(np.sum((np.abs(abst - PHI) < TOL) | (np.abs(abst - 1 / PHI) < TOL)))
CHECK(order == 2880 and n_nonzero == 1350 and n_golden == 384,
      f"image order {order} (banked 2880), nonzero-trace {n_nonzero} (banked 1350), "
      f"golden-magnitude {n_golden} (banked 384)")

class_of, classes = {}, []
for i in range(order):
    if i in class_of:
        continue
    cid = len(classes)
    orbit, class_of[i], fr = [i], cid, [i]
    while fr:
        nf = []
        for j in fr:
            M = elems[j]
            for g, gi in ((S, S.conj().T), (T, T.conj().T)):
                cx = seen[key(g @ M @ gi)]
                if cx not in class_of:
                    class_of[cx] = cid
                    orbit.append(cx)
                    nf.append(cx)
        fr = nf
    classes.append(orbit)
assert sum(len(o) for o in classes) == order
for o in classes:
    assert np.max(np.abs(traces[o] - traces[o[0]])) < 1e-9
golden_cids = [c for c, o in enumerate(classes)
               if abs(abs(traces[o[0]]) - PHI) < TOL or abs(abs(traces[o[0]]) - 1 / PHI) < TOL]
seed = T @ S @ Tinv @ Sinv
seed_cid = class_of[seen[key(seed)]]
CHECK(len(classes) == 37 and len(golden_cids) == 4 and seed_cid in golden_cids
      and len(classes[seed_cid]) == 96,
      f"{len(classes)} classes (banked 37); {len(golden_cids)} golden classes (banked 4); "
      f"seed class size {len(classes[seed_cid])} (banked 96)")
gtr = {c: complex(traces[classes[c][0]]) for c in golden_cids}
for c in golden_cids:
    assert abs(gtr[c].imag) < 1e-9, "golden class trace not real"
CHECK(sorted(round(gtr[c].real, 6) for c in golden_cids)
      == [round(v, 6) for v in (-PHI, -1 / PHI, 1 / PHI, PHI)],
      "the 4 golden classes carry the 4 REAL signed traces {-phi, -1/phi, +1/phi, +phi} "
      f"(sizes {[len(classes[c]) for c in golden_cids]})")


# ============================================================================ PART 2
print()
print("=" * 100)
print("PART 2 — NEW, never in the kill: the eigenphase census of the golden classes")
print("        (the kill counted |trace| only; the face speaks in eigenphases — B753's ±72deg)")
print("=" * 100)


def phase_multiset(M):
    """Exact eigenphases in degrees (finite-order unitary => rational turns)."""
    ev = np.linalg.eigvals(M)
    out = []
    for lam in ev:
        assert abs(abs(lam) - 1) < 1e-9
        fr = Fraction(float(np.angle(lam) / (2 * np.pi))).limit_denominator(240)
        assert abs(complex(np.exp(2j * np.pi * float(fr))) - lam) < 1e-8
        deg = 360 * fr
        if deg <= -180:
            deg += 360
        if deg > 180:
            deg -= 360
        out.append(deg)
    return tuple(sorted(out))


def fmt(ph):
    return "{" + ", ".join(f"{float(d):+.0f}" for d in ph) + "}deg"


golden_named = {}
for c in golden_cids:
    v = gtr[c].real
    name = {round(-PHI, 6): "-phi", round(-1 / PHI, 6): "-1/phi",
            round(1 / PHI, 6): "+1/phi", round(PHI, 6): "+phi"}[round(v, 6)]
    golden_named[name] = c
phases = {name: phase_multiset(elems[classes[c][0]]) for name, c in golden_named.items()}
for name in ("-phi", "-1/phi", "+1/phi", "+phi"):
    tag = "  <-- the SEED's class" if golden_named[name] == seed_cid else ""
    print(f"  class tr = {name:>7}  size {len(classes[golden_named[name]]):>3}  "
          f"eigenphases {fmt(phases[name])}{tag}")
seed_ph = phases["-1/phi"]
CHECK(golden_named["-1/phi"] == seed_cid,
      "the seed's class is the unique tr = -1/phi class (banked: 1 class shares the seed's value)")

pair72 = (Fraction(-72), Fraction(72))
all_ph = {c: phase_multiset(elems[classes[c][0]]) for c in range(len(classes))}
pair72_cids = [c for c in range(len(classes)) if all(p in all_ph[c] for p in pair72)]
print(f"  classes (of all 37) whose eigenphases contain the face's pair {{+-72deg}}: "
      f"{[(c, round(complex(traces[classes[c][0]]).real, 6), len(classes[c])) for c in pair72_cids]}"
      "  [(id, trace, size)]")
CHECK(seed_cid not in pair72_cids and not any(c in golden_cids for c in pair72_cids),
      f"the face's phase pair {{+-72deg}} is carried by NO golden class and NOT by the seed's "
      f"class (it lands only on the classes above); the seed's class phases are {fmt(seed_ph)}")

# ============================================================================ PART 3
print()
print("=" * 100)
print("PART 3 — the face object rebuilt from B753's OWN banked pipeline (one-hop inside the arc)")
print("=" * 100)
import importlib.util

spec = importlib.util.spec_from_file_location(
    "b238", os.path.join(FRONTIER, "B238_su32_levelrank", "su32_wrt.py"))
b238 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b238)
w6, S6, T6, _ = b238.su3_data(2)
n6 = len(w6)
C6 = np.zeros((n6, n6))
for i, wt in enumerate(w6):
    C6[w6.index((wt[1], wt[0])), i] = 1.0
S6i, T6i = np.linalg.inv(S6), np.linalg.inv(T6)
R6, L6 = T6, S6i @ T6i @ S6
U = np.zeros((n6, 2))
for j, (aa, bb) in enumerate([(w6.index((1, 0)), w6.index((0, 1))),
                              (w6.index((2, 0)), w6.index((0, 2)))]):
    U[aa, j], U[bb, j] = 1 / np.sqrt(2), -1 / np.sqrt(2)
U = U.astype(complex)


def rho6(word):
    W = np.eye(n6, dtype=complex)
    for ch in word:
        W = W @ (R6 if ch == "R" else L6)
    return W


def theta_odd_block(M6):
    return np.array([[np.conj(U[:, i]) @ (C6 @ M6) @ U[:, j] for j in range(2)] for i in range(2)])


B_RL = theta_odd_block(rho6("RL"))
tr_B = B_RL[0, 0] + B_RL[1, 1]
unit_dev = np.linalg.norm(B_RL @ B_RL.conj().T - np.eye(2))
ph_B = phase_multiset(B_RL) if unit_dev < 1e-9 else None
CHECK(unit_dev < 1e-9 and abs(tr_B - 1 / PHI) < 1e-9 and ph_B == pair72,
      f"B753's theta-odd weld block at the SEED element g=RL: unitary (dev {unit_dev:.1e}), "
      f"trace {tr_B.real:+.6f}{tr_B.imag:+.1e}j = +1/phi, eigenphases {fmt(ph_B)} — matches "
      "B753/output.txt L11 (e^{+-i 72deg}) and L15 (trace +0.618034)")
CHECK(abs(tr_B - (-1 / PHI)) > 1, "the face's block trace is +1/phi, NOT the seed's -1/phi "
      "(B753 cell 2 computed chat-1's -1/phi/108deg hypothesis False — verified at "
      "B753/output.txt L14-L15)")

# ============================================================================ PART 4
print()
print("=" * 100)
print("PART 4 — Gate 5-Q Q2 (MANDATORY BEFORE USE): both operators discriminate")
print("=" * 100)
CHORD = {"B746-F3-chord(-phi)": -PHI, "B746-F3-chord(+1/phi)": 1 / PHI,
         "B746-F3-chord(+phi^3)": PHI ** 3, "B746-F3-chord(-phi^-3)": -PHI ** -3}


def O(cid):
    tr = complex(traces[classes[cid][0]])
    ph = all_ph[cid]
    echo = set()
    if abs(tr - 1 / PHI) < TOL:
        echo.add("B753-block-trace(+1/phi)")
    if all(p in ph for p in pair72):
        echo.add("B753-phase-pair(+-72deg)")
    for name, v in CHORD.items():
        if abs(tr - v) < TOL:
            echo.add(name)
    return tr, ph, echo


L4 = S @ Tinv @ Sinv
cid_RRL = class_of[seen[key(T @ T @ L4)]]
cid_t = class_of[seen[key(T)]]
probe = [("SEED class (tr=-1/phi)", seed_cid), ("+1/phi class", golden_named["+1/phi"]),
         ("+phi class", golden_named["+phi"]), ("-phi class", golden_named["-phi"]),
         ("GENERIC: rho(RRL) class", cid_RRL), ("GENERIC: rho(t) class", cid_t)]
Ovals = {}
for label, cid in probe:
    tr, ph, echo = O(cid)
    Ovals[label] = (round(tr.real, 6), round(tr.imag, 6), ph, frozenset(echo))
    print(f"  O[{label:<24}] = tr {tr.real:+.6f}{tr.imag:+.6f}j, phases {fmt(ph)}, "
          f"echo {sorted(echo) if echo else '{}'}")
o_seed = Ovals["SEED class (tr=-1/phi)"]
CHECK(o_seed != Ovals["GENERIC: rho(RRL) class"] and o_seed != Ovals["GENERIC: rho(t) class"]
      and Ovals["GENERIC: rho(RRL) class"] != Ovals["GENERIC: rho(t) class"],
      "Q2a[O]: O separates the object from both generic comparators (all three outputs "
      "distinct) — the operator is not the constant map")
echo_sets = {lab: v[3] for lab, v in Ovals.items()}
CHECK(len(set(echo_sets.values())) > 1 and echo_sets["+1/phi class"] and echo_sets["-phi class"],
      "Q2b[O]: the face-ECHO component alone is non-constant across inputs (non-empty on the "
      "+1/phi and -phi classes) — an empty echo is an informative negative, not operator "
      "deadness (the B752 lesson)")

# ============================================================================ PART 5
print()
print("=" * 100)
print("PART 5 — the consultation: where the frozen surface's golden data lands in the image")
print("=" * 100)
CHECK(echo_sets["SEED class (tr=-1/phi)"] == frozenset(),
      "the SEED's class echoes NOTHING in the frozen surface: no banked golden spectral value "
      "and no banked phase pair matches the seed's class")
CHECK("B753-block-trace(+1/phi)" in echo_sets["+1/phi class"]
      and "B753-phase-pair(+-72deg)" not in echo_sets["+1/phi class"],
      "the face's TRACE-level golden echo lands on the OTHER |1/phi| class (a non-seed class); "
      "its PHASE pair {+-72deg} lands on no golden class at all (only on the non-golden classes "
      "listed in PART 2) — the banked face data, wherever it touches the image, touches "
      "NON-seed classes")

arcs = ["B737_candidate_zero", "B739_character_rigidity", "B746_golden_ledger",
        "B753_mixing_structure"]


def grep_arcs(pattern, dirs):
    out = []
    for arc in dirs:
        for root, _, files in os.walk(os.path.join(FRONTIER, arc)):
            for fn in sorted(files):
                if not fn.endswith((".md", ".txt", ".py")):
                    continue
                with open(os.path.join(root, fn), encoding="utf-8", errors="replace") as fh:
                    for ln, line in enumerate(fh, 1):
                        if re.search(pattern, line):
                            out.append((arc, fn, ln, line.strip()))
    return out


hits = grep_arcs(r"-1/phi|−1/φ|-0\.618", arcs)
print(f"  grep for the seed's value (-1/phi | −1/φ | -0.618) across the four frozen arcs: "
      f"{len(hits)} hit(s)")
for arc, fn, ln, line in hits:
    print(f"    {arc}/{fn}:{ln}: {line[:110]}")
refut = re.compile(r"chat-1|asserted|fails|not ")
CHECK(hits and all(arc == "B753_mixing_structure" and refut.search(line)
                   for arc, fn, ln, line in hits),
      f"the seed's value -1/phi occurs in the frozen surface ONLY inside B753's REFUTATION lines "
      f"({len(hits)} hits, all carrying a refutation marker) — the face never speaks -1/phi as a "
      "computed value")

voice_hits = grep_arcs(r"0\.618|1\.618|golden|sqrt5|sqrt\(5\)|2\.2360",
                       ["B737_candidate_zero", "B739_character_rigidity"])
CHECK(len(voice_hits) == 0,
      "voice column re-verified golden-free by VALUE tokens (0.618|1.618|golden|sqrt5|sqrt(5)|"
      "2.2360): 0 hits in all committed B737+B739 files — B746 F11 reconfirmed (the letter 'phi' "
      "is excluded by design: it names the scattering matrix phi(s) there, a notation collision, "
      "not a golden marker; B739's theorem makes this structural: the continuous channel carries "
      "Lambda_K(s-1)/Lambda_K(s) and nothing else)")

# ============================================================================ PART 6
print()
print("=" * 100)
print("PART 6 — Q6 specialness budget: the SAME banked block at the tombstone's comparator words")
print("        (RRL, RLL — the words the tombstone lists with SU(2)_3 trace exactly 0)")
print("=" * 100)
comp = {}
for word in ("RL", "RRL", "RLL"):
    Bw = theta_odd_block(rho6(word))
    trw = Bw[0, 0] + Bw[1, 1]
    dev = np.linalg.norm(Bw @ Bw.conj().T - np.eye(2))
    goldenw = min(abs(abs(trw) - PHI), abs(abs(trw) - 1 / PHI)) < TOL
    comp[word] = (trw, dev, goldenw)
    su2tr = {"RL": "-1/phi", "RRL": "0", "RLL": "0"}[word]
    print(f"  word {word:<4} [SU(2)_3 trace {su2tr:>6}]: theta-odd weld block trace "
          f"{trw.real:+.6f}{trw.imag:+.6f}j, |trace| {abs(trw):.6f}, unitarity dev {dev:.2e}, "
          f"golden-magnitude {goldenw}")
eis = np.exp(2j * np.pi / 3)
CHECK(abs(comp["RRL"][0] - eis) < 1e-9 and abs(comp["RLL"][0] - np.conj(eis)) < 1e-9,
      "the comparator blocks' traces are EXACTLY e^{+-i 2pi/3} (|trace| = 1): being-column "
      "(Eisenstein-unit) values in B746's two-column vocabulary — not golden")
seed_special_weld = comp["RL"][2] and not (comp["RRL"][2] or comp["RLL"][2])
CHECK(True, f"Q6 comparator outcome computed: golden-magnitude block at RL {comp['RL'][2]}, "
      f"at RRL {comp['RRL'][2]}, at RLL {comp['RLL'][2]} -> the face's golden datum "
      f"{'IS' if seed_special_weld else 'is NOT'} seed-special among the tombstone's own words "
      "(3 words are NOT a census — see PART 7/8)")

# the descent question: is B(w) a function of the 2880-image element?
# S4^2 = I (PART 0, exact) so RL and RL*s^2 are the SAME SU(2)_3 element.
# S6^2 != I, so they are potentially DIFFERENT SU(3)_2 elements — a non-trivial test.
S6sq = S6 @ S6
S6sq_vs_I = np.linalg.norm(S6sq - np.eye(n6))
S6_ord4 = np.linalg.norm(S6sq @ S6sq - np.eye(n6))
M6_desc = rho6("RL") @ S6sq              # rho6(RL*s^2): same SU(2)_3 element, different SU(3)_2 element
B_desc = theta_odd_block(M6_desc)
tr_desc = B_desc[0, 0] + B_desc[1, 1]
block_diff = np.linalg.norm(B_RL - B_desc)
print(f"  descent probe: S6^2 != I (||S6^2 - I|| = {S6sq_vs_I:.3f}), S6^4 = I "
      f"(||S6^4 - I|| = {S6_ord4:.1e})")
print(f"    full block at RL      : trace {tr_B.real:+.6f}{tr_B.imag:+.6f}j")
print(f"    full block at RL*s^2  : trace {tr_desc.real:+.6f}{tr_desc.imag:+.6f}j")
print(f"    full block difference norm: {block_diff:.1e}")
CHECK(S6sq_vs_I > 0.1 and block_diff < 1e-12,
      f"descent NOT REFUTED: S6^2 != I in SU(3)_2 (||S6^2-I|| = {S6sq_vs_I:.3f}, the test "
      f"pair is non-trivial), yet the theta-odd blocks at RL and RL*s^2 are IDENTICAL "
      f"(diff {block_diff:.1e}) — the block is invariant under the SU(2)_3-kernel element "
      f"S6^2, consistent with being a function of the SU(2)_3 class (1 pair, not a proof "
      f"of descent for all kernel elements)")

# ============================================================================ PART 7
print()
print("=" * 100)
print("PART 7 — THE GAP DEMONSTRATED: none of the four frozen arcs answers the census question")
print("=" * 100)
for tok, where in ((r"RRL|RLL", arcs), (r"2880", arcs)):
    h = grep_arcs(tok, where)
    CHECK(len(h) == 0, f"token '{tok}' appears NOWHERE in the four frozen arcs ({len(h)} hits) — "
          + ("no arc ever evaluated the weld at any comparator word" if "RRL" in tok else
             "no arc ever touched the finite 2880 image at all"))
weld_hits = grep_arcs(r"weld", arcs)
CHECK(weld_hits and all(arc == "B753_mixing_structure" for arc, _, _, _ in weld_hits),
      f"'weld' appears only in B753 ({len(weld_hits)} hits); B753/compute.py builds it at the "
      "single word g=RL (W_weld = C @ R @ L, its L42) — ONE evaluated word in the whole frozen "
      "surface")
print("  per-arc shortfall (the four arcs, one line each):")
print("   - B753: evaluates B(w) at exactly one word (RL); no comparator, no base rate, no census;")
print("     its own scope line: 'the 2x2 theta-odd block of the twisted weld at g = RL'.")
print("   - B737: scattering/voice only — phi(s)=Lambda_K(s-1)/Lambda_K(s), residue, cusp CM;")
print("     no finite-image or weld quantity anywhere (greps above: 0 hits).")
print("   - B739: the character-rigidity theorem is scoped to the CONTINUOUS channel of the")
print("     scalar weight-0 Laplacian (its 'Honest bounds'); silent on the MTC/weld face.")
print("   - B746: a mapping ledger; its golden-spectral entries cite other floors (F3 chord,")
print("     F8 overlay); its own open doors (F11-adjacent: discrete-spectrum golden question")
print("     owner-gated; door 1 mirror sweep never run) mark the golden-spectral census unrun.")

# ============================================================================ PART 8
print()
print("=" * 100)
print("PART 8 — VERDICT")
print("=" * 100)
core = all(checks)
if core and seed_special_weld:
    print("VERDICT: FACE-OPENS")
    print("""THE OPENED QUESTION (queued, NOT claimed — the kill's own base-rate lesson is exactly
why 3 words are not a census):
  operator      : w |-> (trace, eigenphases) of B(w) = U^dag C rho_{SU(3)_2}(w) U — the face's
                  own theta-odd weld block (B753's banked pipeline), extended from B753's single
                  word to a census.
  input         : the word/SL(2,Z)-class census over the banked 2880 image's 37 classes — with
                  the descent not refuted here (PART 6: RL and RL*s^2, same SU(2)_3 element
                  but different SU(3)_2 elements, produce IDENTICAL blocks — consistent with
                  descent, 1 pair) so the census may be posed on image classes if full descent
                  is confirmed, else on SL(2,Z) classes or the joint level-rank image.
  discriminator : the weld-face golden rate (fraction of classes/words with golden-magnitude
                  block trace) and whether golden-block-ness separates the seed's class from
                  the other 3 golden classes.
  what-an-answer-changes:
                  rare-and-seed-only  -> the tombstone's own revival condition ('a class-level
                  invariant separating the seed from the other golden-magnitude classes')
                  acquires its FIRST computed candidate — next-arc queue entry;
                  base-rate-common    -> K-O's kill extends onto the weld face and the B'
                  exposure closes.
WHY THIS CELL CANNOT SETTLE IT: the computed evidence is 3 words (RL golden; RRL, RLL exactly
e^{+-i 2pi/3}, not golden) — the same sample size whose per-element table the original kill
REFUTED by the full 2880 census; banking 'seed-special' from 3 words would repeat the exact
error K-O died of. The frozen surface contains ONE evaluated word (PART 7): the census does
not exist in the banked record.
WHAT THE CELL DID SETTLE (the kill-upholding side, computed): the seed's class echoes NOTHING
banked (PART 5); -1/phi is spoken by the frozen surface only as B753's refuted assertion; the
voice is golden-free (B746 F11 reconfirmed); the face's banked golden datum carries the
signature of NON-seed classes (trace-echo on the +1/phi class; phase-pair on non-golden
classes only).""")
elif core and not seed_special_weld:
    print("VERDICT: KILL-EXTENDS (the face's golden datum is not seed-special among the tested")
    print("words and the banked face content echoes only non-seed classes — see PARTS 5-6)")
else:
    print("VERDICT: BLOCKED (a core check failed — see FAIL lines above)")
print()
print(f"CHECK-SUMMARY: {sum(checks)}/{len(checks)} passed")
