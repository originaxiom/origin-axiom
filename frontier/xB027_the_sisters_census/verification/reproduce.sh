#!/bin/sh
# xB027 -- C1 (the binding control) then the sister census.
cd "$(dirname "$0")" && python3 census.py b++ 2 3 4 && python3 census.py b+- 2 3 4
