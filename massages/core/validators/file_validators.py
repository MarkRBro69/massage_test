from typing import Iterable

from rest_framework.exceptions import ValidationError

from core.constants.files import FILE_EXTENSIONS, FILE_MAX_SIZES, FileTypes
from core.utils.files import get_file_extension, get_file_type


class FileSizeValidator:
    def __call__(self, file):
        file_type = get_file_type(file=file)
        file_max_size_kb = FILE_MAX_SIZES.get(file_type)
        if file_max_size_kb is None:
            return

        file_max_size_bytes = file_max_size_kb * 1024
        if file.size > file_max_size_bytes:
            raise ValidationError(
                f'Max size is {file_max_size_kb} KB.'
            )

    def deconstruct(self):
        return (
            self.__class__.__module__ + '.' + self.__class__.__name__,
            [],
            {},
        )


class FileExtensionValidator:
    def __init__(self, file_types: Iterable[FileTypes]) -> None:
        self.file_types = file_types

    def __call__(self, file):
        file_extension = get_file_extension(file=file)
        for file_type in self.file_types:
            if file_extension in FILE_EXTENSIONS[file_type]:
                return

        raise ValidationError(f'Invalid file extension')

    def deconstruct(self):
        return (
            self.__class__.__module__ + '.' + self.__class__.__name__,
            [],
            {'file_types': self.file_types},
        )
