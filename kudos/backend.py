import re


class DuplicateEmailError(Exception):
    pass


class InvalidEmailFormatError(Exception):
    pass


class UserBackend(object):

    def __init__(self):
        self._user_list = []

    def create_user(self, email):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEmailFormatError

        if email in self._user_list:
            raise DuplicateEmailError

        self._user_list.append(email)
