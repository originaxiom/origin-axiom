#!/usr/bin/env python3
"""W-L1, the values (card W-L1): frame C at (tau = i, the mark (2/5, 4/5)), in the big run's seven positions, written to
LOOK_VALUES.json before the look script exists. Options: the declared one (the canonical end) and, reported only, the
end shifted by -0.3 and +0.3. The reading pair is (S, S); at tau = i St gives the same (W-A1). No data is read.

    MAIN_CHECKOUT=<a checkout of main> python3 -I -u wl1_values.py
"""
import hashlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "chat1_2026-11-15_wa1"))
import wa1_tau_i_posthoc1 as P  # noqa: E402

POSITIONS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]
OPTIONS = {"tau=i, mark, canonical end": 0.0, "end -0.3 (reported)": -0.3, "end +0.3 (reported)": 0.3}


def main():
    out = {"positions": POSITIONS, "options": {}}
    for name, dL in OPTIONS.items():
        _, (rat, mix) = P.outs((1j, (0.4, 0.8), dL))
        V = mix[("S", "S")]
        vals = [rat["up|S|r2"], rat["up|S|r3"], rat["down|S|r2"], rat["down|S|r3"], float(V[0, 1]), float(V[1, 2]), float(V[0, 2])]
        out["options"][name] = {"values": vals, "end_shift": dL}
    path = os.path.join(HERE, "LOOK_VALUES.json")
    open(path, "w").write(json.dumps(out, indent=1))
    print("written; sha256", hashlib.sha256(open(path, "rb").read()).hexdigest())


if __name__ == "__main__":
    main()
