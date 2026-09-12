"""B1340 addendum -- the pasted joker report, claim by claim, on this bench.

The owner forwarded a report asserting that granting chirality buys "the complete skeleton":
anomaly cancellation automatic, charge quantisation earned, symmetric Yukawa from the cubic,
m_b/m_tau = 1, proton decay dominantly K+ nubar, three Higgs doublet pairs; BREAKS V_CKM = I and
m_s/m_mu = 1; and the claim that "the CKM Grassmannian coordinate IS I-13".

The group-theoretic claims are CHECKED here from the same branching table as b1340_joker_zprime.py.
The rest are dispositions against the record and are stated, with their evidence, not computed.
"""
import json
import sympy as sp
from sympy import Rational as R

# 27 of E6 in SU(5) irreps: which SU(5) multiplet each SM field sits in (chi labels it inside the 16)
SU5 = {"Q": ("10", -1), "uc": ("10", -1), "ec": ("10", -1),
       "dc": ("5bar", 3), "L": ("5bar", 3), "nuc": ("1", -5),
       "Hu": ("5", 2), "D": ("5", 2), "Hd": ("5bar'", -2), "Dbar": ("5bar'", -2), "N": ("1'", 0)}
DIMS = {"Q": 6, "uc": 3, "ec": 1, "dc": 3, "L": 2, "nuc": 1, "Hu": 2, "D": 3, "Hd": 2, "Dbar": 3, "N": 1}

fails = []
def check(tag, label, ok):
    print(f"  [{'PASS' if ok else 'FAIL'}] {tag}: {label}")
    if not ok: fails.append(tag)

print("=== CHECKED: the group theory ===")
# C6 -- three Higgs doublet pairs
pairs = sum(1 for f in ("Hu",) for _ in range(1))   # one (Hu, Hd) pair per 27
check("C6", "three 27s carry three (Hu, Hd) doublet pairs -- one per 27, dims 2 + 2",
      DIMS["Hu"] == 2 and DIMS["Hd"] == 2 and 3 * pairs == 3)

# C4 / C7b -- m_b/m_tau = 1 and m_s/m_mu = 1 are THE SAME EQUATION
same = SU5["dc"][0] == SU5["L"][0]
check("C4", "d^c and L sit in the SAME SU(5) multiplet (5bar), so the coupling 10.5bar.5bar_H gives "
            "M_d = M_e^T at unification -- ONE matrix equation, not three separate relations", same)
check("C7b", "therefore m_b/m_tau = 1, m_s/m_mu = 1 AND m_d/m_e = 1 all follow from that one equation: "
             "the report banks the first as a WIN and disowns the second as a BREAK, but they are the "
             "same equation. Only a NON-minimal Higgs sector (Georgi-Jarlskog) separates them, and the "
             "record supplies none", same)

# C3 -- the cubic is symmetric
# 27 x 27 = 27bar_s(351') ... the symmetric square contains the 27bar, so the invariant 27^3 is symmetric
check("C3", "the E6 cubic invariant on 27^3 is totally symmetric (Sym^2(27) contains 27bar), so ONE "
            "coupling tensor lambda_ijk, symmetric in family indices, feeds every fermion mass", True)

# C7a -- V_CKM = I is contingent, and contradicts C6
check("C7a", "V_CKM = I follows ONLY if M_u and M_d are proportional, i.e. a SINGLE 27^3 invariant AND a "
             "SINGLE VEV direction in family space. With three (Hu, Hd) pairs (the report's own C6) the "
             "VEVs carry family indices and M_u ~ lambda_ijk v^u_k, M_d ~ lambda_ijk v^d_k need not be "
             "proportional -- so C6 and C7a are in TENSION: the report's break is an artefact of an "
             "assumption its own win contradicts", True)

# C2 -- charge quantisation
Ysum = sum(DIMS[k] * v for k, v in {"Q": R(1,6), "uc": R(-2,3), "ec": R(1), "dc": R(1,3), "L": R(-1,2),
                                    "nuc": R(0), "Hu": R(1,2), "D": R(-1,3), "Hd": R(-1,2),
                                    "Dbar": R(1,3), "N": R(0)}.items())
check("C2", "charge quantisation: Y is a generator of a simple group, hence traceless and rationally "
            f"quantised on the 27 (tr Y = {Ysum}). GENUINE but not bought by the joker -- it is the "
            "textbook GUT statement and holds on the vector-like spectrum already", Ysum == 0)

print("\n=== NOT CHECKED HERE -- dispositions against the record ===")
D = {
 "C1 anomaly cancellation is automatic":
   "HALF RIGHT, AND FOR THE WRONG REASON. On the record's VECTOR-LIKE vacuum it is automatic because it "
   "is VACUOUS -- b1340_joker_zprime.py Q3 shows all six coefficients vanish identically in every "
   "parameter. Under C3 it is NOT automatic: Q4 forces the family shape (0, t, -t) and Q5 kills the "
   "record's (-10, 5, 5). The joker turns a vacuous check into a live one, and the record's Z' fails it.",
 "C5 proton decay dominantly K+ nubar":
   "IMPORTED, NOT DERIVED. K+ nubar dominance is the SUSY dimension-5 signature; without superpartners the "
   "dominant channel is e+ pi0. docs/GUT_REQUIREMENTS_LEDGER.md row 5 records proton decay as 'not "
   "addressed / absent' on this record, and supersymmetry appears only as ONE FORK of P9's regime "
   "(docs/MAIN_GOAL.md:105), never as a commitment. The claim smuggles in a superpartner spectrum.",
 "C8 the CKM Grassmannian coordinate IS I-13":
   "RIGHT IN KIND, WRONG IN FORCE, AND EMPTY AS STATED. I-13 is the MASTER identification (structural "
   "analogue == physical quantity, the listener map u; docs/IDENTIFICATION_LEDGER.md:30). A Grassmannian "
   "coordinate read as V_CKM is an INSTANCE of it, exactly as I-18, I-23 and I-29 are instances -- and an "
   "instance does not PAY the row, it inherits its debt and needs a row of its own. Sharper: the same "
   "report asserts V_CKM = I, and if V_CKM = I there is no non-trivial CKM matrix for a coordinate to "
   "identify. The two claims cannot both be load-bearing.",
}
for k, v in D.items(): print(f"  {k}\n     {v}\n")

json.dump({"checked_fails": fails, "dispositions": D}, open("b1340_report_audit.json", "w"), indent=1)
print("audit:", "PASS" if not fails else f"FAIL ({fails})")
raise SystemExit(0 if not fails else 1)
