# Phase 0 – Assumptions

This document lists the assumptions underlying the governance layer.

- A1 – Phased program structure  
  We assume the project will proceed in well-defined phases (0,1,2,...) with
  separate scopes, artifacts, and claims.

- A2 – Explicit claims and non-claims  
  We assume that any meaningful statement about the models must be expressed
  as a claim with an ID, type, evidence pointers, and explicit non-claims.

- A3 – Schema-first corridors  
  We assume that admissible parameter ranges (theta corridors, filters) can be
  encoded as JSON documents validated against explicit JSON Schemas.

- A4 – Snakemake + LaTeX toolchain  
  We assume that a Snakemake-driven workflow and LaTeX papers are suitable
  for long-term reproducible documentation of the project.

- A5 – Public, version-controlled repository  
  We assume that this Git repository is the canonical public record for code,
  schemas, and claims, and that large exploratory artifacts are moved to a
  separate archive as per `docs/ARCHIVE.md`.