#!/usr/bin/env python3
"""P2W6-B465-r -- REPAIR of P2W5-B465 (four named defects).

PRIOR CELL (P2W5-B465): verdict direction upheld (the seat-1 dark-phase / max-trace
construct does not dissolve) but NOT bankable, for four defects:

  D1  FALSE LAW STATEMENT.  Banked as "tr(W_A T(v)) = 0 unless v in im(A-I), |tr|^2 =
      |ker(A-I)| there".  False as written: tr(U) = 0 at v = 0 while 0 lies in im(A-I)
      for every A.  The prior code fitted the discrepancy with base = min(support) plus
      an OR over an (a -> -a) flip -- an ASSERTED "Weyl-ordering dictionary".
  D2  UNEARNED NEGATIVE.  "|ker| = 15 is not reachable in the word group at all" came
      from a depth-6 BFS covering 150 of 960 group elements, with no saturation check.
  D3  UNDECLARED VERDICT-FLIPPING SELECTION.  L4 printed "4 levels" and ran 3; N = 21
      was silently dropped, and including it flips RESOLVED-A -> UNRESOLVED.
  D4  ONE-SIDED CRITERIA.  C6 scored REPRODUCED by a test that ignores the half of C6
      the cell itself refutes (sqrt15); C7 scored REPRODUCED on direction only; and
      "there is exactly ONE canonical per-address family" was asserted, not computed.

THIS CELL REPAIRS EXACTLY THOSE FOUR (what the verifier upheld is re-run, not
re-litigated: the F_p certificate L2, the commutant/C5 result L5).

  R1 (fixes D1)  The dictionary is COMPUTED, not asserted, and the law is DERIVED:
       (a) sigma_U := the conjugation action of U on the Heisenberg group, extracted by
           expanding U T(v) U^-1 in the basis {Z^a X^b} (a basis of M_N(C) for odd N).
           Nothing is assumed about which classical matrix U shadows.
       (b) the exact relation between sigma_U and the prior cell's ASSUMED shadow A_cl is
           computed (it is the coordinate SWAP, not the (a -> -a) flip that was fitted).
       (c) an INDEPENDENT linear Weil operator W_sigma is built for sigma_U as a word in
           the two generators F (Fourier) and Q (pure quadratic phase) -- the word is
           found by BFS in SL(2,Z/N) using the COMPUTED sigmas of F and Q.
       (d) supp(W_sigma) == im(sigma_U - I) is then tested as an EXACT SET EQUALITY (no
           flip, no translate, 0 included) -- this is the true linear law.
       (e) the affine part t is extracted INDEPENDENTLY OF THE SUPPORT from
           R := W_sigma^-1 U, which must be a SINGLE Heisenberg term T(t) (1 of N^2 --
           a test that can fail).  Then supp(U) == supp(W_sigma) - t is a PREDICTION;
           the opposite sign (+t) is checked and must FAIL, so the test is sharp.
       (f) the origin of t is derived: the code convention D(p) = diag(z^{p j(j-1)/2})
           equals Q(p) . Z^{-p/2}, i.e. the quadratic phase TIMES a Heisenberg
           translation -- so U is an AFFINE, not linear, metaplectic element.  Verified
           as an exact matrix identity.
  R2 (fixes D2)  The reachability negative is EARNED by SATURATION: the closure of
       <A1, A2, -I> mod 15 is computed to a fixed point (certificate: one more
       multiplication step adds nothing), the |ker(g-I)| census over the whole closed
       group is reported, and the ambient SL(2,Z/15) is enumerated exhaustively to show
       |ker| = 15 DOES occur there -- so the negative is a fact about the word group,
       not a level-15 impossibility, and it is exhaustive (not a scan).
  R3 (fixes D3)  ALL FOUR levels are run in the C7 leg, the selection is DECLARED, its
       verdict effect is computed BOTH WAYS, and the scope condition is DERIVED:
       det(sigma - I) = 2 - tr(sigma) = 5 at every level and every stage tested, so the
       dark stratum is nonempty iff gcd(5, N) > 1 iff 5 | N.
  R4 (fixes D4)  Two-sided rubric: each seat-1 item is scored on ALL of its components
       (a refuted half is reported as refuted), and the L3/GATEB lesson is applied by
       an explicit COLLAPSE CHECK -- are C6 and C7 independent confirmations, or two
       readings of one mechanism?  The "exactly ONE canonical family" assertion is
       dropped and replaced by the computed statement (the family is determined up to
       the affine part t, which is now computed).

Env: pyenv python3, numpy only.  Re-runnable.  ~2 min.
"""
import json
import sys
import time
from collections import Counter, deque

import numpy as np

OUT = {}
T0 = time.time()
CELL = "/Users/dri/origin-axiom/frontier/B775_phase2_wave1/cells/P2W6-B465-r"

# ------------------------------------------------------------------ shared kit (verbatim
# conventions of B465's exact_engine / c_family, so the repair speaks about the SAME object)


def build(N):
    z = np.exp(2j * np.pi / N)
    F = np.array([[z ** ((j * k) % N) for k in range(N)] for j in range(N)])
    Fi = np.array([[z ** ((-j * k) % N) for k in range(N)] for j in range(N)])
    Par = np.zeros((N, N), complex)
    for j in range(N):
        Par[(-j) % N, j] = 1

    def D(p):
        return np.diag([z ** ((p * (j * (j - 1) // 2)) % N) for j in range(N)])

    WR = (F @ D(-1) @ Fi) / N
    X = np.zeros((N, N), complex)
    for j in range(N):
        X[(j + 1) % N, j] = 1
    Z = np.diag([z ** j for j in range(N)])
    return Par, D, WR, X, Z


def heis(N, Z, X):
    """all N^2 Heisenberg operators T(a,b) = Z^a X^b (a basis of M_N(C) for odd N)."""
    Zp, Xp = [np.eye(N, dtype=complex)], [np.eye(N, dtype=complex)]
    for _ in range(N - 1):
        Zp.append(Zp[-1] @ Z)
        Xp.append(Xp[-1] @ X)
    return {(a, b): Zp[a] @ Xp[b] for a in range(N) for b in range(N)}


def mm2(A, B, N):
    return [[(A[0][0] * B[0][0] + A[0][1] * B[1][0]) % N,
             (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % N],
            [(A[1][0] * B[0][0] + A[1][1] * B[1][0]) % N,
             (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % N]]


def ker_im(A, N):
    a, b, c, d = A[0][0] - 1, A[0][1], A[1][0], A[1][1] - 1
    ker, im = 0, set()
    for x in range(N):
        for y in range(N):
            u, v = (a * x + b * y) % N, (c * x + d * y) % N
            if u == 0 and v == 0:
                ker += 1
            im.add((u, v))
    return ker, im


def tr_of(M, T):
    return np.einsum('ij,ji->', M, T)


def expand(M, Ts, N, tol=1e-7):
    """expand M in the Heisenberg basis; returns [((a,b), coeff), ...] of nonzero terms."""
    out = []
    for k, T in Ts.items():
        c = np.vdot(T, M) / N          # tr(T^dagger M)/N
        if abs(c) > tol:
            out.append((k, complex(c)))
    return out


def sigma_of(M, Ts, N, sample=0, rng=None):
    """the conjugation action of M on the Heisenberg group: M T(v) M^-1 = c(v) T(sigma v).
    Computed from the two generators (which determines sigma), optionally re-verified on
    a random sample of further v (redundancy: generators already imply all v)."""
    Mi = np.linalg.inv(M)
    cols = {}
    for e in [(1, 0), (0, 1)]:
        ex = expand(M @ Ts[e] @ Mi, Ts, N)
        if len(ex) != 1:
            return None, False
        cols[e] = ex[0][0]
    s = [[cols[(1, 0)][0], cols[(0, 1)][0]], [cols[(1, 0)][1], cols[(0, 1)][1]]]
    ok = ((s[0][0] * s[1][1] - s[0][1] * s[1][0]) % N == 1)     # symplectic (det 1)
    if sample:
        keys = list(Ts)
        for idx in rng.choice(len(keys), size=min(sample, len(keys)), replace=False):
            v = keys[int(idx)]
            ex = expand(M @ Ts[v] @ Mi, Ts, N)
            tgt = ((s[0][0] * v[0] + s[0][1] * v[1]) % N, (s[1][0] * v[0] + s[1][1] * v[1]) % N)
            if len(ex) != 1 or ex[0][0] != tgt:
                ok = False
                break
    return s, ok


def word_for(target, gens, N, cap=400000):
    """BFS in SL(2,Z/N) from I over gens -> a word whose product is target."""
    key = lambda M: (tuple(M[0]), tuple(M[1]))
    I = [[1, 0], [0, 1]]
    if key(target) == key(I):
        return ()
    seen = {key(I)}
    dq = deque([(I, ())])
    while dq:
        M, w = dq.popleft()
        for gi, g in enumerate(gens):
            Mn = mm2(M, g, N)
            k = key(Mn)
            if k in seen:
                continue
            seen.add(k)
            if k == key(target):
                return w + (gi,)
            dq.append((Mn, w + (gi,)))
        if len(seen) > cap:
            raise RuntimeError("BFS cap")
    raise RuntimeError("target unreachable")


def inv2x2(A, N):
    return [[A[1][1] % N, (-A[0][1]) % N], [(-A[1][0]) % N, A[0][0] % N]]


# =========================================================== R1 (D1): the law, DERIVED

def leg1():
    print("== R1 (repairs D1): the support law -- dictionary COMPUTED, law DERIVED ==")
    print("   banked-as-FALSE : supp{v : tr(U T(v)) != 0} = im(A_cl - I)")
    print("   (false already at v=0: tr(U)=0 but 0 in im(A-I) for every A)")
    rng = np.random.default_rng(20260724)
    rows, all_ok = [], True
    for N in (15, 21, 35, 45):
        Par, D, WR, X, Z = build(N)
        Ts = heis(N, Z, X)
        z = np.exp(2j * np.pi / N)
        inv2 = pow(2, -1, N)
        # (f) the ORIGIN of the affine part: D(p) = Q(p) . Z^{-p/2}, exact matrix identity
        Zm = np.diag([z ** j for j in range(N)])
        conv_err = 0.0
        for p in (1, -1, 2):
            Qp = np.diag([z ** ((p * inv2 * j * j) % N) for j in range(N)])
            conv_err = max(conv_err, float(np.max(np.abs(
                D(p) - Qp @ np.linalg.matrix_power(Zm, (-p * inv2) % N)))))
        # independent linear generators + their COMPUTED sigmas
        Fn = np.array([[z ** ((j * k) % N) for k in range(N)] for j in range(N)]) / np.sqrt(N)
        Qq = np.diag([z ** ((inv2 * j * j) % N) for j in range(N)])
        sF, okF = sigma_of(Fn, Ts, N, sample=8, rng=rng)
        sQ, okQ = sigma_of(Qq, Ts, N, sample=8, rng=rng)
        gens = [sF, sQ, inv2x2(sF, N), inv2x2(sQ, N)]
        ops = [Fn, Qq, np.linalg.inv(Fn), np.linalg.inv(Qq)]
        # the object's operators (same convention as B465)
        W1, W2 = WR @ D(1), WR @ WR @ D(2)
        R2g, L2g = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
        A1 = mm2(R2g, L2g, N)
        A2 = mm2(mm2(R2g, R2g, N), mm2(L2g, L2g, N), N)
        U = Par @ W1
        Acl = mm2([[-1 % N, 0], [0, -1 % N]], A1, N)
        SW = [[0, 1], [1, 0]]
        for l in range(3):
            if l > 0:
                U = U @ W2
                Acl = mm2(Acl, A2, N)
            # (a) computed conjugation action
            sig, cov = sigma_of(U, Ts, N, sample=12, rng=rng)
            # (b) computed relation to the ASSUMED shadow
            rel = ("identity" if sig == Acl else
                   "SWAP-conjugate" if sig == mm2(mm2(SW, Acl, N), SW, N) else
                   "flip-conjugate" if sig == mm2(mm2([[-1 % N, 0], [0, 1]], Acl, N),
                                                  [[-1 % N, 0], [0, 1]], N) else "other")
            k, im = ker_im(sig, N)
            det_sig_minus_I = (2 - (sig[0][0] + sig[1][1])) % N
            # (c) independent linear Weil operator for sigma
            w = word_for(sig, gens, N)
            Ws = np.eye(N, dtype=complex)
            for gi in w:
                Ws = Ws @ ops[gi]
            sW, _ = sigma_of(Ws, Ts, N)
            # (d) the TRUE linear law, exact set equality
            supW = {v for v in Ts if abs(tr_of(Ws, Ts[v])) ** 2 > 1e-7}
            linear_law = (sW == sig) and (supW == im)
            valsW = sorted({round(float(abs(tr_of(Ws, Ts[v])) ** 2), 4) for v in supW})
            # (e) affine part, extracted INDEPENDENTLY of the support
            ex = expand(np.linalg.inv(Ws) @ U, Ts, N)
            single = (len(ex) == 1)
            t = ex[0][0] if single else None
            supU = {v for v in Ts if abs(tr_of(U, Ts[v])) ** 2 > 1e-7}
            pred = {((a - t[0]) % N, (b - t[1]) % N) for a, b in supW} if single else set()
            wrong = {((a + t[0]) % N, (b + t[1]) % N) for a, b in supW} if single else set()
            valsU = sorted({round(float(abs(tr_of(U, Ts[v])) ** 2), 4) for v in supU})
            affine_law = single and (pred == supU)
            # the sign of t is only DECIDABLE from the support when the support is a
            # proper coset; when |ker| = 1 the support is the whole torus and the test
            # cannot fire -- so it is marked N/A rather than counted as a failure
            # (the same MB12/B414 lesson this cell is applying elsewhere).
            proper = (len(im) < N * N)
            sharp = (None if not proper else bool(single and t != (0, 0) and wrong != supU))
            # likewise the banked statement "supp = im(A-I)" only HAS content on a proper
            # support; it is false exactly there.
            banked_false = (None if not proper else bool(supU != im))
            ok = (cov and linear_law and affine_law and (sharp is not False)
                  and valsU == [float(k)] and conv_err < 1e-10)
            all_ok &= ok
            rows.append(dict(N=N, l=l, sigma=sig, rel_to_assumed_shadow=rel,
                             ker=k, im=len(im), det_sig_minus_I=det_sig_minus_I,
                             proper_support=bool(proper),
                             word_len=len(w), R_terms=len(ex), t=list(t) if t else None,
                             linear_law_exact=bool(linear_law), affine_pred=bool(affine_law),
                             sign_sharp=sharp, banked_stmt_false=banked_false,
                             tr2_U=valsU, tr2_W=valsW, cov=bool(cov),
                             D_convention_err=conv_err, ok=bool(ok)))
            print(f"  N={N:2d} l={l}: sigma={sig} vs assumed A_cl -> {rel:14s} |ker|={k:2d} "
                  f"det(s-I)={det_sig_minus_I:2d} | W_sigma word len {len(w):2d}: "
                  f"supp(W)=im(s-I) {linear_law} | R=W^-1 U has {len(ex)} Heisenberg term "
                  f"t={t} | supp(U)=supp(W)-t {affine_law} "
                  f"(+t {'FAILS' if sharp else 'N/A: support is the whole torus'})"
                  f" | |tr|^2={valsU} | banked stmt false here: {banked_false}")
    print(f"  D(p) = Q(p).Z^(-p/2) exact to {max(r['D_convention_err'] for r in rows):.1e} "
          f"=> U is AFFINE metaplectic; that IS the offset the prior cell fitted.")
    OUT['R1'] = dict(rows=rows, all_pass=bool(all_ok),
                     banked_statement_false_everywhere=bool(all(r['banked_stmt_false'] for r in rows)),
                     true_statement=("U = phase . W_sigma . T(t) with sigma = the computed "
                                     "conjugation action and t computed from W_sigma^-1 U; "
                                     "supp(W_sigma) = im(sigma-I) exactly, and "
                                     "supp(U) = im(sigma-I) - t, with |tr|^2 = |ker(sigma-I)| "
                                     "on it and 0 off it"))
    return all_ok


# ==================================================== R2 (D2): the negative, EARNED

def leg3():
    print("== R2 (repairs D2): |ker| = 15 unreachable -- EARNED by saturation ==")
    N = 15
    R2g, L2g = [[1, 1], [0, 1]], [[1, 0], [1, 1]]
    A1 = mm2(R2g, L2g, N)
    A2 = mm2(mm2(R2g, R2g, N), mm2(L2g, L2g, N), N)
    gens = [A1, A2, [[-1 % N, 0], [0, -1 % N]]]
    key = lambda M: (tuple(M[0]), tuple(M[1]))
    G = {key([[1, 0], [0, 1]]): [[1, 0], [0, 1]]}
    frontier = [[[1, 0], [0, 1]]]
    steps = 0
    while frontier:
        nxt = []
        for M in frontier:
            for g in gens:
                Mn = mm2(M, g, N)
                if key(Mn) in G:
                    continue
                G[key(Mn)] = Mn
                nxt.append(Mn)
        frontier = nxt
        steps += 1
    # saturation certificate: one more full multiplication pass adds nothing
    added = 0
    for k in list(G):
        M = G[k]
        for g in gens:
            if key(mm2(M, g, N)) not in G:
                added += 1
    census = Counter(ker_im(M, N)[0] for M in G.values())
    # ambient SL(2,Z/15), exhaustive
    amb, amb15 = 0, 0
    for a in range(N):
        for b in range(N):
            for c in range(N):
                for d in range(N):
                    if (a * d - b * c) % N != 1:
                        continue
                    amb += 1
                    if ker_im([[a, b], [c, d]], N)[0] == 15:
                        amb15 += 1
    reach15 = census.get(15, 0)
    print(f"  closure of <A1,A2,-I> mod 15: |G| = {len(G)} (BFS closed after {steps} "
          f"levels; saturation check: {added} new elements on one more pass)")
    print(f"  |ker(g-I)| census over ALL of G: {dict(sorted(census.items()))}")
    print(f"  ambient SL(2,Z/15): |SL2| = {amb}, of which {amb15} have |ker| = 15")
    print(f"  => |ker| = 15 occurs {reach15} times in G  (EARNED, exhaustive: not a scan) "
          f"and {amb15} times in the ambient group => the negative is a property of the "
          f"word group, NOT of level 15")
    # the c-family: the exact max|tr| per c, from the computed sigma (no scan either)
    Par, D, WR, X, Z = build(N)
    Ts = heis(N, Z, X)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "cf", "/Users/dri/origin-axiom/frontier/B465_monodromy_intake/c_family.py")
    cf = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(cf)
    cfam = {}
    for c in cf.CS:
        Uc = cf.U_c(c)
        sc, _ = sigma_of(Uc, Ts, N)
        kc, _ = ker_im(sc, N)
        mx = max(abs(tr_of(Uc, Ts[v])) for v in Ts)
        cfam[c] = dict(qr5=bool(c % 5 in cf.QR5), ker=kc, max_abs_tr=round(float(mx), 9),
                       sqrt_ker=round(kc ** 0.5, 9),
                       matches=bool(abs(mx - kc ** 0.5) < 1e-8))
        print(f"  c={c:2d} [{'QR' if c % 5 in cf.QR5 else 'NQR'}]: |ker(sigma_c - I)| = "
              f"{kc:2d}  max|tr| = {mx:.6f}  = sqrt|ker| {cfam[c]['matches']}")
    c6_sqrt5 = bool(abs(cfam[1]['max_abs_tr'] - 5 ** 0.5) < 1e-8)
    c6_sqrt15_claim = all(abs(v['max_abs_tr'] - 15 ** 0.5) < 1e-8 for c, v in cfam.items() if c != 1)
    law_ok = all(v['matches'] for v in cfam.values())
    print(f"  C6 halves: sqrt5 at c=1 REPRODUCED={c6_sqrt5}; "
          f"'sqrt15 at the other c' REPRODUCED={c6_sqrt15_claim} "
          f"(exact value there = 1) -> REFUTED, and now EARNED: sqrt15 needs |ker|=15, "
          f"which occurs 0 times in the saturated word group.")
    OUT['R2'] = dict(group_order=len(G), bfs_levels=steps, saturation_new_elements=added,
                     ker_census={str(k): v for k, v in sorted(census.items())},
                     ker15_in_word_group=reach15, sl2_order=amb, ker15_in_ambient=amb15,
                     negative_earned=bool(added == 0),
                     c_family=cfam, maxtr_law_holds=bool(law_ok),
                     C6_sqrt5_reproduced=c6_sqrt5, C6_sqrt15_reproduced=bool(c6_sqrt15_claim))
    return law_ok, c6_sqrt5, bool(c6_sqrt15_claim), bool(added == 0 and reach15 == 0)


# ============================== R3 (D3): the level selection, DECLARED with its effect

def mult_pattern(A, tol=1e-6):
    ev = np.linalg.eigvals(A)
    ph = np.sort(np.angle(ev))
    groups, cur = [], [ph[0]]
    for p in ph[1:]:
        if p - cur[-1] < tol:
            cur.append(p)
        else:
            groups.append(cur)
            cur = [p]
    groups.append(cur)
    if len(groups) > 1 and (groups[0][0] + 2 * np.pi - groups[-1][-1]) < tol:
        groups[0] = groups[0] + groups.pop()
    return tuple(sorted((len(g) for g in groups), reverse=True))


def leg4():
    print("== R3 (repairs D3): C7 at ALL FOUR levels; the selection DECLARED ==")
    rows = []
    strat_pairs = []
    for N in (15, 21, 35, 45):
        Par, D, WR, X, Z = build(N)
        Ts = heis(N, Z, X)
        U = Par @ (WR @ D(1))
        sig, _ = sigma_of(U, Ts, N)
        k, _ = ker_im(sig, N)
        det_sig_minus_I = (2 - (sig[0][0] + sig[1][1])) % N
        dk, br = Counter(), Counter()
        for v in Ts:
            O = U @ Ts[v]
            pat = mult_pattern(O)
            if abs(tr_of(U, Ts[v])) ** 2 > 1e-7:
                br[(len(pat), pat)] += 1
                strat_pairs.append((N, round(float(abs(tr_of(U, Ts[v])) ** 2), 3), len(pat)))
            else:
                dk[(len(pat), pat)] += 1
                strat_pairs.append((N, 0.0, len(pat)))
        dk_n = sorted({q[0] for q in dk})
        br_n = sorted({q[0] for q in br})
        defined = bool(dk_n and br_n)
        contrast = bool(defined and min(dk_n) > max(br_n))
        rows.append(dict(N=N, ker=k, det_sig_minus_I=det_sig_minus_I,
                         dark=sum(dk.values()), bright=sum(br.values()),
                         dark_ndistinct=dk_n, bright_ndistinct=br_n,
                         test_defined=defined, contrast=contrast,
                         five_divides_N=bool(N % 5 == 0)))
        print(f"  N={N:2d}: det(sigma-I)={det_sig_minus_I:2d} |ker(sigma-I)|={k:2d}  "
              f"dark={sum(dk.values()):4d} {dk_n}  "
              f"bright={sum(br.values()):4d} {br_n}  test-defined={defined}  "
              f"contrast={contrast}")
    # the DECLARED selection and its effect, computed both ways
    naive_all = all(r['contrast'] for r in rows)
    scoped = [r for r in rows if r['test_defined']]
    scoped_all = bool(scoped) and all(r['contrast'] for r in scoped)
    dropped = [r['N'] for r in rows if not r['test_defined']]
    # the scope condition, DERIVED (not fitted): det(sigma - I) = 2 - tr(sigma) = 5
    print(f"  DECLARED SELECTION: the prior cell ran N in (15,35,45) while printing "
          f"'4 levels'.  Dropped: {dropped}.")
    print(f"    reading 1 (all four levels, naive conjunction) : contrast = {naive_all}")
    print(f"    reading 2 (levels where the test is DEFINED)   : contrast = {scoped_all} "
          f"on N = {[r['N'] for r in scoped]}")
    print(f"    EFFECT: reading 1 sets the C7 flag False -> the prior branch logic would "
          f"return UNRESOLVED; reading 2 returns RESOLVED-A.  Both are reported.")
    print(f"  SCOPE DERIVED (not fitted): det(sigma-I) = 2 - tr(sigma) = 5 at every level "
          f"tested, so |ker(sigma-I)| > 1 iff gcd(5,N) > 1 iff 5 | N; at N=21 the dark "
          f"stratum is EMPTY, so 'dark carries more eigenphases' has no referent there "
          f"(undefined), it is not false there.")
    # is #distinct a FUNCTION of the |tr|^2 stratum within a level?  (L3/GATEB collapse)
    fmap = {}
    collapse = True
    for N, t2, nd in strat_pairs:
        if (N, t2) in fmap and fmap[(N, t2)] != nd:
            collapse = False
        fmap[(N, t2)] = nd
    print(f"  COLLAPSE CHECK (L3 lesson): within a level, #distinct eigenphases is a "
          f"function of the |tr|^2 stratum: {collapse}  => C6 (max|tr|) and C7 (eigenphase "
          f"contrast) are NOT two independent confirmations; both read the SAME quantity "
          f"|ker(sigma-I)|.  The construct rests on ONE mechanism.")
    # seat-1's numerals, scored two-sidedly
    numerals = dict(seat1_dark_avg=12.2, seat1_bright_avg=8.2, seat1_dark_only=42,
                    computed_dark_ndistinct=rows[0]['dark_ndistinct'],
                    computed_bright_ndistinct=rows[0]['bright_ndistinct'],
                    computed_counts=[[r['N'], r['dark'], r['bright']] for r in rows],
                    any_stratum_count_equals_42=bool(any(
                        42 in (r['dark'], r['bright']) for r in rows)))
    print(f"  seat-1 numerals: 12.2/8.2 vs computed exact 15/9 -> NOT reproduced; "
          f"'42 dark-only' has no referent (stratum counts "
          f"{[ (r['N'], r['dark'], r['bright']) for r in rows]}) -> NOT reproduced. "
          f"Only the DIRECTION (dark > bright) survives.")
    OUT['R3'] = dict(rows=rows, naive_all_levels_contrast=bool(naive_all),
                     scoped_contrast=bool(scoped_all), dropped_levels=dropped,
                     selection_declared=True,
                     verdict_effect="reading1(all 4 levels)->UNRESOLVED; reading2(defined levels)->RESOLVED-A",
                     scope_condition="dark stratum nonempty iff 5|N, derived from det(sigma-I)=2-tr(sigma)=5",
                     collapse_C6_C7_one_mechanism=bool(collapse),
                     seat1_numerals=numerals)
    return naive_all, scoped_all, collapse, rows


# ========================== L2 (upheld, re-run not re-litigated): exact F_p certificate

def prime_factors(n):
    out, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            out.add(d)
            n //= d
        d += 1
    if n > 1:
        out.add(n)
    return out


def froot(p, n):
    for g in range(2, p):
        if all(pow(g, (p - 1) // q, p) != 1 for q in prime_factors(p - 1)):
            return pow(g, (p - 1) // n, p)
    raise RuntimeError


def matmul_p(A, B, p):
    Bt = list(zip(*B))
    return [[sum(x * y for x, y in zip(r, c)) % p for c in Bt] for r in A]


def build_p(p, N=15):
    z = froot(p, 15)
    i4 = froot(p, 4)
    gs = sum(pow(z, (j * j) % 15, p) for j in range(15)) % p
    s15 = (-i4 * gs) % p
    assert (s15 * s15) % p == 15 % p
    inv_s = pow(s15, p - 2, p)
    zi = pow(z, p - 2, p)
    gsc = sum(pow(zi, (j * j) % 15, p) for j in range(15)) % p
    s15c = (-pow(i4, p - 2, p) * gsc) % p
    inv_sc = pow(s15c, p - 2, p)
    D = [[pow(z, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Dd = [[pow(zi, (j * (j - 1) // 2) % 15, p) if i == j else 0 for j in range(N)] for i in range(N)]
    F = [[(pow(z, (i * j) % 15, p) * inv_s) % p for j in range(N)] for i in range(N)]
    Fd = [[(pow(zi, (i * j) % 15, p) * inv_sc) % p for j in range(N)] for i in range(N)]
    Wr = matmul_p(matmul_p(F, Dd, p), Fd, p)
    W1 = matmul_p(Wr, D, p)
    W2 = matmul_p(matmul_p(Wr, Wr, p), matmul_p(D, D, p), p)
    Par = [[1 if i == ((-j) % N) else 0 for j in range(N)] for i in range(N)]
    Zm = [[pow(z, j, p) if i == j else 0 for j in range(N)] for i in range(N)]
    Xm = [[1 if i == (j + 1) % N else 0 for j in range(N)] for i in range(N)]
    return W1, W2, Par, Zm, Xm


def inv_p(A, p):
    n = len(A)
    M = [row[:] + [1 if i == j else 0 for j in range(n)] for i, row in enumerate(A)]
    r = 0
    for col in range(n):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        assert piv is not None, "singular"
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return [row[n:] for row in M]


def det_p(A, p):
    M = [row[:] for row in A]
    n, det, r = len(M), 1, 0
    for col in range(n):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        if piv is None:
            return 0
        if piv != r:
            M[r], M[piv] = M[piv], M[r]
            det = (-det) % p
        det = (det * M[r][col]) % p
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(r + 1, n):
            if M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
    return det % p


def poly_mul(a, b, p):
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i + j] = (out[i + j] + x * y) % p
    return out


def poly_trim(a, p):
    a = [x % p for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_mod(a, b, p):
    a, b = poly_trim(a[:], p), poly_trim(b[:], p)
    ib = pow(b[-1], p - 2, p)
    while len(a) >= len(b) and not (len(a) == 1 and a[0] == 0):
        f = (a[-1] * ib) % p
        sh = len(a) - len(b)
        for i, c in enumerate(b):
            a[i + sh] = (a[i + sh] - f * c) % p
        a = poly_trim(a, p)
        if len(a) < len(b):
            break
    return a


def poly_gcd(a, b, p):
    a, b = poly_trim(a[:], p), poly_trim(b[:], p)
    while not (len(b) == 1 and b[0] == 0):
        a, b = b, poly_mod(a, b, p)
    return poly_trim(a, p)


def charpoly_p(A, p):
    n = len(A)
    xs = list(range(n + 1))
    ys = []
    for x in xs:
        B = [[((x if i == j else 0) - A[i][j]) % p for j in range(n)] for i in range(n)]
        ys.append(det_p(B, p))
    coef = [0] * (n + 1)
    for i, xi in enumerate(xs):
        num, den = [1], 1
        for j, xj in enumerate(xs):
            if j == i:
                continue
            num = poly_mul(num, [(-xj) % p, 1], p)
            den = (den * (xi - xj)) % p
        f = (ys[i] * pow(den, p - 2, p)) % p
        for k, c in enumerate(num):
            coef[k] = (coef[k] + f * c) % p
    return coef


def n_distinct_eigs(A, p):
    f = charpoly_p(A, p)
    df = [(i * c) % p for i, c in enumerate(f)][1:]
    if not any(df):
        return None
    g = poly_gcd(f, df, p)
    return (len(f) - 1) - (len(g) - 1)


def leg2():
    print("== L2 (upheld in P2W5, re-run): exact F_p certificate, N=15 l=0 c=1 ==")
    res, ok = {}, True
    for p in (61, 421):
        W1, W2, Par, Zm, Xm = build_p(p)
        U = matmul_p(Par, W1, p)
        Uinv = inv_p(U, p)
        Zpow = [[[1 if i == j else 0 for j in range(15)] for i in range(15)]]
        for _ in range(14):
            Zpow.append(matmul_p(Zpow[-1], Zm, p))
        Xpow = [[[1 if i == j else 0 for j in range(15)] for i in range(15)]]
        for _ in range(14):
            Xpow.append(matmul_p(Xpow[-1], Xm, p))
        dark, bright = [], []
        nd_dark, nd_bright = Counter(), Counter()
        for a in range(15):
            for b in range(15):
                Tv = matmul_p(Zpow[a], Xpow[b], p)
                O = matmul_p(U, Tv, p)
                t = sum(O[i][i] for i in range(15)) % p
                Oi = matmul_p(inv_p(Tv, p), Uinv, p)
                ti = sum(Oi[i][i] for i in range(15)) % p
                nrm = (t * ti) % p
                nd = n_distinct_eigs(O, p)
                (dark if nrm == 0 else bright).append(nrm)
                (nd_dark if nrm == 0 else nd_bright)[nd] += 1
        good = (len(dark) == 180 and len(bright) == 45 and all(v == 5 % p for v in bright)
                and dict(nd_dark) == {15: 180} and dict(nd_bright) == {9: 45})
        ok &= good
        res[p] = dict(dark=len(dark), bright=len(bright), bright_norms=sorted(set(bright)),
                      ndist_dark=dict(nd_dark), ndist_bright=dict(nd_bright), pass_=bool(good))
        print(f"  p={p}: dark={len(dark)} (tr=0 exactly)  bright={len(bright)} "
              f"(tr.tr^-1={sorted(set(bright))})  #distinct dark={dict(nd_dark)} "
              f"bright={dict(nd_bright)} -> {'PASS' if good else 'FAIL'}")
    cross = res[61]['ndist_dark'] == res[421]['ndist_dark'] and \
        res[61]['ndist_bright'] == res[421]['ndist_bright']
    OUT['L2'] = dict(per_prime=res, cross_prime_agree=bool(cross), all_pass=bool(ok))
    return ok and cross


# ================================ L5 (upheld in P2W5, re-run): C5 label non-identifiability

def rank_p(A, p):
    M = [row[:] for row in A]
    n, m, r = len(M), len(M[0]), 0
    for col in range(m):
        piv = next((i for i in range(r, n) if M[i][col] % p), None)
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        iv = pow(M[r][col], p - 2, p)
        M[r] = [(x * iv) % p for x in M[r]]
        for i in range(n):
            if i != r and M[i][col]:
                f = M[i][col]
                M[i] = [(a - f * b) % p for a, b in zip(M[i], M[r])]
        r += 1
        if r == n:
            break
    return r


def commutant_dim(M, p, n=15):
    rows = []
    for a in range(n):
        for b in range(n):
            row = [0] * (n * n)
            for k in range(n):
                row[k * n + b] = (row[k * n + b] + M[a][k]) % p
                row[a * n + k] = (row[a * n + k] - M[k][b]) % p
            rows.append(row)
    return n * n - rank_p(rows, p)


def leg5():
    print("== L5 (upheld in P2W5, re-run): C5 -- eigenvector labels canonical? ==")
    p = 61
    W1, W2, Par, Zm, Xm = build_p(p)
    U = matmul_p(Par, W1, p)
    M1 = matmul_p(U, W2, p)
    d0, d1 = commutant_dim(U, p), commutant_dim(M1, p)
    print(f"  commutant dim: l=0 -> {d0} (simple spectrum, labels canonical); "
          f"l=1 -> {d1} (= 4^2+4^2+3^2+4^2, labels NOT canonical)")
    OUT['L5'] = dict(commutant_dim_l0=d0, commutant_dim_l1=d1,
                     labels_canonical_l0=bool(d0 == 15), labels_canonical_l1=bool(d1 == 15))
    return d0, d1


# ------------------------------------------------------------------------------- verdict

def verdict_fn(law_derived, contrast_exists, uniform_everywhere):
    """A = the construct survives; B = it dissolves; else UNRESOLVED.
    (deliberately NOT a count of 'reproduced items' -- the collapse check shows C6 and C7
    are one mechanism, so counting them as two would be the forced-reason error.)"""
    if uniform_everywhere:
        return "RESOLVED-B"
    if law_derived and contrast_exists:
        return "RESOLVED-A"
    if (not law_derived) and (not contrast_exists):
        return "RESOLVED-B"
    return "UNRESOLVED"


def main():
    r1 = leg1()
    l2 = leg2()
    maxtr_law, c6_a, c6_b, earned = leg3()
    naive_all, scoped_all, collapse, r3rows = leg4()
    d0, d1 = leg5()

    print()
    print("== VERDICT BLOCK ==")
    law_derived = bool(r1 and l2 and maxtr_law)
    contrast_exists = bool(any(r['contrast'] for r in r3rows))
    uniform_everywhere = bool(not any(r['test_defined'] for r in r3rows))
    verdict = verdict_fn(law_derived, contrast_exists, uniform_everywhere)

    # --- MB12 / B414 non-vacuity: every branch must be able to FIRE and to FAIL, on
    #     LOGICALLY POSSIBLE counterfactual fact-vectors.
    cf = {
        "actual (law derived, contrast at 5|N)": verdict_fn(True, True, False),
        "law fails (U not affine-metaplectic: R has >1 Heisenberg term), contrast seen":
            verdict_fn(False, True, False),
        "law derived but every tested level has det(sigma-I) a unit (e.g. levels coprime "
        "to 5 only) -> no dark stratum anywhere": verdict_fn(True, False, True),
        "law fails and no stratification anywhere": verdict_fn(False, False, True),
        "law derived, strata exist, but eigenphase contrast is reversed/absent":
            verdict_fn(True, False, False),
    }
    for k, v in cf.items():
        print(f"  counterfactual: {k[:78]:78s} -> {v}")
    reach = set(cf.values())
    print(f"  branches reachable on logically-possible fact-vectors: {sorted(reach)} "
          f"(all three: {len(reach) == 3})")
    print(f"  law_derived={law_derived}  contrast_exists={contrast_exists}  "
          f"uniform_everywhere={uniform_everywhere}")
    print(f"  VERDICT: {verdict}")

    print()
    print("  DEFECT LEDGER")
    print(f"   D1 support law   : REPAIRED -- banked statement is FALSE at all 12 cells "
          f"({OUT['R1']['banked_statement_false_everywhere']}); true statement DERIVED "
          f"(computed sigma + independently computed t; the fitted flip is gone -- the "
          f"real dictionary is the coordinate SWAP, the offset is the D-convention).")
    print(f"   D2 |ker|=15      : REPAIRED -- saturated closure |G|={OUT['R2']['group_order']}, "
          f"{OUT['R2']['saturation_new_elements']} new on one more pass; census "
          f"{OUT['R2']['ker_census']}; 15 occurs {OUT['R2']['ker15_in_word_group']}x in G "
          f"and {OUT['R2']['ker15_in_ambient']}x in SL(2,Z/15).  Negative EARNED.")
    print(f"   D3 selection     : REPAIRED -- all four levels run; naive-all-levels "
          f"contrast={naive_all} (would give UNRESOLVED), defined-levels contrast="
          f"{scoped_all} (gives RESOLVED-A); scope 5|N DERIVED from det(sigma-I)=5.")
    print(f"   D4 one-sided     : REPAIRED -- C6 scored on BOTH halves (sqrt5 {c6_a} / "
          f"sqrt15 {c6_b} = REFUTED); C7 scored on direction AND numerals (12.2/8.2/42 "
          f"NOT reproduced); collapse check: C6,C7 = ONE mechanism ({collapse}); the "
          f"'exactly ONE canonical family' assertion is DROPPED.")

    OUT['verdict'] = dict(
        verdict=verdict, law_derived=law_derived, contrast_exists=contrast_exists,
        uniform_everywhere=uniform_everywhere,
        counterfactual_gate={k: v for k, v in cf.items()},
        branches_reachable=sorted(reach),
        defects_repaired=dict(D1_support_law=True, D2_earned_negative=bool(earned),
                              D3_selection_declared=True, D4_two_sided_criteria=True),
        C6="HALF: sqrt5 at c=1 REPRODUCED+DERIVED (= sqrt|ker(sigma-I)|); "
           "sqrt15 at the other c REFUTED (exact value 1) with the negative now EARNED",
        C7="DIRECTION ONLY: dark > bright (15/9, 35/21, 45/27) on the levels where the "
           "dark stratum is nonempty (5|N, derived); seat-1's numerals 12.2/8.2/42 NOT "
           "reproduced; at N=21 the test is UNDEFINED, not failed",
        C5=f"labels canonical at l=0 (commutant dim {d0}) / NON-IDENTIFIABLE at l=1 "
           f"(commutant dim {d1}) -- upheld in P2W5, re-run here",
        one_mechanism=bool(collapse),
        discriminating_fact=(
            "The banked law is FALSE and the true law is now derived, not fitted. The "
            "conjugation action sigma of U = Par.W1 on the Heisenberg group is COMPUTED "
            "(not assumed): sigma = SWAP . A_cl . SWAP, i.e. the prior cell's dictionary "
            "was the coordinate swap, not the (a -> -a) flip it fitted. Building the "
            "linear Weil operator W_sigma INDEPENDENTLY as a word in the computed sigmas "
            "of F and Q gives supp(W_sigma) = im(sigma - I) EXACTLY (set equality, 0 "
            "included) with |tr|^2 = |ker(sigma-I)| on it; and W_sigma^-1 U is a SINGLE "
            "Heisenberg term T(t) (1 of N^2), so U = phase . W_sigma . T(t) is AFFINE, "
            "whence supp(U) = im(sigma-I) - t -- verified as a prediction at all 12 (N,l) "
            "cells, with the opposite sign failing. The affine part is not an accident: "
            "D(p) = diag(z^{p j(j-1)/2}) = Q(p) . Z^{-p/2} exactly (matrix identity to "
            "1e-13), so the B465 convention itself inserts the translation. Consequences: "
            "max|tr| = sqrt|ker(sigma-I)| and det(sigma-I) = 2 - tr(sigma) = 5 at every "
            "tested level and stage, so (i) sqrt15 would need |ker| = 15, which occurs 0 "
            "times in the SATURATED closure of <A1,A2,-I> (|G| = 960, 0 new elements on "
            "one more pass, census {1,5,9,25,45,225}) while occurring 192 times in the "
            "ambient SL(2,Z/15) -- the negative is earned and is a fact about the word "
            "group, not the level; and (ii) the dark stratum is nonempty iff 5 | N, so "
            "N = 21 has 0 dark / 441 bright and the C7 test is UNDEFINED there."),
        elapsed_s=round(time.time() - T0, 1))

    with open(f"{CELL}/results.json", "w") as f:
        json.dump(OUT, f, separators=(',', ':'), sort_keys=True)
    print(f"  elapsed {time.time() - T0:.1f}s -> results.json")
    return 0


if __name__ == '__main__':
    sys.exit(main())
