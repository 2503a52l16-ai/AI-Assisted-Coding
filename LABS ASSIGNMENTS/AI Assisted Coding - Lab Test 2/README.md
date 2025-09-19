# File Version Bumper (`_vNN` Suffix)

## Problem
In digital media streaming pipelines, files must be versioned with a `_vNN` suffix before their extension.  
If already versioned, increment the version. Otherwise, add `_v01`.

## Approach
- Split base name and extension using `os.path.splitext`.
- Use regex (`_v(\d+)$`) to detect existing suffix.
- If found: increment while preserving zero-padding.
- If not: append `_v01`.

## Assumptions
- Minimum 2-digit padding enforced.
- Works with multi-dot filenames (`.tar.gz` etc.) since `os.path.splitext` preserves last extension.
- Always preserves original extension.

## Complexity
- Regex match and string manipulation are **O(n)** where n = filename length.

## Run Tests
```bash
python -m unittest tests.py
