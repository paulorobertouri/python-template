import logging
from importlib.metadata import PackageNotFoundError, version

import requests

from app.version_data import VersionData

__DEFAULT_PIP_URL = "https://pypi.org/pypi/{package_name}/json"


def get_current_version(package_name: str):
    try:
        module = version(
            package_name,
        )
        if module:
            return VersionData.from_string(module)
    except PackageNotFoundError:
        logging.error("Module not found")
    return None


def get_latest_version(package_name: str):
    try:
        versions = list_versions(package_name)
        return versions[0]
    except Exception:
        logging.error("Error getting latest version")
    return None


def list_versions(package_name: str):
    url = __DEFAULT_PIP_URL.format(
        package_name=package_name,
    )
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    # Get all versions from the json response
    versions = list(data["releases"].keys())

    # Filter out non-semantic versions
    versions = [VersionData.from_string(version) for version in versions]

    # Filter out None values
    versions = [version for version in versions if version]

    # Filter out versions with suffixes
    versions = [version for version in versions if not version.has_suffix()]

    # Sort the versions in descending order
    versions.sort(reverse=True)

    return versions
