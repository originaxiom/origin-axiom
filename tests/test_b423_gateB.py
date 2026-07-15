"""Locks for B423 -- the E6 torsion structure + producer-artifact agreement.

CORRECTED 2026-07-15 (audit item 5.2): the test now RUNS the producer
fresh (the reduced-determinant definition) and compares to the committed
canonical artifact, instead of only reading the JSON.
"""
import importlib.util
import json
import os

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier",
                    "B423_gateB_torsion")
spec = importlib.util.spec_from_file_location(
    "gateB", os.path.join(HERE, "gateB.py"))
gateB = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gateB)

R = json.load(open(os.path.join(HERE, "gateB.json")))


def test_producer_reproduces_artifact():
    fresh = gateB.compute()
    for k in ("taus", "tauE6", "prime_content", "golden_only",
              "control_tauE6", "control_primes"):
        assert fresh[k] == R[k], k


def test_torsion_prime_spectrum():
    assert R["prime_content"] == [2, 3, 5, 7, 11, 13, 17, 19, 29, 41, 47,
                                  89, 199]
    assert R["golden_only"] is False


def test_control_distinctive():
    assert set(R["prime_content"]) != set(R["control_primes"])
    assert 89 in R["prime_content"] and 89 not in R["control_primes"]


def test_per_exponent_tau1():
    assert R["taus"]["1"] == "-5"
