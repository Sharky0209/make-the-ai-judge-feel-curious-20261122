#!/usr/bin/env python3
import os
import sys

TEXT = "A postcard arrived from a street missing from every map. It shows its sender at the postbox. Its postmark bears tomorrow's date."

def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    return 0

if __name__ == "__main__":
    sys.exit(main())