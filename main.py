#!/usr/bin/env python3
"""Write the chosen two-line morning-light poem for make.fun."""

import os
import sys
from pathlib import Path

TEXT = "The cat has not moved since six.\nThe square of light has, and takes her with it."

assert 1 <= len(TEXT) <= 280
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
