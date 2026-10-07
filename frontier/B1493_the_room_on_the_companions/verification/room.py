#!/usr/bin/env python3
"""B1493 -- Theorem C's two supplies and the extension by the line, on B1492's multi-cusp instrument.

For a character nu (values on SnapPy's generators, roots of unity as mpc):
  the LINE chi = nu^4 (b0 = [chi = 1]); its room n(chi) = h^1(N; chi) - rank(restriction to the cusps where chi is trivial);
  the second supply n(nu^3 (x) rho) with rho the SL(2,C) lift (its own interior classes, every cusp stacked);
  the extension W1 = [[V, z], [0, L]] with V = nu (x) four, L = nu^-4, z(g) = c(g) L(g) for a cocycle c of V (x) L*
  (so that W1(gh) = W1(g) W1(h)); I(W1), I(Lambda^2 W1) by the stacked restriction block, with the cusp decomposition.
Controls: at a sign character L = 1 and every number must equal B1492's survey row."""
import sys, json, itertools, pathlib
HERE = pathlib.Path(__file__).resolve().parent
from mpmath import mp, mpf, mpc, matrix, eye, zeros, inverse, exp, pi
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2] / "B1492_the_three_ended_companion_read" / "verification"))
import multicusp as MC          # B1492's sealed instrument, imported from its arc
mp.dps = 40


def zeta(k, n=8): return exp(2j * pi * k / n)


class Room(MC.Site):
    def line(self, chi):           # the rank-one module chi
        return {g: matrix([[chi[g]]]) for g in self.gens}

    def room(self, chi):
        """n(chi) = interior classes of the line: h^1 minus the rank of the restriction to the cusps (stacked block)"""
        E = self.line(chi); c = self.counts(E); return dict(h1=c["a1"], n=c["n"], t0=c["t0"])

    def two(self, nu, power=3):
        """nu^power (x) rho, with rho = the FOUR (the seat's rho_1: Ballas' rho_q at q = 1, signature (3, 1)) -- Theorem C's second
        supply n(nu^3 (x) rho) is the interior-class count of the four twisted by nu^3.  (Corrected after the sealed run, 2026-10-07:
        the sealed code used the SL(2, C) lift here, a different module; the m136 control had shown it -- 0 at members reading
        (-1, -1), which the theorem's bound I(Lambda^2 W1) >= -n(nu^3 (x) rho) forbids -- and it was read only after C3.  The
        sealed outputs are kept in sealed_run/.)"""
        four = self.four({g: 1 for g in self.gens})
        return {g: (nu[g] ** power) * four[g] for g in self.gens}

    def extension_by_line(self, V, L, c):
        """W1 = [[V, z], [0, L]], z(g) = c(g) L(g); c a cocycle of V (x) L* (column vector per generator)"""
        n = next(iter(V.values())).rows; out = {}
        for k, g in enumerate(self.gens):
            W = zeros(n + 1); W[:n, :n] = V[g]
            for i in range(n): W[i, n] = c[k * n + i] * L[g][0, 0]
            W[n, n] = L[g][0, 0]; out[g] = W
        return out

    def read(self, nu):
        """one character: the two supplies, then every class of H^1(V (x) L*) read in W1 and Lambda^2 W1 with its cusp decomposition"""
        chi = {g: nu[g] ** 4 for g in self.gens}; Linv = {g: 1 / chi[g] for g in self.gens}     # L = nu^-4, L* = nu^4 = chi
        b0 = int(all(abs(chi[g] - 1) < MC.TOL for g in self.gens))
        row = dict(nu={g: str(nu[g]) for g in self.gens}, b0=b0, room=self.room(chi), second=self.counts(self.two(nu))["n"],
                   cap_W=b0 + self.room(chi)["n"], readings=[])
        V = self.four(nu); L = {g: matrix([[Linv[g]]]) for g in self.gens}; Lstar = {g: matrix([[chi[g]]]) for g in self.gens}
        VL = {g: V[g] * chi[g] for g in self.gens}                      # V (x) L* (rank 4)
        cusp_triv = []
        for (mu, lam) in self.cusps:
            vm = 1
            for ch in mu: vm *= (nu[ch.lower()] if ch.islower() else 1 / nu[ch.lower()])
            vl = 1
            for ch in lam: vl *= (nu[ch.lower()] if ch.islower() else 1 / nu[ch.lower()])
            cusp_triv.append(bool(abs(vm - 1) < MC.TOL and abs(vl - 1) < MC.TOL))
        row["cusp_trivial"] = cusp_triv; row["m_A"] = sum(cusp_triv)
        interior, other = self.classes(VL); row["interior"] = len(interior); row["other"] = len(other)
        for label, group in (("interior", interior), ("other", other)):
            for idx, (z, dead) in enumerate(group):
                W = self.extension_by_line(V, L, z); L2 = {g: MC.ext2(W[g]) for g in self.gens}
                # the relator check: W1 must be a representation
                relok = all(max(abs(x) for x in (MC.word(r, W) - eye(5))) < 1e-20 for r in self.rels)
                a, b = self.index(W), self.index(L2); k = sum(1 for d in dead if not d)
                row["readings"].append(dict(cls=f"{label} {idx}", dead_on_cusps=dead, k=k, relator_ok=relok, I_W1=a["I"], I_L2W1=b["I"], W1=a["E"], W1dual=a["Edual"]))
        return row


def site(name):
    """a Site for a census name, or for the closed control 'm140(4,1)' through its filled triangulation (no cusps)"""
    import snappy
    if name == "m140(4,1)":
        F = snappy.ManifoldHP(snappy.Manifold(name).filled_triangulation())
        S = Room.__new__(Room); S.name = name; S.M = F; G = F.fundamental_group(); S.gens = G.generators(); S.rels = G.relators(); S.cusps = G.peripheral_curves()
        S.rho = {g: matrix([[mpc(MC.num(G.SL2C(g)[i, j].real()), MC.num(G.SL2C(g)[i, j].imag())) for j in range(2)] for i in range(2)]) for g in S.gens}
        S.m = len(S.cusps); return S
    return Room(name)


def is_character(S, vals):
    """vals: the value of nu on each generator (roots of unity); a character iff every relator maps to 1"""
    for r in S.rels:
        v = 1
        for ch in r: v *= (vals[ch.lower()] if ch.islower() else 1 / vals[ch.lower()])
        if abs(v - 1) > 1e-20: return False
    return True


def sign_characters(S):
    for vals in itertools.product((1, -1), repeat=len(S.gens)):
        nu = dict(zip(S.gens, [mpc(v) for v in vals]))
        if is_character(S, nu): yield vals, nu


def cell_control(name):
    """the sign characters: every W1 row must reproduce B1492's survey (L = 1 there); the room of the trivial line"""
    S = site(name); out = []
    for vals, nu in sign_characters(S):
        r = S.read(nu); out.append(r)
        print(vals, "b0", r["b0"], "room", r["room"], "second", r["second"], "m_A", r["m_A"], "int", r["interior"], "oth", r["other"], [(x["cls"], x["k"], x["I_W1"], x["I_L2W1"], x["relator_ok"]) for x in r["readings"]], flush=True)
    json.dump(out, open(HERE / f"control_{name.replace('(', '_').replace(',', '_').replace(')', '')}.json", "w"), indent=1, default=str)


def cell_room(name):
    """C0: n(chi) for every sign character chi of the LINE (chi = nu^4 for nu of order 8), with n(1) and the per-cusp triviality"""
    S = site(name); out = []
    for vals, chi in sign_characters(S):
        r = S.room(chi); triv = []
        for (mu, lam) in S.cusps:
            vm = 1
            for ch in mu: vm *= (chi[ch.lower()] if ch.islower() else 1 / chi[ch.lower()])
            vl = 1
            for ch in lam: vl *= (chi[ch.lower()] if ch.islower() else 1 / chi[ch.lower()])
            triv.append(bool(abs(vm - 1) < MC.TOL and abs(vl - 1) < MC.TOL))
        row = dict(chi=list(vals), trivial_on_cusp=triv, m_A=sum(triv), **r); out.append(row); print(row, flush=True)
    summary = dict(name=name, rows=out, n_trivial=[r["n"] for r in out if all(v == 1 for v in r["chi"])][0], max_room=max(r["n"] for r in out), rooms=sorted(r["n"] for r in out))
    json.dump(summary, open(HERE / f"room_{name.replace('(', '_').replace(',', '_').replace(')', '')}.json", "w"), indent=1, default=str); print("ROOM", name, "n(1) =", summary["n_trivial"], "max n(chi) =", summary["max_room"])


def chars_of_order8(S, orbits):
    """nu on (a, b, c) from an exponent triple (p, q, r): zeta_8^p etc. -- L8a15 only (H1 = Z^3 on the generators)"""
    for o in orbits:
        yield o, {g: zeta(e) for g, e in zip(S.gens, o["rep"])}


def cell_second(name="L8a15"):
    """C1: n(nu^3 (x) rho) at one representative per order-8 orbit, then every member of the first two orbits (equivariance)"""
    S = site(name); orbits = json.load(open(HERE / "orbits_L8a15.json"))["orbits"]; out = []
    for o, nu in chars_of_order8(S, [x for x in orbits if x["order"] == 8]):
        n = S.counts(S.two(nu))["n"]; chi = {g: nu[g] ** 4 for g in S.gens}; rm = S.room(chi)["n"]
        out.append(dict(rep=o["rep"], size=o["size"], second=n, room=rm, cap_W=rm, cap_L2=n)); print(out[-1], flush=True)
    equi = []
    for o in [x for x in orbits if x["order"] == 8][:2]:
        for c in o["orbit"]:
            nu = {g: zeta(e) for g, e in zip(S.gens, c)}; equi.append(dict(orbit=o["rep"], member=c, second=S.counts(S.two(nu))["n"], room=S.room({g: nu[g] ** 4 for g in S.gens})["n"]))
    json.dump(dict(name=name, orbits=out, equivariance=equi, max_second=max(x["second"] for x in out), max_room=max(x["room"] for x in out)), open(HERE / "second_L8a15.json", "w"), indent=1); print("SECOND max n(nu^3 x rho) =", max(x["second"] for x in out), "max room =", max(x["room"] for x in out))


def cell_read(name, which):
    """C2/C3: the full reading (W1 by the line L = nu^-4) at the representatives named: 'order4' = one per order-4 orbit; 'cap2' = every order-8 representative whose caps both allow >= 2; or a list of exponent triples"""
    S = site(name); orbits = json.load(open(HERE / "orbits_L8a15.json"))["orbits"]
    if which == "order4": reps = [o["rep"] for o in orbits if o["order"] == 4]
    elif which == "cap2":
        sec = json.load(open(HERE / "second_L8a15.json"))["orbits"]; reps = [tuple(x["rep"]) for x in sec if x["room"] >= 2 and x["second"] >= 2]
    else: reps = [tuple(int(t) for t in w.split(",")) for w in which.split(";")]
    out = []
    for rep in reps:
        nu = {g: zeta(e) for g, e in zip(S.gens, rep)}; r = S.read(nu); r["rep"] = list(rep); out.append(r)
        print(rep, "b0", r["b0"], "room", r["room"]["n"], "second", r["second"], "m_A", r["m_A"], "int", r["interior"], "oth", r["other"], [(x["cls"], x["k"], x["I_W1"], x["I_L2W1"], x["relator_ok"]) for x in r["readings"]], flush=True)
        json.dump(out, open(HERE / f"read_{name}_{which if which in ('order4', 'cap2') else 'list'}.json", "w"), indent=1, default=str)
    print("READ", which, "n =", len(out), "min I(W1) =", min((x["I_W1"] for r in out for x in r["readings"]), default=None))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "control": cell_control(sys.argv[2])
    elif cmd == "room": cell_room(sys.argv[2])
    elif cmd == "second": cell_second()
    elif cmd == "read": cell_read(sys.argv[2], sys.argv[3])
