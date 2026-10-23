"""B1733 -- the thread's own lines (P-312, P-336), PROVED. Live: the Smith rule against brute force on a sample of
classes and orders (with the trace rule's first non-squarefree failure); the order-5 pair for the tick; one reversing
symmetry swapping it. Stored: the full checks."""
import json, pathlib, sys
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1733_the_threads_own_lines"
sys.path.insert(0, str(A / "verification"))


def _stored():
    return json.loads((A / "verification" / "the_threads_own_lines.json").read_text(encoding="utf-8"))


def test_the_stored_checks():
    d = _stored(); ab = d["A_B"]
    assert ab["classes"] == 241 and ab["checks"] == 6989 and ab["smith_mismatches"] == 0
    assert ab["trace_mismatches"] == 153 and ab["trace_mismatches_at_squarefree_N"] == 0
    assert ab["order5_cyclic_classes"] == ab["of_which_exactly_v_and_2v"] == 99
    assert d["C"] == {"e*det=-1": {"swap": 28}, "e*det=+1": {"fix": 188}}
    assert d["D"]["mirror_worst"] < 1e-9
    lr = [r for r in d["E"] if r["word"] == "LR"][0]
    assert lr["Q_v_vs_2v"] < 1e-10 and lr["apex_v_vs_2v"] > 1 and abs(lr["Q_reduced"][0]) < 1e-9 and abs(lr["Q_reduced"][1] - 1) < 1e-9


def test_the_smith_rule_live():
    import the_threads_own_lines as T
    for w in ("LR", "LLRR", "LLLLLLLLRR", "LLLRLR", "LRRRRR"):
        M = T.word(w); t = M[0][0] + M[1][1]
        (_, dm), (_, dp) = T.d12(M, 1), T.d12(M, -1)
        for N in range(2, 21):
            assert bool(T.fixed(M, N)) == ((dm % N == 0) or (dp % N == 0)), (w, N)
    M = T.word("LLLLLLLLRR")                                  # the trace rule fails at N = 16 (not squarefree)
    assert ((M[0][0] + M[1][1] - 2) % 16 == 0 or (M[0][0] + M[1][1] + 2) % 16 == 0) and not T.fixed(M, 16)


def test_the_tick_pair_and_its_swap_live():
    import the_threads_own_lines as T
    A = [[3, -1], [1, 0]]                                     # B1720's representative of LR
    pairs = {min(v, ((-v[0]) % 5, (-v[1]) % 5)) for v in T.fixed(((3, -1), (1, 0)), 5)}
    assert pairs == {(1, 1), (2, 2)}
    g = [[-2, 1], [-1, 1]]                                    # det -1, g A g^-1 = A: a glide, g^2 = A
    assert T.mm(g, g) == A
    v = (1, 1); gv = ((v[0] * g[0][0] + v[1] * g[1][0]) % 5, (v[0] * g[0][1] + v[1] * g[1][1]) % 5)
    assert gv in ((2, 2), (3, 3))                             # +-2v: swapped
