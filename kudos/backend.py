import re


class DuplicateEmailError(Exception):
    pass


class InvalidEmailError(Exception):
    pass


class UserBackend(object):

    def __init__(self):
        self._user_list = []

    def create_user(self, email):

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise InvalidEmailError

        if email in self._user_list:
            raise DuplicateEmailError

        self._user_list.append(email)
