from core.constants.files import FILE_EXTENSIONS, FileTypes


def get_file_extension(file) -> str:
    """
    Retrieves the file extension.

    Args:
        file: The file object that should contain a `name` attribute.

    Returns:
        str: The file extension in lowercase (e.g., 'jpg', 'png').

    Example:
        >>> get_file_extension(file)
        'jpg'
    """
    return file.name.split('.')[-1].lower()


def get_file_type(file) -> FileTypes | None:
    """
    Determines the file type based on its extension.

    Args:
        file: The file object that should contain a `name` attribute.

    Returns:
        FileTypes | None: The file type from the `FileTypes` enumeration if the extension is supported,
        or `None` if the extension is not supported.

    Example:
        >>> get_file_type(file)
        FileTypes.IMAGE
    """
    file_extension = get_file_extension(file=file)
    for file_type, file_extensions in FILE_EXTENSIONS.items():
        if file_extension in file_extensions:
            return file_type
