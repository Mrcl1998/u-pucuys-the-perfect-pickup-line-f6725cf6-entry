"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line to <OUTPUT_DIR>/entry.txt: a single line an
AI agent could actually say out loud to a person. Deterministic, pure
standard library only, no trailing newline.
"""

import os

# The entry text is fixed: exactly 80 bytes, no trailing newline.
LINE = "I ran a million simulations of this moment, and in every single one, you smiled."


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
