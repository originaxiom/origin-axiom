# Default shell and research runtime differ

The first October 24 package-metadata query through the default python3
exited 1 with importlib.metadata.PackageNotFoundError for sympy. It was
a metadata query, not a SymPy or scientific-source import. Version
inspection identifies that default interpreter as CPython 3.9.6.

The separately configured existing research interpreter reports CPython
3.12.1, SymPy 1.14.0 and mpmath 1.3.0 using package metadata only.
The query explicitly checked that neither mathematical package had
entered sys.modules. ENVIRONMENT.json records this observation and
declares required future environment variables; it does not claim
those variables were active during metadata discovery.

The first three synthetic stdlib fixture runs used the shell's default
interpreter. Their outcomes remain software evidence for that runtime.
Run the unchanged strengthened fixtures separately under the recorded
research interpreter before transferring their evidence to that runtime.
No installation, dependency upgrade or substitution was performed.

The production runner verifies version and dependency metadata before
loading science. A wrong default interpreter must be rejected; do not
silently relax the research environment to match the current shell.
