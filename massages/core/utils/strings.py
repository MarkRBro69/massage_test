import re
from typing import Sequence

from rest_framework.exceptions import ValidationError


def string_pattern_validator(value: str, patterns: Sequence[re.Pattern]) -> str:
    """
    Validates that the string matches at least one
    of the given regular expression patterns.

    Args:
        value: The input string to validate.
        patterns: A sequence of compiled regular expressions to check against.

    Returns:
        The original string if it matches any of the patterns.

    Raises:
        ValidationError: If the string does not match any of the provided patterns.
    """
    if len(patterns) == 0:
        return value

    for pattern in patterns:
        if pattern.fullmatch(value):
            return value

    raise ValidationError(
        'String format is not valid according to the allowed pattern rules.'
    )
