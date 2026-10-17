"""Shared figure style: Okabe-Ito colours, serif text matched to the body, vector PDF, the data's sha256 checked."""
import hashlib, pathlib, json
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt
ROOT = next(d for d in pathlib.Path(__file__).resolve().parents if (d / "frontier").is_dir())
OUT = pathlib.Path(__file__).resolve().parents[1] / "tex" / "figures"; OUT.mkdir(parents=True, exist_ok=True)
OI = {"black": "#000000", "orange": "#E69F00", "sky": "#56B4E9", "green": "#009E73", "yellow": "#F0E442",
      "blue": "#0072B2", "vermillion": "#D55E00", "purple": "#CC79A7", "grey": "#999999"}
plt.rcParams.update({"font.family": "serif", "font.size": 9, "axes.labelsize": 9, "legend.fontsize": 8,
                     "xtick.labelsize": 8, "ytick.labelsize": 8, "pdf.fonttype": 42, "axes.spines.top": False,
                     "axes.spines.right": False, "figure.dpi": 150})
def load_json(rel, sha_prefix=None):
    p = ROOT / rel; b = p.read_bytes()
    if sha_prefix: assert hashlib.sha256(b).hexdigest().startswith(sha_prefix), rel
    return json.loads(b)
def save(fig, name, source):
    fig.savefig(OUT / f"{name}.pdf", bbox_inches="tight", metadata={"Subject": f"origin-axiom; data: {source}"})
    plt.close(fig); print("wrote", name)
