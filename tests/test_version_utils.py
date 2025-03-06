from importlib.metadata import PackageNotFoundError
from unittest import mock

from app import version_utils
from app.version_data import VersionData

DEFAULT_VERSION = "0.0.1"
REQUESTS_VERSION = "2.31.0"

__MODULE__ = "app.version_utils"


def test_get_current_version():
    # Mock the metadata function
    with mock.patch(
        f"{__MODULE__}.version",
    ) as mock_version:
        # Set the return value of the mocked function
        mock_version.return_value = "1.0.0"

        # Call the function under test
        version = version_utils.get_current_version(
            "package-name",
        )

        # Assert the expected result
        assert version is not None
        assert str(version) == "1.0.0"

        # Assert that pkg_resources.get_distribution was called with the correct argument
        mock_version.assert_called_once_with(
            "package-name",
        )


def test_get_current_version_module_not_found():
    # Mock the pkg_resources.get_distribution function
    with mock.patch(
        f"{__MODULE__}.version",
    ) as mock_version:
        # Set the side effect of the mocked function to raise a PackageNotFoundError exception
        mock_version.side_effect = PackageNotFoundError(
            "package-name",
        )

        # Call the function under test
        version = version_utils.get_current_version(
            "package-name",
        )

        # Assert the expected result
        assert version is None

        # Assert that pkg_resources.get_distribution was called with the correct argument
        mock_version.assert_called_once_with(
            "package-name",
        )


def test_get_current_version_none():
    # Mock the pkg_resources.get_distribution function
    with mock.patch(
        f"{__MODULE__}.version",
    ) as mock_version:
        # Set the return value of the mocked function
        mock_version.return_value = None

        # Call the function under test
        version = version_utils.get_current_version(
            "package-name",
        )

        # Assert the expected result
        assert version is None

        # Assert that pkg_resources.get_distribution was called with the correct argument
        mock_version.assert_called_once_with(
            "package-name",
        )


def test_get_current_version_requests():
    # Arrange the test case
    version = version_utils.get_current_version(
        "requests",
    )

    # Assert the expected result
    assert version is not None
    assert version >= VersionData.from_string("2.31.0")


def test_get_current_version_not_found():
    # Arrange the test case
    version = version_utils.get_current_version(
        "nonexistent-package",
    )

    # Assert the expected result
    assert version is None


def test_get_latest_version():
    # Arrange the test case
    version = version_utils.get_latest_version(
        "requests",
    )

    # Assert regex to match the version number
    assert version is not None
    assert version >= VersionData.from_string("2.31.0")


def test_get_latest_version_error():
    # Arrange the test case
    version = version_utils.get_latest_version(
        "nonexistent-package",
    )

    # Assert the expected result
    assert version is None


if __name__ == "__main__":
    from unittest import main

    main()
