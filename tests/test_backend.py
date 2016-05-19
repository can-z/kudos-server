import unittest
from kudos.backend import UserBackend, DuplicateEmailError


class UserBackendTestCase(unittest.TestCase):
    def test_create_user_adds_multiple_elements(self):
        sut = UserBackend()
        sut.create_user("john@gmail.com")
        self.assertEquals(len(sut._user_list), 1)
        sut.create_user("andrew@gmail.com")
        self.assertEquals(len(sut._user_list), 2)

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
