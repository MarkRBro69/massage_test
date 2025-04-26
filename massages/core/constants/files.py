from enum import Enum


class FileTypes(Enum):
    DOCUMENT = 'document'
    IMAGE = 'image'


# Max size in KB
FILE_MAX_SIZES = {
    FileTypes.DOCUMENT: 100,
}

# Allowed extensions for each file type
FILE_EXTENSIONS = {
    FileTypes.DOCUMENT: {'txt'},
    FileTypes.IMAGE: {'jpg', 'png', 'gif'},
}
