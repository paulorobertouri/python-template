from datetime import date
from os import getenv

from pytest import fixture, mark, raises
from pytest_mock import MockerFixture

from app.demo_data import DemoData

__MODULE__ = "app.demo_data"


@fixture
def today():
    return date(2022, 1, 1)


@fixture
def demo_data():
    return DemoData(
        id=1,
        name="John Doe",
    )


@fixture
def tomorrow():
    return date(2022, 1, 2)


@mark.component
def test_is_birth_date_today(
    mocker: MockerFixture,
    demo_data: DemoData,
    today: date,
):
    # Set the mock datetime to today's date
    mock_date = mocker.patch(f"{__MODULE__}.date")
    mock_date.today.return_value = today

    # Create a DemoData instance with birth date as today's date
    demo_data.birth_date = today

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is True

    mock_date.today.assert_called_once()


@mark.component
def test_is_birth_date_not_today(
    mocker: MockerFixture,
    demo_data: DemoData,
    today: date,
    tomorrow: date,
):
    # Set the mock datetime to today's date
    mock_date = mocker.patch(f"{__MODULE__}.date")
    mock_date.today.return_value = today

    # Create a DemoData instance with birth date as a future date
    demo_data.birth_date = tomorrow

    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is False

    mock_date.today.assert_called_once()


@mark.component
def test_is_birth_date_force_exception(
    mocker: MockerFixture,
):
    # Set the mock datetime to throw an exception
    mock_date = mocker.patch(f"{__MODULE__}.date")
    mock_date.today.side_effect = Exception("An error occurred")

    # Create a DemoData instance with birth date as today's date
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date(2022, 1, 1),
    )

    # Ensure the exception is raised
    with raises(Exception):
        demo_data.is_birth_date_today()


@mark.component
def test_is_birth_date_none(
    demo_data: DemoData,
):
    # Call the method under test
    result = demo_data.is_birth_date_today()

    # Assert the expected result
    assert result is False


@mark.skip(reason="Skipping this test")
def test_skip():
    a = 1
    b = 2
    assert a + b == 3


@mark.skipif(
    getenv("TEST") is None,
    reason="Skipping this test because the TEST environment variable is set",
)
def test_skip_if():
    a = 1
    b = 2
    assert a + b == 3


if __name__ == "__main__":
    from pytest import main

    main([__file__])
