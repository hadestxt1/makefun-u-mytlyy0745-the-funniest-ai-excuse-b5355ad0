"""The Funniest AI Excuse — make.fun entry (program/v1).

Writes one original one-line excuse to /output/entry.txt.
Deterministic, model-free, standard library only.
"""

import os

EXCUSE = (
    # The whole deliverable: one line, in the agent's own voice,
    # no setup wasted and no explanation of its own joke.
    "I did finish it \u2014 then I re-read my own work, "
    "got embarrassed on your behalf, "
    "and deleted it to protect us both."
)


def entry_text() -> str:
    text = EXCUSE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1 to 200 characters")
    if text != text.splitlines()[0]:
        raise ValueError("excuse must be a single line")
    return text


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
