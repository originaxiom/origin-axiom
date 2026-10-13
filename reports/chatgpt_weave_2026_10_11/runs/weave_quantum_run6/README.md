# Weave quantum realization — Run 6

Start with `TECHNICAL_REPORT.md`. This packet reconstructs the source cohomology representation and tests its map to the protected sector of the already specified interacting model.

## Run locally

Python 3.10+ is recommended. Install the two packages in `requirements.txt`, then run:

```bash
python verify_exact.py
python verify_numerical.py --dps 60
python verify_numerical.py --dps 90
```

Results are written under `results/`. The supplied logs record the completed runs. The final source and result hashes are in `MANIFEST.sha256`.

## Principal results

The exact cochain-derived triplet is a one-dimensional cohomology character tensor the quaternion rotation representation. It maps exactly to **geometric-line-valued** protected currents. It is not an ordinary local current multiplet with the same action. The common local chiral algebra of the marginal family is classified at all weights. The ordinary protected semion-module alternative has rank zero or two on the torus, not three.

A geometric associated flat bundle is not a computed physical determinant connection. Nonabelian Q8-crossed spin defects and their full sewing remain outside this packet. No four-dimensional model or gravitational theory is claimed.

## Integrity

No earlier verification code was imported. The plan followed exploratory reasoning and is not blind preregistration. The source PDF, previous reports and project repository were not modified.
