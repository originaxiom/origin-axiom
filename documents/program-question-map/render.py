#!/usr/bin/env python3
"""Render the canonical closure registry as durable Markdown and local HTML."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import os
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import quote


STATUS_ORDER = (
    "OPEN",
    "PROVED",
    "REFUTED",
    "CONDITIONAL",
    "EXTERNAL_BLOCKER",
    "EMPIRICAL",
    "OUT_OF_SCOPE",
)

ANSWER_PREFIX = {
    "OPEN": "Open.",
    "PROVED": "Yes.",
    "REFUTED": "No.",
    "CONDITIONAL": "Conditionally.",
    "EXTERNAL_BLOCKER": "Not yet.",
    "EMPIRICAL": "Empirical evidence only.",
    "OUT_OF_SCOPE": "Outside the declared scope.",
}

STATUS_MEANING = {
    "OPEN": "Registered and typed, but its stated closure test has not yet been executed.",
    "PROVED": "A type-correct proof or reproducible exact computation establishes the scoped claim.",
    "REFUTED": "A proof, counterexample, or exact negative computation defeats the scoped claim.",
    "CONDITIONAL": "The claim follows only after the named underived input is assumed.",
    "EXTERNAL_BLOCKER": "The required construction or theorem is absent; the unblock condition is explicit.",
    "EMPIRICAL": "Only bounded numerical or observational evidence is available.",
    "OUT_OF_SCOPE": "A declared scope rule excludes the question from this campaign.",
}


def load_registry(path: Path) -> tuple[dict, str]:
    raw = path.read_bytes()
    data = json.loads(raw)
    return data, hashlib.sha256(raw).hexdigest()


def item_number(item: dict) -> int:
    return int(item["campaign_id"].split("C", 1)[1])


def answer(item: dict) -> str:
    prefix = ANSWER_PREFIX[item["adjudicated_status"]]
    evidence = " ".join(item.get("evidence", "").split())
    return f"{prefix} {evidence}" if evidence else prefix


def md_escape_table(value: object) -> str:
    return " ".join(str(value).split()).replace("|", "\\|")


def md_text(value: object) -> str:
    return " ".join(str(value).split())


def relative_reference(reference: str, source: Path, output: Path) -> str | None:
    if reference.startswith(("http://", "https://")):
        return reference
    target = Path(reference)
    if not target.is_absolute():
        target = (source.parent / target).resolve()
    if not target.exists():
        return None
    relative = os.path.relpath(target, output.parent.resolve())
    return quote(relative.replace(os.sep, "/"), safe="/:._-()")


def md_references(item: dict, key: str, source: Path, output: Path) -> str:
    references = item.get(key, [])
    if not references:
        return "None registered."
    links = []
    for reference in references:
        href = relative_reference(reference, source, output)
        if href is None:
            links.append(f"`{md_text(reference)}`")
        else:
            links.append(f"[`{md_text(reference)}`]({href})")
    return ", ".join(links)


def id_links(ids: list[str]) -> str:
    if not ids:
        return "None."
    return ", ".join(f"[{item}](#{item.lower()})" for item in ids)


def render_markdown(data: dict, digest: str, source: Path, output: Path, as_of: str) -> str:
    items = sorted(data["items"], key=item_number)
    statuses = Counter(item["adjudicated_status"] for item in items)
    domains = Counter(item["domain"] for item in items)
    by_domain: dict[str, list[dict]] = defaultdict(list)
    for item in items:
        by_domain[item["domain"]].append(item)

    lines = [
        "# Origin Axiom programme question–answer map",
        "",
        f"**As of:** {as_of}",
        "",
        f"**Canonical questions:** {len(items)}",
        "",
        f"**Registry SHA-256:** `{digest}`",
        "",
        "This is the durable, source-linked map of every canonical question currently registered by",
        "the independent closure campaign. It distinguishes a proved narrow theorem from a broader",
        "physical interpretation. `OPEN` is a live obligation. `CONDITIONAL` and",
        "`EXTERNAL_BLOCKER` mean the question is accounted for, not that the parameter-free",
        "programme has answered it affirmatively.",
        "",
        "## How to update this map",
        "",
        "1. Edit the canonical JSON row, never only the rendered prose.",
        "2. Give every new child question a stable `OA-C####` ID before closing its parent.",
        "3. Preserve the narrowest proved scope and name every hidden input.",
        "4. Rerun the renderer and campaign validator; commit the JSON, Markdown, and proof artifact",
        "   together.",
        "",
        "```text",
        "python3 documents/program-question-map/render.py \\",
        "  --source documents/program-question-map/inventory/backbone.json \\",
        "  --markdown documents/PROGRAM_QUESTION_ANSWER_MAP.md \\",
        f"  --as-of {as_of}",
        "```",
        "",
        "## Status dashboard",
        "",
        "| status | count | meaning |",
        "|---|---:|---|",
    ]
    for status in STATUS_ORDER:
        lines.append(
            f"| `{status}` | {statuses.get(status, 0)} | {STATUS_MEANING[status]} |"
        )

    lines.extend((
        "",
        "## Domain dashboard",
        "",
        "| domain | questions |",
        "|---|---:|",
    ))
    for domain in sorted(domains):
        lines.append(f"| `{domain}` | {domains[domain]} |")

    lines.extend((
        "",
        "## Complete index",
        "",
        "| ID | status | domain | question | direct answer |",
        "|---|---|---|---|---|",
    ))
    for item in items:
        lines.append(
            "| [{id}](#{anchor}) | `{status}` | `{domain}` | {question} | {answer} |".format(
                id=item["campaign_id"],
                anchor=item["campaign_id"].lower(),
                status=item["adjudicated_status"],
                domain=md_escape_table(item["domain"]),
                question=md_escape_table(item["question"]),
                answer=md_escape_table(answer(item)),
            )
        )

    lines.extend(("", "## Detailed answer records", ""))
    for domain in sorted(by_domain):
        lines.extend((f"## Domain: `{domain}`", ""))
        for item in sorted(by_domain[domain], key=item_number):
            item_id = item["campaign_id"]
            lines.extend((
                f'<a id="{item_id.lower()}"></a>',
                f"### {item_id} — `{item['adjudicated_status']}`",
                "",
                f"- **Question:** {md_text(item['question'])}",
                f"- **Answer:** {md_text(answer(item))}",
                f"- **Kind/domain:** `{item.get('kind', 'unspecified')}` / `{item['domain']}`",
                f"- **Depends on:** {id_links(item.get('dependencies', []))}",
                f"- **Leads to:** {id_links(item.get('children', []))}",
                f"- **Closure test:** {md_text(item['closure_criterion'])}",
                f"- **Falsifier:** {md_text(item['falsifier'])}",
                f"- **Scope:** {md_text(item.get('scope', 'No additional scope recorded.'))}",
                f"- **Aliases:** {', '.join(f'`{md_text(alias)}`' for alias in item.get('aliases', [])) or 'None.'}",
                f"- **Sources:** {md_references(item, 'sources', source, output)}",
                f"- **Deepest artifacts:** {md_references(item, 'deepest_artifacts', source, output)}",
                "",
            ))

    lines.extend((
        "## Reading the map correctly",
        "",
        "- A `PROVED` row proves only its recorded scope; inspect its dependencies before using it",
        "  downstream.",
        "- An `OPEN` row is a live, typed task; it is neither evidence nor a blocker declaration.",
        "- A `REFUTED` row closes the named route, not every imaginable replacement.",
        "- A `CONDITIONAL` row exposes the exact unpaid input rather than hiding it.",
        "- An `EXTERNAL_BLOCKER` is terminal for the present campaign state but becomes active when",
        "  its stated construction or theorem is supplied.",
        "- New questions discovered during verification must be added before the parent can be called",
        "  exhausted.",
        "",
    ))
    return "\n".join(lines)


def html_linked_ids(ids: list[str]) -> str:
    if not ids:
        return "None"
    return ", ".join(
        f'<a href="#{html.escape(item.lower())}">{html.escape(item)}</a>' for item in ids
    )


def html_references(item: dict, key: str, source: Path, output: Path) -> str:
    references = item.get(key, [])
    if not references:
        return "None registered"
    result = []
    for reference in references:
        href = relative_reference(reference, source, output)
        if href is None:
            result.append(f"<code>{html.escape(reference)}</code>")
        else:
            result.append(
                f'<a href="{html.escape(href, quote=True)}">{html.escape(reference)}</a>'
            )
    return ", ".join(result)


def render_html(data: dict, digest: str, source: Path, output: Path, as_of: str) -> str:
    items = sorted(data["items"], key=item_number)
    statuses = Counter(item["adjudicated_status"] for item in items)
    domains = sorted({item["domain"] for item in items})

    cards = []
    for item in items:
        item_id = item["campaign_id"]
        status = item["adjudicated_status"]
        searchable = " ".join((
            item_id,
            status,
            item["domain"],
            item["question"],
            answer(item),
            " ".join(item.get("aliases", [])),
        )).lower()
        cards.append(f"""
<article class="card" id="{item_id.lower()}" data-status="{status}"
         data-domain="{html.escape(item['domain'])}" data-search="{html.escape(searchable, quote=True)}">
  <header><a class="id" href="#{item_id.lower()}">{item_id}</a>
    <span class="badge {status.lower()}">{status}</span>
    <span class="domain">{html.escape(item['domain'])}</span></header>
  <h2>{html.escape(item['question'])}</h2>
  <p class="answer"><strong>{html.escape(ANSWER_PREFIX[status])}</strong>
    {html.escape(' '.join(item.get('evidence', '').split()))}</p>
  <details>
    <summary>Dependencies, scope, and evidence</summary>
    <dl>
      <dt>Kind</dt><dd>{html.escape(item.get('kind', 'unspecified'))}</dd>
      <dt>Depends on</dt><dd>{html_linked_ids(item.get('dependencies', []))}</dd>
      <dt>Leads to</dt><dd>{html_linked_ids(item.get('children', []))}</dd>
      <dt>Closure test</dt><dd>{html.escape(item['closure_criterion'])}</dd>
      <dt>Falsifier</dt><dd>{html.escape(item['falsifier'])}</dd>
      <dt>Scope</dt><dd>{html.escape(item.get('scope', 'No additional scope recorded.'))}</dd>
      <dt>Aliases</dt><dd>{html.escape(', '.join(item.get('aliases', [])) or 'None')}</dd>
      <dt>Sources</dt><dd>{html_references(item, 'sources', source, output)}</dd>
      <dt>Deepest artifacts</dt><dd>{html_references(item, 'deepest_artifacts', source, output)}</dd>
    </dl>
  </details>
</article>""")

    status_tiles = "".join(
        f'<button class="tile" data-pick-status="{status}"><b>{statuses.get(status, 0)}</b><span>{status}</span></button>'
        for status in STATUS_ORDER
    )
    domain_options = "".join(
        f'<option value="{html.escape(domain)}">{html.escape(domain)}</option>'
        for domain in domains
    )
    cards_html = "\n".join(cards)

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Origin Axiom programme question–answer map</title>
<style>
:root{{--bg:#f5f4ef;--paper:#fff;--ink:#20231f;--muted:#62685f;--line:#d8d9d1;
--open:#b14f00;
--proved:#176b43;--refuted:#a12d2d;--conditional:#946400;--external:#6745a3;
--empirical:#176a87;--out:#606060}}*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);
color:var(--ink);font:16px/1.5 ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}}
main{{max-width:1180px;margin:auto;padding:28px}}h1{{font-size:clamp(2rem,5vw,4rem);line-height:1.02;
letter-spacing:-.04em;margin:.25em 0}}.lede{{max-width:850px;color:var(--muted)}}code{{font-size:.9em}}
.meta{{font-size:.9rem;color:var(--muted)}}.dashboard{{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin:24px 0}}
.tile{{border:1px solid var(--line);background:var(--paper);padding:14px;text-align:left;border-radius:10px;cursor:pointer}}
.tile b{{display:block;font-size:1.7rem}}.tile span{{font-size:.78rem;color:var(--muted)}}
.controls{{position:sticky;top:0;z-index:4;display:grid;grid-template-columns:2fr 1fr 1fr auto;gap:10px;
padding:12px;background:rgba(245,244,239,.96);backdrop-filter:blur(8px);border-block:1px solid var(--line)}}
input,select,button{{font:inherit}}input,select,.reset{{width:100%;padding:10px;border:1px solid var(--line);border-radius:8px;background:#fff}}
.count{{align-self:center;color:var(--muted);white-space:nowrap}}.cards{{display:grid;gap:14px;margin-top:20px}}
.card{{background:var(--paper);border:1px solid var(--line);border-left:6px solid var(--line);border-radius:12px;padding:18px;scroll-margin-top:90px}}
.card[data-status=OPEN]{{border-left-color:var(--open)}}.card[data-status=PROVED]{{border-left-color:var(--proved)}}.card[data-status=REFUTED]{{border-left-color:var(--refuted)}}
.card[data-status=CONDITIONAL]{{border-left-color:var(--conditional)}}.card[data-status=EXTERNAL_BLOCKER]{{border-left-color:var(--external)}}
.card[data-status=EMPIRICAL]{{border-left-color:var(--empirical)}}.card[data-status=OUT_OF_SCOPE]{{border-left-color:var(--out)}}
.card header{{display:flex;gap:9px;align-items:center;flex-wrap:wrap}}.id{{font-weight:800;color:var(--ink)}}
.badge,.domain{{font-size:.72rem;padding:3px 7px;border-radius:99px;background:#ecece7}}.badge{{color:#fff}}
.open{{background:var(--open)}}.proved{{background:var(--proved)}}.refuted{{background:var(--refuted)}}.conditional{{background:var(--conditional)}}
.external_blocker{{background:var(--external)}}.empirical{{background:var(--empirical)}}.out_of_scope{{background:var(--out)}}
.card h2{{font-size:1.18rem;line-height:1.3;margin:.7em 0}}.answer{{margin:.4em 0 1em}}
details{{border-top:1px solid var(--line);padding-top:9px}}summary{{cursor:pointer;color:var(--muted)}}
dl{{display:grid;grid-template-columns:140px 1fr;gap:7px 14px}}dt{{font-weight:700}}dd{{margin:0;min-width:0}}
a{{color:#285f89}}.hidden{{display:none}}@media(max-width:720px){{main{{padding:16px}}.controls{{grid-template-columns:1fr 1fr;position:static}}dl{{grid-template-columns:1fr}}}}
</style>
</head>
<body><main>
<p class="meta">As of {html.escape(as_of)} · {len(items)} canonical questions · registry SHA-256 <code>{digest}</code></p>
<h1>Programme question–answer map</h1>
<p class="lede">Every registered question, its direct status-aware answer, dependencies, scope,
closure test, falsifier, and evidence. Open rows are live work. Conditional and external-blocker rows are accounted for,
but they are not affirmative parameter-free results.</p>
<section class="dashboard">{status_tiles}</section>
<section class="controls">
  <input id="search" type="search" placeholder="Search questions, answers, IDs, aliases…">
  <select id="status"><option value="">All statuses</option>{''.join(f'<option>{s}</option>' for s in STATUS_ORDER)}</select>
  <select id="domain"><option value="">All domains</option>{domain_options}</select>
  <span id="count" class="count"></span>
</section>
<section id="cards" class="cards">{cards_html}</section>
</main>
<script>
const cards=[...document.querySelectorAll('.card')], search=document.querySelector('#search'),
status=document.querySelector('#status'), domain=document.querySelector('#domain'), count=document.querySelector('#count');
function apply(){{const q=search.value.trim().toLowerCase();let shown=0;for(const card of cards){{
const ok=(!q||card.dataset.search.includes(q))&&(!status.value||card.dataset.status===status.value)&&(!domain.value||card.dataset.domain===domain.value);
card.classList.toggle('hidden',!ok);if(ok)shown++;}}count.textContent=`${{shown}} / ${{cards.length}} shown`;}}
[search,status,domain].forEach(x=>x.addEventListener('input',apply));
document.querySelectorAll('[data-pick-status]').forEach(x=>x.addEventListener('click',()=>{{status.value=x.dataset.pickStatus;apply();scrollTo({{top:document.querySelector('.controls').offsetTop,behavior:'smooth'}});}}));
apply();
</script></body></html>
"""


def write_or_check(path: Path, content: str, check: bool) -> None:
    content = content.rstrip() + "\n"
    if check:
        if not path.is_file() or path.read_text(encoding="utf-8") != content:
            raise SystemExit(f"stale generated map: {path}")
        print(f"CURRENT {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    print(f"WROTE {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--markdown", type=Path, required=True)
    parser.add_argument("--html", type=Path)
    parser.add_argument("--as-of", default=date.today().isoformat())
    parser.add_argument("--check", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    source = args.source.resolve()
    markdown = args.markdown.resolve()
    data, digest = load_registry(source)
    write_or_check(
        markdown,
        render_markdown(data, digest, source, markdown, args.as_of),
        args.check,
    )
    if args.html:
        output_html = args.html.resolve()
        write_or_check(
            output_html,
            render_html(data, digest, source, output_html, args.as_of),
            args.check,
        )


if __name__ == "__main__":
    main()
