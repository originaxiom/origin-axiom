#!/usr/bin/env python3
"""Render a paper markdown -> standalone print-styled HTML (math-monograph, for PDF)."""
import re, html, sys
def inline(t):
    t=html.escape(t,quote=False)
    t=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',t)
    t=re.sub(r'(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)',r'<em>\1</em>',t)
    t=re.sub(r'`(.+?)`',r'<code>\1</code>',t)
    return t
def convert(md):
    lines=md.split('\n');out=[];i=0;n=len(lines);title_done=False;para=[]
    def flush_para(buf):
        if not buf:return
        text=' '.join(buf).strip()
        if not text:return
        m=re.match(r'^\*\*((?:Theorem|Lemma|Proposition|Corollary|Definition)\b[^*]*?)\.?\*\*\s*(.*)',text)
        if m:
            out.append(f'<div class="thm"><span class="thm-label">{html.escape(m.group(1))}</span> {inline(m.group(2))}</div>');return
        if text.startswith('*Proof') or text.startswith('*Remark') or text.startswith('*Provenance') or text.startswith('*Scope') or text.startswith('*Story'):
            out.append(f'<p class="proof">{inline(text)}</p>');return
        out.append(f'<p>{inline(text)}</p>')
    def flush_tbl(tbl):
        cells=[[c.strip() for c in r.strip().strip('|').split('|')] for r in tbl if r.strip()]
        body=[c for c in cells if not all(set(x)<=set('-: ') for x in c)]
        if not body:return
        head,data=body[0],body[1:]
        h='<thead><tr>'+''.join(f'<th>{inline(c)}</th>' for c in head)+'</tr></thead>'
        b='<tbody>'+''.join('<tr>'+''.join(f'<td>{inline(c)}</td>' for c in r)+'</tr>' for r in data)+'</tbody>'
        out.append(f'<div class="tbl-wrap"><table>{h}{b}</table></div>')
    while i<n:
        ln=lines[i]
        if not title_done and ln.startswith('# '):
            out.append(f'<h1>{inline(ln[2:].strip())}</h1>');title_done=True;i+=1;continue
        if ln.strip().startswith('**Draft') or ln.strip().startswith('**Complete draft'):
            buf=[ln];i+=1
            while i<n and lines[i].strip() and not lines[i].startswith('#'):buf.append(lines[i]);i+=1
            out.append(f'<div class="status">{inline(" ".join(buf).strip().strip("*"))}</div>');continue
        if ln.strip().startswith('|'):
            flush_para(para);para=[];tbl=[]
            while i<n and lines[i].strip().startswith('|'):tbl.append(lines[i]);i+=1
            flush_tbl(tbl);continue
        if ln.startswith('## '):flush_para(para);para=[];out.append(f'<h2>{inline(ln[3:].strip())}</h2>');i+=1;continue
        if ln.startswith('### '):flush_para(para);para=[];out.append(f'<h3>{inline(ln[4:].strip())}</h3>');i+=1;continue
        if ln.strip()=='---':flush_para(para);para=[];out.append('<hr>');i+=1;continue
        if ln.strip()=='':flush_para(para);para=[];i+=1;continue
        para.append(ln.strip());i+=1
    flush_para(para)
    return '\n'.join(out)
CSS = """
@page{size:A4;margin:19mm 20mm 20mm;}
:root{--paper:#FBFAF6;--ink:#211E1A;--accent:#8C6A26;--accent-soft:#B8934A;--muted:#635F56;
--rule:#E4DED1;--thm-bg:#F5F0E4;--thm-rule:#C1962F;--code-bg:#F1ECE0;
--serif:"Palatino Linotype","Book Antiqua",Palatino,"Iowan Old Style",Georgia,serif;
--sans:"Helvetica Neue",Arial,sans-serif;--mono:"SF Mono",Menlo,Consolas,monospace;}
*{box-sizing:border-box}
html,body{background:var(--paper);color:var(--ink);font-family:var(--serif);line-height:1.52;margin:0;
font-size:10.3pt;-webkit-print-color-adjust:exact;print-color-adjust:exact;font-feature-settings:"kern" 1;}
.wrap{max-width:100%;}
h1{font-size:19pt;line-height:1.16;font-weight:600;letter-spacing:-.01em;margin:0 0 .8em;text-wrap:balance;}
.status{font-family:var(--sans);font-size:7.6pt;line-height:1.42;color:var(--muted);background:var(--thm-bg);
border:.5pt solid var(--rule);border-radius:2px;padding:.7em .85em;margin:0 0 1.6em;}
.status strong{color:var(--accent);}
h2{font-size:13pt;font-weight:600;margin:1.5em 0 .5em;padding-bottom:.22em;border-bottom:.6pt solid var(--rule);
break-after:avoid;text-wrap:balance;}
h3{font-size:10.6pt;font-weight:600;color:var(--accent);font-family:var(--sans);margin:1.1em 0 .35em;break-after:avoid;}
p{margin:0 0 .62em;orphans:2;widows:2;}
p.proof{color:var(--muted);font-size:9.7pt;}
strong{font-weight:600;} em{font-style:italic;}
code{font-family:var(--mono);font-size:.82em;background:var(--code-bg);padding:.05em .3em;border-radius:2px;border:.5pt solid var(--rule);}
hr{border:0;text-align:center;margin:1.4em 0;} hr::before{content:"\\2767";color:var(--accent-soft);}
.thm{background:var(--thm-bg);border-left:2pt solid var(--thm-rule);border-radius:0 2px 2px 0;
padding:.6em .8em;margin:0 0 .7em;font-size:9.9pt;break-inside:avoid;}
.thm-label{font-family:var(--sans);font-size:7pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;
color:var(--accent);margin-right:.5em;}
.tbl-wrap{margin:0 0 .9em;break-inside:avoid;}
table{border-collapse:collapse;width:100%;font-size:8.4pt;font-variant-numeric:tabular-nums;}
th,td{text-align:left;padding:.28em .5em;border-bottom:.5pt solid var(--rule);vertical-align:top;}
th{font-family:var(--sans);font-size:7pt;font-weight:700;letter-spacing:.03em;text-transform:uppercase;
color:var(--accent);border-bottom:1pt solid var(--thm-rule);}
"""
if __name__=='__main__':
    md=open(sys.argv[1]).read()
    body=convert(md)
    doc=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="wrap">{body}</div></body></html>'
    open(sys.argv[2],'w').write(doc)
    print("wrote",sys.argv[2])
