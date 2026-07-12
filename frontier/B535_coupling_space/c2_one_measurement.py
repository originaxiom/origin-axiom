#!/usr/bin/env python3
"""B535 C2: the one-measurement test at word level.

Matrix level is a theorem (B533 audit): measuring beta fixes the incidence
matrix uniquely up to GL(4,Z). Word level: the SAME abelianization lifts to
60*6*24*2 = 17,280 substitutions (all words with sigma's image Parikh
vectors). How much does the one measurement + the grammar constrain?

For every lift: generate the language (sigma^8 from 'a', ~34k chars),
extract the bigram grammar and the length-6 factor set. Count:
  (a) lifts with sigma's exact 7-adjacency grammar
  (b) lifts with sigma's exact length-6 language
  (c) distinct grammars and distinct languages across all lifts
"""
from itertools import permutations
from collections import Counter

SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
DEPTH = 8


def language_data(sub, depth=DEPTH):
    w = 'a'
    for _ in range(depth):
        w = ''.join(sub[c] for c in w)
    bigrams = frozenset(w[i:i+2] for i in range(len(w) - 1))
    six = frozenset(w[i:i+6] for i in range(len(w) - 5))
    return bigrams, six


def main():
    ref_bi, ref_six = language_data(SUB)
    print(f"sigma: {len(ref_bi)} bigrams (banked: 7), "
          f"{len(ref_six)} six-factors")

    arr_a = sorted(set(permutations('abAAB')))
    arr_b = sorted(set(permutations('aAB')))
    arr_A = sorted(set(permutations('abAB')))
    arr_B = sorted(set(permutations('aA')))
    total = len(arr_a) * len(arr_b) * len(arr_A) * len(arr_B)
    print(f"lifts: {len(arr_a)}*{len(arr_b)}*{len(arr_A)}*{len(arr_B)} = {total}")

    n_gram = n_lang = 0
    grammars = Counter()
    languages = Counter()
    gram_hits = []
    for wa in arr_a:
        for wb in arr_b:
            for wA in arr_A:
                for wB in arr_B:
                    sub = {'a': ''.join(wa), 'b': ''.join(wb),
                           'A': ''.join(wA), 'B': ''.join(wB)}
                    bi, six = language_data(sub)
                    grammars[bi] += 1
                    languages[six] += 1
                    if bi == ref_bi:
                        n_gram += 1
                        gram_hits.append(sub)
                        if six == ref_six:
                            n_lang += 1

    print(f"\nRESULTS over {total} lifts of the measured abelianization:")
    print(f"  lifts with sigma's exact 7-bigram grammar: {n_gram}")
    print(f"  lifts with sigma's exact length-6 language: {n_lang}")
    print(f"  distinct bigram grammars: {len(grammars)}")
    print(f"  distinct length-6 languages: {len(languages)}")

    sizes = sorted(languages.values(), reverse=True)
    print(f"  language class sizes (top 10): {sizes[:10]}")
    print(f"  grammar size distribution: "
          f"{Counter(len(g) for g in grammars).most_common()}")

    if n_gram <= 40:
        print(f"\n  the grammar-matching lifts:")
        for s in gram_hits:
            same = language_data(s)[1] == ref_six
            print(f"    a->{s['a']} b->{s['b']} A->{s['A']} B->{s['B']}"
                  f"{'   [= sigma language]' if same else ''}")


if __name__ == '__main__':
    main()
