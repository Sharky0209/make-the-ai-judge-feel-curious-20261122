#!/usr/bin/env python3
import os

TEXT = "An atlas lies open to the sea's edge. In the margin, a small door has been drawn. Wet sand lies beneath it. Who came through?"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(TEXT)

if __name__ == "__main__":
    main()