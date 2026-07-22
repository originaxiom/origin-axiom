"""B755 cell 1 -- the genus-2 mirror CS-flip witness (B140's NOT-LOCATED fact).

Build a chiral hyperbolic genus-2 surface bundle via snappy.twister, take its
mirror, verify: equal volume, opposite Chern-Simons, non-isometric (chiral).
Deterministic; monodromy words fixed below.
"""
import snappy
from snappy import twister

CANDIDATE_WORDS = ["abcDef", "aBcDeF", "abcDe", "abcdEf", "aabcDef", "abCdeF", "abcDDf", "abcdef"]


def build(word):
    surf = twister.Surface("S_2_1")
    return surf.bundle(word)


def mirror_of(M):
    Mm = M.copy()
    Mm.reverse_orientation()
    return Mm


def main():
    for word in CANDIDATE_WORDS:
        try:
            M = build(word)
        except Exception as exc:
            print(f"[{word}] build failed: {exc}")
            continue
        try:
            M = M.high_precision()
            vol = M.volume()
            if float(vol) < 0.9:
                print(f"[{word}] not hyperbolic enough (vol {vol}); skip")
                continue
            sol = M.solution_type()
            if "positively oriented" not in sol:
                print(f"[{word}] solution_type {sol}; skip")
                continue
            cs = M.chern_simons()
        except Exception as exc:
            print(f"[{word}] geometry failed: {exc}")
            continue
        Mm = mirror_of(M)
        volm = Mm.volume()
        csm = Mm.chern_simons()
        # chirality route 1: CS obstruction -- an orientation-preserving isometry
        # M ~ mirror forces 2*CS = 0 mod 1/2 (snappy's cusped CS is defined mod 1/2)
        twocs = 2 * float(cs)
        d = min(abs(twocs - 0.5 * k) for k in range(-8, 9))
        cs_chiral = d > 1e-9
        # chirality route 2: inspect the isometries' orientation (cusp-map dets)
        iso_chiral = None
        try:
            isos = M.is_isometric_to(Mm, return_isometries=True)
            det2 = lambda m: m[0, 0] * m[1, 1] - m[0, 1] * m[1, 0]
            iso_chiral = not any(all(det2(m) == 1 for m in iso.cusp_maps())
                                 for iso in isos)
        except Exception as exc:
            iso_chiral = f"undecided ({str(exc)[:40]})"
        chiral = cs_chiral
        print(f"[{word}] chirality: CS-route (2CS = {twocs:+.5f}, dist to (1/2)Z = {d:.5f}) "
              f"=> chiral {cs_chiral}; isometry-orientation route => {iso_chiral}")
        print(f"[{word}] vol = {vol}  mirror vol = {volm}  |dv| = {abs(float(vol)-float(volm)):.2e}")
        print(f"[{word}] CS  = {cs}  mirror CS = {csm}  CS+CSm = {float(cs)+float(csm):+.2e}")
        vol_ok = abs(float(vol) - float(volm)) < 1e-9
        cs_ok = abs(float(cs) + float(csm)) < 1e-9
        if vol_ok and cs_ok and chiral:
            print(f"CHECK: WITNESSED -- genus-2 chiral bundle '{word}': vol equal, CS opposite, non-isometric mirror")
            return
        if vol_ok and cs_ok and chiral is None:
            print(f"[{word}] vol/CS pattern holds but chirality undecided; trying next word")
    print("CHECK: NO WITNESS FOUND in the candidate list -- report as such")


main()
