"""R78 named geometry, interval checks in Sage; no record writes."""
import sage.all  # required before snappy to enable verified interval methods
import json
import snappy


def certify(manifold, label):
    intervals = []
    for bits in (100, 160):
        success, shapes = manifold.verify_hyperbolicity(bits_prec=bits)
        intervals.append({"bits": bits, "verified": bool(success), "shape_count": len(shapes),
                          "shapes": [str(z) for z in shapes]})
        print(json.dumps({"label": label, "interval": intervals[-1]}), flush=True)
        assert success, (label, bits, "hyperbolicity not certified")
    signature = manifold.isometry_signature(verified=True)
    assert isinstance(signature, str) and signature
    return {"label": label, "homology": str(manifold.homology()),
            "cusps": manifold.num_cusps(), "orientable": manifold.is_orientable(),
            "complete": all(c["is_complete"] for c in manifold.cusp_info()),
            "isometry_signature_verified": signature, "intervals": intervals}


def main():
    results = {}
    for name, expected_h1 in (("b+-LRLR", "Z/3 + Z/3 + Z"),
                              ("b++LRLR", "Z/5 + Z"),
                              ("b++LRLRLRLR", "Z/3 + Z/15 + Z")):
        manifold = snappy.Manifold(name)
        rec = certify(manifold, name)
        assert rec["homology"] == expected_h1
        assert rec["cusps"] == 1 and rec["orientable"] and rec["complete"]
        names = manifold.identify()
        assert names, (name, "no named census identification")
        # identify() is only navigation. Equality below is a verified
        # complete-cusped isometry comparison, not a floating-point match.
        chosen = names[0].name()
        named = snappy.Manifold(chosen)
        named_rec = certify(named, chosen)
        assert rec["isometry_signature_verified"] == named_rec["isometry_signature_verified"]
        rec["census_name"] = chosen
        rec["named_certificate"] = named_rec
        results[name] = rec
    print(json.dumps({"snappy_version": snappy.__version__, "sage_version": sage.all.version(),
                      "results": results, "physical_identification": False}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
