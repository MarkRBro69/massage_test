from core.constants.regular_expressions import USERNAME_REGEX_COMPILED
from core.utils.strings import string_pattern_validator


class UsernameValidator:
    def __call__(self, username: str) -> None:
        string_pattern_validator(value=username, patterns=(USERNAME_REGEX_COMPILED,))

    def deconstruct(self):
        return (
            self.__class__.__module__ + '.' + self.__class__.__name__,
            [],
            {},
        )
