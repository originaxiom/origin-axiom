#!/usr/bin/env python3
import re, sys
import os as _os; exec(open(_os.path.join(_os.path.dirname(_os.path.abspath(__file__)),'md2tex.py')).read().split('print("md2tex')[0])  # import functions

PREAMBLE=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amsthm}
\usepackage{unicode-math}
\setmathfont{STIX Two Math}
\usepackage{microtype}
\usepackage[colorlinks=true,linkcolor=black,citecolor=black,urlcolor=black]{hyperref}
\theoremstyle{plain}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\theoremstyle{remark}
\newtheorem*{remark}{Remark}
\setlength{\parskip}{0.35em}
\setlength{\parindent}{0pt}
'''

def convert_body(md, drop_status=True):
    lines=md.split('\n'); out=[]; i=0; n=len(lines); para=[]
    def flush_para(buf):
        if not buf: return
        text=' '.join(buf).strip()
        if not text: return
        m=re.match(r'^\*\*((Theorem|Lemma|Proposition|Corollary|Definition)\b[^*]*?)\.?\*\*\s*(.*)',text)
        if m:
            env=m.group(2).lower(); label=m.group(1)
            # optional name in parens after the keyword
            nm=re.match(r'^(?:Theorem|Lemma|Proposition|Corollary|Definition)\s+\S+\s*\(([^)]*)\)',label) or re.match(r'^(?:Theorem|Lemma|Proposition|Corollary|Definition)\s*\(([^)]*)\)',label)
            opt='['+inline(nm.group(1))+']' if nm else ''
            out.append(f'\\begin{{{env}}}{opt}\n'+inline(m.group(3))+f'\n\\end{{{env}}}')
            return
        if text.startswith('*Proof') or text.startswith('*Sketch'):
            body=text.strip('*'); 
            out.append(r'\begin{proof}'+inline(body.replace('Proof.','').replace('Sketch.',''))+r'\end{proof}'); return
        if text.startswith('*Remark') or text.startswith('*Provenance') or text.startswith('*Scope') or text.startswith('*Story'):
            out.append(r'\begin{remark}'+inline(text.strip('*'))+r'\end{remark}'); return
        out.append(inline(text))
    def flush_tbl(tbl):
        def splitrow(r):
            r=r.strip().strip('|').replace(r'\|','\x00')
            return [c.strip().replace('\x00','|') for c in r.split('|')]
        cells=[splitrow(r) for r in tbl if r.strip()]
        body=[c for c in cells if not all(set(x)<=set('-: ') for x in c)]
        if not body: return
        head,data=body[0],body[1:]
        cols='l'*len(head)
        out.append(r'\begin{center}\small\begin{tabular}{'+cols+r'}\hline')
        out.append(' & '.join(r'\textbf{'+inline(c)+'}' for c in head)+r' \\ \hline')
        for r in data: out.append(' & '.join(inline(c) for c in r)+r' \\')
        out.append(r'\hline\end{tabular}\end{center}')
    while i<n:
        ln=lines[i]
        if ln.startswith('# '): i+=1; continue  # title handled separately
        if drop_status and (ln.strip().startswith('**Draft') or ln.strip().startswith('**Complete draft')):
            i+=1
            while i<n and lines[i].strip() and not lines[i].startswith('#'): i+=1
            continue
        if ln.strip().startswith('|'):
            flush_para(para); para=[]; tbl=[]
            while i<n and lines[i].strip().startswith('|'): tbl.append(lines[i]); i+=1
            flush_tbl(tbl); continue
        if ln.startswith('## '):
            flush_para(para); para=[]
            h=ln[3:].strip(); h=re.sub(r'^\d+\.\s*','',h)
            if h.lower().startswith('abstract'):
                i+=1
                while i<n and not (lines[i].startswith('## ') or lines[i].strip()=='---'): i+=1
                continue
            out.append(r'\section{'+inline(h)+'}'); i+=1; continue
        if ln.startswith('### '):
            flush_para(para); para=[]; out.append(r'\subsection{'+inline(ln[4:].strip())+'}'); i+=1; continue
        if ln.strip()=='---': flush_para(para); para=[]; i+=1; continue
        if ln.strip().startswith('*MSC'): i+=1; continue
        if ln.strip()=='': flush_para(para); para=[]; i+=1; continue
        para.append(ln.strip()); i+=1
    flush_para(para)
    return '\n\n'.join(out)

def extract(md):
    title=re.search(r'^# (.+)$',md,re.M).group(1)
    # abstract: text under "## Abstract" up to next ##
    am=re.search(r'## Abstract\s*\n(.+?)\n## ',md,re.S)
    abs=am.group(1).strip() if am else ''
    msc=re.search(r'\*MSC ([^.]+)\.',md)
    return title, abs, (msc.group(1) if msc else '')

def build(md_path, author, bib):
    md=open(md_path).read()
    title, abs_txt, msc = extract(md)
    body=convert_body(md)
    tex=PREAMBLE
    tex+=r'\title{'+inline(title)+'}'+'\n'
    tex+=r'\author{'+author+'}'+'\n'
    tex+=r'\date{2026}'+'\n'
    tex+=r'\begin{document}'+'\n\\maketitle\n'
    if abs_txt:
        tex+=r'\begin{abstract}'+'\n'+inline(' '.join(abs_txt.split('\n')))+'\n'+r'\end{abstract}'+'\n'
    tex+=body+'\n'
    if bib:
        tex+='\n'+r'\begin{thebibliography}{99}'+'\n'+bib+'\n'+r'\end{thebibliography}'+'\n'
    tex+='\n'+r'\end{document}'+'\n'
    return tex

if __name__=='__main__':
    AUTHOR=r'Dritëro M.'
    BIB_P1=r"""\bibitem{howe} R.~Howe, \emph{On the character of Weil's representation}, Trans. Amer. Math. Soc. \textbf{177} (1973), 287--298.
\bibitem{thomas} T.~Thomas, \emph{The character of the Weil representation}, J. London Math. Soc. \textbf{77} (2008), 221--239.
\bibitem{kr} P.~Kurlberg and Z.~Rudnick, \emph{Hecke theory and equidistribution for the quantization of linear maps of the torus}, Duke Math. J. \textbf{103} (2000), 47--77.
\bibitem{cg} A.~Coste and T.~Gannon, \emph{Remarks on Galois symmetry in rational conformal field theories}, Phys. Lett. B \textbf{323} (1994), 316--321.
\bibitem{cohen} E.~Cohen, \emph{Representations of even functions (mod $r$)}, Duke Math. J. \textbf{25} (1958), 401--421.
\bibitem{mccarthy} P.~J. McCarthy, \emph{Introduction to Arithmetical Functions}, Springer, 1986.
\bibitem{serre} J.-P. Serre, \emph{Linear Representations of Finite Groups}, Springer, 1977.
\bibitem{hb} J.~H. Hannay and M.~V. Berry, \emph{Quantization of linear maps on a torus}, Physica D \textbf{1} (1980), 267--290.
\bibitem{ladisch} F.~Ladisch, \emph{The character of the Weil representation of a finite abelian group of odd order}, arXiv:2303.09676 (2023).
\bibitem{dln} C.~Dong, X.~Lin, and S.-H. Ng, \emph{Congruence property in conformal field theory}, Algebra Number Theory \textbf{9} (2015), 2121--2166."""
    BIB_P2=r"""\bibitem{brakes} W.~R. Brakes, \emph{Manifolds with multiple knot-surgery descriptions}, Math. Proc. Cambridge Philos. Soc. \textbf{87} (1980), 443--448.
\bibitem{nr} W.~D. Neumann and A.~W. Reid, \emph{Arithmetic of hyperbolic manifolds}, in Topology '90, de Gruyter (1992), 273--310.
\bibitem{thurston} W.~P. Thurston, \emph{The Geometry and Topology of Three-Manifolds}, Princeton lecture notes, 1980.
\bibitem{gs} A.~Ghosh and P.~Sarnak, \emph{Integral points on Markoff type cubic surfaces}, Invent. Math. \textbf{229} (2022), 689--749.
\bibitem{km} R.~Kirby and P.~Melvin, \emph{Dedekind sums, $\mu$-invariants and the signature cocycle}, Math. Ann. \textbf{299} (1994), 231--267."""
    BIB_P3=r"""\bibitem{markov} A.~A. Markoff, \emph{Sur les formes quadratiques binaires ind\'efinies}, Math. Ann. \textbf{15} (1879), 381--406.
\bibitem{goldman} W.~M. Goldman, \emph{The modular group action on real SL(2)-characters of a one-holed torus}, Geom. Topol. \textbf{7} (2003), 443--486.
\bibitem{cl} S.~Cantat and F.~Loray, \emph{Dynamics on character varieties and Malgrange irreducibility of Painlev\'e VI}, Ann. Inst. Fourier \textbf{59} (2009), 2927--2978.
\bibitem{dirichlet} P.~G.~L. Dirichlet, \emph{Vorlesungen \"uber Zahlentheorie}, 1863.
\bibitem{hb} J.~H. Hannay and M.~V. Berry, \emph{Quantization of linear maps on a torus}, Physica D \textbf{1} (1980), 267--290.
\bibitem{cantat} S.~Cantat, \emph{Bers and H\'enon, Painlev\'e and Schr\"odinger}, Duke Math. J. \textbf{149} (2009), 411--460.
\bibitem{bgmw} I.~Biswas, S.~Gupta, M.~Mj, and J.~Whang, \emph{Surface group representations in $SL_2(\mathbb{C})$ with finite mapping class orbits}, Geom. Topol. \textbf{26} (2022), 679--719."""

    BIB_P4=r'''\bibitem{cohn} H.~Cohn, \emph{Approach to Markoff's minimal forms through modular functions}, Ann. of Math. \textbf{61} (1955), 1--12.
\bibitem{reutenauer} C.~Reutenauer, \emph{From Christoffel Words to Markoff Numbers}, Oxford Univ. Press, 2019.
\bibitem{sarnak} P.~Sarnak, \emph{Reciprocal geodesics}, Clay Math. Proc. \textbf{7} (2007), 217--237.
\bibitem{gehring} F.~W. Gehring and G.~J. Martin, \emph{Commutators, collars and the geometry of M\"obius groups}, J. Anal. Math. \textbf{63} (1994), 175--219.
\bibitem{northshield} S.~Northshield, \emph{Square roots of $2\times2$ matrices}, Contemp. Math. \textbf{517} (2010), 289--304.
\bibitem{lm} C.~G. Latimer and C.~C. MacDuffee, \emph{A correspondence between classes of ideals and classes of matrices}, Ann. of Math. \textbf{34} (1933), 313--316.
\bibitem{tww} Y.~Tian, S.~Wang, and Z.~Wang, \emph{Achirality of Sol 3-manifolds}, arXiv:2406.13241 (2024).
\bibitem{hb} J.~H. Hannay and M.~V. Berry, \emph{Quantization of linear maps on a torus}, Physica D \textbf{1} (1980), 267--290.
\bibitem{kr} P.~Kurlberg and Z.~Rudnick, \emph{Hecke theory and equidistribution for the quantization of linear maps of the torus}, Duke Math. J. \textbf{103} (2000), 47--77.
\bibitem{howe} R.~Howe, \emph{On the character of Weil's representation}, Trans. Amer. Math. Soc. \textbf{177} (1973), 287--298.
\bibitem{thomas} T.~Thomas, \emph{The character of the Weil representation}, J. London Math. Soc. \textbf{77} (2008), 221--239.
\bibitem{appleby} D.~M. Appleby, \emph{SIC-POVMs and the extended Clifford group}, J. Math. Phys. \textbf{46} (2005), 052107.
\bibitem{serre} J.-P. Serre, \emph{Linear Representations of Finite Groups}, Springer, 1977.
\bibitem{cohen} E.~Cohen, \emph{Representations of even functions (mod $r$)}, Duke Math. J. \textbf{25} (1958).'''
    p=sys.argv[1]
    bib = BIB_P4 if 'P4' in p else BIB_P1 if 'P1' in p else BIB_P2 if 'P2' in p else BIB_P3 if 'P3' in p else ''
    print(build(p, AUTHOR, bib))
