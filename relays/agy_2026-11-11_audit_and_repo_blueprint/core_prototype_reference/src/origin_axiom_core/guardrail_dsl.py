"""Zero-Trust Mathematical-Physics & Formal Verification Guardrail Compiler (Guardrails 1-6).

Enforces the Six Mathematical-Physics & Quantitative Modeling Guardrails plus
First-Class Equivariant Cochain Complexes via Python AST static analysis,
cryptographic gate sealing, and runtime tracked/phantom types:

  1. Guardrail 1 (No Zero-Bit Credit for Post-Inspection Selection):
     - `@stabilization_potential`: rejects target-coordinate identifiers or hardcoded
       coordinate shifts `(x - const)` and dynamically checks `||grad V(x*)|| < grad_tol`
       and `lambda_min(Hess V(x*)) > 0`.
     - `LedgerContext.select_from` + `@zero_bit_prediction`: charges `+log2(N)` bits
       for discrete candidate scans and blocks unpriced post-selection claims.
  2. Guardrail 2 (Ban Proof by Literal Flag/Zero Assignment):
     - `@theorem`, `@observable`, `@referee`: AST-scans return values, local aliases,
       subscript mutations, and constant-folded arithmetic, banning hardcoded booleans/zeros.
  3. Guardrail 3 (Mandatory Unitary Basis-Scrambling Gate):
     - `FramedMatrix` + `@observable`: blocks single-Dirac left-right SVD overlaps and
       scrambles all frames across independent Haar-random unitaries `U_L M U_R^dagger`
       asserting `< 1e-12` invariance.
  4. Guardrail 4 (Literature Benchmark Gate Before RGE Integration):
     - `GatedRGEIntegrator`: checks differential variable scaling (`ln_mu`, `ln_mu2`, `t_2pi`)
       and seals `.integrate_model()` behind an HMAC-SHA256 benchmark receipt (`<= 1e-3`).
  5. Guardrail 5 (Strict Non-Dimensionalization of Input Ledgers):
     - `LedgerContext` + `TrackedValue`: allows at most ONE dimensionful anchor (e.g. `v_EW`)
       and requires dimensionless output ratios before ledger finalization.
  6. Guardrail 6 (Zero-Trust Countercheck Rule for Referee Scripts):
     - `@producer` + `@referee`: statically and dynamically forbids a `@referee` from
       importing, calling, aliasing, reflecting, or reading cached output of any `@producer`.
"""

from __future__ import annotations

import ast
import dataclasses
import functools
import hashlib
import hmac
import inspect
import json
import math
import os
import textwrap
from typing import Any, Callable, Dict, List, Optional, Sequence, Set, Tuple, Union

import numpy as np


class GuardrailCompilerError(Exception):
    """Base exception for all static and dynamic guardrail violations."""


class Guardrail1PostInspectionError(GuardrailCompilerError):
    """Raised when a potential embeds its target vacuum or fails stabilization."""


class Guardrail1UnpricedScanError(GuardrailCompilerError):
    """Raised when discrete candidate selection bits are hidden in a 0-bit claim."""


class Guardrail2LiteralClaimError(GuardrailCompilerError):
    """Raised when a @theorem or @observable returns a hardcoded literal flag/zero."""


class Guardrail3IllegalLeftRightOverlapError(GuardrailCompilerError):
    """Raised when extracting left-right overlap V^T U or U^dagger V of a Dirac matrix."""


class Guardrail3BasisDependenceError(GuardrailCompilerError):
    """Raised when an @observable varies under Haar unitary basis scrambling."""


class Guardrail4BenchmarkGateError(GuardrailCompilerError):
    """Raised when RGE integration runs without or fails a literature benchmark."""


class Guardrail5UnpricedScaleError(GuardrailCompilerError):
    """Raised when a ledger uses >1 dimensionful anchor or leaves outputs dimensionful."""


class Guardrail6ProducerEchoError(GuardrailCompilerError):
    """Raised when a @referee function calls, imports, aliases, or echoes a @producer."""


class ComplexChainError(GuardrailCompilerError):
    """Raised when adjacent cochain differentials fail d_{k+1} d_k = 0."""


class IntertwinerError(GuardrailCompilerError):
    """Raised when a claimed symmetry operator is singular or fails to intertwine differentials."""


PRODUCER_REGISTRY: Set[str] = set()
_ACTIVE_REFEREE_STACK: List[str] = []
_ACTIVE_ZERO_BIT_SCAN_LOG: List[List[Tuple[str, float]]] = []
_RGE_GATE_SECRET: bytes = os.urandom(32)


class ProducerOutputDict(dict):
    """Tainted dictionary returned by a @producer function."""

    def __init__(self, *args: Any, producer_name: str = "<unknown>", **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.producer_name = producer_name


def _parse_function_ast(fn: Callable[..., Any]) -> ast.FunctionDef:
    try:
        src = textwrap.dedent(inspect.getsource(fn))
    except OSError as exc:
        raise GuardrailCompilerError(f"Cannot inspect source code of {fn.__name__}.") from exc
    tree = ast.parse(src)
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            return node  # type: ignore[return-value]
    raise GuardrailCompilerError(f"No FunctionDef found in AST of {fn.__name__}.")


def _is_pure_constant_expr(node: ast.AST, allowed_var_names: Set[str]) -> bool:
    has_constant = False
    for sub in ast.walk(node):
        if isinstance(sub, ast.Name):
            if sub.id in allowed_var_names:
                return False
            if sub.id not in {"math", "np", "numpy", "cmath", "sqrt", "pi", "e", "cos", "sin", "exp", "log"}:
                return False
        elif isinstance(sub, ast.Constant) and isinstance(sub.value, (int, float, complex)):
            has_constant = True
    return has_constant


def _is_forbidden_literal_node(node: ast.AST, local_vars: Optional[Set[str]] = None) -> Tuple[bool, str]:
    if isinstance(node, ast.Constant):
        if isinstance(node.value, bool):
            return True, f"boolean literal `{node.value!r}`"
        if isinstance(node.value, (int, float, complex)) and node.value == 0:
            return True, f"zero literal `{node.value!r}`"
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        is_lit, desc = _is_forbidden_literal_node(node.operand, local_vars)
        if is_lit:
            return True, f"signed {desc}"
    if isinstance(node, ast.BinOp):
        if isinstance(node.op, ast.Mult):
            for side in (node.left, node.right):
                if isinstance(side, ast.Constant) and isinstance(side.value, (int, float, complex)) and side.value == 0:
                    return True, f"zero-multiplier expression `{ast.unparse(node)}`"
        if local_vars is not None and _is_pure_constant_expr(node, local_vars):
            return True, f"constant-folded expression `{ast.unparse(node)}`"
    return False, ""


def _inspect_returned_ast_expr(
    node: ast.AST,
    tainted_locals: Dict[str, str],
    computed_vars: Set[str],
    fn_name: str,
    lineno: int,
) -> None:
    is_lit, desc = _is_forbidden_literal_node(node, computed_vars)
    if is_lit:
        raise Guardrail2LiteralClaimError(
            f"[Guardrail 2 AST Violation in `{fn_name}` line {lineno}]: Return of hardcoded {desc} is forbidden."
        )
    if isinstance(node, ast.Name) and node.id in tainted_locals:
        raise Guardrail2LiteralClaimError(
            f"[Guardrail 2 AST Violation in `{fn_name}` line {lineno}]: "
            f"Returned variable `{node.id}` holds hardcoded {tainted_locals[node.id]}."
        )
    if isinstance(node, ast.Dict):
        for val_node in node.values:
            if val_node is not None:
                _inspect_returned_ast_expr(val_node, tainted_locals, computed_vars, fn_name, lineno)
    elif isinstance(node, (ast.Tuple, ast.List, ast.Set)):
        for elt in node.elts:
            _inspect_returned_ast_expr(elt, tainted_locals, computed_vars, fn_name, lineno)
    elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == "dict":
        for kw in node.keywords:
            if kw.value is not None:
                _inspect_returned_ast_expr(kw.value, tainted_locals, computed_vars, fn_name, lineno)


def scan_ast_guardrail2_no_literal_claims(fn: Callable[..., Any]) -> None:
    fn_def = _parse_function_ast(fn)
    arg_names = {arg.arg for arg in fn_def.args.args}
    computed_vars: Set[str] = set(arg_names)
    tainted_locals: Dict[str, str] = {}
    pure_literal_containers: Set[str] = set()

    def _is_pure_literal_container(expr: ast.AST) -> bool:
        if isinstance(expr, ast.Constant):
            return True
        if isinstance(expr, (ast.Tuple, ast.List, ast.Set)):
            return all(_is_pure_literal_container(e) for e in expr.elts)
        if isinstance(expr, ast.Dict):
            return all((k is None or _is_pure_literal_container(k)) for k in expr.keys) and all(
                (v is not None and _is_pure_literal_container(v)) for v in expr.values
            )
        return False

    for node in ast.walk(fn_def):
        if isinstance(node, ast.Assign):
            is_lit, desc = _is_forbidden_literal_node(node.value, computed_vars)
            is_const_box = _is_pure_literal_container(node.value) and not isinstance(node.value, ast.Constant)
            for target in node.targets:
                if isinstance(target, ast.Name):
                    if is_lit:
                        tainted_locals[target.id] = desc
                    elif is_const_box:
                        pure_literal_containers.add(target.id)
                    else:
                        computed_vars.add(target.id)
                elif isinstance(target, ast.Subscript) and isinstance(target.value, ast.Name):
                    if is_lit:
                        tainted_locals[target.value.id] = f"subscript `{ast.unparse(target)} = {desc}`"
        elif isinstance(node, ast.AnnAssign) and node.value is not None:
            is_lit, desc = _is_forbidden_literal_node(node.value, computed_vars)
            if isinstance(node.target, ast.Name):
                if is_lit:
                    tainted_locals[node.target.id] = desc
                else:
                    computed_vars.add(node.target.id)

    def _only_pure_literals(expr: ast.AST) -> bool:
        if isinstance(expr, ast.Constant):
            return True
        if isinstance(expr, ast.Name):
            return expr.id in pure_literal_containers
        if isinstance(expr, ast.Subscript):
            return _only_pure_literals(expr.value) and _only_pure_literals(expr.slice)
        if isinstance(expr, (ast.Tuple, ast.List, ast.Set)):
            return all(_only_pure_literals(e) for e in expr.elts)
        return False

    for node in ast.walk(fn_def):
        if isinstance(node, ast.Assert) and isinstance(node.test, ast.Compare):
            operands = [node.test.left] + list(node.test.comparators)
            if all(_only_pure_literals(op) for op in operands):
                raise Guardrail2LiteralClaimError(
                    f"[Guardrail 2 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                    f"Tautological literal container assertion `{ast.unparse(node.test)}` is forbidden."
                )
        if isinstance(node, ast.Return) and node.value is not None:
            _inspect_returned_ast_expr(node.value, tainted_locals, computed_vars, fn.__name__, node.lineno)


def scan_ast_guardrail3_no_dirac_lr_overlap(fn: Callable[..., Any]) -> None:
    fn_def = _parse_function_ast(fn)
    svd_lr_pairs: List[Tuple[str, str]] = []
    for node in ast.walk(fn_def):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Call):
            call_str = ast.unparse(node.value.func) if hasattr(ast, "unparse") else ""
            if "svd" in call_str.lower():
                if len(node.targets) == 1 and isinstance(node.targets[0], ast.Tuple):
                    elts = node.targets[0].elts
                    if len(elts) == 3 and all(isinstance(e, ast.Name) for e in elts):
                        svd_lr_pairs.append((elts[0].id, elts[2].id))  # type: ignore[attr-defined]
    if not svd_lr_pairs:
        return
    for node in ast.walk(fn_def):
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.MatMult):
            names_left = {n.id for n in ast.walk(node.left) if isinstance(n, ast.Name)}
            names_right = {n.id for n in ast.walk(node.right) if isinstance(n, ast.Name)}
            for u_name, v_name in svd_lr_pairs:
                if (u_name in names_left and v_name in names_right) or (v_name in names_left and u_name in names_right):
                    raise Guardrail3IllegalLeftRightOverlapError(
                        f"[Guardrail 3 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                        f"Illegal left-right Dirac SVD overlap `{ast.unparse(node)}`."
                    )
        elif isinstance(node, ast.Call):
            func_str = ast.unparse(node.func) if hasattr(ast, "unparse") else ""
            if any(k in func_str for k in ("matmul", "dot", "einsum", "vdot", "inner")):
                arg_names = {n.id for a in node.args for n in ast.walk(a) if isinstance(n, ast.Name)}
                for u_name, v_name in svd_lr_pairs:
                    if u_name in arg_names and v_name in arg_names:
                        raise Guardrail3IllegalLeftRightOverlapError(
                            f"[Guardrail 3 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                            f"Illegal left-right Dirac SVD overlap in `{ast.unparse(node)}`."
                        )


def scan_ast_guardrail6_no_producer_in_referee(fn: Callable[..., Any]) -> None:
    fn_def = _parse_function_ast(fn)
    forbidden_keywords = {"producer", "cached_producer", "producer_output", "frontier"} | set(PRODUCER_REGISTRY)
    banned_reflection = {"getattr", "globals", "locals", "eval", "exec", "__import__", "open"}
    banned_io_modules = {"subprocess", "pickle", "shelve", "importlib"}
    banned_io_attrs = {"read_text", "read_bytes", "load", "loads", "loadtxt", "genfromtxt", "popen", "system"}

    for node in ast.walk(fn_def):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if any(k in alias.name for k in forbidden_keywords) or alias.name.split(".")[0] in banned_io_modules:
                    raise Guardrail6ProducerEchoError(
                        f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                        f"Forbidden import `{alias.name}`."
                    )
        elif isinstance(node, ast.ImportFrom):
            mod_name = node.module or ""
            if mod_name.split(".")[0] in banned_io_modules:
                raise Guardrail6ProducerEchoError(
                    f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                    f"Forbidden import from `{mod_name}`."
                )
            for alias in node.names:
                if any(k in mod_name for k in forbidden_keywords) or alias.name in PRODUCER_REGISTRY or "producer" in alias.name.lower():
                    raise Guardrail6ProducerEchoError(
                        f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                        f"Forbidden producer import `{alias.name}` from `{mod_name}`."
                    )
        elif isinstance(node, ast.Name):
            if node.id in PRODUCER_REGISTRY or "producer" in node.id.lower():
                raise Guardrail6ProducerEchoError(
                    f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                    f"References producer symbol `{node.id}`."
                )
            if node.id in banned_reflection or node.id in banned_io_modules:
                raise Guardrail6ProducerEchoError(
                    f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                    f"Forbidden reflection/IO `{node.id}`."
                )
        elif isinstance(node, ast.Attribute):
            if node.attr in PRODUCER_REGISTRY or "producer" in node.attr.lower() or node.attr in banned_io_attrs:
                raise Guardrail6ProducerEchoError(
                    f"[Guardrail 6 AST Violation in referee `{fn.__name__}` line {node.lineno}]: "
                    f"Forbidden producer/IO attribute `.{node.attr}`."
                )


def scan_ast_guardrail1_potential_target_free(
    fn: Callable[..., Any],
    forbidden_target_identifiers: Optional[Set[str]] = None,
) -> None:
    fn_def = _parse_function_ast(fn)
    arg_names = {arg.arg for arg in fn_def.args.args}
    default_forbidden = {
        "tau_target", "tau_star", "tau_golden", "x_target", "x_star",
        "target_vacuum", "re_tau_star", "im_tau_star",
    }
    if forbidden_target_identifiers:
        default_forbidden |= set(forbidden_target_identifiers)

    for node in ast.walk(fn_def):
        if isinstance(node, ast.Name) and node.id not in arg_names:
            low = node.id.lower()
            if node.id in default_forbidden or "target" in low or "star" in low or "golden" in low:
                raise Guardrail1PostInspectionError(
                    f"[Guardrail 1 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                    f"Potential references target identifier `{node.id}`."
                )
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Sub):
            if isinstance(node.left, ast.Name) and node.left.id in arg_names:
                if _is_pure_constant_expr(node.right, arg_names):
                    if not (isinstance(node.right, ast.Constant) and node.right.value == 0):
                        raise Guardrail1PostInspectionError(
                            f"[Guardrail 1 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                            f"Potential embeds coordinate shift `({ast.unparse(node.left)} - {ast.unparse(node.right)})`."
                        )
            if isinstance(node.right, ast.Constant):
                val = node.right.value
                if isinstance(val, float) and not val.is_integer():
                    raise Guardrail1PostInspectionError(
                        f"[Guardrail 1 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                        f"Potential embeds tuned non-integer constant `{val!r}`."
                    )
            elif _is_pure_constant_expr(node.right, arg_names):
                raise Guardrail1PostInspectionError(
                    f"[Guardrail 1 AST Violation in `{fn.__name__}` line {node.lineno}]: "
                    f"Potential embeds constant target expression `{ast.unparse(node.right)}`."
                )


def _assert_all_numeric_leaves_finite(val: Any, fn_name: str, key_path: str = "return") -> None:
    if isinstance(val, (int, float, complex, np.number)):
        if not np.isfinite(val):
            raise GuardrailCompilerError(f"Non-finite output in `{fn_name}` at `{key_path}`: {val!r}")
    elif isinstance(val, np.ndarray):
        if val.dtype.kind in {"i", "u", "f", "c"} and not np.all(np.isfinite(val)):
            raise GuardrailCompilerError(f"Array output contains NaN/Inf in `{fn_name}` at `{key_path}`.")
    elif isinstance(val, dict):
        for k, v in val.items():
            _assert_all_numeric_leaves_finite(v, fn_name, key_path=f"{key_path}.{k}")
    elif isinstance(val, (tuple, list, set, frozenset)):
        for idx, item in enumerate(val):
            _assert_all_numeric_leaves_finite(item, fn_name, key_path=f"{key_path}[{idx}]")


def _check_runtime_theorem_value(val: Any, fn_name: str, tol: float, key_path: str = "return") -> None:
    _assert_all_numeric_leaves_finite(val, fn_name, key_path=key_path)
    if isinstance(val, bool):
        raise Guardrail2LiteralClaimError(
            f"[Guardrail 2 Runtime Violation in `{fn_name}` at `{key_path}`]: returned boolean `{val}`."
        )
    if isinstance(val, dict):
        for k, v in val.items():
            _check_runtime_theorem_value(v, fn_name, tol, key_path=f"{key_path}.{k}")
            if any(tag in str(k).lower() for tag in ("residual", "error", "diff", "violation")):
                arr = np.asarray(v, dtype=float)
                val_float = float(np.max(np.abs(arr)))
                if val_float >= tol:
                    raise GuardrailCompilerError(
                        f"[@theorem `{fn_name}` Failed]: `{k}` = {val_float:.3e} >= {tol:.1e}."
                    )
    elif isinstance(val, (tuple, list)):
        for idx, item in enumerate(val):
            _check_runtime_theorem_value(item, fn_name, tol, key_path=f"{key_path}[{idx}]")


def theorem(tol: float = 1e-12) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        scan_ast_guardrail2_no_literal_claims(fn)

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            result = fn(*args, **kwargs)
            _check_runtime_theorem_value(result, fn.__name__, tol)
            return result

        return wrapper

    return decorator


def producer(fn: Callable[..., Any]) -> Callable[..., Any]:
    PRODUCER_REGISTRY.add(fn.__name__)

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        if _ACTIVE_REFEREE_STACK:
            raise Guardrail6ProducerEchoError(
                f"[Guardrail 6 Runtime Violation]: Referee `{_ACTIVE_REFEREE_STACK[-1]}` called producer `{fn.__name__}`."
            )
        res = fn(*args, **kwargs)
        if isinstance(res, dict):
            return ProducerOutputDict(res, producer_name=fn.__name__)
        return res

    return wrapper


def referee(fn: Callable[..., Any]) -> Callable[..., Any]:
    scan_ast_guardrail6_no_producer_in_referee(fn)
    scan_ast_guardrail2_no_literal_claims(fn)

    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        for a in list(args) + list(kwargs.values()):
            if isinstance(a, ProducerOutputDict):
                raise Guardrail6ProducerEchoError(
                    f"[Guardrail 6 Runtime Violation in `{fn.__name__}`]: received `ProducerOutputDict`."
                )
        _ACTIVE_REFEREE_STACK.append(fn.__name__)
        try:
            res = fn(*args, **kwargs)
        finally:
            _ACTIVE_REFEREE_STACK.pop()
        if isinstance(res, ProducerOutputDict):
            raise Guardrail6ProducerEchoError(f"[Guardrail 6 Runtime Violation in `{fn.__name__}`]: echoed producer dict.")
        _assert_all_numeric_leaves_finite(res, fn.__name__)
        return res

    return wrapper


def stabilization_potential(
    forbidden_target_identifiers: Optional[Set[str]] = None,
    grad_tol: float = 1e-8,
    eps: float = 1e-6,
) -> Callable[[Callable[..., float]], Callable[..., float]]:
    def decorator(fn: Callable[..., float]) -> Callable[..., float]:
        scan_ast_guardrail1_potential_target_free(fn, forbidden_target_identifiers)

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> float:
            val = float(fn(*args, **kwargs))
            if not math.isfinite(val):
                raise Guardrail1PostInspectionError(f"Potential `{fn.__name__}` returned non-finite {val}.")
            return val

        def verify_minimum(x_candidate: Union[float, Sequence[float], np.ndarray]) -> Dict[str, Any]:
            x = np.asarray(x_candidate, dtype=float).ravel()
            if not np.all(np.isfinite(x)):
                raise Guardrail1PostInspectionError("Candidate vacuum coordinate contains NaN/Inf.")
            n = x.size
            grad = np.zeros(n, dtype=float)
            hess = np.zeros((n, n), dtype=float)
            f0 = wrapper(x if n > 1 else float(x[0]))
            for i in range(n):
                dx_i = np.zeros(n, dtype=float)
                dx_i[i] = eps
                fp = wrapper((x + dx_i) if n > 1 else float(x[0] + eps))
                fm = wrapper((x - dx_i) if n > 1 else float(x[0] - eps))
                grad[i] = (fp - fm) / (2.0 * eps)
                hess[i, i] = (fp - 2.0 * f0 + fm) / (eps ** 2)
                for j in range(i + 1, n):
                    dx_j = np.zeros(n, dtype=float)
                    dx_j[j] = eps
                    hij = (
                        wrapper(x + dx_i + dx_j)
                        - wrapper(x + dx_i - dx_j)
                        - wrapper(x - dx_i + dx_j)
                        + wrapper(x - dx_i - dx_j)
                    ) / (4.0 * eps * eps)
                    hess[i, j] = hij
                    hess[j, i] = hij
            grad_norm = float(np.linalg.norm(grad))
            min_eig = float(np.min(np.linalg.eigvalsh(hess)))
            if not math.isfinite(grad_norm) or grad_norm >= grad_tol:
                raise Guardrail1PostInspectionError(f"||grad V|| = {grad_norm:.3e} >= {grad_tol:.1e}.")
            if not math.isfinite(min_eig) or min_eig <= 0.0:
                raise Guardrail1PostInspectionError(f"min Hessian eig = {min_eig:.3e} <= 0.")
            return {
                "x_star": x.tolist(),
                "potential_value": f0,
                "grad_norm": grad_norm,
                "min_hessian_eigval": min_eig,
            }

        wrapper.verify_minimum = verify_minimum  # type: ignore[attr-defined]
        return wrapper

    return decorator


def _parse_unit_map(unit: Union[str, Dict[str, int], None]) -> Dict[str, int]:
    if unit is None or unit in ("", "1", "dimensionless"):
        return {}
    if isinstance(unit, dict):
        return {k: v for k, v in unit.items() if v != 0}
    return {unit: 1}


def _format_unit_map(unit_map: Dict[str, int]) -> str:
    if not unit_map:
        return "1"
    return "*".join(k if unit_map[k] == 1 else f"{k}^{unit_map[k]}" for k in sorted(unit_map))


@dataclasses.dataclass(frozen=True)
class TrackedValue:
    value: Union[float, np.ndarray]
    unit_map: Dict[str, int] = dataclasses.field(default_factory=dict)
    selection_events: frozenset[Tuple[str, float]] = dataclasses.field(default_factory=frozenset)
    empirical_sources: frozenset[str] = dataclasses.field(default_factory=frozenset)
    anchor_sources: frozenset[str] = dataclasses.field(default_factory=frozenset)

    @property
    def unit(self) -> str:
        return _format_unit_map(self.unit_map)

    @property
    def is_dimensionless(self) -> bool:
        return len(self.unit_map) == 0

    @property
    def selection_bits(self) -> float:
        return float(sum(bits for _, bits in self.selection_events))

    def _coerce(self, other: Any) -> "TrackedValue":
        if isinstance(other, TrackedValue):
            return other
        if isinstance(other, (int, float, np.number, np.ndarray)):
            return TrackedValue(value=float(other) if isinstance(other, (int, float, np.number)) else other)
        raise TypeError(f"Cannot combine TrackedValue with {type(other)!r}")

    def _merge(
        self, other: "TrackedValue", new_u: Dict[str, int]
    ) -> Tuple[Dict[str, int], frozenset[Tuple[str, float]], frozenset[str], frozenset[str]]:
        anc = self.anchor_sources | other.anchor_sources
        if len(anc) > 1:
            raise Guardrail5UnpricedScaleError(f"Multiple dimensionful anchors {sorted(anc)} combined.")
        return (
            {k: v for k, v in new_u.items() if v != 0},
            self.selection_events | other.selection_events,
            self.empirical_sources | other.empirical_sources,
            anc,
        )

    def __mul__(self, other: Any) -> "TrackedValue":
        o = self._coerce(other)
        nu = dict(self.unit_map)
        for k, e in o.unit_map.items():
            nu[k] = nu.get(k, 0) + e
        u, s, em, an = self._merge(o, nu)
        return TrackedValue(self.value * o.value, u, s, em, an)

    def __rmul__(self, other: Any) -> "TrackedValue":
        return self.__mul__(other)

    def __truediv__(self, other: Any) -> "TrackedValue":
        o = self._coerce(other)
        nu = dict(self.unit_map)
        for k, e in o.unit_map.items():
            nu[k] = nu.get(k, 0) - e
        u, s, em, an = self._merge(o, nu)
        return TrackedValue(self.value / o.value, u, s, em, an)


class LedgerContext:
    def __init__(self, name: str = "default_ledger") -> None:
        self.name = name
        self.anchor_name: Optional[str] = None
        self.anchor_unit: Optional[str] = None
        self.anchor_value: Optional[TrackedValue] = None
        self.imported_ratios: Dict[str, TrackedValue] = {}
        self.scan_counter: int = 0

    def declare_anchor(self, name: str, value: float, unit: str) -> TrackedValue:
        umap = _parse_unit_map(unit)
        if not umap:
            raise Guardrail5UnpricedScaleError(f"Anchor `{name}` must carry a dimensionful unit.")
        if self.anchor_name is not None:
            raise Guardrail5UnpricedScaleError(
                f"Cannot declare second dimensionful anchor `{name}`; `{self.anchor_name}` is already fixed."
            )
        self.anchor_name = name
        self.anchor_unit = unit
        tv = TrackedValue(value=float(value), unit_map=umap, anchor_sources=frozenset({name}))
        self.anchor_value = tv
        return tv

    def import_dimensionless_ratio(
        self, name: str, value_in_anchor_units: float, anchor: Optional[TrackedValue] = None
    ) -> TrackedValue:
        anc = anchor or self.anchor_value
        ratio = float(value_in_anchor_units) / float(anc.value) if anc is not None else float(value_in_anchor_units)
        tv = TrackedValue(
            value=ratio,
            unit_map={},
            empirical_sources=frozenset({name}),
            anchor_sources=anc.anchor_sources if anc is not None else frozenset(),
        )
        self.imported_ratios[name] = tv
        return tv

    def select_from(
        self, candidates: Sequence[Any], score_fn: Callable[[Any], float], label: str = "discrete_scan"
    ) -> TrackedValue:
        n = len(candidates)
        if n == 0:
            raise ValueError("select_from requires >= 1 candidate.")
        best_c = min(candidates, key=score_fn)
        bits = math.log2(n) if n > 1 else 0.0
        self.scan_counter += 1
        ev = (f"{label}#{self.scan_counter}(N={n})", bits)
        if bits > 0.0 and _ACTIVE_ZERO_BIT_SCAN_LOG:
            _ACTIVE_ZERO_BIT_SCAN_LOG[-1].append(ev)
        if isinstance(best_c, TrackedValue):
            return TrackedValue(
                value=best_c.value,
                unit_map=dict(best_c.unit_map),
                selection_events=best_c.selection_events | ({ev} if bits > 0 else frozenset()),
                empirical_sources=best_c.empirical_sources,
                anchor_sources=best_c.anchor_sources,
            )
        return TrackedValue(value=best_c, unit_map={}, selection_events=frozenset({ev}) if bits > 0 else frozenset())

    def finalize_prediction(self, prediction: TrackedValue) -> Dict[str, Any]:
        if not prediction.is_dimensionless:
            raise Guardrail5UnpricedScaleError(f"Prediction carries un-normalized unit `{prediction.unit}`.")
        return {
            "dimensionless_value": float(np.asarray(prediction.value)),
            "unit": prediction.unit,
            "selection_bits": prediction.selection_bits,
            "empirical_sources": sorted(prediction.empirical_sources),
            "empirical_input_count": len(prediction.empirical_sources),
            "anchor_used": sorted(prediction.anchor_sources),
        }


def zero_bit_prediction(fn: Callable[..., TrackedValue]) -> Callable[..., TrackedValue]:
    @functools.wraps(fn)
    def wrapper(*args: Any, **kwargs: Any) -> TrackedValue:
        _ACTIVE_ZERO_BIT_SCAN_LOG.append([])
        try:
            res = fn(*args, **kwargs)
            ambient = list(_ACTIVE_ZERO_BIT_SCAN_LOG[-1])
        finally:
            _ACTIVE_ZERO_BIT_SCAN_LOG.pop()
        if not isinstance(res, TrackedValue):
            raise GuardrailCompilerError(f"`{fn.__name__}` must return TrackedValue.")
        events = set(res.selection_events) | set(ambient)
        bits = sum(b for _, b in events)
        if bits > 0.0 or len(res.empirical_sources) > 0:
            raise Guardrail1UnpricedScanError(
                f"`{fn.__name__}` claims 0 bits, but incurred {bits:.2f} selection bits and {len(res.empirical_sources)} empirical inputs."
            )
        return res

    return wrapper


def haar_random_unitary(n: int, rng: np.random.Generator) -> np.ndarray:
    z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / math.sqrt(2.0)
    q, r = np.linalg.qr(z)
    d = np.diag(r)
    ph = np.where(np.abs(d) > 0, d / np.abs(d), 1.0 + 0.0j)
    return q * ph[np.newaxis, :]


@dataclasses.dataclass
class FramedMatrix:
    matrix: np.ndarray
    left_frame: str
    right_frame: str
    is_majorana_symmetric: bool = False

    def __post_init__(self) -> None:
        self.matrix = np.asarray(self.matrix, dtype=complex)
        if self.matrix.ndim != 2 or not np.all(np.isfinite(self.matrix)):
            raise Guardrail3BasisDependenceError("Invalid or non-finite FramedMatrix.")
        if self.is_majorana_symmetric:
            if self.left_frame != self.right_frame or float(np.linalg.norm(self.matrix - self.matrix.T)) > 1e-12:
                raise Guardrail3IllegalLeftRightOverlapError("Invalid Majorana symmetric FramedMatrix.")

    def transform(self, frame_unitaries: Dict[str, np.ndarray]) -> "FramedMatrix":
        u_l = frame_unitaries[self.left_frame]
        new_m = u_l @ self.matrix @ (u_l.T if self.is_majorana_symmetric else frame_unitaries[self.right_frame].conj().T)
        return FramedMatrix(new_m, self.left_frame, self.right_frame, self.is_majorana_symmetric)


def observable(
    haar_samples: int = 24,
    tol: float = 1e-12,
    seed: int = 20261111,
    distinct_right_frames: bool = False,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
        scan_ast_guardrail2_no_literal_claims(fn)
        scan_ast_guardrail3_no_dirac_lr_overlap(fn)

        @functools.wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            base_val = fn(*args, **kwargs)
            base_arr = np.asarray(base_val, dtype=complex)
            if not np.all(np.isfinite(base_arr)):
                raise Guardrail3BasisDependenceError(f"`{fn.__name__}` returned NaN/Inf.")
            frame_dims: Dict[str, int] = {}
            right_seen: List[str] = []

            def _collect(obj: Any) -> None:
                if isinstance(obj, FramedMatrix):
                    if not obj.is_majorana_symmetric and obj.left_frame == obj.right_frame:
                        raise Guardrail3IllegalLeftRightOverlapError("Dirac frame collision.")
                    right_seen.append(obj.right_frame)
                    frame_dims[obj.left_frame] = obj.matrix.shape[0]
                    frame_dims[obj.right_frame] = obj.matrix.shape[1]
                elif isinstance(obj, (list, tuple)):
                    for x in obj:
                        _collect(x)
                elif isinstance(obj, dict):
                    for x in obj.values():
                        _collect(x)

            _collect(args)
            _collect(kwargs)
            if not frame_dims:
                raise Guardrail3BasisDependenceError(f"`{fn.__name__}` requires FramedMatrix input.")
            if distinct_right_frames and len(right_seen) != len(set(right_seen)):
                raise Guardrail3BasisDependenceError("Duplicate right-handed frames.")

            def _xf(obj: Any, us: Dict[str, np.ndarray]) -> Any:
                if isinstance(obj, FramedMatrix):
                    return obj.transform(us)
                if isinstance(obj, list):
                    return [_xf(x, us) for x in obj]
                if isinstance(obj, tuple):
                    return tuple(_xf(x, us) for x in obj)
                if isinstance(obj, dict):
                    return {k: _xf(v, us) for k, v in obj.items()}
                return obj

            rng = np.random.default_rng(seed)
            for _ in range(haar_samples):
                us = {f: haar_random_unitary(d, rng) for f, d in frame_dims.items()}
                s_arr = np.asarray(fn(*_xf(args, us), **_xf(kwargs, us)), dtype=complex)
                dev = float(np.max(np.abs(s_arr - base_arr)))
                if not np.all(np.isfinite(s_arr)) or dev >= tol:
                    raise Guardrail3BasisDependenceError(f"`{fn.__name__}` varied by {dev:.3e} under Haar scrambling.")
            return base_val

        return wrapper

    return decorator


class GatedRGEIntegrator:
    VALID_LOG_VARIABLES: Dict[str, float] = {
        "ln_mu": 1.0,
        "ln_mu2": 2.0,
        "t_2pi": 1.0 / (2.0 * math.pi),
    }

    def __init__(
        self,
        rhs_fn: Callable[[float, np.ndarray], np.ndarray],
        log_variable: str = "ln_mu",
        declared_multiplier_to_dln_mu: Optional[float] = None,
    ) -> None:
        if log_variable not in self.VALID_LOG_VARIABLES:
            raise Guardrail4BenchmarkGateError(f"Invalid log_variable `{log_variable}`.")
        expected = self.VALID_LOG_VARIABLES[log_variable]
        if declared_multiplier_to_dln_mu is not None and abs(declared_multiplier_to_dln_mu - expected) > 1e-12:
            raise Guardrail4BenchmarkGateError("Differential variable multiplier mismatch.")
        self.rhs_fn = rhs_fn
        self.log_variable = log_variable
        self.multiplier_to_dln_mu = expected
        self._benchmark_verified = False
        self._seal_token: Optional[str] = None
        self.benchmark_receipt: Optional[Dict[str, Any]] = None

    def _compute_hmac_seal(self, receipt: Dict[str, Any]) -> str:
        payload = json.dumps(
            {"id": id(self), "rhs": id(self.rhs_fn), "var": self.log_variable, "receipt": receipt},
            sort_keys=True,
        ).encode("utf-8")
        return hmac.new(_RGE_GATE_SECRET, payload, hashlib.sha256).hexdigest()

    def _rk4(self, y0: np.ndarray, mu_init: float, mu_final: float, n_steps: int = 2000) -> np.ndarray:
        h = math.log(mu_final / mu_init) / float(n_steps)
        y = np.asarray(y0, dtype=float).copy()
        s = self.multiplier_to_dln_mu
        tau = 0.0
        for _ in range(n_steps):
            k1 = s * np.asarray(self.rhs_fn(s * tau, y), dtype=float)
            k2 = s * np.asarray(self.rhs_fn(s * (tau + 0.5 * h), y + 0.5 * h * k1), dtype=float)
            k3 = s * np.asarray(self.rhs_fn(s * (tau + 0.5 * h), y + 0.5 * h * k2), dtype=float)
            k4 = s * np.asarray(self.rhs_fn(s * (tau + h), y + h * k3), dtype=float)
            y = y + (h / 6.0) * (k1 + 2.0 * k2 + 2.0 * k3 + k4)
            tau += h
        if not np.all(np.isfinite(y)):
            raise Guardrail4BenchmarkGateError("RGE trajectory diverged.")
        return y

    def verify_literature_benchmark(
        self,
        y0: Sequence[float],
        mu_init: float,
        mu_target: float,
        published_target: Sequence[float],
        rtol: float = 1e-3,
        citation: str = "Literature Benchmark",
    ) -> Dict[str, Any]:
        if rtol > 1e-3:
            raise Guardrail4BenchmarkGateError("rtol must be <= 1e-3 (>= 3 sig figs).")
        y_num = self._rk4(np.atleast_1d(np.asarray(y0, dtype=float)), mu_init, mu_target)
        y_pub = np.atleast_1d(np.asarray(published_target, dtype=float))
        rel_err = float(np.max(np.abs(y_num - y_pub) / np.maximum(np.abs(y_pub), 1e-15)))
        if not math.isfinite(rel_err) or rel_err > rtol:
            raise Guardrail4BenchmarkGateError(f"Benchmark `{citation}` failed: rel_err={rel_err:.3e} > {rtol:.1e}.")
        receipt = {"citation": citation, "relative_error": rel_err, "integrated_value": y_num.tolist()}
        self.benchmark_receipt = receipt
        self._benchmark_verified = True
        self._seal_token = self._compute_hmac_seal(receipt)
        return receipt

    def integrate_model(self, y0: Sequence[float], mu_init: float, mu_final: float) -> np.ndarray:
        if not self._benchmark_verified or self.benchmark_receipt is None or self._seal_token is None:
            raise Guardrail4BenchmarkGateError("Gate locked before benchmark verification.")
        if not hmac.compare_digest(self._seal_token, self._compute_hmac_seal(self.benchmark_receipt)):
            raise Guardrail4BenchmarkGateError("Benchmark seal tampered.")
        return self._rk4(np.atleast_1d(np.asarray(y0, dtype=float)), mu_init, mu_final)


@dataclasses.dataclass
class IntertwinerSpec:
    degree: int
    op_k: np.ndarray
    op_k_plus_1: np.ndarray
    eta_phase: complex = 1.0 + 0.0j
    target_differential: Optional[np.ndarray] = None
    name: str = "symmetry_intertwiner"


class EquivariantCochainComplex:
    def __init__(
        self,
        differentials: Sequence[np.ndarray],
        grading_dims: Optional[Sequence[int]] = None,
        intertwiners: Optional[Sequence[IntertwinerSpec]] = None,
        tol: float = 1e-12,
    ) -> None:
        self.differentials = [np.asarray(d, dtype=complex) for d in differentials]
        self.tol = tol
        self.grading_dims = (
            list(grading_dims)
            if grading_dims is not None
            else [self.differentials[0].shape[1]] + [d.shape[0] for d in self.differentials]
        )
        self.chain_residuals: List[float] = []
        for k in range(len(self.differentials) - 1):
            res = float(np.linalg.norm(self.differentials[k + 1] @ self.differentials[k], ord="fro"))
            self.chain_residuals.append(res)
            if not math.isfinite(res) or res >= self.tol:
                raise ComplexChainError(f"||d_{k+1} d_{k}||_F = {res:.3e} >= {self.tol:.1e}.")
        self.intertwiner_residuals: Dict[str, float] = {}
        if intertwiners:
            for spec in intertwiners:
                k = spec.degree
                d_src = self.differentials[k]
                d_tgt = np.asarray(spec.target_differential, dtype=complex) if spec.target_differential is not None else d_src
                a_k = np.asarray(spec.op_k, dtype=complex)
                a_kp1 = np.asarray(spec.op_k_plus_1, dtype=complex)
                if np.linalg.matrix_rank(a_k, tol=1e-10) < a_k.shape[0] or np.linalg.matrix_rank(a_kp1, tol=1e-10) < a_kp1.shape[0]:
                    raise IntertwinerError(f"Singular intertwiner `{spec.name}`.")
                res = float(np.linalg.norm(a_kp1 @ d_src - complex(spec.eta_phase) * (d_tgt @ a_k), ord="fro"))
                self.intertwiner_residuals[spec.name] = res
                if not math.isfinite(res) or res >= self.tol:
                    raise IntertwinerError(f"Intertwiner `{spec.name}` residual {res:.3e} >= {self.tol:.1e}.")
        self.ranks = [int(np.linalg.matrix_rank(d, tol=1e-10)) if d.size > 0 else 0 for d in self.differentials]
        self.betti_numbers = [
            self.grading_dims[k]
            - (self.ranks[k] if k < len(self.ranks) else 0)
            - (self.ranks[k - 1] if k > 0 else 0)
            for k in range(len(self.grading_dims))
        ]
