from __future__ import annotations

import json
import hashlib
from pathlib import Path

import matplotlib.pyplot as plt


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> int:
    root = Path(__file__).resolve().parents[3]  # origin-axiom/phase2
    cert_path = root / "outputs" / "tests" / "phase2_binding_certificate.json"
    if not cert_path.exists():
        raise FileNotFoundError(f"Missing certificate JSON: {cert_path}")

    cert = json.loads(cert_path.read_text(encoding="utf-8"))
    off = cert["off"]
    on = cert["on"]

    # Bar data
    labels = ["OFF raw", "OFF constrained", "ON raw", "ON constrained"]
    vals = [off["raw"], off["constrained"], on["raw"], on["constrained"]]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.bar(range(len(vals)), vals)
    ax.set_xticks(range(len(vals)))
    ax.set_xticklabels(labels, rotation=20, ha="right")
    ax.set_ylabel("|R|")
    ax.set_title("Phase 2 Binding Certificate: OFF non-invasive, ON applies floor")

    out_pdf = root / "outputs" / "figures" / "figF_binding_certificate.pdf"
    out_pdf.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(out_pdf)
    plt.close(fig)

    sig = sha256_file(out_pdf)
    (out_pdf.with_suffix(".sig.txt")).write_text(sig + "\n", encoding="utf-8")

    meta = {
        "source": str(cert_path),
        "off_run_id": cert["run_ids"]["off"],
        "on_run_id": cert["run_ids"]["on"],
        "off": off,
        "on": on,
        "pdf": str(out_pdf),
        "pdf_sha256": sig,
    }
    (out_pdf.with_suffix(".meta.json")).write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

    print("Wrote:", out_pdf)
    print("SHA256:", sig)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
