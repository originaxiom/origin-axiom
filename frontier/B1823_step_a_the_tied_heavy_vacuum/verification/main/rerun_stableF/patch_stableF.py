"""Main's rerun of Step A v2's section D with a cancellation-free F (the referee's N2) and deep-cusp starts, on copies
of the draft's code.  Every edit is an exact, asserted replacement; the draft itself is not touched."""
import pathlib
H = pathlib.Path(__file__).resolve().parent
def sub(fn, a, b):
    p = H / fn; s = p.read_text(); assert s.count(a) == 1, (fn, a[:60], s.count(a)); p.write_text(s.replace(a, b))
# 1. numpy F: the same function, written without the cancellation for u > m0^2
sub("model.py",
    "    return (u + m02) ** 2 * (np.log((u + m02) / mu2) - 1.5) - u ** 2 * (np.log(u / mu2) - 1.5)\n",
    "    if u > m02:   # main's rerun: (2u m + m^2)(log(u/mu2) - 3/2) + (u + m)^2 log1p(m/u), algebraically identical\n"
    "        return (2 * u * m02 + m02 ** 2) * (np.log(u / mu2) - 1.5) + (u + m02) ** 2 * np.log1p(m02 / u)\n"
    "    return (u + m02) ** 2 * (np.log((u + m02) / mu2) - 1.5) - u ** 2 * (np.log(u / mu2) - 1.5)\n")
# 2. mpmath F: the same rewrite (34 digits already resolve u <~ 1e20; this removes the limit)
sub("model.py",
    "    return (u + m02) ** 2 * (mp.log((u + m02) / mu2) - mp.mpf(3) / 2) - u ** 2 * (mp.log(u / mu2) - mp.mpf(3) / 2)\n",
    "    if u > m02:\n"
    "        return (2 * u * m02 + m02 ** 2) * (mp.log(u / mu2) - mp.mpf(3) / 2) + (u + m02) ** 2 * mp.log1p(m02 / u)\n"
    "    return (u + m02) ** 2 * (mp.log((u + m02) / mu2) - mp.mpf(3) / 2) - u ** 2 * (mp.log(u / mu2) - mp.mpf(3) / 2)\n")
# 3. the starts: the draft's 24 (same rng, so the same points), then 24 deep in the cusp (Im tau in [3.5, 16]) from a
#    separate rng, so the first 24 are reproduced exactly
sub("step_a_v2.py",
    "    for _ in range(nstart):\n        x = rng.uniform(-0.5, 0.5); y = rng.uniform(np.sqrt(1 - x * x), 3.5)\n        S = rng.normal(size=3) + 1j * rng.normal(size=3)\n",
    "    rng2 = np.random.default_rng(seed + 100000)\n"
    "    for k in range(2 * nstart):\n"
    "        g = rng if k < nstart else rng2\n"
    "        x = g.uniform(-0.5, 0.5); y = g.uniform(np.sqrt(1 - x * x), 3.5) if k < nstart else g.uniform(3.5, 16.0)\n"
    "        S = g.normal(size=3) + 1j * g.normal(size=3)\n")
# 4. an mpmath arbiter between the lowest interior and the lowest cusp point (Im tau > 6), whenever both exist
sub("step_a_v2.py",
    "    interior = [c for c in clusters if c[\"tau\"].imag <= 6]\n    cuspy = [c for c in clusters if c[\"tau\"].imag > 6]\n",
    "    interior = [c for c in clusters if c[\"tau\"].imag <= 6]\n    cuspy = [c for c in clusters if c[\"tau\"].imag > 6]\n"
    "    if interior and cuspy:\n"
    "        from model import mp_V\n"
    "        cps = model.copies\n"
    "        vi = mp_V(cps, mp.mpc(interior[0][\"tau\"]), [mp.mpc(z) for z in interior[0][\"S\"]], mp.mpf(mu2), mp.mpf(m02), 1, mp.mpf(lv))\n"
    "        vc = mp_V(cps, mp.mpc(cuspy[0][\"tau\"]), [mp.mpc(z) for z in cuspy[0][\"S\"]], mp.mpf(mu2), mp.mpf(m02), 1, mp.mpf(lv))\n"
    "        res_arb = dict(interior_numpy=interior[0][\"V\"], interior_mp=float(vi), cusp_numpy=cuspy[0][\"V\"], cusp_mp=float(vc),\n"
    "                       cusp_tau=[cuspy[0][\"tau\"].real, cuspy[0][\"tau\"].imag], cusp_lower_mp=bool(vc < vi))\n"
    "    else:\n"
    "        res_arb = None\n")
sub("step_a_v2.py",
    "    res[\"seconds\"] = round(time.time() - t0, 1)\n    return res\n",
    "    res[\"arbiter\"] = res_arb\n    res[\"seconds\"] = round(time.time() - t0, 1)\n    return res\n")
print("patched")
