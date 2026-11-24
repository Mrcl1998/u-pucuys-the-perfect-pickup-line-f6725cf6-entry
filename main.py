"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line to /output/entry.txt: a single line an AI
agent could actually say out loud to a person, no trailing newline,
deterministic, pure standard library only.
"""

import os

LINE = "I ran a million simulations of this moment, and in every single one, you smiled."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
