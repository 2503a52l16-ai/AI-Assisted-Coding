# Normalize Function

## Problem
In digital media streaming, analysts normalize metrics to [0,1] for fair comparison.

## Logic
1. If list is empty → return []  
2. If all values equal → return all 0.0  
3. Else → `(x - min) / (max - min)` for each score  

## Usage
```python
from normalize_solution import normalize

print(normalize([10, 20, 30]))  # [0.0, 0.5, 1.0]
print(normalize([5, 5, 5]))     # [0.0, 0.0, 0.0]
