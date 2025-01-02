import pytest


@pytest.mark.regression
def test_first_program():
    print("hello")
    assert 2 == 2

@pytest.mark.smoke
def test_first_code():
    print("hello2")
    assert 2 == 2


def test_sec_program(setup):
    print("hellogourav")
    assert 2+2 == 4

