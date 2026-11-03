"""S297, second batch (law rows against dated notes): rows 155, 311, 327 sharpened; the scope of 'the canonical end' stated
once on B1667's row; MAINS_PLAN's strip row given the end formula. Also recorded here: row 258 (sharpened by hand, the
old-era reader's minor lag, verified against B1477). Each replacement asserted unique; each verified by main at its source."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[4]
S = "carried here 2026-11-03, S297"
edits = {
 "docs/LAW_MAP.md": [
  # 155 -- the closer retired (B1750, GENESIS v1.55); the signature is the holonomy's (B716)
  ("The object supplies the boundaries (cusp + flow); the observer supplies every closing |",
   "The object supplies the boundaries (cusp + flow); the observer supplies every closing [superseded by B1750 (GENESIS "
   "v1.55, 2026-10-24): the closer retired as an explanatory move, the observer re-typed (RETRACTED_PHRASES, S219); and "
   "the Lorentzian signature is the holonomy's, not the observer's (B716's sharpening of 2026-10-29); " + S + "] |"),
  # 311 -- the k = -1/2 mod 6 class at the canonical radius
  ("near ω the residual ℤ₃ charge sets them (k mod 6);",
   "near ω the residual ℤ₃ charge sets them (k mod 6) [in B1646's L-free coupling, the large-L limit; at the canonical "
   "radius (L = 0.65, 2.5) the k ≡ −½ mod 6 class has m₂/m₃ ∝ ∣ε∣ and m₁/m₃ ∝ ∣ε∣³, the 15/2 and 7/2 classes stand "
   "(B1691's S248 note, RETRACTIONS); " + S + "];"),
  # 327 -- the comparison baseline is B1726's small-cut, seat's-menu figure
  ("the specificity is ∂R's, which passes", "the specificity is ∂R's [B1726's figure: the small-cut end at L_max's height "
   "and the seat's menu; under W138's widest menu 3.365%, and at the exact norms the six fail (B1726's row; " + S + ")], "
   "which passes"),
  # the scope of 'the canonical end', once, on B1667's row
  ("**THE CANONICAL CUSP: THE FIBRE'S GEOMETRY FIXES THE END RADIUS AT ORDER ONE (B1667; the fibre frame)**",
   "**THE CANONICAL CUSP: THE FIBRE'S GEOMETRY FIXES THE END RADIUS AT ORDER ONE (B1667; the fibre frame)** [scope of "
   "every later row's 'at the canonical end' (S297): the frame's machinery (b1656_funcs) takes the end through the "
   "small-cut channel norm 2πL + c_s at these heights; at L_max the exact twisted norms lie 35–38% below it, at L₂ 0.6% "
   "(S238, RETRACTIONS; FL-11; P-421); a result 'at the canonical end' is a result of that formula, and only the six's "
   "best rows have been re-read at the exact norms (they fail)]"),
 ],
 "docs/MAINS_PLAN.md": [
  ("and the comparison scale (M_Z, a choice; P-363) — a READING, ungraded |",
   "and the comparison scale (M_Z, a choice; P-363) — a READING, ungraded [and the end formula: at L_max the small-cut "
   "norm, not the horoball's exact norm; with the exact norms the six fail (S238; P-421; " + S + ")] |"),
 ],
}
for f, rs in edits.items():
    p = ROOT / f; t = p.read_text(encoding="utf-8")
    for old, new in rs:
        assert t.count(old) == 1, (f, t.count(old), old[:60])
        t = t.replace(old, new)
    p.write_text(t, encoding="utf-8")
print("second batch applied:", {f: len(r) for f, r in edits.items()})
