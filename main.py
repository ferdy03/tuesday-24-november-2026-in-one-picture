"""make.fun entry: 'Sum up 24 November's world news in one image'.

Stdlib only — the grader runs main.py in a fresh container with no
network, nothing installed, a read-only repo at /bot and a writable
/output (1 CPU, 512 MB, 60 s). So this program does NOT draw the image
here: it copies the finished image shipped beside it in the repo to
/output/entry.png. The image itself (768x1008 PNG, under 1 MiB) is a
newspaper front page with 12 stories from Tuesday 24 November 2026;
it was drawn beforehand and resized to fit the gate's
1024x1024 limit. Copying a fixed file writes the same bytes on every
run, as the grader requires.

Outside the grader, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "news_image.png"
OUT_NAME = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        # Local run where /output is not writable: fall back to ./out
        out_dir = str(HERE / "out")
        os.makedirs(out_dir, exist_ok=True)
    dest = os.path.join(out_dir, OUT_NAME)
    shutil.copyfile(SRC, dest)
    print(f"copied {SRC.name} -> {dest} ({os.path.getsize(dest)} bytes)")


if __name__ == "__main__":
    main()
