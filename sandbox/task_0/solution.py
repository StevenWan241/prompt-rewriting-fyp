def has_close_elements(numbers: list[float], threshold: float) -> bool:
    """Return True if any two numbers are closer to each other than threshold."""
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if (abs(numbers[i] - numbers[j]) < threshold):
                return True
    return False
    