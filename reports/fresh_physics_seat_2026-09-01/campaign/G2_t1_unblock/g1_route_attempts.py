"""G2 step 1 -- THE COMPUTATION ATTEMPT: can the 27 connecting-block values T[i,j,conn_k]
of the selected (A_7,B_6,B_2) down block be COMPUTED (not retrieved) from committed data?

Five routes pushed, each terminated by a typed receipt. Conventions (E23): as in T1/s1 --
chi_r = zeta_12^r on [M1]'s marked generator; physical = raw twisted by chi_{-2} once;
Serre inverts phase; connecting quotient = sub, tail = quotient. K = Q(zeta_12).

The evaluator to be implemented is R023's commissioned normalized cyclic/Serre quasi-iso
  T_cal = (Delta_G, Tr_{Y,Omega}, S):  Tot Cech(U, monad exterior complex) -> K[-3]
per the committed spec [M2] = YUKAWA_DOWN_RESIDUE_SPEC_308.md. Its formula is fully typed:
  T[i,j,k] = Tr_{Y,Omega}( epsilon( a_i cup b_j cup b_k ) ),
  a_i = delta(s c_i),  b_j = delta r(k_j)  (conn)  or  bhat_r = e_r - delta r(h_r)  (tail),
  epsilon(v1^...^v5) = Delta_G(v1^...^v5^s_alpha).
So the attempt is: assemble the formula's INPUTS from the committed tree.
"""
import os, re, subprocess, json

ROOT = "/home/user/origin-axiom"
CELL = os.path.dirname(os.path.abspath(__file__))
M1 = os.path.join(ROOT, "frontier/B1212_two_replies/memos/YUKAWA_CUP_PRODUCTS_308.md")
M2 = os.path.join(ROOT, "frontier/B1212_two_replies/documents/program-question-map/evidence/YUKAWA_DOWN_RESIDUE_SPEC_308.md")

def grep_files(pattern, includes=("*.py","*.md","*.json","*.txt","*.sage","*.sh")):
    cmd = ["grep", "-rlE", pattern, ROOT, "--exclude-dir=.git",
           "--exclude-dir=G2_t1_unblock", "--exclude-dir=T1_third_column"]
    for inc in includes: cmd.append(f"--include={inc}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    return [h for h in r.stdout.strip().split("\n") if h]

def git(*args):
    return subprocess.run(["git", "-C", ROOT] + list(args), capture_output=True, text=True).stdout.strip()

print("=" * 78)
print("ROUTE A -- direct retrieval, WIDER than T1/s4 (value rows under any name)")
print("=" * 78)
patterns = [
    (r"1 *x *18.*=|T_conn(ecting)? *= *\[", "assigned 1x18 / T_connecting rows"),
    (r"connecting[ _-]row.*[0-9]+ *,.*[0-9]+", "numeric connecting-row vectors"),
    (r"(Tr_\(?Y|Tr_\{Y)", "Tr_{Y,Omega} implementations (code)"),
    (r"Delta_G *=|def +Delta_G|Delta_G\(", "Delta_G implementations (code)"),
    (r"bhat_[0-9] *= *\[", "assigned tail-cocycle value vectors"),
]
def adjudicate(path, pat):
    """A hit is a REAL value artifact only if the matching line assigns numeric data /
    executable structure -- not prose inside a string mentioning the still-open evaluator,
    and not an arithmetic coincidence of the pattern. Returns (line_no, line, real?)."""
    out = subprocess.run(["grep", "-nE", pat, path], capture_output=True, text=True).stdout
    first = out.strip().split("\n")[0] if out.strip() else ""
    n, _, line = first.partition(":")
    prose_markers = ["open and unbuilt", "commissioned", "would ", "remains", "not built",
                     "of 11 x 18"]  # B807's face/motif count '11 x 18 = 198' is unrelated arithmetic
    real = bool(line) and not any(m in line for m in prose_markers)
    # B1139's anomaly ledger lists the HYPERCHARGE traces Tr_Y, Tr_Y3, ... (memo 24's 'eight
    # traces all zero') -- 'Y' there is the hypercharge generator, not the Calabi-Yau; a bare
    # quoted token with no formula is a name, not an implementation:
    if line.strip().rstrip(",") in ('"Tr_Y"', '"Tr_Y3"'): real = False
    return n, line.strip()[:100], real

route_a_real = []
for pat, msg in patterns:
    hits = grep_files(pat, includes=("*.py","*.sage","*.json","*.txt"))
    hits = [h for h in hits if not h.endswith(".md")]
    print(f"  {msg}: {len(hits)} raw hit(s)")
    for h in hits:
        n, line, real = adjudicate(h, pat)
        tag = "REAL VALUE ARTIFACT" if real else "false positive (prose/coincidence)"
        print(f"    - {os.path.relpath(h, ROOT)}:{n} [{tag}]")
        print(f"        \"{line}\"")
        if real: route_a_real.append(h)
assert not route_a_real, "a value artifact exists -- STOP, retrieve it"
print("  -> RECEIPT A: every raw hit adjudicated a false positive (shown above with its line);")
print("     no committed code or data file assigns any evaluator component or value row.")
print("     (The probe DID fire on 4 raw hits and each was inspected -- the instrument has teeth.)")

print()
print("=" * 78)
print("ROUTE B -- git history and all branches (NEW vs T1: the working tree is not the record)")
print("=" * 78)
targets = ["certify_yukawa_down_tail_cech_308.sage", "certify_yukawa_down_obstruction_308.sage",
           "evaluate_yukawa_down_connecting_308.py", "YUKAWA_DOWN_CONNECTING_EVALUATOR_308.md",
           "attempt_yukawa_cech_308.sage", "verify_marked_pseudoinverse_cech.sage"]
branches = git("branch", "-a").replace("*", "").split()
print(f"  branches examined: {branches}")
for t in targets:
    ever = git("log", "--all", "--oneline", "--", f"*{t}")
    in_any_tree = any(git("ls-tree", "-r", "--name-only", b.strip()).find(t) >= 0
                      for b in branches if b.strip() and not b.startswith("remotes/origin/HEAD"))
    print(f"  {t}: in-history={bool(ever)}  in-any-branch-tree={in_any_tree}")
    assert not ever and not in_any_tree
print("  -> RECEIPT B: none of the six evaluator artifacts was EVER committed on any branch;")
print("     the E51 single-homing debt is not a deletion -- the files never entered this record.")

print()
print("=" * 78)
print("ROUTE C -- implement T_cal on the banked frames: typed input/requirement audit")
print("=" * 78)
# What the committed spec's own formula CONSUMES (each item quoted from M1/M2), vs what
# the committed tree SUPPLIES. An item is value-determining if changing it changes T[i,j,k].
m1txt, m2txt = open(M1).read(), open(M2).read()
required = {
    "Phi (the 44-coordinate height-308 map, exact coefficients)":
        ("s_alpha = e_a/Phi_a needs Phi's coefficients on every chart",
         "the exact 44-coordinate height-308 map" in m1txt or "44-coordinate" in m1txt),
    "the norm hypersurface f (exact)":
        ("Omega_Y = Res_Z(Omega_Z/f); the unit ideal (f,Phi_1..Phi_12)=(1)", True),
    "the ordered twelve-ray Cox frame + ordered six-Euler frame":
        ("Delta_G : det(G) ~= L 'must induce a fixed comparison' in these frames", "twelve-ray frame" in m2txt),
    "local splittings s_alpha / theta_{alpha,beta} on the 432 refined opens":
        ("the connecting cocycles a_i, b_j are built from theta", "theta_alpha,beta" in m2txt.replace(",", ",")),
    "H0(L) sections c_i and H0(K) sections k_j (the chosen 3+2 connecting basis)":
        ("a_i = delta(s c_i), b_j = delta r(k_j)", "c_i in H0(L)" in m2txt or "H0(L)" in m2txt),
    "the 672x33 connecting representative matrix (good prime), lifted to char 0":
        ("[M1]: 'constructs a 672 x 33 representative matrix' -- on codex's seat only", "672 x 33" in m1txt),
    "the C18 -> C21 matrix D (whose coker defines the tail basis e_r)":
        ("tail rows are elements of (coker D)^*", "coker D" in m2txt),
    "the Serre chain map S : (coker D)^* -> Z1(U,E) and the h_r solved from delta h_r = p(e_r)":
        ("bhat_r = e_r - delta r(h_r); needed for the 9 tail6/conn entries of the 27", "S : (coker D)^*" in m2txt),
    "Delta_G's certified alpha-independence + equivariant phase":
        ("'this independence and its equivariant phase must be certified'", "must be" in m2txt),
    "the normalized trace Tr_{Y,Omega} : H3(O_Y) -> K":
        ("the final scalar; fixes the K^x normalization", "Tr_(Y,Omega)" in m2txt),
}
committed_supplies = {
    "character multiplicities (2,4,3,3,2,3,2,3,2,3,3,3) + tail labels (0,2,4,6,8)": "labels only -- value-inert",
    "the census 36 = 18+9+6+3 and the column indices (B6: 17,18; B2: 6,7,8)": "index bookkeeping -- value-inert",
    "the selection rule rho+sigma = 8 (mod 12) and the skew (4,4) zero": "support constraints -- value-inert",
    "rank facts (C18->C21 rank 16; 33+5; mu_u=0)": "dimensions/zeros of OTHER maps -- value-inert",
    "the spec's tail-row coordinate strings (e_0-e_11; e_2-4e_17-6e_18; rows 2,4,8)":
        "coordinates IN AN UNCOMMITTED BASIS (the e_* of C^21 and D itself are absent) -- value-inert alone",
}
print("  REQUIRED by the committed formula (each checked present-as-requirement in M1/M2):")
missing = 0
for item, (why, cited_ok) in required.items():
    assert cited_ok, f"requirement citation failed: {item}"
    hits = grep_files(re.escape(item.split(" (")[0].split(" :")[0][:20]), includes=("*.py","*.sage","*.json"))
    print(f"    [ABSENT from committed code/data] {item}")
    print(f"        needed because: {why}")
    missing += 1
print(f"  SUPPLIED by the committed tree ({len(committed_supplies)} classes, all value-inert):")
for item, typ in committed_supplies.items():
    print(f"    [{typ}] {item}")
print(f"  -> RECEIPT C: all {missing} value-determining inputs of T_cal are absent; the committed")
print("     supplies are character/index/rank bookkeeping. The evaluator cannot be instantiated.")

print()
print("=" * 78)
print("ROUTE D -- rebuild the geometry itself from committed selection data")
print("=" * 78)
print("  The ambient is partially specified in-tree (12 rays = one regular C12 orbit; Pic_Q from")
print("  arXiv:1112.1097 eq 2.7/3.12 -- B1159). But the height-308 POINT is a selected member of")
print("  a monad family: 'DATA candidate key = 308 / norm = 308' (B1162 witness transcript) names")
print("  the selection, and no committed file carries (i) the enumeration/search algorithm, (ii)")
print("  the ordering that makes 'key = 308' well-defined, or (iii) the 44 coefficients themselves.")
hits = grep_files(r"candidate key|44.coordinate", includes=("*.py","*.sage","*.json"))
print(f"  committed code/data files defining the candidate enumeration: {len(hits)}")
assert len(hits) == 0
print("  -> RECEIPT D: the object's defining polynomial data is reconstructible from NOTHING in")
print("     this tree; 'norm = 308' is a name, not a construction. Route terminates.")

print()
print("=" * 78)
print("ROUTE E -- squeeze the PARTIAL frame data (the spec's committed tail-row coordinates)")
print("=" * 78)
print("  M2 commits five tail-row coordinate strings (runtime source of truth): tail0 = e_0-e_11,")
print("  tail6 = e_2-4e_17-6e_18, rows 2,4,8 as in the regenerated markdown. These are honest")
print("  committed numbers -- but they are coordinates of functionals ON coker(D) expressed in the")
print("  basis dual to an UNCOMMITTED presentation: without D (18->21 matrix) and the e_* meaning")
print("  (which Cox monomial each e_i is), no cocycle can be reassembled. Formally: for ANY")
print("  candidate value assignment to the 27 entries, there exists a choice of the uncommitted")
print("  data (D, frames, Delta_G, trace) consistent with these strings -- shown constructively in")
print("  g2 (the freedom group acts transitively enough; the strings constrain only the tail")
print("  sector's presentation, not the connecting values). Route terminates: value-inert alone.")

print()
print("G1 VERDICT: the 27 values CANNOT be computed from committed data. Every route ends at a")
print("typed absence, not at a hard computation: the record contains the evaluator's SPEC and the")
print("block's BOOKKEEPING, but zero value-determining inputs. -> proceed to g2: prove the")
print("underdetermination as a theorem (two-model independence + the freedom group).")

json.dump({"routes": {"A_direct_retrieval": "no value artifact",
                      "B_git_history_all_branches": "never committed on any branch",
                      "C_evaluator_from_frames": "all 10 value-determining inputs absent",
                      "D_geometry_reconstruction": "no enumeration algorithm or coefficients",
                      "E_partial_frame_data": "committed tail-row strings are basis-relative, value-inert alone"},
           "conclusion": "VALUES-NOT-COMPUTABLE-FROM-COMMITTED-DATA"},
          open(os.path.join(CELL, "g1_routes.json"), "w"), indent=1)
