import pytest


# adding scope allows the fixture to run only once when running multiple testcases using that feature
@pytest.fixture(scope="class")
def setup():
    print("this will be the first thing to be executed")
    yield
    print("this will be the last thing to be executed")


@pytest.fixture()
def dataLoad():
    print("This is the data load")
    return ["Salma", "Wanja's Academy", "salmawanja@gmail.com"]


@pytest.fixture(params=[("Chrome", "Firefox", "IE"), ("Firefox", "IE"), ("IE", "ss")])
def crossBrowser(request):
    return request.param
