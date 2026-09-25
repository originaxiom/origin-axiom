"""F15 typed-field-zero adapter; original producer remains frozen."""
from pathlib import Path
import importlib.util
import json

spec=importlib.util.spec_from_file_location('f15_original_adapter',Path(__file__).with_name('verify.py'))
v=importlib.util.module_from_spec(spec); spec.loader.exec_module(v)
original_coords=v.coords


def coords(a):
    rows=a.to_list(); k=a.domain
    if sum((rows[i][i] for i in range(4)),k.zero)!=k.zero:
        raise ValueError('matrix is not tracefree')
    values=[rows[i][j] for i,j in v.POSITIONS]+[rows[i][i] for i in range(3)]
    return v.DM([[x] for x in values],(15,1),k)


v.coords=coords


if __name__=='__main__':
    for middle in (14,34):
        for embedding in (1,-1):
            print(json.dumps(v.report(middle,embedding),sort_keys=True),flush=True)
