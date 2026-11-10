#!/usr/bin/env python3
"""Static census of every lock file: does it compute, run the arc script, or only read committed text?
A heuristic classification by imports and assert shapes; spot-check before quoting a single file.
Run from the repository root:  python3 relays/advisor_2026-11-10_audit/tools/lock_census.py
Read-only: writes its JSON next to itself."""
import ast, glob, os, re, collections, json, sys
files = sorted(glob.glob('tests/test_*.py') + glob.glob('frontier/B*/verification/test_b*.py'))
MATH = {'numpy','sympy','mpmath','scipy','snappy','fractions','math','cmath','itertools','origin_axiom','flint','decimal'}
stats=[]
for f in files:
    src=open(f,encoding='utf-8',errors='replace').read()
    try: tree=ast.parse(src)
    except SyntaxError as e:
        stats.append(dict(f=f,err=str(e))); continue
    imports=set()
    for n in ast.walk(tree):
        if isinstance(n,ast.Import):
            for a in n.names: imports.add(a.name.split('.')[0])
        elif isinstance(n,ast.ImportFrom) and n.module: imports.add(n.module.split('.')[0])
    tests=[n for n in ast.walk(tree) if isinstance(n,ast.FunctionDef) and n.name.startswith('test')]
    n_assert=sum(isinstance(n,ast.Assert) for n in ast.walk(tree))
    # string-in-text asserts: assert "..." in X  /  assert X in text
    n_strin=0; n_exists=0
    for n in ast.walk(tree):
        if isinstance(n,ast.Assert):
            t=n.test
            seg=ast.get_source_segment(src,t) or ''
            if isinstance(t,ast.Compare) and any(isinstance(o,(ast.In,ast.NotIn)) for o in t.ops) and isinstance(t.left,(ast.Constant,ast.JoinedStr)) : n_strin+=1
            elif re.search(r'\bin\s+(txt|text|src|body|out|s|t|doc|findings|log|content|raw|md|f|run|transcript)\b',seg): n_strin+=1
            if 'exists(' in seg or 'isfile(' in seg or 'is_file()' in seg: n_exists+=1
    reads_file = bool(re.search(r'open\(|read_text\(|json\.load|\.read\(\)',src))
    runs_sub = 'subprocess' in imports or 'runpy' in imports or 'importlib' in imports
    math_imp = bool(imports & MATH)
    skip = len(re.findall(r'importorskip|pytest\.skip|skipif|pytest\.mark\.skip|xfail',src))
    tested_no_assert=[t.name for t in tests if not any(isinstance(n,(ast.Assert,ast.Raise)) or (isinstance(n,ast.Call) and getattr(getattr(n,'func',None),'attr','') in('raises','approx','fail','check_call','check_output')) for n in ast.walk(t))]
    stats.append(dict(f=f,ntests=len(tests),n_assert=n_assert,n_strin=n_strin,n_exists=n_exists,reads_file=reads_file,runs_sub=runs_sub,math_imp=math_imp,skip=skip,noassert=tested_no_assert,imports=sorted(imports)))
ok=[s for s in stats if 'err' not in s]
print('lock files',len(files),'parse errors',len(stats)-len(ok),'test functions',sum(s['ntests'] for s in ok),'asserts',sum(s['n_assert'] for s in ok))
cls=collections.Counter()
for s in ok:
    frac = s['n_strin']/s['n_assert'] if s['n_assert'] else 0
    if s['n_assert']==0: c='NO_ASSERT'
    elif not s['math_imp'] and not s['runs_sub'] and s['reads_file']: c='TEXT_ONLY (no math import, no subprocess; reads files)'
    elif not s['math_imp'] and s['runs_sub']: c='RUNS_SCRIPT (subprocess/import of arc script, no math lib in test)'
    elif s['math_imp'] and frac>=0.8: c='MATH_IMPORT but >=80% string-in-text asserts'
    elif s['math_imp']: c='MATH (imports a math lib; computed asserts present)'
    else: c='OTHER'
    s['cls']=c; cls[c]+=1
for k,v in cls.most_common(): print(f'{v:5d}  {k}')
print('files with skip markers',sum(1 for s in ok if s['skip']), 'total skip sites',sum(s['skip'] for s in ok))
na=[(s['f'],s['noassert']) for s in ok if s['noassert']]
print('test functions with no assert/raise/approx:',sum(len(x[1]) for x in na),'in',len(na),'files')
for x in na[:25]: print('   ',x[0],x[1][:4])
print('string-in-text asserts total',sum(s['n_strin'] for s in ok),'of',sum(s['n_assert'] for s in ok))
json.dump(stats,open(os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'lockcensus.json'),'w'))
