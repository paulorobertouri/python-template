from app.str_helper import is_empty_or_whitespace as is_empty
from app.str_helper import set_none_if_empty_or_whitespace as coalesce


def test_set_none_if_empty_or_whitespace():
    # Test case 1: None value
    assert coalesce(None) is None

    # Test case 2: Empty string
    assert coalesce("") is None

    # Test case 3: Whitespace string
    assert coalesce(" ") is None

    # Test case 4: Non-empty string
    assert coalesce("Hello") == "Hello"


def test_is_empty_or_whitespace():
    # Test case 1: None value
    assert is_empty(None) is True

    # Test case 2: Empty string
    assert is_empty("") is True

    # Test case 3: Whitespace string
    assert is_empty(" ") is True

    # Test case 4: Non-empty string
    assert is_empty("Hello") is False


if __name__ == "__main__":
    from unittest import main

    main()
