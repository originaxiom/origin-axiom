"""B1682 -- the word side of the record count, verified on main (the SM seat's W110), and the web seat's read that the
input of GENESIS v1.49 is equivalent to two records. Live, from main's own check: the length counts by direct reduction
(the left moves by main's own count); a small census -- at n = 3 to length 5 no class keeps its length under every
R_ij^{+-1}, while at n = 2 to length 8 the census does find kept classes, exactly the powers of [a, b] (the bite); the
genus-2 boundary word kept by the handle twists and moved between the handles. Stored: main's full census (to n = 5)
and the seat's run, with the received files' hashes."""
import hashlib, importlib.util, json, pathlib, random
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1682_the_word_side_of_the_record_count_verified"


def _mk():
    spec = importlib.util.spec_from_file_location("mk", A / "verification" / "main_check" / "main_kept_words.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m


def test_the_length_counts_live():
    m = _mk(); rng = random.Random(82)
    for _ in range(150):
        n = rng.randint(2, 5); w = m.random_cyclic(n, rng.randint(1, 20), rng); k = len(w)
        for i in range(1, n + 1):
            ni = sum(1 for x in w if abs(x) == i)
            for j in (j for j in range(1, n + 1) if j != i):
                for e in (1, -1):
                    assert len(m.cyc(m.apply(m.R(i, j, e), w))) == k + ni - 2 * m.count_R(w, i, j, e)
                    assert len(m.cyc(m.apply(m.Lm(i, j, e), w))) == k + ni - 2 * m.count_L(w, i, j, e)


def test_the_census_small_with_its_bite():
    m = _mk()
    r3 = m.census(3, 5)
    assert r3["classes"] == 868 and not r3["len_kept_R"] and not r3["len_kept_L"] and not r3["kept_tv"]
    r2 = m.census(2, 8)
    powers = sorted([m.key(m.comm(1, 2) * k) for k in (1, 2)] + [m.key(m.inv(m.comm(1, 2) * k)) for k in (1, 2)])
    assert sorted(r2["kept_record"]) == powers and sorted(r2["kept_tv"]) == powers     # the bite: found where they exist
    t4 = m.t4()
    assert all(t4["twists_keep_the_word"]) and t4["between_handle_transvections"] == 8 and all(t4["moved"])


def test_stored_runs_and_received_hashes():
    d = json.loads((A / "verification" / "main_check" / "main_kept_words.json").read_text(encoding="utf-8"))
    assert all(d["hold"].values()) and d["T1"]["failures"] == 0
    assert [d["T2"][s]["classes"] for s in ("2", "3", "4", "5")] == [69996, 63590, 141492, 102528]
    assert len(d["T2"]["2"]["kept_record"]) == 6 and len(d["T2"]["2"]["len_kept_R"]) == 356
    run = (A / "verification" / "received" / "the_kept_words_run.txt").read_text(encoding="utf-8")
    assert "cells: {'C1': True, 'C2': True, 'C3': True, 'C4': True}" in run
    for line in (A / "SHA256_RECEIVED.txt").read_text().splitlines():
        h, name = line.split()
        assert hashlib.sha256((A / "verification" / "received" / name).read_bytes()).hexdigest() == h, name
    v = json.loads((A / "arc_verdict.json").read_text(encoding="utf-8"))
    assert v["verdict"] == "PROVED" and v["rests_on_seat"] == ["sm:W110"]
