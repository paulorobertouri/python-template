from typing import Optional


def set_none_if_empty_or_whitespace(
    value: Optional[str],
):
    if value is None:
        return None
    if value.strip() == "":
        return None
    return value


def is_empty_or_whitespace(
    value: Optional[str],
):
    return set_none_if_empty_or_whitespace(value) is None
