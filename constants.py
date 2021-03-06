import re

USER_NOT_FOUND = "User not found"
USER_DELETED = "User deleted"
SUCCESSFULLY_AUTORIZED = "Successfully authorized"
INVALID_CREDENTIALS = "Invalid Credentials"
PW_DO_NOT_MATCH = "Passwords do not match"
USER_ALREADY_EXISTS = "User already exists"
CREATED_SUCCESSFULLY = "Created Successfully"

HAS_LOWERCASE_LETTERS = re.compile(r'[a-z]')
HAS_UPPERCASE_LETTERS = re.compile(r'[A-Z]')
HAS_NUMBERS = re.compile(r'[0-9]')
HAS_SYMBOLS = re.compile(r'[~`! @#$%^&*()_\-+={[}]|\:;\"\'<,>.?/]')
