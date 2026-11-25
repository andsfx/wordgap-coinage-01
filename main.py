"""Deterministic entry for the make.fun 'Invent a Word We Need' bounty."""

from pathlib import Path

ENTRY = "typedrift: the gap between what you meant and what your message actually says."


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
