"""B1384 S5 -- the M6 physical gate re-derived with this branch's own code (the web seats' m6_physical_gate report, sections 2 and 4,
read for insight only).  Tools, all this branch's:
B1384's Reidemeister-Schreier cover of m004 (deck = conjugation by a; M6 -> M2 has deck group <a^2>), B1374's index library over GF(p),
B1375's generation-shaped selection (five charged sectors firing with one sign).

For each generation-shaped background found (chi, psi_Y, psi_gamma) and each charged sector s (psi_s = psi_Y^sy psi_gamma^sg):
  V = rho_chi (x) psi_s, its deck translates V o sigma^(2a), a = 0, 1, 2; the six diagonal characters L_{a,+-} = (chi^{+-1} psi_s) o sigma^(2a).
  (0) the three translates are distinct and carry the same index;
  (1) the six diagonal characters are trivial on the cusp (mu, lambda);
  (2) every ordered pair i != j: the character L_i / L_j has h^1 = 1 and restriction rank r_1 = 1 to the cusp torus (interior 0);
  (3) the upper (chi^2) and lower (chi^-2) extension cocycles: their values on mu and lambda, and the product on lambda (non-zero means a
      rank-2 deformation turning on both moves the longitude's eigenvalues off 1 at first order, so the cusp-fixed vector is lost).
Everything over three primes p = 1 mod 120."""
import importlib.util, time
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[3]


def load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


HC = load("b1384_handoff_checks", "frontier/B1384_the_generated_state_space/verification/handoff_checks.py")
IL = HC.IL
SECTORS = [("Q", 1, 3), ("u^c", -4, 3), ("e^c", 6, 3), ("d^c", 2, 1), ("L", -3, 1), ("nu^c", 0, -5)]
N = 120


def build(p):
    F = IL.GF(p)
    z = F.root_of_unity(N)
    gens, words, rewrite, rels, mu, lam = HC.rs_cover(6)
    return F, z, gens, words, rewrite, rels, mu, lam


def deck_images(gens, words, rewrite, k):
    """sigma^k(g) = a^k g a^-k rewritten in the cover's generators (from coset 0)"""
    out = {}
    for g in gens:
        w, kk = rewrite("a" * k + words[g] + "A" * k, 0)
        assert kk == 0
        out[g] = w
    return out


def ab(word, gens):
    return IL.abelian_exponents(word, gens)


def compose(chi, images, gens):
    """(chi o sigma^k)(g) = chi(sigma^k(g)), exponents mod N"""
    return {g: sum(e * chi[h] for h, e in ab(images[g], gens).items()) % N for g in gens}


def mul(a, b, gens, s=1):
    return {g: (a[g] + s * b[g]) % N for g in gens}


def power(a, k, gens):
    return {g: (k * a[g]) % N for g in gens}


def on(chi, word, gens):
    return sum(e * chi[h] for h, e in ab(word, gens).items()) % N


def run(p, per_locus=2, want_loci=2, max_loci=60):
    F, z, gens, words, rewrite, rels, mu, lam = build(p)
    chars = HC.characters_via_smith(gens, rels, N)
    assert len(chars) == 38400, len(chars)
    key = lambda c: tuple(c[g] for g in gens)
    pindex = {key(c): i for i, c in enumerate(chars)}
    sig2 = deck_images(gens, words, rewrite, 2)
    sig4 = deck_images(gens, words, rewrite, 4)
    # the non-split loci: chi != 1 with h^1(chi^2) >= 1
    loci = []
    for chi in chars:
        if not any(chi.values()):
            continue
        sq = {g: pow(z, 2 * chi[g], p) for g in gens}
        h1, ct = IL.h1_and_cocycle(F, gens, rels, mu, lam, sq)
        if ct is not None:
            loci.append((chi, h1, ct))
    # the T5 grouping of characters by their cusp values
    by_cusp = {}
    for i, psi in enumerate(chars):
        by_cusp.setdefault((on(psi, mu, gens), on(psi, lam, gens)), []).append(i)
    fifth = {}
    for i, psi in enumerate(chars):
        fifth.setdefault(key(power(psi, 5, gens)), []).append(i)
    cache = {}

    def rep_of(chi, ct, psi):
        cv = {g: pow(z, chi[g], p) for g in gens}
        rho = IL.reducible_rep(F, gens, cv, ct)
        pv = {g: pow(z, psi[g], p) for g in gens}
        return IL.Rep(F, gens, IL.module(F, gens, rho, 1, pv))

    def I_of(li, psi):
        k = (li, key(psi))
        if k not in cache:
            chi, h1, ct = loci[li]
            V = rep_of(chi, ct, psi)
            assert V.check_relators(rels)
            cache[k] = IL.index(V, rels, mu, lam)[0]
        return cache[k]

    found = []
    loci_done = 0
    for li, (chi, h1, ct) in enumerate(loci[:max_loci]):
        km, kl = on(chi, mu, gens), on(chi, lam, gens)
        cand = sorted(set(by_cusp.get(((-km) % N, (-kl) % N), []) + by_cusp.get((km, kl), [])))
        fire = {}
        for i in cand:
            I = I_of(li, chars[i])
            if I != 0:
                fire[i] = I
        here = 0
        for iu, Iu in fire.items():
            if here >= per_locus:
                break
            for iv, Iv in fire.items():
                if here >= per_locus:
                    break
                if Iu != Iv:
                    continue
                w = mul(chars[iu], chars[iv], gens, -1)
                for iy in fifth.get(key(w), []):
                    pY = chars[iy]
                    pG = mul(chars[iu], power(pY, -2, gens), gens)
                    c = [I_of(li, mul(power(pY, sy, gens), power(pG, sg, gens), gens)) for (_, sy, sg) in SECTORS]
                    if c[0] == c[1] == c[2] == c[3] == c[4] != 0:
                        found.append((li, pY, pG, c))
                        here += 1
                        break
        if here:
            loci_done += 1
        if loci_done >= want_loci:
            break
    # the checks on each background found
    rows = []
    for (li, pY, pG, c) in found:
        chi, h1, ct = loci[li]
        # the lower extension: chi^-2 cocycle
        sqm = {g: pow(z, (-2 * chi[g]) % N, p) for g in gens}
        h1m, ctm = IL.h1_and_cocycle(F, gens, rels, mu, lam, sqm)
        up_mu = sum(IL.Rep(F, gens, {g: [[pow(z, 2 * chi[g] % N, p)]] for g in gens}).fox(mu)[g][0][0] * ct[g] for g in gens) % p
        up_lam = sum(IL.Rep(F, gens, {g: [[pow(z, 2 * chi[g] % N, p)]] for g in gens}).fox(lam)[g][0][0] * ct[g] for g in gens) % p
        lo_mu = sum(IL.Rep(F, gens, {g: [[sqm[g]]] for g in gens}).fox(mu)[g][0][0] * ctm[g] for g in gens) % p if ctm else None
        lo_lam = sum(IL.Rep(F, gens, {g: [[sqm[g]]] for g in gens}).fox(lam)[g][0][0] * ctm[g] for g in gens) % p if ctm else None
        chi_cusp = (on(chi, mu, gens), on(chi, lam, gens))
        for (lab, sy, sg), Isec in zip(SECTORS, c):
            if lab == "nu^c":
                continue
            ps = mul(power(pY, sy, gens), power(pG, sg, gens), gens)
            L0p, L0m = mul(chi, ps, gens), mul(power(chi, -1, gens), ps, gens)
            Ls = [L0p, L0m, compose(L0p, sig2, gens), compose(L0m, sig2, gens), compose(L0p, sig4, gens), compose(L0m, sig4, gens)]
            cusp_trivial = all(on(L, mu, gens) == 0 and on(L, lam, gens) == 0 for L in Ls)
            distinct_blocks = len({(key(Ls[2 * a]), key(Ls[2 * a + 1])) for a in range(3)}) == 3
            # the deck translates' indices: V o sigma^(2a) is rho_{chi o s} (x) psi o s with the pulled-back cocycle
            idx = []
            base = rep_of(chi, ct, ps)
            for s_img in (None, sig2, sig4):
                # the deck translate V o sigma^k: g -> V(sigma^k(g)), a representation since Gamma6 is normal in pi_1(m004)
                V = base if s_img is None else IL.Rep(F, gens, {g: base.word(s_img[g]) for g in gens})
                assert V.check_relators(rels)
                idx.append(IL.index(V, rels, mu, lam)[0])
            arrows = Counter()
            for i in range(6):
                for j in range(6):
                    if i == j:
                        continue
                    q = mul(Ls[i], Ls[j], gens, -1)
                    if not any(q.values()):
                        arrows["trivial"] += 1
                        continue
                    R = IL.Rep(F, gens, {g: [[pow(z, q[g], p)]] for g in gens})
                    a0, a1, t0, t1, r1 = IL.cohomology_data(R, rels, mu, lam)
                    arrows[(a1, r1, a1 - r1)] += 1
            rows.append(dict(p=p, locus=li, chi_on_cusp=chi_cusp, sector=lab, I=Isec, deck_indices=idx, distinct_blocks=distinct_blocks,
                             six_cusp_trivial=cusp_trivial, arrows={str(k): v for k, v in arrows.items()},
                             upper=(up_mu, up_lam), lower=(lo_mu, lo_lam), lam_product=(up_lam * lo_lam % p) if ctm else None,
                             h1_chi2=h1, h1_chim2=h1m))
    return dict(p=p, chars=len(chars), loci=len(loci), backgrounds=[(li, key(pY), key(pG), c) for (li, pY, pG, c) in found], rows=rows)


if __name__ == "__main__":
    out = {}
    for p in (601, 1201, 1321):
        t0 = time.time()
        r = run(p)
        out[p] = r
        print("p = %d: %d characters, %d non-split loci, %d generation-shaped backgrounds found: %s (%.0f s)"
              % (p, r["chars"], r["loci"], len(r["backgrounds"]), r["backgrounds"], time.time() - t0), flush=True)
        for row in r["rows"]:
            print("   ", row, flush=True)
        print("DONE")
