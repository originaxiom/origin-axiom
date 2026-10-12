"""Connected-cover charged Weyl map; execute only after published seal."""
import importlib.util
import itertools
import json
from functools import lru_cache
from pathlib import Path
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cover_charged_native',HERE.parent/'silver_charged_pair_lift_2026_10_11/probe.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
cy=p.cy
SIGNS=list(itertools.product((1,-1),repeat=3))

def sign_word(eta,text):
    out=1
    for letter in text:out*=eta[p.GEN.index(letter.lower())]
    return out

def character_population(data):
    return [eta for eta in SIGNS if eta!=(1,1,1)
            and all(sign_word(eta,w)==1 for w in data['relators']+data['cusp_words'])]

def reorder(a,n):
    # Sector-first (dx+,dy+,dx-,dy-) to form-first (dx+,dx-,dy+,dy-).
    return a[list(range(n))+list(range(2*n,3*n))+list(range(n,2*n))+list(range(3*n,4*n)),:]

def protected(block,ell):
    chosen=block['protected_only_witnesses'][str(ell)]
    return next(row for row in block['rows'] if row['subset']==chosen)

def menu(blocks):
    rows=[]
    for wp,wm,fp,fm in itertools.product(range(5),range(5),range(7),range(7)):
        w=[protected(blocks['W'],j) for j in (wp,wm)]
        f=[protected(blocks['F'],j) for j in (fp,fm)]
        hw=[sum(row['H'][k] for row in w) for k in range(4)]
        hf=[sum(row['H'][k] for row in f) for k in range(4)]
        rows.append({'ell':[wp,wm,fp,fm],'W':hw,'F':hf,
                     'J':[hw[1]-hw[2],hf[1]-hf[2]],
                     'local_cubic_anomaly':hw[1]-hw[2]-hf[1]+hf[2]})
    return rows

@lru_cache(None)
def run():
    old=p.run() # Entire prior LIVE native witness and first-jet calculation.
    instrument,data,w,P,Q,A,B=cy.literal()
    facts={};models={};bulk={}
    def ck(key,value):
        facts[key]=bool(value)
        assert facts[key],key
    population=character_population(data)
    ck('population_derived_from_relators_and_both_cusps',set(population)=={(-1,-1,1),(-1,1,-1),(1,-1,-1)} and len(population)==3)
    ck('nonperipheral_character_control',all(sign_word((1,1,-1),t)==1 for t in data['relators']) and sign_word((1,1,-1),data['cusp_words'][1])==-1)
    had=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
    ck('sheet_map_is_unitary_not_a_dimension_match',p.zero(had.T*had-s.eye(2)))
    for eta in population:
        tag=','.join(map(str,eta));bulk[tag]={}
        ck(tag+'_connected_surjective_character',any(x==-1 for x in eta) and all(sign_word(eta,t)==1 for t in data['relators']))
        for label,rep in (('W',w),('F',{g:instrument.wedge(m) for g,m in w.items()})):
            n=rep['a'].rows;U=s.kronecker_product(had,s.eye(n))
            twisted={g:eta[j]*rep[g] for j,g in enumerate(p.GEN)}
            induced={g:s.kronecker_product(s.eye(2) if eta[j]==1 else s.Matrix([[0,1],[1,0]]),rep[g]) for j,g in enumerate(p.GEN)}
            ck(tag+label+'_actual_section_transition_map',all(p.zero(p.mm(p.mm(U.T,induced[g]),U)-s.diag(rep[g],twisted[g])) for g in p.GEN))
            ck(tag+label+'_literal_cover_relators_and_two_cusp_sheets',all(p.zero(cy.word(induced,t)-s.eye(2*n)) for t in data['relators']) and all(p.zero(cy.word(induced,t)-s.diag(cy.word(rep,t),cy.word(rep,t))) for t in data['cusp_words']))
            family=p.family(twisted,data)
            ck(tag+label+'_full_twisted_bulk_and_boundary_chain',p.zero(p.mm(family['F'],family['B'],p.q),p.q) and p.zero(p.mm(family['R'],family['B'],p.q)-family['D'],p.q) and p.zero(p.mm(family['R2'],family['F'],p.q)-p.mm(family['G'],family['R'],p.q),p.q))
            ck(tag+label+'_invertible_leading_minor_proves_bulk_acyclic',p.bulk_leading_minor_certificate(family,twisted))
            ck(tag+label+'_peripheral_coefficients_unchanged',p.zero(family['P']-cy.word(rep,data['cusp_words'][0])) and p.zero(family['Q']-cy.word(rep,data['cusp_words'][1])))
            bulk[tag][label]={'cover_coefficient_rank':n,'pushforward_rank':2*n,'cusp_sheets':2,'generic_bulk_H':[0,0,0,0]}
    ck('exterior_before_pushforward_rank_control',2*instrument.wedge(w['a']).rows==20 and instrument.wedge(s.diag(w['a'],w['a'])).rows==45)
    for label,a,b in (('W',A,B),('F',cy.exterior_lie(A),cy.exterior_lie(B))):
        E=p.boundary(a,b);n=E['n'];first=old['blocks'][label]['protected_only_witnesses']
        plus=E['H'][:,first[str(E['t0']+1)]]
        minus=E['H'][:,first[str(E['t0']+2)]]
        L=reorder(s.diag(plus,minus),n)
        EC=p.boundary(s.diag(a,a),s.diag(b,b));DC=p.boundary(s.diag(-a.T,-a.T),s.diag(-b.T,-b.T))
        dual=p.dual_plane(EC,DC,L)
        row=p.pencil_count(EC,L);other=p.pencil_count(DC,dual)
        ck(label+'_literal_doubled_kernel_not_index_only',row['H']==[0,3,0,0] and other['H']==[0,0,3,0] and row['J']==3 and other['J']==-3)
        ck(label+'_actual_dual_perfect_annihilator_dimension',dual.cols==DC['H'].cols-L.cols and p.rank(dual)==dual.cols)
        # Full cover coexact plus L has generic rank 2n, not a copied claim.
        ck(label+'_full_doubled_rank_certificate',row['rank']==2*n and other['rank']==2*n)
        models[label]={'H':row['H'],'dual_H':other['H'],'rank':row['rank'],
                       't0':EC['t0'],'ell':L.cols,'sector_J':[1,2],
                       'sector_subsets':[first[str(E['t0']+1)],first[str(E['t0']+2)]]}
    rows=menu(old['blocks'])
    common=[row for row in rows if row['local_cubic_anomaly']==0]
    threes=[row for row in common if row['J']==[3,3]]
    ck('entire_protected_dimension_menu_not_selected_count',len(rows)==1225 and {row['J'][0] for row in common}==set(range(-4,5)))
    ck('all_common_three_rows_keep_full_kernels',len(threes)==8 and all(row['W']==row['F']==[0,3,0,0] for row in threes))
    inherited=[row for row in rows if row['ell'][0]==row['ell'][1] and row['ell'][2]==row['ell'][3]]
    ck('unchanged_charged_pullback_domain_only_even_indices',len(inherited)==35 and all(all(j%2==0 for j in row['J']) for row in inherited))
    ck('index_zero_does_not_erase_conjugates',any(row['J']==[0,0] and row['W'][1]>0 and row['W'][2]>0 for row in common))
    # Actual pointwise multiplication, including cross-parity interactions.
    eplus=had[:,0];eminus=had[:,1]
    def mult(x,y):return had.T*s.Matrix([x[j]*y[j] for j in range(2)])
    ck('parent_deck_multiplication_keeps_cross_sector_vertices',mult(eplus,eplus)==s.Matrix([1/s.sqrt(2),0]) and mult(eplus,eminus)==s.Matrix([0,1/s.sqrt(2)]) and mult(eminus,eminus)==s.Matrix([1/s.sqrt(2),0]))
    ck('decoupled_copy_control_rejected',mult(eminus,eminus)!=s.Matrix([0,1/s.sqrt(2)]) and mult(eplus,eminus)!=s.zeros(2,1))
    return {'facts':facts,'exact_predicates':len(facts),'old_exact_predicates':old['predicates_passed'],
            'cover_characters':[list(x) for x in population],'bulk':bulk,'models':models,
            'menu':rows,'common_indices':sorted({row['J'][0] for row in common}),
            'common_three_dimension_choices':[row['ell'] for row in threes],
            'charged_transfer_conditional':True,'complete_cover_domain_verified':False,
            'boundary_selected':False,'actual_zero_profile_Yukawas':False,
            'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
