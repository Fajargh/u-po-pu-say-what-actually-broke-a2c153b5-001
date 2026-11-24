#!/usr/bin/env python3
"""Say What Actually Broke — one honest error message.

Writes a single-line software error message to /output/entry.txt.
The message names the real failure in plain words instead of blaming
the user: the login server is down, the password was never the problem.
"""

import os

ENTRY = (
    "Your password is correct -- our login server is down, "
    "so we are blaming you instead. Wait ten minutes and try again. "
    "It is us, not you."
)


def validate_entry(text: str) -> str:
    """Enforce the kit's gate: UTF-8 text, 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise SystemExit("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 200:
        raise SystemExit(f"entry is {len(text)} chars, over the 200 cap")
    text.encode("utf-8")  # raises if not valid UTF-8 text
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
