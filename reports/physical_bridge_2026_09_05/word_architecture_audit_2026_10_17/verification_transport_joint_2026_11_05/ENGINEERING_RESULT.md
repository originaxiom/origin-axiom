All eight synthetic wrapper fixtures passed on the research CPython 3.12.1
runtime with isolated mode, bytecode disabled and site startup disabled.
The source was sealed at `3f5d2ea51` after the prior engineering design
at `1f11431e7`. The exact first-run stdout, stderr and outcome are preserved
under `engineering/attempt_01.*`. The eight tests reported 0.194 seconds;
the captured process took 0.532 seconds and exited zero. Source hashes
remained unchanged.

The fixtures verify exact binding and one delegation, rejection of changed
or missing infrastructure, propagation of nonzero returns and exceptions,
the static thirteen-method population, the synthetic bridge's exact two
class exports and rejection of missing bridge attributes. Every imported
test module in these fixtures was generated in its temporary directory.
The real scientific sources were read only as AST population metadata.

A separate standard-library distribution metadata query, also with site
startup disabled, found CPython 3.12.1, SymPy 1.14.0 and mpmath 1.3.0.
Neither mathematical package entered sys.modules. Its exact stdout/stderr
are preserved as `engineering/runtime_metadata_01.*`, and the environment
record pins the input/output digests and required future settings.

These outcomes concern software loading, binding and runtime metadata.
The thirteen mathematical methods remain unrun, unimported and uncollected.
The joint packet still requires a complete scientific specification,
independent source-completeness review, exact main acceptance and strict
prospective admission from a clean isolated checkout. The inherited working
seat changes remain outside that checkout and outside these results.
