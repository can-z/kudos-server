import unittest
from kudos.backend import UserBackend, DuplicateEmailError
from kudos.backend import InvalidEmailFormatError


class UserBackendTestCase(unittest.TestCase):
    def test_create_user_adds_multiple_elements(self):
        sut = UserBackend()
        sut.create_user("john@gmail.com")
        self.assertEquals(len(sut._user_list), 1)
        sut.create_user("andrew@gmail.com")
        self.assertEquals(len(sut._user_list), 2)
        sut.create_user("can@gmail.com")
        self.assertEquals(len(sut._user_list), 3)

    def test_create_different_user(self):
        sut = UserBackend()
        email = "john@gmail.com"
        sut.create_user(email)
        self.assertEquals(sut._user_list[0], email)

        email_2 = "andrew@gmail.com"
        sut.create_user(email_2)

        self.assertTrue(sut._user_list[0] != sut._user_list[1])

    def test_it_does_not_allow_duplicate_emails(self):
        sut = UserBackend()
        email = "john@gmail.com"
        sut.create_user(email)
        with self.assertRaises(DuplicateEmailError):
            sut.create_user(email)

    def test_invalid_email_format(self):
        sut = UserBackend()
        email = "invalidEmail@email_address"
        with self.assertRaises(InvalidEmailFormatError):
            sut.create_user(email)
