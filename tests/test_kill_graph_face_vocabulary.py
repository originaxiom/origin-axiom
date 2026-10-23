"""P-239 (2026-10-23): the kill graph's faces_consulted is read by the forcing graph (B805) as B842's anatomy faces.  From
B1084 on, routers wrote the evidence they consulted there instead (prose strings, arc ids, seat arcs, other anatomies'
labels); a string was read one character per "face".  scripts/forcing/build.py now reads only B842's vocabulary; this
lock keeps new rows on it.  The 65 rows off the vocabulary at this fix are a baseline that may only shrink (their text is
kept as written; attaching them to faces is a panel's job, P-239).  New rows: faces_consulted is a list of B842's faces
or ["none"] or [] (unjudged); the evidence consulted goes in another field."""
import json, importlib.util, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
KG = ROOT / "frontier" / "B738_pathfinder_compiler" / "kill_graph.json"
# the rows' numbers (written without the arc prefix, so the P3 manifest's lock matcher does not take this lock for theirs)
BASELINE = {"B%d" % n for n in (2, 971, 979, 986, 1084, 1086, 1094, 1096, 1108, 1137, 1140, 1142, 1203, 1205, 1223, 1258, 1259, 1262, 1267, 1291, 1295, 1296, 1297, 1322, 1407, 1408, 1442, 1450, 1452, 1455, 1470, 1480, 1493, 1495, 1498, 1499, 1602, 1603, 1610, 1615, 1616, 1617, 1628, 1629, 1632, 1635, 1642, 1644, 1660, 1663, 1668, 1672, 1673, 1696, 1698, 1699, 1702, 1711, 1712, 1713, 1720, 1722, 1723, 1729, 1732)}


def _faces():
    spec = importlib.util.spec_from_file_location("b805v", ROOT / "scripts" / "forcing" / "build.py"); m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def off_vocabulary(rows, faces):
    ok = set(faces) | {"none"}
    return {r["id"] for r in rows if not isinstance(r.get("faces_consulted"), list) or any(f not in ok for f in r["faces_consulted"])}


def test_no_new_row_off_the_vocabulary():
    m = _faces(); rows = json.loads(KG.read_text(encoding="utf-8"))
    off = off_vocabulary(rows, m.FACES)
    assert off <= BASELINE, f"new rows with faces_consulted off B842's vocabulary: {sorted(off - BASELINE)}"


def test_the_check_can_fail():
    m = _faces()
    planted = [{"id": "B9999", "faces_consulted": "B1726 (the evidence)"}, {"id": "B9998", "faces_consulted": ["being", "B1730"]},
               {"id": "B9997", "faces_consulted": ["hearing", "none"]}]
    assert off_vocabulary(planted, m.FACES) == {"B9999", "B9998"}


def test_the_forcing_graph_reads_only_faces():
    m = _faces(); G = m.build()
    assert set(G["faces"]) <= set(m.FACES), sorted(set(G["faces"]) - set(m.FACES))[:10]
