"""Separate quadratic Fraction cover/degree certificate; no native import."""
import importlib.util
import itertools
import json
from functools import lru_cache
from pathlib import Path
HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('cover_charged_fraction',HERE.parent/'silver_charged_pair_lift_2026_10_11/reference.py')
r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
c=r.c;K=c.K

def word_sign(eta,text):
    result=1
    for letter in text:result*=eta['abt'.index(letter.lower())]
    return result

def reorder(a,n):
    return [a[j] for j in list(range(n))+list(range(2*n,3*n))+list(range(n,2*n))+list(range(3*n,4*n))]

def count(E,L):
    n=E['n'];M=c.cat(E['U'],L);ranks=[]
    for value in range(n+1):
        pencil=c.cat(c.add(c.scale(E['b'],-1),c.scale(c.I(n),-value)),E['a'])
        ranks.append(r.rank(c.mm(pencil,M)))
    rank=max(ranks);h=[0,len(M[0])-rank,n-rank,0]
    return {'H':h,'J':h[1]-h[2],'rank':rank}

def protected(block,ell):
    subset=block['protected_only_witnesses'][str(ell)]
    return next(row for row in block['rows'] if row['subset']==subset)

@lru_cache(None)
def run():
    old=r.run();data,w,P,Q,A,B=c.literal();checks={};models={};bulk={}
    def ck(key,value):checks[key]=bool(value);assert checks[key],key
    population=[eta for eta in itertools.product((1,-1),repeat=3) if eta!=(1,1,1) and all(word_sign(eta,text)==1 for text in data['relators']+data['cusp_words'])]
    ck('derive_three_connected_peripheral_trivial_sign_covers',set(population)=={(-1,-1,1),(-1,1,-1),(1,-1,-1)})
    had=c.scale([[1,1],[1,-1]],K(0,1)/2)
    ck('normalized_sheet_graph_norm_isometry',c.equal(c.mm(c.tr(had),had),c.I(2)))
    for eta in population:
        tag=','.join(map(str,eta));bulk[tag]={}
        for label,rep in (('W',w),('F',{g:c.old.exterior(m) for g,m in w.items()})):
            n=len(rep['a']);twisted={g:c.scale(rep[g],eta[j]) for j,g in enumerate('abt')}
            U=c.scale(c.stack(c.cat(c.I(n),c.I(n)),c.cat(c.I(n),c.scale(c.I(n),-1))),K(0,1)/2)
            induced={g:c.diag(rep[g],rep[g]) if eta[j]==1 else c.stack(c.cat(c.Z(n),rep[g]),c.cat(rep[g],c.Z(n))) for j,g in enumerate('abt')}
            ck(tag+label+'_literal_unitary_section_map',all(c.equal(c.mm(c.mm(c.tr(U),induced[g]),U),c.diag(rep[g],twisted[g])) for g in 'abt'))
            ck(tag+label+'_all_relators_peripheral_maps',all(c.equal(r.word_fox_jets(induced,text)[0][0],c.I(2*n)) for text in data['relators']) and all(c.equal(r.word_fox_jets(induced,text)[0][0],c.diag(r.word_fox_jets(rep,text)[0][0],r.word_fox_jets(rep,text)[0][0])) for text in data['cusp_words']))
            fam=r.family_jets(twisted,data)
            ck(tag+label+'_independent_chain_and_leading_minor',c.zero(c.mm(fam['F'][0],fam['B'][0])) and c.equal([row[:2*n] for row in fam['F'][1]],c.diag(twisted['t'],twisted['t'])) and r.rank(twisted['t'])==n and c.zero(c.add(c.mm(fam['R2'][0],fam['F'][0]),c.mm(fam['G'][0],fam['R'][0]),-1)))
            bulk[tag][label]={'cover_coefficient_rank':n,'pushforward_rank':2*n,'cusp_sheets':2,'generic_bulk_H':[0,0,0,0]}
    ck('induction_exterior_noncommutation_detected',len(c.old.exterior(c.diag(w['a'],w['a'])))==45 and 2*len(c.old.exterior(w['a']))==20)
    for label,a,b in (('W',A,B),('F',c.wedge_derivative(A),c.wedge_derivative(B))):
        E=r.boundary(a,b);n=E['n'];first=old['blocks'][label]['protected_only_witnesses']
        plus=r.subset(E['H'],first[str(E['t0']+1)]);minus=r.subset(E['H'],first[str(E['t0']+2)])
        L=reorder(c.diag(plus,minus),n)
        EC=r.boundary(c.diag(a,a),c.diag(b,b));DC=r.boundary(c.diag(c.scale(c.tr(a),-1),c.scale(c.tr(a),-1)),c.diag(c.scale(c.tr(b),-1),c.scale(c.tr(b),-1)))
        dual,_=r.paired_plane(EC,DC,L)
        row,other=count(EC,L),count(DC,dual)
        ck(label+'_degree_bound_actual_doubled_charged_and_dual_kernel',row['H']==[0,3,0,0] and other['H']==[0,0,3,0] and row['rank']==2*n and other['rank']==2*n-3)
        ck(label+'_impossible_dual_full_rank_rejected',other['rank']!=2*n and len(DC['U'][0])+len(dual[0])==2*n-3)
        ck(label+'_dual_annihilator_full_dimension',len(dual[0])==len(DC['H'][0])-len(L[0]) and r.rank(dual)==len(dual[0]))
        models[label]={'H':row['H'],'dual_H':other['H'],'rank':row['rank'],'dual_rank':other['rank'],
                       't0':EC['t0'],'ell':len(L[0]),'sector_J':[1,2],
                       'sector_subsets':[first[str(E['t0']+1)],first[str(E['t0']+2)]]}
    rows=[]
    for wp,wm,fp,fm in itertools.product(range(5),range(5),range(7),range(7)):
        wrows=[protected(old['blocks']['W'],j) for j in (wp,wm)]
        frows=[protected(old['blocks']['F'],j) for j in (fp,fm)]
        hw=[sum(row['H'][k] for row in wrows) for k in range(4)];hf=[sum(row['H'][k] for row in frows) for k in range(4)]
        rows.append({'ell':[wp,wm,fp,fm],'W':hw,'F':hf,'J':[hw[1]-hw[2],hf[1]-hf[2]],'local_cubic_anomaly':hw[1]-hw[2]-hf[1]+hf[2]})
    common=[row for row in rows if row['local_cubic_anomaly']==0];threes=[row for row in common if row['J']==[3,3]]
    ck('entire_dimension_menu_and_complete_three_kernels',len(rows)==1225 and len(threes)==8 and all(row['W']==row['F']==[0,3,0,0] for row in threes))
    inherited=[row for row in rows if row['ell'][0]==row['ell'][1] and row['ell'][2]==row['ell'][3]]
    ck('inherited_charged_domain_even_not_all_domain_kill',len(inherited)==35 and all(j%2==0 for row in inherited for j in row['J']))
    ck('conjugates_cannot_be_deleted_at_zero_index',any(row['J']==[0,0] and row['W'][1]*row['W'][2]>0 for row in common))
    plus=[had[0][0],had[1][0]];minus=[had[0][1],had[1][1]]
    def mult(x,y):return c.mm(c.tr(had),[[x[j]*y[j]] for j in range(2)])
    ck('actual_parent_multiplication_cross_parities_not_copies',c.equal(mult(plus,minus),[[0],[K(0,1)/2]]) and c.equal(mult(minus,minus),[[K(0,1)/2],[0]]))
    return {'checks':checks,'exact_predicates':len(checks),'old_exact_predicates':old['predicates_passed'],
            'cover_characters':[list(x) for x in population],'bulk':bulk,'models':models,'menu':rows,
            'common_indices':sorted({row['J'][0] for row in common}),
            'common_three_dimension_choices':[row['ell'] for row in threes],
            'charged_transfer_conditional':True,'complete_cover_domain_verified':False,
            'boundary_selected':False,'actual_zero_profile_Yukawas':False,
            'outside_review':False,'full_goal_achieved':False}

if __name__=='__main__':print(json.dumps(run(),indent=2,sort_keys=True))
