# Reporting repair, after the first native run

The first sealed native run exited 1: JSON could not serialize a SymPy
NegativeOne in the exact relation matrix. All scientific functions had
returned before the output loop; this is NOT recorded as a successful
native run. Preserve the original source and complete failed output.

The v2 wrapper changes only serialization: convert SymPy Integer to Python
int and reject every other unsupported type. No mathematical source, proof,
assertion, witness or expected outcome is changed. Add explicit serializer
controls. Commit/hash the wrapper and controls before rerunning. The first
failure remains part of the record, not silently overwritten.
