"""B47 -- S1 verdict ledger."""

from __future__ import annotations


def main() -> None:
    print("=" * 72)
    print("B47 -- S1 verdict ledger")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    verdicts = {
        "B38": "CONDITIONAL",
        "B39": "STALLED",
        "B40": "CONDITIONAL",
        "B41": "STALLED",
        "B42": "STALLED",
        "B43": "CONDITIONAL",
        "B44": "CONDITIONAL",
        "B45": "CONDITIONAL",
        "B46": "STALLED",
    }

    print("\n[1] campaign verdict table")
    for probe, verdict in verdicts.items():
        print(f"    {probe}: {verdict}")

    assert "DERIVED" not in verdicts.values()
    assert verdicts["B40"] == "CONDITIONAL"

    final_status = "CONDITIONAL_ON_T1"
    dependency = "T1 -> S1 -> I=1/4 -> lambda/h=1"

    print("\n[2] final S1 status")
    print(f"    status = {final_status}")
    print(f"    dependency = {dependency}")
    assert final_status == "CONDITIONAL_ON_T1"

    print("\nVerdict: CONDITIONAL")
    print("S1 is not derived from A1-A7 plus exchange. The strongest honest")
    print("statement is T1 -> S1 -> lambda/h=1, with T1 named explicitly.")


if __name__ == "__main__":
    main()
