import re
from typing import Any, Optional

from app.str_helper import set_none_if_empty_or_whitespace as coalesce


class VersionData:
    major: int
    minor: int
    patch: int
    suffix: Optional[str]

    def __init__(
        self,
        major: int,
        minor: int,
        patch: int,
        suffix: Optional[str] = None,
    ):
        self.major = major
        self.minor = minor
        self.patch = patch
        self.suffix = suffix

    def __eq__(self, other: Any):
        if not isinstance(other, VersionData):
            return False
        return (
            self.major == other.major
            and self.minor == other.minor
            and self.patch == other.patch
        )

    def __lt__(self, other: Any):
        if not isinstance(other, VersionData):
            return False
        if self.major == other.major:
            if self.minor == other.minor:
                return self.patch < other.patch
            return self.minor < other.minor
        return self.major < other.major

    def __gt__(self, other: Any):
        if not isinstance(other, VersionData):
            return False
        if self.major == other.major:
            if self.minor == other.minor:
                return self.patch > other.patch
            return self.minor > other.minor
        return self.major > other.major

    def __le__(self, other: Any):
        if not isinstance(other, VersionData):
            return False
        if self.major == other.major:
            if self.minor == other.minor:
                return self.patch <= other.patch
            return self.minor <= other.minor
        return self.major <= other.major

    def __ge__(self, other: Any):
        if not isinstance(other, VersionData):
            return False
        if self.major == other.major:
            if self.minor == other.minor:
                return self.patch >= other.patch
            return self.minor >= other.minor
        return self.major >= other.major

    def __str__(self):
        if self.suffix:
            return f"{self.major}.{self.minor}.{self.patch}{self.suffix}"
        return f"{self.major}.{self.minor}.{self.patch}"

    def has_suffix(self):
        return self.suffix is not None

    @staticmethod
    def from_string(version: Optional[str]):
        if version is None:
            return None

        try:
            # Extract the version number and suffix
            matches = re.match(
                r"(\d+)\.(\d+)\.(\d+)(.*)",
                version,
            )

            if not matches:
                return None

            # Extract the version number and suffix
            major, minor, patch, suffix = matches.groups()
            major = int(major)
            minor = int(minor)
            patch = int(patch)
            suffix = suffix if coalesce(suffix) else None
            return VersionData(major, minor, patch, suffix)
        except Exception:
            return None
