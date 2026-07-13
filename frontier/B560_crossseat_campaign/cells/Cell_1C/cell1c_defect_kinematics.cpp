#include <bits/stdc++.h>
using namespace std;

struct HashPair {
    uint64_t first;
    uint64_t second;
    bool operator==(const HashPair& other) const {
        return first == other.first && second == other.second;
    }
};

struct HashPairHasher {
    size_t operator()(const HashPair& value) const {
        return value.first ^ (
            value.second + 0x9e3779b97f4a7c15ULL
            + (value.first << 6) + (value.first >> 2)
        );
    }
};

struct Component {
    int start;
    int end;
    int charge;
};

struct AnnihilationWitness {
    int charge;
    int length;
    string background;
    string pair_configuration;
    Component first;
    Component second;
};

struct FusionWitness {
    int first_charge;
    int second_charge;
    int total_charge;
    int length;
    string background;
    string split_configuration;
    string fused_configuration;
    vector<Component> split_components;
    Component fused_component;
};

struct MotionWitness {
    int charge;
    int length;
    string background;
    string first_configuration;
    string second_configuration;
    Component first_component;
    Component second_component;
};

int letter_charge(char letter) {
    if (letter == 'a') return 1;
    if (letter == 'b') return 3;
    if (letter == 'A') return 6;
    return 7;
}

vector<Component> difference_components(
    const string& background,
    const string& configuration
) {
    vector<Component> result;
    int index = 0;
    const int size = static_cast<int>(background.size());

    while (index < size) {
        while (
            index < size
            && background[index] == configuration[index]
        ) {
            ++index;
        }
        if (index == size) break;

        const int start = index;
        int charge = 0;
        while (
            index < size
            && background[index] != configuration[index]
        ) {
            charge += (
                letter_charge(configuration[index])
                - letter_charge(background[index])
            );
            charge %= 11;
            if (charge < 0) charge += 11;
            ++index;
        }
        result.push_back({start, index - 1, charge});
    }

    return result;
}

string grow_word(int depth) {
    const map<char, string> substitution = {
        {'a', "abAAB"},
        {'b', "aAB"},
        {'A', "abAB"},
        {'B', "aA"},
    };

    string word = "a";
    for (int generation = 0; generation < depth; ++generation) {
        string next;
        next.reserve(word.size() * 4);
        for (char letter : word) {
            next += substitution.at(letter);
        }
        word.swap(next);
    }
    return word;
}

struct RollingHash {
    vector<uint64_t> power_first;
    vector<uint64_t> power_second;
    vector<uint64_t> prefix_first;
    vector<uint64_t> prefix_second;

    explicit RollingHash(const string& word) {
        const uint64_t base_first = 1315423911ULL;
        const uint64_t base_second = 11400714819323198485ULL;
        const int size = static_cast<int>(word.size());

        power_first.assign(size + 1, 1);
        power_second.assign(size + 1, 1);
        prefix_first.assign(size + 1, 0);
        prefix_second.assign(size + 1, 0);

        for (int index = 0; index < size; ++index) {
            power_first[index + 1] = (
                power_first[index] * base_first
            );
            power_second[index + 1] = (
                power_second[index] * base_second
            );
            prefix_first[index + 1] = (
                prefix_first[index] * base_first
                + static_cast<unsigned char>(word[index]) + 1
            );
            prefix_second[index + 1] = (
                prefix_second[index] * base_second
                + static_cast<unsigned char>(word[index]) + 1
            );
        }
    }

    HashPair get(int start, int length) const {
        return {
            prefix_first[start + length]
                - prefix_first[start] * power_first[length],
            prefix_second[start + length]
                - prefix_second[start] * power_second[length],
        };
    }
};

vector<int> exact_factor_representatives(
    const string& word,
    const RollingHash& hash,
    int length
) {
    unordered_map<HashPair, vector<int>, HashPairHasher> buckets;
    buckets.reserve(4 * length + 100);

    for (
        int start = 0;
        start + length <= static_cast<int>(word.size());
        ++start
    ) {
        const HashPair key = hash.get(start, length);
        auto& representatives = buckets[key];

        bool already_seen = false;
        for (int representative : representatives) {
            if (
                word.compare(
                    representative,
                    length,
                    word,
                    start,
                    length
                ) == 0
            ) {
                already_seen = true;
                break;
            }
        }

        if (!already_seen) {
            representatives.push_back(start);
        }
    }

    vector<int> result;
    for (const auto& [key, representatives] : buckets) {
        result.insert(
            result.end(),
            representatives.begin(),
            representatives.end()
        );
    }
    return result;
}

bool factor_sets_equal_by_count(
    const string& smaller_word,
    const RollingHash& smaller_hash,
    const string& larger_word,
    const RollingHash& larger_hash,
    int length,
    int larger_count
) {
    // sigma^9(a) is a prefix of sigma^10(a), so its factor set is a
    // subset. Equal exact counts therefore imply equal factor sets.
    const int smaller_count = static_cast<int>(
        exact_factor_representatives(
            smaller_word,
            smaller_hash,
            length
        ).size()
    );
    return smaller_count == larger_count;
}

string component_text(const Component& component) {
    return (
        to_string(component.start)
        + "-" + to_string(component.end)
        + ":" + to_string(component.charge)
    );
}

int main() {
    const int context_radius = 3;
    const int maximum_length = 500;

    const string word_depth_9 = grow_word(9);
    const string word_depth_10 = grow_word(10);
    const RollingHash hash_depth_9(word_depth_9);
    const RollingHash hash_depth_10(word_depth_10);

    map<int, MotionWitness> motion_witnesses;
    map<int, AnnihilationWitness> annihilation_witnesses;
    map<pair<int, int>, FusionWitness> fusion_witnesses;

    int stable_length_count = 0;
    int factor_count_at_maximum = 0;

    for (
        int factor_length = 2 * context_radius + 1;
        factor_length <= maximum_length;
        ++factor_length
    ) {
        const vector<int> representatives =
            exact_factor_representatives(
                word_depth_10,
                hash_depth_10,
                factor_length
            );

        if (factor_length == maximum_length) {
            factor_count_at_maximum = static_cast<int>(
                representatives.size()
            );
        }

        if (
            factor_sets_equal_by_count(
                word_depth_9,
                hash_depth_9,
                word_depth_10,
                hash_depth_10,
                factor_length,
                static_cast<int>(representatives.size())
            )
        ) {
            ++stable_length_count;
        }

        unordered_map<string, vector<int>> boundary_groups;
        for (int start : representatives) {
            const string boundary_key = (
                word_depth_10.substr(start, context_radius)
                + "|"
                + word_depth_10.substr(
                    start + factor_length - context_radius,
                    context_radius
                )
            );
            boundary_groups[boundary_key].push_back(start);
        }

        for (const auto& [boundary, positions] : boundary_groups) {
            if (positions.size() < 2) continue;

            vector<string> factors;
            factors.reserve(positions.size());
            for (int position : positions) {
                factors.push_back(
                    word_depth_10.substr(position, factor_length)
                );
            }

            for (
                int background_index = 0;
                background_index < static_cast<int>(factors.size());
                ++background_index
            ) {
                const string& background = factors[background_index];

                vector<pair<int, Component>> one_component;
                vector<pair<int, vector<Component>>> two_components;

                for (
                    int alternative_index = 0;
                    alternative_index < static_cast<int>(factors.size());
                    ++alternative_index
                ) {
                    if (alternative_index == background_index) continue;

                    const vector<Component> components =
                        difference_components(
                            background,
                            factors[alternative_index]
                        );

                    if (
                        components.size() == 1
                        && components[0].charge != 0
                    ) {
                        one_component.push_back({
                            alternative_index,
                            components[0],
                        });
                    }

                    if (
                        components.size() == 2
                        && components[0].charge != 0
                        && components[1].charge != 0
                    ) {
                        two_components.push_back({
                            alternative_index,
                            components,
                        });

                        if (
                            (
                                components[0].charge
                                + components[1].charge
                            ) % 11 == 0
                        ) {
                            const int charge =
                                components[0].charge;

                            if (
                                annihilation_witnesses.count(charge)
                                == 0
                            ) {
                                annihilation_witnesses[charge] = {
                                    charge,
                                    factor_length,
                                    background,
                                    factors[alternative_index],
                                    components[0],
                                    components[1],
                                };
                            }
                        }
                    }
                }

                for (
                    int first_index = 0;
                    first_index
                        < static_cast<int>(one_component.size());
                    ++first_index
                ) {
                    for (
                        int second_index = first_index + 1;
                        second_index
                            < static_cast<int>(one_component.size());
                        ++second_index
                    ) {
                        const auto& first =
                            one_component[first_index];
                        const auto& second =
                            one_component[second_index];

                        if (
                            first.second.charge
                                == second.second.charge
                            && (
                                first.second.start
                                    != second.second.start
                                || first.second.end
                                    != second.second.end
                            )
                        ) {
                            const int charge =
                                first.second.charge;

                            if (
                                motion_witnesses.count(charge)
                                == 0
                            ) {
                                motion_witnesses[charge] = {
                                    charge,
                                    factor_length,
                                    background,
                                    factors[first.first],
                                    factors[second.first],
                                    first.second,
                                    second.second,
                                };
                            }
                        }
                    }
                }

                for (const auto& split : two_components) {
                    const int first_charge =
                        split.second[0].charge;
                    const int second_charge =
                        split.second[1].charge;
                    const int total_charge =
                        (first_charge + second_charge) % 11;

                    if (total_charge == 0) continue;

                    for (const auto& fused : one_component) {
                        if (
                            fused.second.charge != total_charge
                        ) {
                            continue;
                        }

                        const pair<int, int> key = {
                            first_charge,
                            second_charge,
                        };

                        if (fusion_witnesses.count(key) == 0) {
                            fusion_witnesses[key] = {
                                first_charge,
                                second_charge,
                                total_charge,
                                factor_length,
                                background,
                                factors[split.first],
                                factors[fused.first],
                                split.second,
                                fused.second,
                            };
                        }
                    }
                }
            }
        }
    }

    cout << "SUMMARY"
         << "\t" << maximum_length
         << "\t" << stable_length_count
         << "\t" << factor_count_at_maximum
         << "\t" << motion_witnesses.size()
         << "\t" << annihilation_witnesses.size()
         << "\t" << fusion_witnesses.size()
         << "\n";

    for (const auto& [charge, witness] : motion_witnesses) {
        cout << "MOTION"
             << "\t" << witness.charge
             << "\t" << witness.length
             << "\t" << witness.background
             << "\t" << witness.first_configuration
             << "\t" << witness.second_configuration
             << "\t" << component_text(
                    witness.first_component
                )
             << "\t" << component_text(
                    witness.second_component
                )
             << "\n";
    }

    for (
        const auto& [charge, witness] :
        annihilation_witnesses
    ) {
        cout << "ANNIHILATION"
             << "\t" << witness.charge
             << "\t" << witness.length
             << "\t" << witness.background
             << "\t" << witness.pair_configuration
             << "\t" << component_text(witness.first)
             << "\t" << component_text(witness.second)
             << "\n";
    }

    for (const auto& [charges, witness] : fusion_witnesses) {
        cout << "FUSION"
             << "\t" << witness.first_charge
             << "\t" << witness.second_charge
             << "\t" << witness.total_charge
             << "\t" << witness.length
             << "\t" << witness.background
             << "\t" << witness.split_configuration
             << "\t" << witness.fused_configuration
             << "\t" << component_text(
                    witness.split_components[0]
                )
             << "\t" << component_text(
                    witness.split_components[1]
                )
             << "\t" << component_text(
                    witness.fused_component
                )
             << "\n";
    }

    return 0;
}
