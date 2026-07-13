from decimal import Decimal
from pathlib import Path
import csv,json,subprocess,sys
ROOT=Path(__file__).resolve().parent

def test_master_counts():
 c=json.loads((ROOT/'CELL3_FIXED_CHARACTER_CERTIFICATE.json').read_text())
 assert c['numerical_discovery']['recovered_support_points']==253
 assert c['numerical_discovery']['recovered_irreducible_support_points']==247
 assert c['local_certification']['interval_krawczyk_reduced_irreducible_points']==246
 assert c['local_certification']['exact_tracezero_nonreduced_double_points']==1
 assert c['reducible_exact_classification']['semisimple_character_count']==6

def test_intervals_separate_kappa_ab():
 R=json.loads((ROOT/'CELL3_INTERVAL_CERTIFICATES.json').read_text())
 assert len(R)==246 and all(r['success'] and r['irreducible_certified'] for r in R)
 boxes=[]
 for r in R:
  v=r['kappa_intervals'][0];boxes.append((Decimal(v['re_lo']),Decimal(v['re_hi']),Decimal(v['im_lo']),Decimal(v['im_hi'])))
 for i,a in enumerate(boxes):
  assert not(a[0]<=Decimal(-2)<=a[1] and a[2]<=0<=a[3])
  for b in boxes[i+1:]:
   assert a[1]<b[0] or b[1]<a[0] or a[3]<b[2] or b[3]<a[2]

def test_special_exact():
 s=subprocess.run([sys.executable,str(ROOT/'cell3_special_points_exact.py')],capture_output=True,text=True)
 assert s.returncode==0,s.stderr
 assert 'det(I-M): -11' in s.stdout

def test_atlas_rows():
 rows=list(csv.DictReader((ROOT/'cell3_fixed_character_atlas.csv').open()))
 assert len(rows)==253
 assert sum(r['character_class']=='IRREDUCIBLE' for r in rows)==247
 assert sum(r['character_class']=='REDUCIBLE' for r in rows)==6
 assert sum(r['local_scheme_status']=='REDUCED_SIMPLE' for r in rows)==246
 assert sum(r['local_scheme_status']=='NONREDUCED_DOUBLE_C_EPS_OVER_EPS2' for r in rows)==1

def test_global_completeness_open():
 c=json.loads((ROOT/'CELL3_FIXED_CHARACTER_CERTIFICATE.json').read_text())
 assert c['global_completeness']['status']=='OPEN_BLOCKED'
 assert c['classification']['complete_fixed_character_scheme']=='BLOCKED_BY_GLOBAL_DEGREE_CERTIFICATE'
