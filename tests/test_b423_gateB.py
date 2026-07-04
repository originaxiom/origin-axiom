"""Locks for B423 -- the E6 torsion Fibonacci-square structure + the honest bar verdict."""
import json
import os
HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B423_gateB_torsion")
R = json.load(open(os.path.join(HERE, "gateB.json")))
def test_torsion_prime_spectrum():
    assert R["prime_content"] == [2,3,5,7,11,13,17,19,29,41,47,89,199]
    assert R["golden_only"] is False
def test_control_distinctive():
    # figure-eight (Fibonacci) prime set differs from silver (Pell) control
    assert set(R["prime_content"]) != set(R["control_primes"])
    assert 89 in R["prime_content"] and 89 not in R["control_primes"]
def test_per_exponent_tau1():
    assert R["taus"]["1"] == "-5"
