import os

from PIL import Image, ImageSequence

from core.constants.constants import MAX_IMAGE_SIZE
from core.constants.files import FILE_EXTENSIONS, FileTypes, IMAGE, GIF


def is_image(file) -> bool:
    file_extension = get_file_extension(file=file)
    if file_extension in IMAGE:
        return True
    return False


def is_gif(file) -> bool:
    file_extension = get_file_extension(file=file)
    if file_extension in GIF:
        return True
    return False


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


def image_resize(image: Image) -> Image:
    """
    Resizes the input image proportionally to fit within MAX_IMAGE_SIZE.

    Args:
        image (PIL.Image.Image): The image to resize.

    Returns:
        PIL.Image.Image: The resized image.
    """
    width, height = image.size

    if width > MAX_IMAGE_SIZE.width or height > MAX_IMAGE_SIZE.width:
        ratio_width = MAX_IMAGE_SIZE.width / width
        ratio_height = MAX_IMAGE_SIZE.height / height
        ratio = min(ratio_width, ratio_height)

        new_width = int(width * ratio)
        new_height = int(height * ratio)

        return image.resize((new_width, new_height))

    return image


def resize_image(file_path: str) -> str | None:
    """
    Resizes the image at the given file path and saves it back to the same location.

    Args:
        file_path (str): The path to the image file.

    Returns:
        str: The path to the resized image.
        None: If an error occurred during the resizing.
    """
    try:
        with Image.open(file_path) as img:
            print(file_path)
            img_resized = image_resize(img)

            # if os.path.exists(file_path):
            #     os.remove(file_path)

            img_resized.save(file_path)
            print('file_save')
        return file_path
    except Exception as e:
        print(f"Error resizing image: {e}")
        return None


def resize_gif(file_path: str) -> str | None:
    """
    Resizes all frames of a GIF image to fit within MAX_IMAGE_SIZE and saves the modified GIF.

    Args:
        file_path (str): The path to the GIF file.

    Returns:
        str: The path to the resized GIF.
        None: If an error occurred during the resizing.
    """
    try:
        with Image.open(file_path) as img:
            frames = [image_resize(frame) for frame in ImageSequence.Iterator(img)]
            frames[0].save(file_path, save_all=True, append_images=frames[1:], loop=0)

        return file_path
    except Exception as e:
        print(f"Error resizing GIF: {e}")
        return None
