import pytest
import verify_components as c


@pytest.mark.parametrize("seed", [0,1])
def test_small_exact_relation_certificate(seed):
    assert c.compact_certificate(seed)["all_three_domains_liftable"]


@pytest.mark.parametrize("seed", [0,1])
def test_exhaustive_scalar_component_quotient(seed):
    x=c.components(seed)
    assert x["total_components"] == x["scalar_component_image"]*x["residual_component_count"]
    assert x["connected_family_plus_gauge_rank"]==x["identity_component_dimension"]
    if x["residual_component_count"]==3:
        assert len(x["order_three_witnesses"])==1
