"""Preserve exact interval lower bound through the original receipt checker."""
import importlib.util
import json
from pathlib import Path

import sage.all as sa

path = Path(__file__).with_name('partial_filling_interval.py')
spec = importlib.util.spec_from_file_location('partial_interval_original', path)
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)
original_quarter_lattice = base.quarter_lattice


def quarter_lattice(interval):
    row = original_quarter_lattice(interval)
    lo = int(sa.floor(4*interval.lower()))-1
    hi = int(sa.ceil(4*interval.upper()))+1
    lower = min(abs(interval-sa.QQ(k)/4).lower() for k in range(lo, hi+1))
    row['distance_lower_decimal'] = row['distance_lower']
    row['distance_lower'] = str(sa.QQ(lower))
    return row


base.quarter_lattice = quarter_lattice


if __name__ == '__main__':
    result = base.run()
    print(json.dumps(result, indent=2, sort_keys=True), flush=True)
    base.assert_certificate(result)
    # Native high-precision interval again, independent of serialized fields.
    N = base.snappy.Manifold(base.INPUT)
    N.dehn_fill((2, 1), 0)
    F = N.filled_triangulation([0])
    value = F.complex_volume(verified_modulo_2_torsion=True, bits_prec=160)
    real = value.real().parent()
    c = value.imag()/(2*real.pi()**2)
    expected = real('0.15759004087917847567899149801673152006645612249762745423')
    # The numerical value is not certified; consistency is a control only.
    difference = c-expected
    assert not quarter_lattice(difference)['excludes']
    assert quarter_lattice(c)['excludes']
    print('INTERVAL CERTIFICATE CONTROL: PASS', flush=True)
