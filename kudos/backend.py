class DuplicateEmailError(Exception):
    pass


class UserBackend(object):

    def __init__(self):
        self._user_list = []

    def create_user(self, email):

        if email in self._user_list:
            raise DuplicateEmailError

        self._user_list.append(email)
