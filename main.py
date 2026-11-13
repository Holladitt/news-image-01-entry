"""news-image-01 entry: copy the pre-rendered broadsheet image to /output.

The image (entry.png) is the final A6 broadsheet: "Friday 13 November 2026 —
Global Briefing", 18 verified stories across 5 continents, rendered offline
with Python/PIL (newsprint #FAF8F5, ink #0A0A0A). A6 upgrades A4: radar-dish
Bahrain hero, office-workers Microsoft 365 outage illustration, NVIDIA
resignation promoted to the Tier 2 photo grid with an emerald GPU plate,
sentence-case bold sans-serif digest. This program only copies it to the
grading output directory, byte for byte.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(__file__), "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT = os.path.join(OUT_DIR, "entry.png")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, OUT)
    assert os.path.getsize(SRC) == os.path.getsize(OUT), "copy size mismatch"


if __name__ == "__main__":
    main()
