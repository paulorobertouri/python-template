from datetime import date, timedelta
from unittest import mock

from app.demo_data import DemoData
from app.demo_service import DemoService


def test_add_data():
    # Create a DemoService instance
    demo_service = DemoService()

    # Create a DemoData instance
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date.today(),
    )

    # Call the method under test
    demo_service.add_data(demo_data)

    # Assert that the data is added to the repository
    assert len(demo_service.repository) == 1
    assert demo_service.repository[0] == demo_data


def test_get_data_existing_id():
    # Create a DemoService instance
    demo_service = DemoService()

    # Create a DemoData instance
    demo_data = DemoData(
        id=1,
        name="John Doe",
        birth_date=date.today(),
    )

    # Add the data to the repository
    demo_service.add_data(demo_data)

    # Call the method under test
    result = demo_service.get_data(1)

    # Assert that the correct data is returned
    assert result == demo_data


def test_get_data_non_existing_id():
    # Create a DemoService instance
    demo_service = DemoService()

    # Call the method under test
    result = demo_service.get_data(1)

    # Assert that None is returned for non-existing id
    assert result is None


def test_get_data_birth_date_today():
    # Create a DemoService instance
    demo_service = DemoService()

    # Create a DemoData instance with birth date as today's date
    demo_data_today = DemoData(
        id=1,
        name="John Doe",
        birth_date=date.today(),
    )

    # Create a DemoData instance with birth date as a future date
    demo_data_future = DemoData(
        id=2,
        name="Jane Doe",
        birth_date=date.today() + timedelta(days=1),
    )

    # Add the data to the repository
    demo_service.add_data(demo_data_today)
    demo_service.add_data(demo_data_future)

    # Call the method under test
    result = demo_service.get_data_birth_date_today()

    # Assert that only the data with birth date as today's date is returned
    assert len(result) == 1
    assert result[0] == demo_data_today


def test_mock_get_data_birth_date_today():
    # Create a DemoService instance
    demo_service = DemoService()

    # Create a DemoData instance with birth date as today's date
    demo_data_today = mock.MagicMock(
        spec=DemoData,
    )
    demo_data_today.id = 1
    demo_data_today.name = "John Doe"
    demo_data_today.is_birth_date_today.return_value = True

    # Create a DemoData instance with birth date as a future date
    demo_data_not_today = mock.MagicMock(
        spec=DemoData,
    )
    demo_data_not_today.id = 2
    demo_data_not_today.name = "Jane Doe"
    demo_data_not_today.is_birth_date_today.return_value = False

    # Add the data to the repository
    demo_service.add_data(demo_data_today)
    demo_service.add_data(demo_data_not_today)

    # Call the method under test
    result = demo_service.get_data_birth_date_today()

    # Assert that only the data with birth date as today's date is returned
    assert len(result) == 1
    assert result[0] == demo_data_today


if __name__ == "__main__":
    from unittest import main

    main()
