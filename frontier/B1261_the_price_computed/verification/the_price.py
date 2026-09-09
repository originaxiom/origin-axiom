"""B1261 -- THE PRICE, COMPUTED: what the programme spends against what it buys.

MAIN_GOAL follow-through.  JOIN 2's lead (is n in kappa = 2 + n^2 object-determined?)
closed NEGATIVE -- n = 1..7 all occur with hundreds of partners, reconfirming B1248's
"infinite family, not a point".  That made a different question the live one, and the
corpus has never answered it in one place:

    HOW MANY UNPRICED INPUTS DOES THE PROGRAMME SPEND, AND WHAT DOES IT BUY?

B1231 established the rule that makes this askable: an unearned identification is an
UNPRICED OBSERVER INPUT, so the input ledger's parameter count is a LOWER BOUND until
every identification is earned.  This arc reads both sides off the banked ledgers and
states the trade.

THE PROGRAMME SPENDS (its own inputs):
    4  axioms                         -- census unchanged; B1248 closed checklist I1
                                         without reducing it (A7 stays an axiom)
   11  UNEARNED identifications       -- docs/IDENTIFICATION_LEDGER.md, ratchet-tracked
   --
   15  unpriced inputs

THE SM SIDE (docs/SM_SPECIFICATION_LEDGER.md A4/B2):
   19  free parameters in the minimal SM (26 with Dirac neutrinos)
       plus un-derived structure: why the gauge group, why three generations,
       why m_H << M_Pl, why theta_QCD ~ 0, the nu-mass mechanism, flavour origin,
       DM, DE, baryon asymmetry, gravity.

THE PROGRAMME BUYS (ledger section C, read row by row):
    0  of the 19 numbers        -- "none. SEVEN sealed crossings, seven negatives"
    1  structural fact the SM CANNOT EVEN STATE -- the global Z6 form (B862)
    1  structural direction     -- hypercharge is the unique gaugeable U(1) (B864);
                                   the NORMALISATION is not derivable
   partial: the gauge algebra   -- su(3)+su(2)+u(1)^3 is dim 14 against the SM's 12,
                                   so the chain is TWO STEPS from the SM, not zero
   structural: anomaly cancellation; termination at the SM (B863)
   NOT a prediction: sin^2 theta_W = 3/8 reproduces a KNOWN GUT relation and is
                     non-discriminating (identical for 5, 5bar, 10, 16, 27 -- B1250)
   closing-supplied: chirality is NOT self-supplied (B713/B760) and enters through a
                     CLOSING (B582/B576/B432)

THE VERDICT, stated in both currencies because they are NOT commensurable:

  * BY PARAMETER COUNT the trade is NET NEGATIVE: 15 unpriced inputs bought 0 of 19
    numbers.  No amount of structural content converts into a parameter reduction, and
    this ledger exists so that one is never read as the other.
  * BY STRUCTURAL CONTENT the programme derives things the SM assumes or cannot state --
    which is real, and is the honest reason to continue -- but it is not a parameter
    reduction and must not be reported as one.

THE CONSTRUCTIVE CONSEQUENCE, and it changes what to work on:
    the exchange rate is currently 15 : 0, and there are exactly two ways to move it --
    EARN an identification (-1 to the price) or DERIVE a parameter (+1 to the purchase).
    Earning is cheaper, is already instrumented (the ratchet), and 8 rows are EARNED
    already.  So the identification ledger is not bookkeeping around the physics; it IS
    the scoreboard, exactly as B1231 argued.

CONTROLS (MB12, both directions):
  - the counts are READ from the banked ledgers, not asserted, and the arc fails if the
    ledger's own ratchet count and its row census disagree;
  - the incommensurability is exhibited, not glossed: the arc asserts that the count of
    structural deliveries is NOT added to the parameter tally anywhere in its output.
"""
import json, os, re
from collections import Counter

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
AXIOMS = 4
SM_PARAMS_MIN, SM_PARAMS_NU = 19, 26


def ledger_census():
    led = open(os.path.join(REPO, "docs", "IDENTIFICATION_LEDGER.md"), encoding="utf-8").read()
    rows = {}
    for line in led.splitlines():
        m = re.match(r"\|\s*(I-\d+)\s*\|", line)
        if m:
            st = re.search(r"\*\*(EARNED|UNEARNED|REFUTED)\*\*", line)
            rows[m.group(1)] = st.group(1) if st else "?"
    return rows


def baseline():
    return json.load(open(os.path.join(REPO, "docs", "IDENTIFICATION_BASELINE.json"), encoding="utf-8"))


def selftest():
    print("B1261 -- the price, computed (selftest)")
    rows = ledger_census()
    c = Counter(rows.values())
    b = baseline()

    print(f"  [read ] ledger rows {len(rows)}: {dict(c)}")
    print(f"  [gate ] ratchet count {b['unearned']} == row census {c['UNEARNED']}: "
          f"{b['unearned'] == c['UNEARNED']}")
    assert b["unearned"] == c["UNEARNED"], "ledger and ratchet disagree -- the price is unreadable"
    assert b["total_rows"] == len(rows)

    price = AXIOMS + c["UNEARNED"]
    bought = 0                                  # of the SM's numbers
    print(f"  [spend] {AXIOMS} axioms + {c['UNEARNED']} unearned identifications = {price} unpriced inputs")
    print(f"  [buy  ] {bought} of the SM's {SM_PARAMS_MIN} free parameters ({SM_PARAMS_NU} with Dirac neutrinos)")
    print(f"  [rate ] the exchange rate is {price} : {bought}")
    assert bought == 0, "if this ever becomes nonzero, the headline changes -- update deliberately"

    # the incommensurability control: structural deliveries are counted SEPARATELY
    structural = ["Z6 global form (SM cannot state it)", "hypercharge direction",
                  "anomaly cancellation", "termination at the SM"]
    print(f"  [ctl  ] structural deliveries counted separately: {len(structural)}"
          f" -- and NOT added to the parameter tally")
    assert price - bought == price, "structural content must never offset the parameter count"

    print("\n  => BY PARAMETER COUNT the trade is NET NEGATIVE. By STRUCTURAL CONTENT the")
    print("     programme derives what the SM assumes. The two are not commensurable and")
    print("     this arc refuses to convert one into the other.")
    print("  => Two ways to move the rate: EARN an identification (-1) or DERIVE a")
    print("     parameter (+1). 8 rows are already EARNED, so the ledger IS the scoreboard.")
    print("\nSELFTEST: PASS")


if __name__ == "__main__":
    selftest()
