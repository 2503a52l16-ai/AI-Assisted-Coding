import re
import os

def bump_version(name: str) -> str:
    """
    Increment or add a version suffix (_vNN) before the file extension.

    Rules:
    - If `_vNN` exists (where NN is an integer), increment by 1.
    - If no suffix, append `_v01` before extension.
    - Preserve the file extension (including multi-dot like .tar.gz).
    - Always keep at least 2-digit padding (e.g., v01, v02).
    """

    # Handle known multi-part extensions first
    compound_exts = [".tar.gz", ".tar.bz2", ".tar.xz"]
    for ext in compound_exts:
        if name.endswith(ext):
            base = name[: -len(ext)]
            extension = ext
            break
    else:
        base, extension = os.path.splitext(name)

    match = re.search(r"_v(\d+)$", base)
    if match:
        num_str = match.group(1)
        num_len = max(len(num_str), 2)  # enforce at least 2 digits
        new_num = int(num_str) + 1
        new_num_str = str(new_num).zfill(num_len)
        new_base = base[:match.start()] + f"_v{new_num_str}"
    else:
        new_base = base + "_v01"

    return new_base + extension
