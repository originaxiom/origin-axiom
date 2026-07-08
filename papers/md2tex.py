import re
SUB={'₀':'0','₁':'1','₂':'2','₃':'3','₄':'4','₅':'5','₆':'6','₇':'7','₈':'8','₉':'9',
     '₊':'+','₋':'-','ₐ':'a','ₙ':'n','ᵢ':'i','ⱼ':'j','ₖ':'k','ₘ':'m','ₚ':'p','ₛ':'s','ₜ':'t'}
SUP={'⁰':'0','¹':'1','²':'2','³':'3','⁴':'4','⁵':'5','⁶':'6','⁷':'7','⁸':'8','⁹':'9',
     'ⁿ':'n','⁺':'+','⁻':'-','ᵀ':'T','ʲ':'j','ˡ':'l','ᵐ':'m','ᵏ':'k'}
OPS={'⟹':r'\Longrightarrow ','⟺':r'\Longleftrightarrow ','⟨':r'\langle ','⟩':r'\rangle ',
     '≅':r'\cong ','≈':r'\approx ','≠':r'\neq ','≤':r'\le ','≥':r'\ge ','≡':r'\equiv ',
     '⊆':r'\subseteq ','⊂':r'\subset ','×':r'\times ','·':r'\cdot ','±':r'\pm ','∓':r'\mp ',
     '∈':r'\in ','∉':r'\notin ','∏':r'\prod ','∑':r'\sum ','→':r'\to ','↦':r'\mapsto ',
     '∅':r'\varnothing ','∘':r'\circ ','∩':r'\cap ','∪':r'\cup ','⊕':r'\oplus ','⊗':r'\otimes ',
     '∀':r'\forall ','∃':r'\exists ','⋊':r'\rtimes ','−':'-','≪':r'\ll ','⟂':r'\perp ','↔':r'\leftrightarrow ','≢':r'\not\equiv ','⟸':r'\Longleftarrow ','ℓ':r'\ell ','′':r'\prime '}
GREEK={'κ':r'\kappa ','λ':r'\lambda ','μ':r'\mu ','ν':r'\nu ','ξ':r'\xi ','π':r'\pi ',
     'ρ':r'\rho ','σ':r'\sigma ','τ':r'\tau ','φ':r'\varphi ','χ':r'\chi ','ψ':r'\psi ',
     'ω':r'\omega ','α':r'\alpha ','β':r'\beta ','γ':r'\gamma ','δ':r'\delta ',
     'ε':r'\varepsilon ','ζ':r'\zeta ','η':r'\eta ','θ':r'\theta ','ϑ':r'\vartheta ',
     'ϕ':r'\phi ','Γ':r'\Gamma ','Δ':r'\Delta ','Θ':r'\Theta ','Λ':r'\Lambda ',
     'Ξ':r'\Xi ','Π':r'\Pi ','Σ':r'\Sigma ','Φ':r'\Phi ','Ψ':r'\Psi ','Ω':r'\Omega '}
BB={'ℚ':r'\mathbb{Q}','ℤ':r'\mathbb{Z}','ℝ':r'\mathbb{R}','ℂ':r'\mathbb{C}','ℕ':r'\mathbb{N}','𝔽':r'\mathbb{F}'}
HARD=set('_^[]√′')|set(SUB)|set(SUP)|set(GREEK)|set(BB)|set(OPS)|set('=<>|/')
def is_math_tok(t):
    if not t: return False
    return any(c in HARD for c in t)
def mathify(run):
    run=run.replace('#',r'\#').replace('{',r'\{').replace('}',r'\}')
    def mat(m):
        rr=re.findall(r'\[([^\[\]]*)\]',m.group(1))
        body=r'\\'.join(' & '.join(c.strip() for c in r.split(',')) for r in rr)
        return r'\left(\begin{smallmatrix}'+body+r'\end{smallmatrix}\right)'
    run=re.sub(r'\[(\[[^\[\]]*\](?:\s*,\s*\[[^\[\]]*\])*)\]',mat,run)
    # sqrt
    run=re.sub(r'√\s*\(([^()]*)\)',lambda m:r'\sqrt{'+m.group(1)+'}',run)
    run=re.sub(r'√\s*(−?\d+|[A-Za-z]|[₀-₉]+)',lambda m:r'\sqrt{'+m.group(1)+'}',run)
    run=run.replace('√',r'\surd ')
    run=re.sub('['+''.join(SUB)+']+',lambda m:'_{'+''.join(SUB[c] for c in m.group(0))+'}',run)
    run=re.sub('['+''.join(SUP)+']+',lambda m:'^{'+''.join(SUP[c] for c in m.group(0))+'}',run)
    # literal _x ^x -> grouped
    run=re.sub(r'_([A-Za-z0-9])',r'_{\1}',run)
    run=re.sub(r'\^([A-Za-z0-9])',r'^{\1}',run)
    for k,v in GREEK.items(): run=run.replace(k,v)
    for k,v in BB.items(): run=run.replace(k,v)
    for k,v in OPS.items(): run=run.replace(k,v)
    run=run.replace('#',r'\#').replace('{',r'\{').replace('}',r'\}') if False else run
    return run
def wrap_math(text):
    toks=text.split(' ');out=[];i=0
    OPSET={'=','+','-','/','·','<','>','|',':'}
    while i<len(toks):
        if is_math_tok(toks[i]):
            j=i; last_op=False
            while j<len(toks):
                base=toks[j].strip('.,;:')
                if is_math_tok(toks[j]):
                    j+=1; last_op=(base in OPSET)
                elif base in OPSET:
                    j+=1; last_op=True
                elif last_op and re.match(r'^[A-Za-z0-9()]+$',base):
                    j+=1; last_op=False
                else:
                    break
            run=' '.join(toks[i:j])
            lead='';trail=''
            while run and run[-1] in '.,;:)': 
                if run[-1]==')' and run.count('(')>=run.count(')'): break
                trail=run[-1]+trail; run=run[:-1]
            while run and run[0] in '(': 
                if run.count(')')>=run.count('('): break
                lead=lead+run[0]; run=run[1:]
            out.append(lead+r'\('+mathify(run)+r'\)'+trail if run else lead+trail)
            i=j
        else:
            out.append(toks[i]); i+=1
    return ' '.join(out)
def esc_text(t):
    t=t.replace('\\',r'\textbackslash{}')
    t=t.replace('ω̄',r'\(\bar\omega\)').replace('̄','')
    t=t.replace('∎','')
    t=t.replace('&',r'\&').replace('%',r'\%').replace('#',r'\#').replace('~',r'\textasciitilde{}')
    t=t.replace('§',r'\S{}').replace('″',"''").replace('‴',"'''").replace('ℓ',r'\(\ell\)')
    t=t.replace('−','-')
    for k,v in GREEK.items(): t=t.replace(k,r'\('+v.strip()+r'\)')
    for k,v in BB.items(): t=t.replace(k,r'\('+v+r'\)')
    return t
def _process(seg):
    seg=wrap_math(seg)
    maths=[]
    seg=re.sub(r'\\\(.*?\\\)',lambda m:(maths.append(m.group(0)),f'@@M{len(maths)-1}@@')[1],seg)
    seg=esc_text(seg)
    seg=seg.replace('{',r'\{').replace('}',r'\}')
    for k,mm in enumerate(maths): seg=seg.replace(f'@@M{k}@@',mm)
    return seg
def inline(t):
    codes=[]
    t=re.sub(r'`([^`]+)`',lambda m:(codes.append(m.group(1)),f'@@C{len(codes)-1}@@')[1],t)
    parts=re.split(r'(\*\*.+?\*\*|(?<!\*)\*(?!\*)[^*]+?\*(?!\*))',t)
    out=[]
    for p in parts:
        if not p: continue
        if p.startswith('**') and p.endswith('**') and len(p)>4:
            out.append(r'\textbf{'+_process(p[2:-2])+'}')
        elif p.startswith('*') and p.endswith('*') and len(p)>2:
            out.append(r'\emph{'+_process(p[1:-1])+'}')
        else:
            out.append(_process(p))
    r=''.join(out)
    for k,c in enumerate(codes):
        r=r.replace(f'@@C{k}@@',r'\texttt{'+c.replace('_',r'\_').replace('&',r'\&')+'}')
    return r
