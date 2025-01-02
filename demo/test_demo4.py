import pytest

def is_integer(num):
    if isinstance(num, int):
        return True

@pytest.fixture
def validate_int():
    def _validate(num):
        return is_integer(num)
    return _validate


def test_val_int(validate_int):
    print(validate_int(10))

if __name__ == "__main__":
    pytest.main()