from datetime import date, timedelta
from unittest import TestCase
from unittest.mock import MagicMock, patch

from app.demo_data import DemoData

__MODULE__ = "app.demo_data"


class TestDemoData(TestCase):
    def setUp(self):
        self.demo_data = DemoData(
            id=1,
            name="John Doe",
        )

    def test_is_birth_date_today(self):
        # Set the birth date as today's date
        self.demo_data.birth_date = date.today()

        # Call the method under test
        result = self.demo_data.is_birth_date_today()

        # Assert the expected result
        assert result is True

    def test_is_birth_date_not_today(self):
        # Set the birth date as a future
        self.demo_data.birth_date = date.today() + timedelta(days=1)

        # Call the method under test
        result = self.demo_data.is_birth_date_today()

        # Assert the expected result
        assert result is False

    @patch(f"{__MODULE__}.date")
    def test_is_birth_date_force_exception(self, mock_date):
        # Set the mock datetime to throw an exception
        mock_date.today = MagicMock(
            side_effect=Exception("An error occurred"),
        )

        # Create a DemoData instance with birth date as today's date
        demo_data = DemoData(
            id=1,
            name="John Doe",
            birth_date=date(2022, 1, 1),
        )

        # Ensure the exception is raised
        with self.assertRaises(Exception):
            demo_data.is_birth_date_today()

    def test_is_birth_date_none(self):
        # Call the method under test
        result = self.demo_data.is_birth_date_today()

        # Assert the expected result
        assert result is False


if __name__ == "__main__":
    from unittest import main

    main()
