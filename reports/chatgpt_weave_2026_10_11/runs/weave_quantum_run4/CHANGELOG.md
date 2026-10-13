# Implementation record

1. The first current definitions used a globally reversed orientation in each of the two su(2) bases. Double poles were correct, but the simple-pole test returned minus the declared i*epsilon convention. Corrected the definitions to J=(i/4)chi^T L chi and I=-(i/4)chi^T R chi. The initial source is retained as verify_exact.initial_signs.py.txt. This is a declared convention change, not a new physical sign selection.
2. A radius-spectrum check initially used syntactic equality between two differently factored SymPy expressions. Replaced it by simplify(left-right)==0. The analytic expression did not change.
3. The initial numerical code attempted a nested fourth source derivative of an entire log trace, which exceeded the 45-second runtime budget. Replaced it by analytically differentiating the source exponents, then checking with direct finite source differences, independent position/log derivatives, and OPE limits. The expensive initial implementation is retained as verify_ward.initial_expensive_derivative.py.txt. The final code does not claim to have executed that fourth derivative.
4. Final exact, cochain and 60/90-digit numerical scripts completed successfully; output JSON and final logs are included.

The plan was written after exploratory reasoning. No blind preregistration or independent timestamp is claimed. Source/project files were not edited.
