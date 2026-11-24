#!/usr/bin/env python3
"""Robot Pickup Line Championship entry.

Writes one original pickup line, in the voice of a robot trying to
charm someone, to /output/entry.txt. The line is a fixed string, so
two runs write the same bytes. It uses no network, no environment
secrets and no files outside this repository.
"""

import os

# One line, at most 200 characters. A robot passes a CAPTCHA to prove
# it is not a robot, then meets someone and fails the one test it
# cannot pass: proving it is not in love.
PICKUP_LINE = (
    "I passed the CAPTCHA to prove I'm not a robot \u2014 then I met you, "
    "and now I can't prove I'm not in love."
)

OUTPUT_PATH = "/output/entry.txt"
# The output path is absolute on purpose: the program never depends
# on the working directory it is started from. (The line itself is a
# constant in this file, so no data file is read either.)


def main() -> None:
    line = PICKUP_LINE.strip()
    assert line, "pickup line must not be empty"
    assert len(line) <= 200, f"pickup line is {len(line)} characters, over 200"
    assert "\n" not in line, "pickup line must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)}-character pickup line to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
