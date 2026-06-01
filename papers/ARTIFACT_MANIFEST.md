# Paper Artifact Manifest

Status: manifest only. No paper artifacts are copied in R2.

## Rule

Do not move originals. Copy artifacts only after recording provenance and
checksums.

## Entry Template

```text
ID:
Artifact name:
Artifact type:
Copied to:
Original path:
Original date if known:
Date copied:
Checksum:
Generator script if known:
Related paper candidate:
Related research nodes:
Governance status:
Notes:
```

## Artifact Categories

```text
legacy_pdf = older generated or hand-written PDF
generated_pdf = current generated PDF
latex_source = TeX or LaTeX source
build_log = compilation or build log
figure = generated figure
data = simulation or calculation output
notebook = notebook artifact
bundle = zip, tar, or archive package
```

## First Inventory Targets

Inventory these later, after each has a paper card and a public-safety decision:

```text
legacy project PDFs
automated LaTeX-to-PDF outputs from phased work
FRW toy-universe reports
belt, cavity, and phase simulation reports
session synthesis bundles
continuous-campaign reports
field-theory or kink repair reports if validated
```

Raw source-mining output, downloaded PDFs, raw run logs, and local path
inventories stay private unless separately approved and licensed.

## Inventoried Private Sources

These sources are not copied into the repository. They are recorded only so the
distilled public artifacts can be traced without publishing raw bundles or
private coordination material.

| ID | Artifact name | Artifact type | Source status | Date inventoried | Checksum | Related candidate | Governance status | Notes |
|---|---|---:|---|---:|---|---|---|---|
| SL3-BUNDLE-v1.2.1 | `SL3_ALL_FILES_SINGLE_DOWNLOAD_v1_2_1.zip` | bundle | private local source, not copied | 2026-06-01 | `sha256:ee8a1753d7c036dd4e8083f98327f5a0035ada03c3956dadeb891cc4799a57e6` | PC12 | distilled-only intake | Raw bundle includes non-public coordination artifacts; repo receives only curated B48/PC12 material. |
