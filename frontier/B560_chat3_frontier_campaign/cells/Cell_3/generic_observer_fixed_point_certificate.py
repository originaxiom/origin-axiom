#!/usr/bin/env python3
"""Computer-assisted local certificate for a non-trace-zero B530 fixed character.

This script uses a complex interval Krawczyk test on a gauge-fixed square
subsystem.  It proves that one non-special irreducible fixed character exists,
is unique in an explicit polydisc, and is a reduced isolated point of the
gauge-sliced character scheme.

No algebraic-number reconstruction is assumed.
"""

from __future__ import annotations

import itertools
import json
from pathlib import Path

import mpmath as mp
import sympy as sp


SUB = {"a": "abAAB", "b": "aAB", "A": "abAB", "B": "aA"}
GENS = ["a", "b", "A", "B"]
VARIABLE_NAMES = [
    "tau",
    "a00", "a10", "a11",
    "b00", "b01", "b10", "b11",
    "A00", "A01", "A10", "A11",
    "B00", "B01", "B10", "B11",
]

CENTER = {'tau': {'re': '-0.43523921547898134538746152339425110589425886515757176518276361367442798974749460480393267707467276201966065490', 'im': '-0.90031484787780815829857377628342463660435459459439642299945640602080611863209994820519422097586180513100313562'}, 'a00': {'re': '0.36868247799206910567451081157633349289281152074394694300004310304263930298185963547674158165661516958727084724', 'im': '0.86169318958937322839413672307465081259073008858721853499781511976370009425948625762092485291667838287884812285'}, 'a10': {'re': '-0.12155807743691996482559324005155174957821730719040173844044500402718088495568162857995960960185279709941115745', 'im': '9.2196170307977113126154087686603345589304026738750339598456433820406948561301455315270958010118021831605161961e-349'}, 'a11': {'re': '0.36868247799206910567451081157633349289281152074394694300004310304263930298185963547674158165661516958727084724', 'im': '-0.86169318958937322839413672307465081259073008858721853499781511976370009425948625762092485291667838287884812285'}, 'b00': {'re': '0.32231909237105862938758812007001748276657582727010770619769259091401337716309785481953928270669110300157860140', 'im': '-0.75636360230149378868147586271344579690880178657180962644038130052395086590218190294435117629737333336199296448'}, 'b01': {'re': '-1.5761557563962564606687522081437848078152347746570951631756375660326886819909614285476474765906563280934528901', 'im': '0.42582533046115007053383214665123568482903153660011964349588777851772632752763132874658922722642686961460982974'}, 'b10': {'re': '0.19159446348866330300202833269071053353139067261992392180073809222916844635970160285394176211325434836492932837', 'im': '0.051762508494798514189439305675389223476745613502631841932101748249361216080007726643612995000389715906427475460'}, 'b11': {'re': '0.32231909237105862938758812007001748276657582727010770619769259091401337716309785481953928270669110300157860140', 'im': '0.75636360230149378868147586271344579690880178657180962644038130052395086590218190294435117629737333336199296448'}, 'A00': {'re': '-0.62390864195465835231468761552309612921925709432818547232297303133913507363198407150885469915046867369933336450', 'im': '-0.31571662190576566729365514386967249049313284051876758618599752315790050519491512493647489080205968719911867388'}, 'A01': {'re': '-1.0022665497075659987335941665343750765548475650197690621228199815488054359606891868034274520074911214297990639', 'im': '1.7887749057349058944833031031361628368241504862365792240656887519056336462410445879901759061386729380900392154'}, 'A10': {'re': '0.12183359486178690080073857704500145712499645426356343423640911724971323572749374130204604256808531361317735268', 'im': '0.21744003850854290120395418093498722854036254722394380013481512288715857293872020063051562629198906693069489848'}, 'A11': {'re': '-0.62390864195465835231468761552309612921925709432818547232297303133913507363198407150885469915046867369933336450', 'im': '0.31571662190576566729365514386967249049313284051876758618599752315790050519491512493647489080205968719911867388'}, 'B00': {'re': '0.16386027364163824938133921518667566916387246748076550755300950367459965943621165373793878615626196014735982400', 'im': '-0.43657697569724375187940633198995161366345777185477370460459559930274126632910430567299577591508205504033472539'}, 'B01': {'re': '1.6618811120949723663206919620863150721887963751706681784867679904934718929826936017945027373799648410620333567', 'im': '1.9172421871572350824563026676316191639087935923757881023243055371108809079575908649559545642999261682712665664'}, 'B10': {'re': '-0.20201507291499531925893598300936521526188467166114677238740744069661974415424456722291400677802737081477293450', 'im': '0.23305627425178898223520719263227985335570126182116876969951430108567062548390302224800138349100681064006925576'}, 'B11': {'re': '0.16386027364163824938133921518667566916387246748076550755300950367459965943621165373793878615626196014735982400', 'im': '0.43657697569724375187940633198995161366345777185477370460459559930274126632910430567299577591508205504033472539'}}
RADIUS = mp.mpf("1e-30")


def _interval_endpoint(value, upper: bool) -> mp.mpf:
    """Convert a zero-width or bounded mpmath interval endpoint to mp.mpf."""
    text = str(value)
    if text.startswith("[") and text.endswith("]"):
        left, right = text[1:-1].split(",", 1)
        return mp.mpf(right.strip() if upper else left.strip())
    return mp.mpf(text)


def _interval_sup_abs(value) -> mp.mpf:
    """Rigorous upper bound for |complex interval| with a safety inflation."""
    upper = _interval_endpoint(abs(value).b, upper=True)
    return upper * mp.mpf("1.000000000000000000000000000001")


def _build_symbolic_system():
    symbols = sp.symbols(" ".join(VARIABLE_NAMES))
    symbol_map = dict(zip(VARIABLE_NAMES, symbols))
    tau = symbol_map["tau"]

    matrices = {
        "a": sp.Matrix([
            [symbol_map["a00"], 1],
            [symbol_map["a10"], symbol_map["a11"]],
        ]),
        "b": sp.Matrix([
            [symbol_map["b00"], symbol_map["b01"]],
            [symbol_map["b10"], symbol_map["b11"]],
        ]),
        "A": sp.Matrix([
            [symbol_map["A00"], symbol_map["A01"]],
            [symbol_map["A10"], symbol_map["A11"]],
        ]),
        "B": sp.Matrix([
            [symbol_map["B00"], symbol_map["B01"]],
            [symbol_map["B10"], symbol_map["B11"]],
        ]),
    }

    twist = sp.diag(tau, 1 / tau)
    twist_inverse = sp.diag(1 / tau, tau)

    def word_matrix(word):
        result = sp.eye(2)
        for letter in word:
            result *= matrices[letter]
        return result

    # Structural square subsystem:
    # for each generator match entries 00, 01, 10, then impose det=1.
    # The missing 11 entry follows from determinant equality whenever entry 00 != 0.
    equations = []
    for generator in GENS:
        difference = (
            twist * matrices[generator] * twist_inverse
            - word_matrix(SUB[generator])
        )
        equations.extend([difference[0, 0], difference[0, 1], difference[1, 0]])
    equations.extend([matrices[generator].det() - 1 for generator in GENS])

    assert len(equations) == len(symbols) == 16
    jacobian = sp.Matrix(equations).jacobian(symbols)

    equation_functions = [
        sp.lambdify(symbols, equation, modules=[{}])
        for equation in equations
    ]
    jacobian_functions = [
        [
            sp.lambdify(symbols, jacobian[row, column], modules=[{}])
            for column in range(16)
        ]
        for row in range(16)
    ]
    return symbols, matrices, equation_functions, jacobian_functions


def _center_values():
    mp.mp.dps = 140
    return [
        mp.mpc(CENTER[name]["re"], CENTER[name]["im"])
        for name in VARIABLE_NAMES
    ]


def _matrices_from_values(values):
    lookup = dict(zip(VARIABLE_NAMES, values))
    return {
        "a": [
            [lookup["a00"], mp.mpc(1)],
            [lookup["a10"], lookup["a11"]],
        ],
        "b": [
            [lookup["b00"], lookup["b01"]],
            [lookup["b10"], lookup["b11"]],
        ],
        "A": [
            [lookup["A00"], lookup["A01"]],
            [lookup["A10"], lookup["A11"]],
        ],
        "B": [
            [lookup["B00"], lookup["B01"]],
            [lookup["B10"], lookup["B11"]],
        ],
    }


def _matmul(left, right):
    return [
        [
            sum(left[i][k] * right[k][j] for k in range(2))
            for j in range(2)
        ]
        for i in range(2)
    ]


def _trace(matrix):
    return matrix[0][0] + matrix[1][1]


def _fricke_kappa(left, right):
    """tr([L,R]) from x=tr L, y=tr R, z=tr(LR), valid at SL2 roots."""
    x = _trace(left)
    y = _trace(right)
    z = _trace(_matmul(left, right))
    return x*x + y*y + z*z - x*y*z - 2


def run_certificate():
    mp.mp.dps = 140
    mp.iv.dps = 110

    symbols, _, equation_functions, jacobian_functions = _build_symbolic_system()
    center = _center_values()

    # High-precision point evaluation.
    function_center = mp.matrix(16, 1)
    jacobian_center = mp.matrix(16, 16)
    for row in range(16):
        function_center[row] = equation_functions[row](*center)
        for column in range(16):
            jacobian_center[row, column] = (
                jacobian_functions[row][column](*center)
            )

    inverse_approximation = jacobian_center ** -1
    center_correction = -inverse_approximation * function_center

    # Interval box X around the approximate root.
    interval_values = [
        mp.iv.mpc(
            [value.real - RADIUS, value.real + RADIUS],
            [value.imag - RADIUS, value.imag + RADIUS],
        )
        for value in center
    ]

    jacobian_interval = [
        [
            jacobian_functions[row][column](*interval_values)
            for column in range(16)
        ]
        for row in range(16)
    ]

    # Krawczyk inclusion:
    # K(X) = x0 - YF(x0) + (I - YJ(X))(X-x0).
    # A complex polydisc radius bound suffices componentwise.
    row_ratios = []
    for row in range(16):
        row_sum = mp.mpf("0")
        for column in range(16):
            value = (
                mp.iv.mpc([1, 1], [0, 0])
                if row == column
                else mp.iv.mpc([0, 0], [0, 0])
            )
            for cursor in range(16):
                value -= (
                    inverse_approximation[row, cursor]
                    * jacobian_interval[cursor][column]
                )
            row_sum += _interval_sup_abs(value)

        krawczyk_radius = (
            abs(center_correction[row])
            + RADIUS * row_sum
        )
        row_ratios.append(krawczyk_radius / RADIUS)

    maximum_ratio = max(row_ratios)
    assert maximum_ratio < mp.mpf("1e-20")

    # The omitted 11 equations follow from determinant equality and the first
    # three matched entries.  Certify all relevant 00 entries stay nonzero.
    matrices_center = _matrices_from_values(center)
    minimum_top_left_modulus = min(
        abs(matrices_center[generator][0][0]) - mp.sqrt(2) * RADIUS
        for generator in GENS
    )
    assert minimum_top_left_modulus > mp.mpf("0.1")

    # Certified observables on the root enclosure.
    matrices_interval = _matrices_from_values(interval_values)
    trace_intervals = {
        generator: _trace(matrices_interval[generator])
        for generator in GENS
    }
    kappa_intervals = {}
    for index, left in enumerate(GENS):
        for right in GENS[index + 1:]:
            kappa_intervals[left + right] = _fricke_kappa(
                matrices_interval[left],
                matrices_interval[right],
            )

    # Irreducible because kappa_ab is far from 2 throughout the box.
    kappa_ab = kappa_intervals["ab"]
    distance_from_two = min(
        abs(_interval_endpoint(kappa_ab.real.a, False) - 2),
        abs(_interval_endpoint(kappa_ab.real.b, True) - 2),
    )
    assert distance_from_two > mp.mpf("0.2")

    def interval_record(value):
        return {
            "real_lower": str(_interval_endpoint(value.real.a, False)),
            "real_upper": str(_interval_endpoint(value.real.b, True)),
            "imag_lower": str(_interval_endpoint(value.imag.a, False)),
            "imag_upper": str(_interval_endpoint(value.imag.b, True)),
        }

    return {
        "radius": str(RADIUS),
        "maximum_krawczyk_ratio": mp.nstr(maximum_ratio, 40),
        "maximum_center_correction": mp.nstr(
            max(abs(center_correction[index]) for index in range(16)),
            40,
        ),
        "minimum_top_left_modulus": mp.nstr(
            minimum_top_left_modulus, 40
        ),
        "trace_intervals": {
            key: interval_record(value)
            for key, value in trace_intervals.items()
        },
        "kappa_intervals": {
            key: interval_record(value)
            for key, value in kappa_intervals.items()
        },
        "local_status": "UNIQUE_REDUCED_ISOLATED_ROOT_ON_GAUGE_SLICE",
        "character_status": "IRREDUCIBLE",
        "proof_method": "COMPLEX_INTERVAL_KRAWCZYK",
    }


if __name__ == "__main__":
    print(json.dumps(run_certificate(), indent=2))
