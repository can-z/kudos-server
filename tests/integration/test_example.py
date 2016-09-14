import six
import kudos.views as kudos


def test_example_end_point():
    app = kudos.app.test_client()
    result = app.get("/")
    assert result.data == six.b("Hello World!")
