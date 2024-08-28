import pytest
from hw1 import meep


def test_fail():
    assert (meep(5) == False)


def test_pass():
    assert meep(3) == True