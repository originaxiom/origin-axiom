"""One-off: build docs/total_inputs_scoreboard.json (P-418, P-579, P-661). Frame B from the firewalled reader's
audit/scaffold/agy_joints.json (names and types only; main's corrections applied); frame A from main's own record."""
import json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]   # run once from the audit room (S300c); it reads the gitignored reader file audit/scaffold/agy_joints.json
src = json.loads((ROOT / "audit/scaffold/agy_joints.json").read_text(encoding="utf-8"))
J = src["joints"]; J = J if isinstance(J, list) else list(J.values())
OBS = ["m_u/m_c", "m_c/m_t", "m_d/m_s", "m_s/m_b", "m_e/m_mu", "m_mu/m_tau", "|V_us|", "|V_cb|", "|V_ub|", "J (or delta_CP)",
       "m_b/m_t (firewalled)", "m_tau/m_b (firewalled)", "y_t", "g_1", "g_2", "g_3", "theta-bar", "m_H", "v",
       "M_Pl/v", "rho_DE/v^4", "eta_B", "Omega_DM/Omega_b"]
REGISTER = {"B01": "P-629", "B02": "P-625, P-384", "B03": "P-384", "B05": "P-295", "B07": "P-402", "B08": "P-402",
            "B09": "P-531", "B10": "P-570, P-597", "B11": "P-446", "B42": "P-597", "B47": "P-663", "B19": "P-624"}
SAME = {"B01": "A01", "B02": "A02", "B03": "A03", "B04": "A04", "B05": "A05", "B07": "A06", "B09": "A08", "B10": "A12",
        "B11": "A10", "B12": "A11"}
B = []
for x in J:
    feeds = x["feeds_route_a"]; feeds = feeds if isinstance(feeds, list) else json.loads(feeds)
    t = x["type"]
    basis = x.get("main_basis", "")
    if x["id"] == "F1":
        basis = "main's frame as banked: LAW_MAP 'A HIGGS IN M: ONE GENERATION EXACTLY MASSLESS' (B1644), the four-channel coupling with 'given Λ, the dictionary' (B1656), 'THE FAMILY GROUP IS THE FRAME' (B1736), and T-KERNEL-SUM-TWIST (B1832) -- conditional on the frame's own givens (the shared block and frame A's joints)"
    if x["id"] == "F2":
        basis = "main's hypercharge dictionary as banked with the frame: LAW_MAP 'given Λ, the dictionary' (B1656's row)"
    if x["id"] == "F7":          # main's correction (S300c): no theorem row; the mirror is verified, not proved
        t = "VERIFIED-BY-MAIN"
        basis = "LAW_MAP 'THE LL PAIR AT THE DOUBLED LINE, THE MIRROR AS A MATRIX' (B1832): exact to 10^-15 on main's code, verified, not proved (the reader cited a theorem row that does not exist)"
    B.append({"id": x["id"], "name": x["name"], "type": t, "lane_label": x.get("lane_claim", ""), "basis": basis,
              "feeds": feeds, "register": REGISTER.get(x["id"], ""), "same_as": SAME.get(x["id"], "")})
TEN = list(range(1, 11)); OUTS = TEN + [11, 12, 17]
A = [
 ("A01", "the modulus tau (Re tau, Im tau) on the strip, Im tau near 3", "FITTED", "FL-04; B1829's REGRADE: the strip was found by sealed looks at the data (P-585's look count)", OUTS, "P-629"),
 ("A02", "the slope 2/5 of the line class", "CHOSEN", "P-384 (the referee: mostly a pick); P-625: the slope selection is not value-free", OUTS, "P-384, P-625"),
 ("A03", "the offset odd/10 within the class", "CHOSEN", "P-384", OUTS, "P-384"),
 ("A04", "the Higgs direction (a census theta-power direction)", "CHOSEN", "B1829's candidate rows; FL-09's menu", OUTS, "P-366"),
 ("A05", "the reading (S~, S, S) at a0 = 0", "CHOSEN", "FL-09; B1744 (the reading is not forced); B1832's S300 section (FR-FIB at a0 = 0 against FR-COV)", OUTS, "P-295"),
 ("A06", "the horocycle L_max (over L_2)", "CHOSEN", "P-402: selected by the data, not absorbed by tau (the web seat's sealed H2)", OUTS, "P-402"),
 ("A07", "the end: the small-cut norm", "CHOSEN", "P-421: no geometric ground since S238; at the exact norms the six fail (B1829, S297)", OUTS, "P-421"),
 ("A08", "the generations' metric H = I", "CHOSEN", "B1822; FL-11", OUTS, "P-531"),
 ("A09", "the channel weights sqrt(2 pi L + c_s), a flat norm and cut with a hyperbolic radius", "ANSATZ", "FL-11 (UNSTATED)", OUTS, ""),
 ("A10", "the lepton factor c = 3", "CHOSEN", "FL-12 (inserted by hand); B1789, B1793, B1817 (not derived)", [5, 6, 12], "P-446"),
 ("A11", "one address: one tau, one line, one point coupling for all sectors", "CHOSEN", "FL-07 (UNSTATED in code)", OUTS, "P-555"),
 ("A12", "the scale: tree level at M_Z, no running", "CHOSEN", "FL-13, FL-21; P-570, P-590", OUTS, "P-570"),
]
FA = [{"id": i, "name": n, "type": t, "basis": b, "feeds": f, "register": r,
       "same_as": next((k for k, v in SAME.items() if v == i), "")} for i, n, t, b, f, r in A]
SHARED = [
 {"id": "S01", "name": "a flat bundle on the fibre (no curvature, flux or continuous moduli from the geometry)", "type": "ANSATZ", "basis": "FL-02 (OPEN, GAP6); 107 of 173 value-kills sit on flat premises (P-571)", "register": "P-571"},
 {"id": "S02", "name": "the orientation: the orientable, amphichiral member (SE2)", "type": "CHOSEN", "basis": "FL-03; GENESIS SE2", "register": ""},
]
data = {
 "rule": "the owner's ruling of 2026-10-29 (P-418): a total-inputs scoreboard beside '0 of 19' -- the 19, the identification price, and each frame's counted choices; progress = the totals falling. The owner, 2026-11-04 (P-661): a complete picture with its borrowed joints named, so the joints can be earned later.",
 "observables": OBS,
 "identification_price": {"count": 13, "basis": "4 + 9, B1266's union-find over IDENTIFICATION_LEDGER (the owner's ruling of 2026-10-29, P-418)"},
 "earned": 0,
 "shared_block": SHARED,
 "frames": {
  "A": {"name": "the record's candidate: THE SIX ON THE STRIP (FR-FIB at the small-cut end; B1829, P-585)", "claims": TEN,
        "held_out": [11, 12], "graded_input": [17], "no_frame": [13, 14, 15, 16, 18, 19], "joints": FA,
        "status": "a CANDIDATE at level 1 (screen); its level-2 confirmation is one held-out target short (P-597)"},
  "B": {"name": "the agy lane's complete picture: its master scorecard, Route A, at 18c607040", "claims": list(range(1, 24)),
        "held_out": [], "graded_input": [], "no_frame": [], "joints": B,
        "status": "0 certified by the lane's own counter; its labels call borrowed joints FORCED (B1832 sec. 5); its values for P-585's held-out targets sealed (P-624)",
        "source": "a firewalled reader through the mask (names and types only), verified by main: every FORCED-BY-MAIN basis checked to exist; F7 corrected to VERIFIED-BY-MAIN"},
 },
}
(ROOT / "docs/total_inputs_scoreboard.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("written", len(FA), len(B))
