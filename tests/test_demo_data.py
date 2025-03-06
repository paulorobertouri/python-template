import unittest
from datetime import date, timedelta
from os import getenv

from app.demo_data import DemoData


def test_is_birth_date_today():
    # Create a DemoData instance with birth date as today's date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date.today(),
    )

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is True


def test_is_birth_date_not_today():
    # Create a DemoData instance with birth date as a future date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date.today() + timedelta(days=1),
    )

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is False


def test_is_birth_date_none():
    # Create a DemoData instance with birth date as None
    demo_data = DemoData(
        id=1,
        name="John Doe",
    )

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is False


@unittest.skip("Skipping this test")
def test_skip():
    a = 1
    b = 2
    assert a + b == 3


@unittest.skipIf(
    getenv("TEST") is None,
    "Skipping test because TEST is not set",
)
def test_skip_if():
    a = 1
    b = 2
    assert a + b == 3


if __name__ == "__main__":
    from unittest import main

    main()
