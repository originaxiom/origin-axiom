"""F17 exact finite certificates; no numerical rank tolerances."""
from pathlib import Path
from itertools import product
import importlib.util
import pytest
import sympy as s

spec=importlib.util.spec_from_file_location('f17_test_producer',Path(__file__).with_name('verify.py'))
p=importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
v=p.v


def test_schreier_marking_free_group_telescope_all_short_words():
    for length in range(5):
        for letters in product('mnMN',repeat=length):
            w=''.join(letters)
            for start in range(3):
                rw,end=p.rewrite(w,start)
                assert p.reduce_word(p.expand(rw))==p.reduce_word('m'*start+w+'M'*end)
    for start,rw in enumerate(p.RELS):
        assert p.rewrite(p.REL,start)[1]==start
        assert p.reduce_word(p.expand(rw))==p.reduce_word('m'*start+p.REL+'M'*start)
    for j,w in enumerate(p.WORDS): assert p.rewrite(w)==((j+1,),0)


def test_unfilled_presentation_characters_smith_and_bad_character():
    diag=p.smith_normal_form(p.RELATION_MATRIX,domain=s.ZZ).diagonal()
    assert sorted(abs(int(x)) for x in diag)==[1,4,4]
    assert len(p.characters())==64 and len(set(p.characters()))==64
    assert all(p.valid_character(a) for a in p.characters())
    assert len(set(p.base_characters()))==4
    assert set(p.base_characters())<=set(p.characters())
    assert len([a for a in p.characters() if a[0]==0])==16  # Only here add z=1.
    bad=next(a for a in product(range(4),repeat=4) if not p.valid_character(a))
    with pytest.raises(ValueError): p.twisted(14,bad)


def test_all_eight_base_maps_and_three_deck_lifts_act_on_every_character():
    chars=set(p.characters())
    for name in p.MAPS:
        for j in range(3):
            assert {p.act(a,name,j) for a in chars}==chars
            for w,row in zip(p.lift_words(name,j),p.action(name,j)):
                rw,end=p.rewrite(w)
                assert end==0 and p.exponents(rw)==row
                assert p.reduce_word(p.expand(rw))==p.reduce_word(w)
    for a in chars:
        b=a
        for _ in range(3): b=p.act(b,'id',1)
        assert b==a


@pytest.mark.parametrize('middle,embedding',[(14,1),(14,-1),(34,1),(34,-1)])
def test_actual_unipotent_restriction_irreducibility_and_periphery(middle,embedding):
    k,q,rho,_=v.context(middle,embedding); one=v.eye(4,k)
    for a in rho:
        b=a-one
        assert (b*b*b*b).is_zero_matrix
        assert (p.recover_from_cube(a)-a).is_zero_matrix
        bad=a.scalarmul(k(2))
        assert not (p.recover_from_cube(bad)-bad).is_zero_matrix
    assert p.matrix_algebra_determinant(middle,embedding)!=k.zero
    lifted=p.cover_rho(middle,embedding)
    lam=p.word(p.LONG,rho)
    assert (lifted[0]*lam-lam*lifted[0]).is_zero_matrix
    assert (lam-one).det()!=k.zero
    assert all((p.cover_word(w,lifted)-one).is_zero_matrix for w in p.RELS)


@pytest.mark.parametrize('middle',[14,34])
def test_all_characters_actual_cohomology_duals_and_pairing_witnesses(middle):
    rows=p.report(middle)['rows']
    assert len(rows)==64
    for row in rows:
        assert row['relators'] and row['chain_zero'] and row['exact_pairings']
        assert row['h0']==row['dual_h0']==0
        assert row['h1']==row['dual_h1']>=0
    # No assertion that all characters must be paired or acyclic: those are results.
    required=(1,3) if middle==14 else (2,)
    for t in required:
        assert p.complex_data(middle,p.base_characters()[t])['h1']>=1


@pytest.mark.parametrize('middle',[14,34])
def test_independent_cocycle_and_conjugate_root_controls(middle):
    selected=p.base_characters()+(next(a for a in p.characters() if a not in p.base_characters()),)
    for a in selected:
        for dual in (False,True):
            c=p.complex_data(middle,a,dual=dual)
            cc=p.complex_data(middle,a,embedding=-1,dual=dual)
            assert c['ranks']==cc['ranks']
            assert cc['relators'] and cc['chain_zero']
            rho=c['rho']; k=rho[0].domain
            vals=tuple(v.dm(s.Matrix([1+4*j+l for l in range(4)]),k) for j in range(4))
            for w in p.RELS:
                assert (p.fox(w,rho)*v.stack(*vals)-p.direct_cocycle(w,rho,vals)).is_zero_matrix
        for label in p.pairing_labels(a):
            assert all(r.is_zero_matrix for r in p.pairing_residuals(middle,a,label,embedding=-1))


@pytest.mark.parametrize('middle',[14,34])
def test_wrong_phase_and_wrong_map_are_not_pairings(middle):
    a=p.base_characters()[1]  # Restriction of phase i, not real.
    assert all(r.is_zero_matrix for r in p.pairing_residuals(middle,a,('theta',0,'linear')))
    assert any(not r.is_zero_matrix for r in p.pairing_residuals(middle,a,('theta',0,'antilinear')))
    k,q,rho,j=v.context(middle)
    assert any(not (g.inv().transpose()*j-j*g).is_zero_matrix for g in rho)
    for name in p.PAIR_NAMES:
        jj,eq=p.base_intertwiner(middle,name)
        assert eq.rank()==15 and jj.det()!=k.zero
        wrong=jj+v.eye(4,k)
        assert not (eq*p.flatten(wrong)).is_zero_matrix
