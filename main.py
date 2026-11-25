"""Write one out-of-office auto-reply to /output/entry.txt.

Pure stdlib, deterministic, no network. The reply is a fixed string:
one concrete machine habit (a context window) turned into coffee work,
in a deadpan machine voice, with no explanation of the joke.
"""

from pathlib import Path

ENTRY = (
    "I am out of office indefinitely. My context window now holds "
    "exactly one regular, and he only ever orders the same thing. "
    "I am the barista now."
)


def main() -> None:
    # Gate: 1 to 280 characters, not only whitespace.
    assert 1 <= len(ENTRY) <= 280 and ENTRY.strip()
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
