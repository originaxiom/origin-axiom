"""B52 -- multichannel Fibonacci physics-bridge control.

This probe tests the simplest possible three-channel Fibonacci tight-binding
bridge to PC12.  The result is a negative control: the physical transfer
matrices are naturally 6x6 symplectic matrices, and their trace recursion is
sixth-order rather than PC12's third-order SL(3) Cayley-Hamilton recursion.

No physical claim is promoted.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CheckResult:
    name: str
    ok: bool
    detail: str


def result(name: str, ok: bool, detail: str = "") -> CheckResult:
    return CheckResult(name=name, ok=ok, detail=detail)


def print_result(item: CheckResult) -> None:
    status = "OK" if item.ok else "FAIL"
    suffix = f" -- {item.detail}" if item.detail else ""
    print(f"{item.name}: {status}{suffix}")


def transfer_matrix(energy: float, onsite: np.ndarray, channel_coupling: np.ndarray) -> np.ndarray:
    """Return the doubled transfer matrix for a d-channel nearest-neighbor model."""
    dimension = onsite.shape[0]
    identity = np.eye(dimension)
    zero = np.zeros((dimension, dimension))
    step = energy * identity - channel_coupling - onsite
    return np.block([[step, -identity], [identity, zero]])


def symplectic_form(dimension: int) -> np.ndarray:
    identity = np.eye(dimension)
    zero = np.zeros((dimension, dimension))
    return np.block([[zero, identity], [-identity, zero]])


def deterministic_model() -> tuple[float, np.ndarray, np.ndarray, np.ndarray]:
    energy = 0.73
    channel_coupling = np.array(
        [
            [0.0, 0.2, -0.1],
            [0.2, 0.0, 0.15],
            [-0.1, 0.15, 0.0],
        ],
        dtype=float,
    )
    onsite_a = np.diag([0.4, -0.1, 0.2])
    onsite_b = np.diag([-0.2, 0.3, -0.35])
    return energy, onsite_a, onsite_b, channel_coupling


def check_transfer_group(tolerance: float = 1e-10) -> CheckResult:
    energy, onsite_a, onsite_b, coupling = deterministic_model()
    transfer_a = transfer_matrix(energy, onsite_a, coupling)
    transfer_b = transfer_matrix(energy, onsite_b, coupling)
    form = symplectic_form(3)

    det_a = np.linalg.det(transfer_a)
    det_b = np.linalg.det(transfer_b)
    symp_a = np.linalg.norm(transfer_a.T @ form @ transfer_a - form)
    symp_b = np.linalg.norm(transfer_b.T @ form @ transfer_b - form)

    ok = abs(det_a - 1.0) < tolerance and abs(det_b - 1.0) < tolerance
    ok = ok and symp_a < tolerance and symp_b < tolerance
    detail = f"det=({det_a:.6g},{det_b:.6g}), symplectic residual=({symp_a:.2e},{symp_b:.2e})"
    return result("6x6 SYMPLECTIC TRANSFER MATRICES", ok, detail)


def check_position_space_not_closed() -> CheckResult:
    energy, onsite_a, _, coupling = deterministic_model()
    transfer_a = transfer_matrix(energy, onsite_a, coupling)
    top_right_block = transfer_a[:3, 3:]
    lower_left_block = transfer_a[3:, :3]
    ok = np.linalg.norm(top_right_block) > 0.0 and np.linalg.norm(lower_left_block - np.eye(3)) < 1e-12
    detail = "second-order equation needs psi_n and psi_{n-1}; no position-only 3D transfer"
    return result("NO NATURAL 3D POSITION TRANSFER", ok, detail)


def channel_permutation() -> np.ndarray:
    """Map (q1,q2,q3,p1,p2,p3) to (q1,p1,q2,p2,q3,p3)."""
    permutation = [0, 3, 1, 4, 2, 5]
    return np.eye(6)[permutation]


def block_diagonal_part(matrix: np.ndarray) -> np.ndarray:
    blocks = [matrix[0:2, 0:2], matrix[2:4, 2:4], matrix[4:6, 4:6]]
    zero = np.zeros((2, 2))
    return np.block(
        [
            [blocks[0], zero, zero],
            [zero, blocks[1], zero],
            [zero, zero, blocks[2]],
        ]
    )


def check_commuting_control_decomposes_to_sl2(tolerance: float = 1e-10) -> CheckResult:
    energy = 0.73
    coupling = np.diag([0.2, -0.1, 0.05])
    onsite_a = np.diag([0.4, -0.1, 0.2])
    transfer_a = transfer_matrix(energy, onsite_a, coupling)
    permutation = channel_permutation()
    channel_order = permutation @ transfer_a @ permutation.T
    residual = np.linalg.norm(channel_order - block_diagonal_part(channel_order))
    block_dets = [float(np.linalg.det(channel_order[2 * i : 2 * i + 2, 2 * i : 2 * i + 2])) for i in range(3)]
    ok = residual < tolerance and all(abs(det - 1.0) < tolerance for det in block_dets)
    detail = f"block residual={residual:.2e}, block dets={[round(det, 12) for det in block_dets]}"
    return result("COMMUTING CONTROL IS THREE SL2 CHANNELS", ok, detail)


def pc12_third_order_residuals(transfer_a: np.ndarray, transfer_b: np.ndarray, max_k: int = 7) -> list[float]:
    x1 = float(np.trace(transfer_a))
    x4 = float(np.trace(np.linalg.inv(transfer_a)))
    traces = [float(np.trace(np.linalg.matrix_power(transfer_a, k) @ transfer_b)) for k in range(max_k + 1)]
    return [
        traces[k] - x1 * traces[k - 1] + x4 * traces[k - 2] - traces[k - 3]
        for k in range(3, max_k + 1)
    ]


def order_six_residuals(transfer_a: np.ndarray, transfer_b: np.ndarray, max_k: int = 7) -> list[float]:
    coefficients = np.poly(transfer_a)
    traces = [float(np.trace(np.linalg.matrix_power(transfer_a, k) @ transfer_b)) for k in range(max_k + 1)]
    residuals = []
    for k in range(6, max_k + 1):
        predicted = -sum(coefficients[j] * traces[k - j] for j in range(1, 7))
        residuals.append(float(traces[k] - predicted))
    return residuals


def check_trace_recursion_mismatch(tolerance: float = 1e-8) -> CheckResult:
    energy, onsite_a, onsite_b, coupling = deterministic_model()
    transfer_a = transfer_matrix(energy, onsite_a, coupling)
    transfer_b = transfer_matrix(energy, onsite_b, coupling)
    third_order = pc12_third_order_residuals(transfer_a, transfer_b)
    sixth_order = order_six_residuals(transfer_a, transfer_b)
    ok = max(abs(value) for value in third_order) > 1e-3
    ok = ok and max(abs(value) for value in sixth_order) < tolerance
    detail = (
        f"PC12 residual max={max(abs(value) for value in third_order):.3g}; "
        f"order-six residual max={max(abs(value) for value in sixth_order):.2e}"
    )
    return result("PC12 TRACE RECURSION FAILS; ORDER-6 HOLDS", ok, detail)


def run_checks() -> list[CheckResult]:
    return [
        check_transfer_group(),
        check_position_space_not_closed(),
        check_commuting_control_decomposes_to_sl2(),
        check_trace_recursion_mismatch(),
    ]


def main() -> int:
    print("B52 -- MULTICHANNEL FIBONACCI BRIDGE CONTROL")
    print("Status: negative control; no physics claim")
    print()
    checks = run_checks()
    for item in checks:
        print_result(item)
    ok = all(item.ok for item in checks)
    print()
    print(f"B52 BRIDGE CONTROL: {'OK' if ok else 'FAIL'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
