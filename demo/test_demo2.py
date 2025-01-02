import pytest

@pytest.mark.xfail
# @pytest.mark.skip
@pytest.mark.smoke
def test_first_program():
    print("hi")
    assert 'hi' == 'hello'

@pytest.mark.skipif(1==1, reason="not true")
def test_third_program():
    print("hi")
    assert 'hi' == 'hello'
