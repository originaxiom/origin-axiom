"""Which SCHEDULED rows of docs/HARVEST_LEDGER.md can actually be read on this bench?

The source field is `path` @ commit -- and the COMMIT REF SITS OUTSIDE THE BACKTICKS. A parser that
splits the backtick content on ' @' finds no commit, defaults to HEAD, and reports that NOTHING is
readable. That is wrong and it is the trap this script exists to avoid: parse the path from the
backticks and the commit from the field, then ask git.
"""
import re, subprocess, collections, json, sys
rows=[l.rstrip() for l in open('docs/HARVEST_LEDGER.md') if l.startswith('| ') and '**SCHEDULED**' in l]
def readable(commit,path):
    return subprocess.run(['git','cat-file','-e',f'{commit}:{path}'],capture_output=True).returncode==0
ok=[]; bad=[]
for r in rows:
    p=[x.strip() for x in r.split('|')]
    if len(p)<6: bad.append(('?','?','no source')); continue
    src=p[5]
    cm=re.search(r'@\s*([0-9a-f]{7,40})',src)          # <- commit is OUTSIDE the backticks
    commit=cm.group(1) if cm else 'HEAD'
    hit=None
    for path in re.findall(r'`([^`]+)`',src):
        path=path.strip().rstrip(',')
        if readable(commit,path): hit=(commit,path); break
    (ok if hit else bad).append((p[2],p[3],p[4][:70])+(hit or (src[:60],)))
print(f"SCHEDULED rows {len(rows)} | readable {len(ok)} | not readable {len(bad)}")
for lbl,s in (("readable",ok),("not readable",bad)):
    print(f"-- {lbl}, by seat --")
    for k,v in collections.Counter(a[0][:24] for a in s).most_common(8): print(f"   {k:26s} {v}")
json.dump([{'seat':a[0],'arc':a[1],'claim':a[2],'commit':a[3],'path':a[4]} for a in ok if len(a)>4],
          open('readable_scheduled.json','w'),indent=1)
