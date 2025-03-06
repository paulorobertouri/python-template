from unittest.mock import patch

from app.version_data import VersionData

DEFAULT_VERSION = "0.0.1"


def test_version_from_string():
    # Arrange the test case
    version = VersionData.from_string("1.0.0")

    # Assert the expected result
    assert version is not None
    assert str(version) == "1.0.0"


def test_version_from_string_invalid():
    # Arrange the test case
    version = VersionData.from_string("invalid")

    # Assert the expected result
    assert version is None


def test_version_from_string_empty():
    # Arrange the test case
    version = VersionData.from_string("")

    # Assert the expected result
    assert version is None


def test_version_from_string_none():
    # Arrange the test case
    version = VersionData.from_string(None)

    # Assert the expected result
    assert version is None


def test_version_from_string_exception():
    # Mock re.match to raise an exception
    with patch(
        "re.match",
        side_effect=Exception(),
    ):
        # Arrange the test case
        version = VersionData.from_string("1.0.0")

        # Assert the expected result
        assert version is None


def test_version_has_no_suffix():
    # Arrange the test case
    version = VersionData.from_string("1.0.0")

    # Assert the expected result
    assert version is not None
    assert version.has_suffix() is False
    assert str(version) == "1.0.0"


def test_version_has_suffix():
    # Arrange the test case
    version = VersionData.from_string("1.0.0-beta")

    # Assert the expected result
    assert version is not None
    assert version.has_suffix() is True
    assert str(version) == "1.0.0-beta"


def test_equal():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.0")

    # Assert the expected result
    assert version1 == version2


def test_not_equal():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.1")

    # Assert the expected result
    assert version1 != version2


def test_greater_than():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.1")

    # Assert the expected result
    assert version1 is not None
    assert version2 is not None
    assert version2 > version1


def test_less_than():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.1")

    # Assert the expected result
    assert version1 is not None
    assert version2 is not None
    assert version1 < version2


def test_greater_than_or_equal():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.0")

    # Assert the expected result
    assert version1 is not None
    assert version2 is not None
    assert version1 >= version2


def test_less_than_or_equal():
    # Arrange the test case
    version1 = VersionData.from_string("1.0.0")
    version2 = VersionData.from_string("1.0.0")

    # Assert the expected result
    assert version1 is not None
    assert version2 is not None
    assert version1 <= version2


def test_version_data_default():
    # Arrange the test case
    version = VersionData(0, 0, 1)

    # Assert the expected result
    assert str(version) == DEFAULT_VERSION


def test_version_data_sort():
    # Arrange the test case
    version1 = VersionData(1, 0, 2)
    version2 = VersionData(1, 0, 1)
    version3 = VersionData(1, 0, 0)
    version4 = VersionData(2, 1, 0)
    version5 = VersionData(0, 0, 7)
    version6 = VersionData(1, 1, 0)
    version7 = VersionData(1, 2, 1)
    version8 = VersionData(1, 2, 2)
    versions = [
        version1,
        version2,
        version3,
        version4,
        version5,
        version6,
        version7,
        version8,
    ]

    # Assert the expected result
    versions.sort(reverse=True)
    versions_str = [str(version) for version in versions]
    assert versions_str == [
        "2.1.0",
        "1.2.2",
        "1.2.1",
        "1.1.0",
        "1.0.2",
        "1.0.1",
        "1.0.0",
        "0.0.7",
    ]
    assert str(versions[0]) == "2.1.0"
    assert str(versions[-1]) == "0.0.7"


def test_version_data__eq__():
    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 == version2


def test_version_data__lt__():
    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 0, 1)

    # Assert the expected result
    assert version1 < version2

    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 1, 0)

    # Assert the expected result
    assert version1 < version2

    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(2, 0, 0)

    # Assert the expected result
    assert version1 < version2


def test_version_data__gt__():
    # Arrange the test case
    version1 = VersionData(1, 0, 1)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 > version2

    # Arrange the test case
    version1 = VersionData(1, 1, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 > version2

    # Arrange the test case
    version1 = VersionData(2, 0, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 > version2


def test_version_data__le__():
    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 <= version2

    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 0, 1)

    # Assert the expected result
    assert version1 <= version2

    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 1, 0)

    # Assert the expected result
    assert version1 <= version2

    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(2, 0, 0)

    # Assert the expected result
    assert version1 <= version2


def test_version_data__ge__():
    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 >= version2

    # Arrange the test case
    version1 = VersionData(1, 0, 1)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 >= version2

    # Arrange the test case
    version1 = VersionData(1, 1, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 >= version2

    # Arrange the test case
    version1 = VersionData(2, 0, 0)
    version2 = VersionData(1, 0, 0)

    # Assert the expected result
    assert version1 >= version2


def test_version_data__operator_invalid():
    # Arrange the test case
    version1 = VersionData(1, 0, 0)
    version2 = "invalid"

    # Assert the expected result
    assert not (version1 == version2)
    assert not (version1 < version2)
    assert not (version1 > version2)
    assert not (version1 <= version2)
    assert not (version1 >= version2)
    assert version1 != version2


def test_version_data__str__():
    # Arrange the test case
    version = VersionData(1, 0, 0)

    # Assert the expected result
    assert str(version) == "1.0.0"


def test_version_data__str__with_suffix():
    # Arrange the test case
    version = VersionData(1, 0, 0, "-beta")

    # Assert the expected result
    assert str(version) == "1.0.0-beta"


def test_version_data_has_suffix():
    # Arrange the test case
    version = VersionData(1, 0, 0, "-beta")

    # Assert the expected result
    assert version.has_suffix() is True


def test_version_data_has_no_suffix():
    # Arrange the test case
    version = VersionData(1, 0, 0)

    # Assert the expected result
    assert version.has_suffix() is False


if __name__ == "__main__":
    from unittest import main

    main()
