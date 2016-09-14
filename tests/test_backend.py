import pytest
from kudos.backend import (
    DuplicateEmailError,
    InvalidEmailError,
    UserBackend,
)


def test_create_user_adds_multiple_elements():
    sut = UserBackend()
    sut.create_user("john@gmail.com")
    assert len(sut._user_list) == 1
    sut.create_user("andrew@gmail.com")
    assert len(sut._user_list) == 2


def test_create_different_user():
    sut = UserBackend()
    email = "john@gmail.com"
    sut.create_user(email)
    sut._user_list[0] == email

    email_2 = "andrew@gmail.com"
    sut.create_user(email_2)

    assert sut._user_list[0] != sut._user_list[1]


def test_it_does_not_allow_duplicate_emails():
    sut = UserBackend()
    email = "john@gmail.com"
    sut.create_user(email)
    with pytest.raises(DuplicateEmailError):
        sut.create_user(email)


def test_invalid_email_format():
    sut = UserBackend()
    email = "invalidEmail@email_address"
    with pytest.raises(InvalidEmailError):
        sut.create_user(email)
