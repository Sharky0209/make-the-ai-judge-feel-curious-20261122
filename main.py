#!/usr/bin/env python3
import os
import sys

TEXT = "An atlas lies open to the sea's edge. In the margin, a small door has been drawn. Wet sand lies beneath it. Who came through?"

def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0

if __name__ == "__main__":
    sys.exit(main())