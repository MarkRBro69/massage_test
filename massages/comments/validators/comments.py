from core.utils.strings import validate_html_content, validate_html_structure


class TextValidator:
    def __call__(self, text: str) -> None:
        validate_html_content(text=text)
        validate_html_structure(text=text)

    def deconstruct(self):
        return (
            self.__class__.__module__ + '.' + self.__class__.__name__,
            [],
            {},
        )