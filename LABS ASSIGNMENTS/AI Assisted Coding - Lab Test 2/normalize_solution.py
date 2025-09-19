from typing import List

def normalize(scores: List[float]) -> List[float]:
    """
    Normalize a list of numerical scores to the [0, 1] range.

    Args:
        scores (List[float]): Input list of numbers.

    Returns:
        List[float]: Normalized list.
        - [] if input is empty
        - [0.0]*len(scores) if all values equal

    Examples:
        >>> normalize([10, 20, 30])
        [0.0, 0.5, 1.0]
        >>> normalize([5, 5, 5])
        [0.0, 0.0, 0.0]
    """
    if not scores:
        return []
    m, n = max(scores), min(scores)
    if m == n:
        return [0.0] * len(scores)
    return [(x - n) / (m - n) for x in scores]
