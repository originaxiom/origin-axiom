"""Step B's sigma-only file, written ONCE (main's ruling on the third review: sigma comes from a committed sigma-only file,
relative errors only, disclosed as seen; the pre-seal drivers never import compare.py).  2026-10-30, data-free in effect:
it writes no central value.

- The nine (c/t, u/t, s/b, d/b, mu/tau, e/tau, |V_us|, |V_cb|, |V_ub|): B1741's sealed measure, compare.sigmas() (natural
  log, the relative error in quadrature with ALLOW = 0.10), called in this process; only its sigmas are kept.
- |J|: the PDG 2024 CKM review's global fit (Review of Particle Physics, Phys. Rev. D 110, 030001; section 12.3), its
  asymmetric error +0.13/-0.12 (x 1e-5) symmetrised to a relative 0.125 / J; the same global fit whose moduli B1741's
  sigmas reproduce (|V_ub| 2.4%, |V_cb| 1.9%).  The relative error alone is written: REL_J below.
The file records the sigmas, the relative errors they imply, the order, and the sources; never a central value."""
import contextlib, io, json, math, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
B1741 = ROOT / "frontier" / "B1741_tau_from_the_thread_rule_the_line_free" / "verification"
ALLOW = 0.10
REL_J = 0.0401          # PDG 2024 global fit, (0.13 + 0.12) / 2 over its central value, rounded to 3 digits
ORDER = ["c/t", "u/t", "s/b", "d/b", "mu/tau", "e/tau", "|V_us|", "|V_cb|", "|V_ub|", "|J|"]


def main(out):
    sys.path.insert(0, str(B1741))
    with contextlib.redirect_stdout(io.StringIO()):
        import compare
        six, nine = compare.sigmas()
    six = [float(x) for x in six]; nine = [float(x) for x in nine]
    assert len(six) == 6 and len(nine) == 9 and all(abs(a - b) < 1e-15 for a, b in zip(six, nine[:6]))
    sig = nine + [math.sqrt(REL_J ** 2 + ALLOW ** 2)]
    rel = [math.sqrt(max(s * s - ALLOW ** 2, 0.0)) for s in sig]
    assert all(0.0999 < s < 0.25 for s in sig)
    doc = {"what": "Step B's sigma-only file: natural-log sigmas of the ten (the relative error in quadrature with ALLOW); no central value",
           "order": ORDER, "allow": ALLOW, "sigma_natural_log": sig, "relative_errors_implied": rel,
           "sources": {"nine": "B1741 compare.sigmas() (its sealed measure), called once by extract_sigma.py; central values not read",
                       "J": "PDG 2024 CKM review (Phys. Rev. D 110, 030001, section 12.3), the global fit's asymmetric error symmetrised: relative 0.0401"},
           "written": "2026-10-30, once; disclosed as seen (THE FINAL ATTACK, Step B card section 7)"}
    pathlib.Path(out).write_text(json.dumps(doc, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"sigma_natural_log": [round(s, 6) for s in sig]}))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else str(pathlib.Path(__file__).resolve().parent / "SIGMA_ONLY.json"))
