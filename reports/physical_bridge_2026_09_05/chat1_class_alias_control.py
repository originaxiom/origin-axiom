"""Resolve one published tessellation name; retain the original scientific code."""
from hashlib import sha256
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import sys

SOURCE = Path(__file__).with_name('chat1_class_control.py')
LEGACY = 'otet06_0000'
SIGNATURE = 'gLLPQccdfeefqjsqqjj'
ORIGINAL_SHA256 = '61a4ef5f17f36a80946f6b311b1658a57a43845c12adec3a272f328df9e6411e'
if sha256(SOURCE.read_bytes()).hexdigest() != ORIGINAL_SHA256:
    raise ValueError('Original science differs from its pre-execution seal')
SPEC = spec_from_file_location('chat1_original_sealed_control', SOURCE)
ORIGINAL = module_from_spec(SPEC)
SPEC.loader.exec_module(ORIGINAL)


def exact_run():
    native_row = ORIGINAL.triangulation_row

    def resolved_row(name):
        if name != LEGACY:
            return native_row(name)
        row = native_row(SIGNATURE)
        row['name'] = LEGACY
        row['constructor_input'] = SIGNATURE
        row['alias_source'] = 'Fominykh et al., Table 2, page 7, 2015 author PDF'
        return row

    ORIGINAL.triangulation_row = resolved_row
    try:
        result = ORIGINAL.exact_run()
    finally:
        ORIGINAL.triangulation_row = native_row
    result['alias_control'] = dict(legacy_name=LEGACY, constructor_signature=SIGNATURE,
                                 original_source_sha256=ORIGINAL_SHA256,
                                 original_first_run_succeeded=False)
    return result


if __name__ == '__main__':
    result = exact_run()
    print(json.dumps(result, indent=2, sort_keys=True))
    sys.exit(0 if result['all_checks_pass'] else 1)
