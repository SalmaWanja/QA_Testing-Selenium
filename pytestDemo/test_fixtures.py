import pytest


@pytest.mark.usefixtures("setup")
class TestFeatureOptimize:

    def test_setup1(self):
        print("This will be executed after the first fixture")

    def test_setup2(self):
        print("This will be executed after the first fixture")

    def test_setup3(self):
        print("This will be executed after the first fixture")

    def test_setup4(self):
        print("This will be executed after the first fixture")
