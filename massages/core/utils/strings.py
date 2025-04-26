import re
from typing import Sequence
from lxml import etree

from rest_framework.exceptions import ValidationError

from core.constants.regular_expressions import TAG_REGEX, ALLOWED_TAGS, ALLOWED_ATTRIBUTES, ATTR_REGEX


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


def validate_html_content(text: str) -> None:
    """
    Validates that the HTML text contains only allowed tags and attributes,
    and that it follows valid XHTML structure (all tags are properly closed).

    This function checks if:
    - The HTML contains only tags from the allowed set.
    - The attributes of each tag are within the allowed attributes for that tag.
    - The HTML is a valid XHTML with properly closed tags.

    Args:
        text (str): The HTML content to validate.

    Raises:
        ValidationError: If any of the conditions are violated, a ValidationError
                         is raised with a message indicating the issue.
    """
    for match in TAG_REGEX.finditer(text):
        tag = match.group(1)
        attrs_string = match.group(2)

        if tag not in ALLOWED_TAGS:
            raise ValidationError(f"Tag <{tag}> is not allowed.")

        if not match.group(0).startswith('</'):
            attrs = ATTR_REGEX.findall(attrs_string)
            if tag in ALLOWED_ATTRIBUTES:
                for attr in attrs:
                    if attr not in ALLOWED_ATTRIBUTES[tag]:
                        raise ValidationError(f"Attribute '{attr}' is not allowed in <{tag}> tag.")
            elif attrs:
                raise ValidationError(f"Tag <{tag}> should not have attributes.")


def validate_html_structure(text: str) -> None:
    """
    Validate the structure of an HTML snippet by parsing it as XHTML.

    This function attempts to parse the provided HTML `text` by wrapping it
    with a root element `<root>` and then using an XML parser to check its
    validity. If the HTML structure is invalid, an exception is raised with
    details of the syntax error.

    Args:
        text (str): The HTML text to validate.

    Raises:
        ValidationError: If the HTML structure is invalid, an exception is raised
                         with the specific error message.
    """
    parser = etree.XMLParser(recover=False)
    try:
        etree.fromstring(f"<root>{text}</root>", parser=parser)
    except etree.XMLSyntaxError as e:
        raise ValidationError(f"Invalid XHTML structure: {e}")
