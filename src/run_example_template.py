"""
File: src/run_example_template.py
Purpose: Minimal example script showing the standard header and CLI pattern.
Axiom link: This is just a template; real scripts will link to a specific test
  of the non-cancelling principle or related toy models.
Inputs:
  - --steps int : number of dummy steps to run.
Outputs:
  - Prints a short log to stdout (no files).
Usage:
  - python3 src/run_example_template.py --steps 5
"""

import argparse
import sys

def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Origin Axiom script template example."
    )
    parser.add_argument(
        "--steps",
        type=int,
        default=3,
        help="Number of dummy steps to run (default: 3).",
    )
    return parser.parse_args(argv)

def main(argv=None):
    args = parse_args(argv)
    print("=== Origin Axiom template script ===")
    print(f"Running {args.steps} dummy steps...")
    for i in range(args.steps):
        print(f"Step {i+1} / {args.steps}")
    print("Done.")

if __name__ == "__main__":
    main()
