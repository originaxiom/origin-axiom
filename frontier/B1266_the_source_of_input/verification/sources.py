"""B1266 -- THE SOURCE OF INPUT: the 14 overcounts, the irreducible number is 11.

Owner: "should we find the source of input".  Yes -- and doing it corrects B1261.

B1261 measured the trade as 4 axioms + 10 UNEARNED identifications = 14 unpriced inputs
against the SM's 19 free parameters.  But that counts ROWS, and the rows are not
independent: several state, in their own earning conditions, that they reduce to another.

READ FROM THE LEDGER'S OWN TEXT (not from impression):
    I-18  "earning it means ... i.e. paying I-13, the listener map u"
    I-23  "... i.e. paying I-13 on this instance"      (and its claim says "an I-13 instance")
    I-11  "the same map as I-10, restricted to the boundary"
so I-18 and I-23 are instances of I-13, and I-11 is I-10.  Two parser traps had to be
avoided: I-25's earning text references I-1, but I-1 is EARNED (McKay) and an earned row is
not a debt; and I-10/I-11 reference each other, a 2-cycle that a naive transitive closure
splits into two roots instead of one.  Union-find over the dependency relation, restricted
to edges into still-UNEARNED rows, gives:

    10 unearned rows  ->  7 IRREDUCIBLE SOURCES
        [3] I-13, I-18, I-23   THE LISTENER MAP u
        [2] I-10, I-11         THE FORK (internal A1 / theta-polarisation = spacetime spin)
        [1] I-6                the 2T quotient = the transverse ALE Gamma
        [1] I-7                the object's Z/3 = the boundary CFT module group
        [1] I-14               L3 grading = L4 commensurator unit
        [1] I-25               which sl2 embedding the object supplies
        [1] I-26               h^1 = the number of 4d chiral generations

    PRICE RESTATED: 4 axioms + 7 sources = 11 IRREDUCIBLE INPUTS, not 14.

BOTH NUMBERS ARE REAL AND THEY MEASURE DIFFERENT THINGS, which is why this arc keeps both:
    14 = ROWS OUTSTANDING -- the work items, what the ratchet tracks, what must each be
         individually discharged in the register;
    11 = IRREDUCIBLE INPUTS -- the actual free inputs of the theory, since earning I-13
         discharges I-18 and I-23 with it, and earning I-10 discharges I-11.
The comparison that means something against the SM's 19 is 11, not 14.  B1261's headline is
CORRECTED here, not withdrawn: its accounting method was right and its row count was right;
what it did not do was quotient by the rows' own stated reductions.

AND THE SOURCES CLASSIFY BY TYPE, which says what kind of work each needs:
    H5-TYPE (the object supplies a FAMILY, the observer picks a point) -- I-6 (2 quotients),
        I-14 (85 gradings), I-25 (4 embeddings): measured multiplicities, B1263/B1264/B1256.
    MISSING BRIDGE -- I-10/I-11 (the fork; B1265 shows the real form is DERIVED and the
        obstruction is RANK, inner vs outer), I-26 (an index theorem across a dimension gap).
    THE MASTER -- I-13, which three rows reduce to.
    UNCLASSIFIED -- I-7.

CONTROLS (MB12, both directions):
  - edges are read from the ledger text, and edges into EARNED or REFUTED rows are excluded,
    so a reference to a discharged row cannot masquerade as a dependency;
  - the mutual I-10/I-11 cycle is resolved by union-find rather than closure, and the arc
    asserts they land in ONE group -- a naive closure would report 8 and be wrong;
  - the source count must be strictly less than the row count, and the difference must equal
    the number of rows that state a reduction (3), or the reduction is miscounted.
"""
import os, re

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
AXIOMS = 4
SM_PARAMS = 19


def parse_ledger():
    led = open(os.path.join(REPO, "docs", "IDENTIFICATION_LEDGER.md"), encoding="utf-8").read()
    status, earn, claim = {}, {}, {}
    for line in led.splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|", line)
        if not m:
            continue
        c = re.split(r"(?<!\\)\|", line)
        rid = m.group(1)
        st = re.search(r"\*\*(EARNED|UNEARNED|REFUTED)\*\*", line)
        status[rid] = st.group(1) if st else "?"
        earn[rid] = c[9].strip() if len(c) > 9 else ""
        claim[rid] = c[2].strip()
    return status, earn, claim


def sources():
    status, earn, claim = parse_ledger()
    un = [r for r in status if status[r] == "UNEARNED"]
    edges = {}
    for r in un:
        refs = {x for x in re.findall(r"I-\d+", earn[r]) if x != r and status.get(x) == "UNEARNED"}
        if "paying I-13" in earn[r]:
            refs.add("I-13")
        if "the same map as I-10" in earn[r]:
            refs.add("I-10")
        edges[r] = sorted(refs)
    parent = {r: r for r in un}

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]; a = parent[a]
        return a

    for r, ds in edges.items():
        for d in ds:
            ra, rb = find(d), find(r)
            if ra != rb:
                parent[rb] = ra
    groups = {}
    for r in un:
        groups.setdefault(find(r), []).append(r)
    return un, edges, {k: sorted(v) for k, v in groups.items()}


def selftest():
    print("B1266 -- the source of input (selftest)")
    un, edges, groups = sources()
    print(f"  [rows ] unearned rows: {len(un)}")
    print(f"  [srcs ] irreducible sources: {len(groups)}")
    for k, v in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        print(f"           [{len(v)}] {v}")
    assert len(un) == 14 and len(groups) == 8   # 2026-09-07 (B1296): +I-27, a new H5-type source; 2026-09-08 (B1298): +I-28, joins I-27's source; 2026-09-09: +I-29 (joins I-13's source), +I-30 (joins I-27's); was 10 / 7, then 12 / 8

    # the I-10/I-11 cycle must be ONE source -- a naive closure reports two
    fork = [v for v in groups.values() if "I-10" in v]
    print(f"  [ctl  ] the I-10/I-11 mutual cycle resolves to ONE group: {fork[0]}")
    assert fork and sorted(fork[0]) == ["I-10", "I-11"]

    # a reference to an EARNED row must not create a dependency
    print(f"  [ctl  ] I-25's edges (its text cites I-1, which is EARNED): {edges['I-25']}")
    assert edges["I-25"] == [], "a reference to a discharged row must not count as a debt"

    reduced = len(un) - len(groups)
    print(f"  [ctl  ] rows that are instances of another: {reduced} (14 rows - 8 sources)")
    assert reduced == 6   # 2026-09-08 (B1298): I-28 is an instance of I-27; 2026-09-09: I-29 of I-13, I-30 of I-27; was 3 (= 10 - 7), then 4

    print(f"\n  PRICE, two readings, both kept:")
    print(f"    rows outstanding (what the ratchet tracks) : {AXIOMS} + {len(un)} = {AXIOMS+len(un)}")
    print(f"    IRREDUCIBLE INPUTS (the theory's free inputs): {AXIOMS} + {len(groups)} = {AXIOMS+len(groups)}")
    print(f"    against the SM's {SM_PARAMS} free parameters -- the meaningful comparison is"
          f" {AXIOMS+len(groups)}, not {AXIOMS+len(un)}")
    assert AXIOMS + len(groups) == 12   # 2026-09-07 (B1296): I-27 is an eighth source; was 11
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
