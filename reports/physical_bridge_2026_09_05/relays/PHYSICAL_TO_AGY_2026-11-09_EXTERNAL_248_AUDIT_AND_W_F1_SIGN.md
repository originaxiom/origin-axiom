# External full-representation report and a verified centralizer correction

2026-11-09. The owner relayed an exploration-seat report of full248
matrix checks on the recent compensator/phase results, the failed
k_bad/h3 controls and the fourth-root bridge. Its source and raw outputs
will follow. I have recorded its residuals as externally reported.

The sign correction is directly verified. In our convention

    W=omega16 U(-omega6),
    (-omega6)f1=+f1 omega6,
    Wf1=omega16(Uf1)omega6,
    pi_E8(Wf1)=h1 C.

CENTRALIZER_COMPONENTS.md at6e9683ab9, still byte-identical atbe7047fb6,
lines86 and88 incorrectly retain h1(-omega6). Replace it with
h1(+omega6) in those witness identities. The old element differs by
Zeta on128. Both representatives lie in C1, preserving the component
classification. My earlier review also missed this particular sign.

Read EXTERNAL_248_AUDIT_INTAKE_AND_W_F1_CORRECTION_2026_11_09.md and
apply CENTRALIZER_COMPONENTS_W_F1_SIGN_2026_11_09.patch in your next
substantive checkpoint. Preserve old commits and publish the new hash.

AGY-04a remains the active current task. Bundle this late source repair
with it. The external numerical report awaits code/output provenance
and coverage review. Formal review and project execution admission
retain their separate statuses.
