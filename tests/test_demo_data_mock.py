from datetime import date
from unittest.mock import patch

from app.demo_data import DemoData

__MODULE__ = "app.demo_data"


@patch(f"{__MODULE__}.date")
def test_is_birth_date_today(mock_date):
    # Set the mock datetime to today's date
    mock_date.today.return_value = date(2022, 1, 1)

    # Create a DemoData instance with birth date as today's date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date(2022, 1, 1),
    )

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is True

    mock_date.today.assert_called_once()


@patch(f"{__MODULE__}.date")
def test_is_birth_date_not_today(mock_date):
    # Set the mock datetime to today's date
    mock_date.today.return_value = date(2022, 1, 1)

    # Create a DemoData instance with birth date as a future date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date(2022, 1, 2),
    )

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is False

    mock_date.today.assert_called_once()


@patch(f"{__MODULE__}.date")
def test_is_birth_date_force_exception(mock_date):
    # Set the mock datetime to throw an exception
    mock_date.today.side_effect = Exception("An error occurred")

    # Create a DemoData instance with birth date as today's date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date(2022, 1, 1),
    )

    # Ensure the exception is raised
    try:
        demo_data.is_birth_date_today()
    except Exception as e:
        assert str(e) == "An error occurred"
    else:
        assert False, "Expected an exception"


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


if __name__ == "__main__":
    from unittest import main

    main()
