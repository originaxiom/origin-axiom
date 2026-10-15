"""Load the instrument's definitions (everything above the line 'T0 = time.time()') into a namespace.
Does NOT run the cell blocks. Uses a fake __file__ inside the scratch dir."""
import pathlib, sys
SCR = pathlib.Path(__import__("tempfile").gettempdir()).joinpath("c2_review")
SRC = pathlib.Path(__file__).resolve().parents[2].joinpath("the_electrons_zero.py").read_text()
head = SRC.split("T0 = time.time()")[0]
def load():
    ns = {"__file__": str(SCR / "fake_instrument.py"), "__name__": "inst"}
    exec(compile(head, "the_electrons_zero_head", "exec"), ns)
    return ns
if __name__ == "__main__":
    ns = load()
    print(sorted(k for k in ns if not k.startswith("__"))[:80])
