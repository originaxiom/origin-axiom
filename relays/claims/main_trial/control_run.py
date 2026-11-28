"""How main's trial controls run an arc's script with one deliberate change (P-885; 2026-11-27).

The controls first ran the changed text with exec in their own process. The intake's guard (T7b, Review 88's item 4)
refuses exec, eval, compile and importlib in any script it reruns, because it cannot read what they run. So the changed
text is written beside the arc's script as `_control_<name>`, so that the script's own imports of its sibling files
still resolve, run as a separate process with this interpreter in that folder, and removed afterwards. The banked script
itself is never edited. Imported by the controls; prints nothing itself."""
import os
import pathlib
import subprocess
import sys


def run_changed(script, text, args=()):
    """(exit status, standard output, standard error) of `text` run in place of `script`, from the script's folder"""
    script = pathlib.Path(script)
    copy = script.with_name("_control_" + script.name)
    copy.write_text(text, encoding="utf-8")
    try:
        r = subprocess.run([sys.executable, "-B", str(copy), *map(str, args)], cwd=str(script.parent),
                           capture_output=True, text=True, env=dict(os.environ))
    finally:
        if copy.exists():
            copy.unlink()
    return r.returncode, r.stdout, r.stderr
