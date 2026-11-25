"""Entry for make.fun bounty "The Word You'd Delete From the Dictionary".

Entry text (6 characters, limit: at most 77 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = 'Moist.'

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
