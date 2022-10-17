import pytest


# @pytest.mark.smoke
# @pytest.mark.skip
def test_fristGreeting(setup):
    print("Salma Wanja Mbogori")


def test_secondGreeting(setup):
    print("Good Morning!")


def test_crossBrowser1(crossBrowser):
    print(crossBrowser[1])
