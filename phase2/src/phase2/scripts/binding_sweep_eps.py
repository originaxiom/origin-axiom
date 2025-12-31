from __future__ import annotations

import subprocess
from pathlib import Path
from datetime import datetime, timezone
import yaml


def phase2_root() -> Path:
    return Path(__file__).resolve().parents[3]  # .../origin-axiom/phase2


def utc_stamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def sh(cmd: str) -> None:
    subprocess.check_call(cmd, shell=True)


def main() -> int:
    root = phase2_root()

    base_cfg = root / "config" / "phase2.yaml"
    if not base_cfg.exists():
        raise FileNotFoundError(f"Missing base config: {base_cfg}")

    cfg = yaml.safe_load(base_cfg.read_text(encoding="utf-8"))

    # If you later add a sweep list in config, we can read it. For now, fallback is fine.
    eps_list = None
    try:
        eps_list = cfg.get("model", {}).get("epsilon", {}).get("sweep_values", None)
    except Exception:
        eps_list = None
    if not eps_list:
        eps_list = [1e-12, 1e-9, 1e-6, 1e-3, 1e-1, 1.0, 3.0, 10.0, 30.0, 100.0]

    tmp_dir = root / "outputs" / "tests" / f"_tmp_cfg_{utc_stamp()}"
    tmp_dir.mkdir(parents=True, exist_ok=True)

    ts = utc_stamp()

    for i, eps in enumerate(eps_list):
        cfg_i = yaml.safe_load(base_cfg.read_text(encoding="utf-8"))
        cfg_i.setdefault("model", {}).setdefault("constraint", {})["enabled"] = True
        cfg_i.setdefault("model", {}).setdefault("epsilon", {})["value"] = float(eps)

        out_cfg = tmp_dir / f"eps_{i:02d}.yaml"
        out_cfg.write_text(yaml.safe_dump(cfg_i, sort_keys=False), encoding="utf-8")

        # IMPORTANT: timestamp must be LAST token after '_' for Phase2 run_id contract
        run_id = f"phase2_epssweep_{i:02d}_{ts}"

        cmd = (
            f'cd "{root}" && PYTHONPATH="src" python -m phase2.modes.run_mode_sum '
            f'--config "{out_cfg}" --task residual --run-id "{run_id}"'
        )
        sh(cmd)

    print(f"Completed eps sweep: {len(eps_list)} runs. tmp_cfg_dir={tmp_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
