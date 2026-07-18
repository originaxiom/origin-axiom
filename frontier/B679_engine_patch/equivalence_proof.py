"""equivalence_proof.py -- old-vs-patched gate_report: bit-for-bit equivalence
battery + speedup table.

Loads the byte-snapshot of the current shared engine (engine_v7_current.py,
snapshot of <seat-workdir>/veins/v7_conduit/engine_v7.py, sha256 recorded in
PATCH_REPORT.md) and the prepared engine_v7_patched.py as two independent
modules, then:

  (0) mechanically verifies the two files are IDENTICAL outside the
      gate_report function (ast-based line-span excision);
  (1) verifies the exact/rational + build path is bit-identical between the
      two modules (PRIM, h, c, theta_split, S, T entries compared on raw
      mpf/mpc mantissa tuples) -- expected trivially, since that code is
      byte-identical, but asserted rather than assumed;
  (2) for every distinct call pattern found in the repo's importing cells
      (An_Level(3,k) positional / keyword / name= forms; build(verbose=False);
      gate_report(S,T) bare and gate_report(S,T,label=...); rho_A1_matrix;
      SU(2) constructor path; verlinde_N) runs OLD gate_report and PATCHED
      gate_report on the SAME (S,T) and asserts:
        - rep dict: same key ORDER, every value bit-identical (._mpf_),
        - rho matrix: every entry bit-identical (._mpc_/._mpf_),
        - label path: captured stdout character-identical;
  (3) times both, small through N=45 (SU(3)_8) -- the speedup table.

Battery sizes (SU(3)_k has N=(k+1)(k+2)/2 primaries):
  k=1 (N=3), SU(2)_3 (N=4), k=2 (N=6), k=4 (N=15), k=6 (N=28), k=8 (N=45).
The repo's importing cells call An_Level with n=3, k=1..13 and gate_report
only via d4_ceiling.py (k=1..12, label=...); N=45 exercises the >=40 regime
where the old O(N^5) cost is hours-scale per ladder.
"""
import ast
import io
import os
import sys
import time
import contextlib
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))


def load_module(fname, modname):
    spec = importlib.util.spec_from_file_location(modname, os.path.join(HERE, fname))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def source_without_gate_report(fname):
    src = open(os.path.join(HERE, fname)).read()
    tree = ast.parse(src)
    span = None
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == "gate_report":
            span = (node.lineno, node.end_lineno)
    assert span, f"no gate_report in {fname}"
    lines = src.splitlines(keepends=True)
    return "".join(lines[: span[0] - 1] + lines[span[1]:]), span


def bits(x):
    """Raw-mantissa representation: equal iff bit-for-bit equal."""
    if hasattr(x, "_mpf_"):
        return ("mpf", x._mpf_)
    if hasattr(x, "_mpc_"):
        return ("mpc", x._mpc_)
    return ("other", type(x).__name__, repr(x))


def mat_bits(M):
    return [[bits(M[i, j]) for j in range(M.cols)] for i in range(M.rows)]


def rep_bits(rep):
    return [(k, bits(v)) for k, v in rep.items()]


checks = 0


def ok(cond, msg):
    global checks
    assert cond, "FAILED: " + msg
    checks += 1
    print(f"  [ok] {msg}")


def run_gate(mod, S, T, label=""):
    buf = io.StringIO()
    t0 = time.perf_counter()
    with contextlib.redirect_stdout(buf):
        rep, rho = mod.gate_report(S, T, label=label) if label else mod.gate_report(S, T)
    dt = time.perf_counter() - t0
    return rep, rho, buf.getvalue(), dt


def main():
    out = sys.stdout
    cur = load_module("engine_v7_current.py", "ev7_current")
    pat = load_module("engine_v7_patched.py", "ev7_patched")

    print("== (0) file-level: patched differs from current ONLY inside gate_report")
    src_c, span_c = source_without_gate_report("engine_v7_current.py")
    src_p, span_p = source_without_gate_report("engine_v7_patched.py")
    ok(src_c == src_p,
       f"sources identical outside gate_report (current lines {span_c}, patched lines {span_p})")

    print("== (1) exact/rational + build path bit-identical between modules")
    for ctor, tag in [
        (lambda m: m.An_Level(3, 2), "An_Level(3, 2) positional"),
        (lambda m: m.An_Level(3, 3, name="SU(3)_3"), "An_Level(3, 3, name=...)"),
        (lambda m: m.An_Level(n=3, k=2, name="SU(3)_2"), "An_Level(n=3, k=2, name=...) keyword"),
        (lambda m: m.An_Level(2, 3), "An_Level(2, 3) (SU(2)_3, engine's own validation case)"),
    ]:
        Lc, Lp = ctor(cur), ctor(pat)
        ok(Lc.PRIM == Lp.PRIM and Lc.N == Lp.N, f"{tag}: PRIM identical (N={Lc.N})")
        ok(Lc.h == Lp.h and Lc.c == Lp.c, f"{tag}: exact h (Fractions) and c identical")
        ok(Lc.theta_split() == Lp.theta_split(), f"{tag}: theta_split identical")
        Sc, Tc = Lc.build(verbose=False)
        Sp, Tp = Lp.build(verbose=False)
        ok(mat_bits(Sc) == mat_bits(Sp), f"{tag}: S bit-identical")
        ok(mat_bits(Tc) == mat_bits(Tp), f"{tag}: T bit-identical")

    print("== (2)+(3) gate_report old vs patched: bit-identity + timing")
    print("  (rho_A1_matrix / verlinde_N cross-checks included at small N)")
    table = []
    battery = [("SU(2)_3", 2, 3), ("SU(3)_1", 3, 1), ("SU(3)_2", 3, 2),
               ("SU(3)_4", 3, 4), ("SU(3)_6", 3, 6), ("SU(3)_8", 3, 8)]
    for name, n, k in battery:
        L = cur.An_Level(n, k, name=name)
        S, T = L.build(verbose=False)
        print(f"-- {name}: N={L.N}  (old is O(N^5): may take a while at large N)")
        out.flush()

        # bare call pattern
        rep_o, rho_o, _, t_old = run_gate(cur, S, T)
        rep_n, rho_n, _, t_new = run_gate(pat, S, T)
        ok(rep_bits(rep_o) == rep_bits(rep_n),
           f"{name}: rep dict bit-identical incl. key order {list(rep_o.keys())}")
        ok(mat_bits(rho_o) == mat_bits(rho_n), f"{name}: rho matrix bit-identical")

        # label= call pattern (the d4_ceiling.py pattern) -- printed output identical
        _, _, txt_o, _ = run_gate(cur, S, T, label=f"{name} (kappa={k + L.hvee[n]})")
        _, _, txt_n, _ = run_gate(pat, S, T, label=f"{name} (kappa={k + L.hvee[n]})")
        ok(txt_o == txt_n, f"{name}: label= printed output character-identical")

        # rho_A1_matrix direct (a3_stage/d4_su3_run pattern) -- unchanged code, asserted
        w1c, w2c, devc = cur.rho_A1_matrix(S, T)
        w1p, w2p, devp = pat.rho_A1_matrix(S, T)
        ok(mat_bits(w1c) == mat_bits(w1p) and mat_bits(w2c) == mat_bits(w2p)
           and bits(devc) == bits(devp), f"{name}: rho_A1_matrix outputs bit-identical")

        if L.N <= 6:
            Nv_c = cur.verlinde_N(S)
            Nv_p = pat.verlinde_N(S)
            ok([[[bits(x) for x in r] for r in pl] for pl in Nv_c]
               == [[[bits(x) for x in r] for r in pl] for pl in Nv_p],
               f"{name}: verlinde_N bit-identical")

        # timing rows use the bare-call timings above (old timed once: O(N^5))
        table.append((name, L.N, t_old, t_new, t_old / t_new if t_new > 0 else float("inf")))
        print(f"   old {t_old:10.3f} s   patched {t_new:8.3f} s   speedup x{t_old / t_new:9.1f}")
        out.flush()

    print()
    print("== SPEEDUP TABLE (gate_report, same (S,T), same process) ==")
    print(f"{'theory':>10} {'N':>4} {'old (s)':>12} {'patched (s)':>12} {'speedup':>10}")
    for name, N, to, tn, sp in table:
        print(f"{name:>10} {N:>4} {to:>12.3f} {tn:>12.3f} {sp:>9.1f}x")
    print()
    print(f"ALL EQUIVALENCE ASSERTIONS PASSED: {checks} checks, bit-for-bit.")


if __name__ == "__main__":
    main()
