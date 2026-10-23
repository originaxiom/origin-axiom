ROOT = pathlib.Path(__file__).resolve().parents[3]
def _git(path):
    return subprocess.run(["git", "show", f"3412bf09d:{path}"], cwd=ROOT, capture_output=True, check=True).stdout
_bd = _git("frontier/B1637_fits_on_the_ruled_branch/received/HZ2021_running_masses_MZ.json")
_bc = _git("frontier/B1612_the_mixing_patterns_the_weave_fixes/verification/data.json")
_m = json.loads(_bd)["masses_GeV"]; _v, _s = _m["value"], _m["sigma"]; _ck = json.loads(_bc)["ckm_abs"]; _C, _CS = _ck["value"], _ck["sigma"]
_PAIRS = [("c", "t"), ("u", "t"), ("s", "b"), ("d", "b"), ("mu", "tau"), ("e", "tau")]
T6 = np.log(np.array([_v[a] / _v[b] for a, b in _PAIRS]))
T9 = np.concatenate([T6, np.log(np.array([_C[0][1], _C[1][2], _C[0][2]]))])
REL = np.array([math.hypot(_s[a] / _v[a], _s[b] / _v[b]) for a, b in _PAIRS] + [_CS[0][1] / _C[0][1], _CS[1][2] / _C[1][2], _CS[0][2] / _C[0][2]])
SIG = np.sqrt(REL ** 2 + 0.10 ** 2)
JPDG = 3.08e-5
def nine_of(M, hor, hu, hd, c=3.0):
    Yu = B.coupling(rbs.S_of(hu), M[("up", hor)]); Yd = B.coupling(rbs.S_of(hd), M[("down", hor)]); Ye = B.coupling(rbs.S_of(hd), M[("lep", hor)])
    L = []
    for Y in (Yu, Yd, Ye):
        sv = np.linalg.svd(Y, compute_uv=False); L += [math.log(sv[1] / sv[0]), math.log(sv[2] / sv[0])]
    L[4] += math.log(c); L[5] -= math.log(c)
    ck = tic.ckm_left(Yu, Yd)
    L9 = np.array(L + [math.log(max(x, 1e-300)) for x in ck[:3]])
    chi6 = float(np.sum(((L9[:6] - T6) / SIG[:6]) ** 2)); chi9 = float(np.sum(((L9 - T9) / SIG) ** 2))
    D = math.exp((L[4] - L[2]) + (L[3] - L[5]))
    return {"chi2_six": round(chi6, 2), "chi2_nine": round(chi9, 2), "model/data": [round(x, 3) for x in np.exp(L9 - T9)], "J": ck[3], "D": round(D, 3)}
