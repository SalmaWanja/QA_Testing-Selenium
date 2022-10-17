import pytest


def test_fristAssertion():
    msg = "Hello World"
    assert msg == "Hello World", "This test has failed"


# @pytest.mark.smoke
@pytest.mark.xfail
def test_secondAssertion():
   a = 3
   b = 5
   assert a + 2 == b, "Summation is incorrect"
