from core.constants.files import FILE_EXTENSIONS, FileTypes


def get_file_extension(file) -> str:
    return file.name.split('.')[-1].lower()


def get_file_type(file) -> FileTypes | None:
    file_extension = get_file_extension(file=file)
    for file_type, file_extensions in FILE_EXTENSIONS.items():
        if file_extension in file_extensions:
            return file_type
