"""B1686 -- the SM seat's W60 and W62 on main (P-222). Live: main's lattice builder (one triangle at -1 on small tori;
the bite: the other crossing order gives three on the torus <(6,3), (-3,3)>), Kramers at phi = 0, the real-form solver
against a dense solve; W62's lattice cells re-read from the committed spectra and compared with the seat's recorded
read-out (M1-M6, to 1e-8); W62's closed-form cells. Stored: W60's cells and the received files' hashes."""
import hashlib, importlib.util, io, contextlib, json, pathlib, sys
import numpy as np
A = pathlib.Path(__file__).resolve().parents[1] / "frontier" / "B1686_w60_w62_on_main"
V = A / "verification"
sys.path.insert(0, str(V))


def _load(name):
    spec = importlib.util.spec_from_file_location(name, V / (name + ".py"))
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    return m


def test_the_builder_live_with_the_bite():
    L = _load("lattice")
    def negatives(v1, v2, order):
        T = L.Torus(v1, v2); T.operator((0.0, 0.0), 2, order=order)
        return sum(1 for _, h in T.plaquettes(2) if np.allclose(h, -np.eye(2))), T
    for v1, v2 in (((6, 0), (0, 6)), ((5, 1), (-2, 6)), ((6, 3), (-3, 3))):
        assert negatives(v1, v2, "first-left")[0] == 1
    assert negatives((6, 3), (-3, 3), "first-right")[0] == 3                  # the bite: the other crossing order
    T = L.Torus((6, 0), (0, 6))
    w = np.linalg.eigvalsh(T.operator((0.0, 0.0), 2).toarray())
    assert np.abs(w[0::2] - w[1::2]).max() < 1e-12                             # Kramers at phi = 0
    H = T.operator((0.13, 0.31), 2)
    assert np.abs(L.lowest(H, 10) - np.linalg.eigvalsh(H.toarray())[:10]).max() < 1e-12


def test_w62_lattice_cells_reread_against_the_seat():
    m = _load("main_w62")
    with contextlib.redirect_stdout(io.StringIO()):
        c = m.lattice_cells(write=False)
    s = json.loads((V / "received" / "the_matter_and_the_shape.json").read_text(encoding="utf-8"))
    assert all(c[k]["holds"] for k in ("M1", "M2", "M3", "M4", "M5", "M6")) and c["M0"]["one_negative_triangle_everywhere"]
    assert abs(c["M4"]["beta"] - s["M4"]["beta (dV_rho = beta dE3)"]) < 1e-8
    assert abs(c["M2"]["max_abs_dD_4n"] - s["M2"]["max |dD| at 4n"]) < 1e-8
    for k, sk in (("n8400", "n"), ("n33600", "4n")):
        assert abs(c["M1"]["max_err"][k] - s["M1"]["largest |dV_comb - dV_per| by size"][sk]) < 1e-10
    seat_axis = sorted(s["M5"]["axis by y"].values()); main_axis = sorted(v for _, v in c["M5"]["axis"])
    assert np.allclose(seat_axis, main_axis, atol=1e-8)
    assert c["truncation_control"]["n33600"] < 1e-8 and -0.99 < c["D_shape_n33600"]["c_E2_over_31_1024"] < -0.98


def test_w62_closed_form_live():
    m = _load("main_w62")
    with contextlib.redirect_stdout(io.StringIO()):
        o = m.closed_form_cells()
    a2 = o["A2"]
    assert abs(a2["V_H_omega"] + 1.5530) < 1e-3 and abs(a2["V_H_i"] + 3.7854) < 1e-3 and a2["monotone_decreasing_omega_to_i"]
    assert abs(a2["grad_omega"][0] + 7.518) < 1e-2 and abs(a2["grad_omega"][1] + 4.341) < 1e-2
    assert max(o["A3_rel_errors"].values()) < 1e-4
    cc = o["contents_cusp_coefficients_zeta6"]
    assert all(v > 0 for line in cc.values() for v in line.values())                    # every content runs to a cusp
    assert abs(cc["(Fraction(1, 2), Fraction(1, 2))"]["(a) matter + Higgs"] - 9.57421875) < 1e-12
    omega = [r for r in o["A1"] if abs(r["tau"][0] + 0.5) < 1e-9]
    assert omega and all(r["T1_equals_mirror_err"] < 1e-12 for r in o["A1"])            # T moves it except at omega's mirror


def test_w60_stored_and_received_hashes():
    d = json.loads((V / "main_w60.json").read_text(encoding="utf-8"))
    conv = d["convergence_lowest10_rel_change"]
    assert 1e-4 < min(conv) and max(conv) < 3e-3
    assert d["net_2torsion_below_fine_grid_min"] and min(d["net_at_2torsion_N96"]) < -147.6 < d["net_fine_grid_min"]["value"]
    assert d["grid96_corr_with_periodic_part"] > 0.999 and -0.80 < d["grid96_diffraction_over_periodic_at_(1/6,1/6)"] < -0.78
    for line in (A / "SHA256_RECEIVED.txt").read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"): continue
        h, name = line.split()[:2]
        p = V / "received" / name
        if p.exists():
            assert hashlib.sha256(p.read_bytes()).hexdigest() == h, name
