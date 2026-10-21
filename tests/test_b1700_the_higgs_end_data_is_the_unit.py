"""B1700 -- the Higgs's end data is the unit (P-245). Live: the exact computation (one canonical condition, dimension
three, DR in the space and its only member holomorphic off v+, the hierarchy exponents). Stored: B1641's index table
agrees (-chi_{27/2} = -3 at one unit, chi_{3/2} = 0 without)."""
import glob, importlib.util, io, contextlib, json, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
A = ROOT / "frontier" / "B1700_the_higgs_end_data_is_the_unit"


def test_the_units_sheaf_live():
    spec = importlib.util.spec_from_file_location("b1700", A / "verification" / "the_units_sheaf.py")
    m = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(m)
    o = m.out
    assert o["conditions"] == [[1, -1]] and o["dim_weight_27/2_canonical"] == 3
    assert o["Delta_DR_in_kernel"] and o["dim_holomorphic_on_P_and_N"] == 1 and o["the_P_N_holomorphic_member_is_DR"]
    assert sorted(o["basis_line_orders_weight_3/2"]) == [[-7, -1, -5], [-7, -1, -5], [1, -1, 3]]
    assert o["m2/m3_exponent_DR"] == "1/2" and sorted(o["m2/m3_exponent_basis"]) == ["0", "0", "1/2"]
    assert o["m2/m3_exponent_generic"] == ["0", "0", "0"]


def test_b1641_index_agrees():
    d = json.loads(pathlib.Path(glob.glob(str(ROOT / "frontier" / "B1641_*" / "verification" / "w46_on_main.json"))[0]).read_text(encoding="utf-8"))
    for row in d["W3"].values():
        assert row["table"]["0,n=1"][0] == -3.0 and row["table"]["0,n=0"][0] == 0.0
    assert d["W2"]["chi_3/2_rho_T"] == 0.0
