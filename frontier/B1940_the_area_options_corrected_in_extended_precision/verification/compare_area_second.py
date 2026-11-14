"""The area options' second computation, compared (main, 2026-11-14, committed BEFORE any seat's area output exists; the
rule's amendment A15, after the web seat's W-F21 caveat on O4). The decision is fixed here: per value,
|d ln| <= 3 sqrt(e_main^2 + e_seat^2 + delta^2), with delta = 5.4e-3 (B1932's rule, its error (b)) and each code's stated
relative error; an option AGREES when all seven of its values do. Beside it, for information only, z against the two
codes' stated errors alone. The adapter that reads a seat's file only maps its names onto the seven positions; it prints
none of the seat's numbers, only these differences.
    from compare_area_second import compare      # compare(main_vals, main_errs, seat_vals, seat_errs)"""
import math, json, pathlib
DELTA = 5.4e-3
POSITIONS = ["up m2/m3", "up m1/m3", "down m2/m3", "down m1/m3", "|V12|", "|V23|", "|V13|"]
HERE = pathlib.Path(__file__).resolve().parent


def compare(main_vals, main_errs, seat_vals, seat_errs):
    assert len(main_vals) == len(seat_vals) == 7
    rows = []
    for m, em, s, es in zip(main_vals, main_errs, seat_vals, seat_errs):
        rm, rs = em / m, es / s
        dl = math.log(s) - math.log(m)
        tol = 3 * math.sqrt(rm ** 2 + rs ** 2 + DELTA ** 2)
        z = dl / math.sqrt(rm ** 2 + rs ** 2) if rm or rs else float("inf")
        rows.append({"dln_over_tol": dl / tol, "z_sampling": z})
    return {"agrees": all(abs(r["dln_over_tol"]) <= 1 for r in rows), "worst": max(abs(r["dln_over_tol"]) for r in rows), "rows": rows}


def main_area_options():
    V = json.loads((HERE / "BIG_RUN_VALUES_v2.json").read_text())
    return {o: (V["options"][o]["values"], V["options"][o]["error"]) for o in ("W-|b (area)", "W+|b (area)")}
