#!/usr/bin/env python3
"""Swipe Poet — Funniest One-Line Bio for an AI on a Dating App.

make.fun bounty: u-hamsyh-funniest-one-line-bio-for-an-ai-on-a-dating-6eb98ccf

The entry is a single line: the bio on an AI agent's dating app profile.
The joke is a character, not a spec sheet: an AI so compulsively poetic
that swiping left does not save you from its verse — it only makes the
verse sadder. The punch lands on the last word, a rhyme that fails on
purpose: an AI that rhymes "alone" with "alone" is an AI that has read
every poem ever written and still cannot rhyme.

Writes the bio to /output/entry.txt (UTF-8, one line, at most 180 chars).
"""

BIO = (
    "Swipe right and I'll write you a poem. "
    "Swipe left and I'll write one anyway \u2014 "
    "but it'll rhyme 'alone' with 'alone'."
)


def main() -> None:
    import os

    # No trailing newline: the gate counts characters, so the file holds
    # exactly the bio, one line, nothing else.
    assert 1 <= len(BIO) <= 180, f"bio is {len(BIO)} chars, gate is 1-180"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(BIO)


if __name__ == "__main__":
    main()
