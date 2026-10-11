# First native field-parameter failure

The published pre-execution seal is be7c1bf1e0e8d41a15d7d3b440ac5cde8661eb12.
The first native run stopped in assembly of R2 before reaching any new
family assertion: the inner matrix multiplication was given q*Q but the
default constant field K. Pass the already-declared variable q to that
inner multiplication. The exterior/character/domain/model/proof and all
criteria remain unchanged. No literal matrix or selected plane is changed.

The raw failed transcript and its SHA256 are retained outside the worktree.
The public transcript redacts only local user/worktree paths for privacy;
the raw and public hashes are separately recorded, not equated. The first
reference run independently completed with exit0 and is retained unchanged.
Repair, hashes and failure custody are committed/pushed before native replay.
This repair is an instrument correction, not a physical or mathematical kill.
