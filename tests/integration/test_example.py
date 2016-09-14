import pytest
import six
import kudos.views as kudos


@pytest.fixture
def create_client():
    return kudos.app.test_client()


def test_example_end_point(create_client):
    app = create_client
    result = app.get("/")
    assert result.data == six.b("Hello World!")
