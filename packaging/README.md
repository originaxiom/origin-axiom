# Namespace reservations

Ready-to-publish placeholders. Status (2026-07-14): PyPI both names AVAILABLE;
npm both names AVAILABLE; brew reserved via the tap
github.com/originaxiom/homebrew-origin-axiom; crates.io / Docker Hub need
account signup (anonymous checks blocked).

## Publish — PyPI (needs a pypi.org account + API token)
    cd packaging/pypi-origin-axiom  && python3 -m build && twine upload dist/*
    cd packaging/pypi-originaxiom   && python3 -m build && twine upload dist/*
Note PEP 541: pure name-squats can be reclaimed — these placeholders carry the
real project description and a functional module, which is the tolerated form.

## Publish — npm (needs an npmjs.com account, `npm login`)
    cd packaging/npm-origin-axiom  && npm publish --access public
    cd packaging/npm-originaxiom   && npm publish --access public

## Brew
Already reserved: `brew tap originaxiom/origin-axiom` resolves to the tap repo.
Formulas land there when tooling ships.
