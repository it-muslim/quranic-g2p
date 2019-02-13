from typing import Dict, List

import json
import re


def all_matches(pattern: str, string: str) -> List[str]:
    """Assume that the first group is the one we need."""
    pattern = re.compile(pattern)
    result = []
    match = pattern.search(string)
    while match is not None:
        result.append(match.start(1))
        match = pattern.search(string, match.start(0) + 1)
    return result

def merge_variants(text: str, variants: List[List[str]]) -> Dict[str, List[str]]:
    pass

def main():
    with open("rules.example.json") as fin:
        rules = json.load(fin)

    with open("text.txt") as fin:
        text = " ".join(fin.read().strip().split())

    variants = [[] for _ in text]
    for rule in rules.values():
        for pattern, pronunciations in rule.items():
            indices = all_matches(pattern, text)
            for idx in indices:
                variants[idx] += pronunciations

    print(variants)


if __name__ == "__main__":
    main()
