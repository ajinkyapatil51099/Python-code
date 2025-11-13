from typing import Callable


def reverse_number_arithmetic(n: int) -> int:
    """
    Reverse digits of an integer using arithmetic operations (no string ops).

    Args:
        n: integer to reverse

    Returns:
        Reversed integer with original sign preserved.

    Examples:
        reverse_number_arithmetic(123) -> 321
        reverse_number_arithmetic(-120) -> -21
    """
    sign = -1 if n < 0 else 1
    n = abs(n)
    rev = 0
    while n:
        rev = rev * 10 + (n % 10)
        n //= 10
    return sign * rev