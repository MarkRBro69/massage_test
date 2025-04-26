import re

USERNAME_REGEX = r"^[a-zA-Z0-9]+$"
USERNAME_REGEX_COMPILED = re.compile(USERNAME_REGEX)

ALLOWED_TAGS = {'a', 'code', 'i', 'strong'}
ALLOWED_ATTRIBUTES = {
    'a': {'href', 'title'},
}

TAG_REGEX = re.compile(r'</?(\w+)(.*?)>', re.DOTALL)

ATTR_REGEX = re.compile(r'(\w+)=[\'"].*?[\'"]')
