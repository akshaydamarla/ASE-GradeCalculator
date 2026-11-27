import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from calculator import calculate_average, calculate_grade  # noqa: E402


def test_calculate_average():
    assert calculate_average([80, 90, 100]) == 90


def test_calculate_grade_a():
    assert calculate_grade(95) == "A"


def test_calculate_grade_f():
    assert calculate_grade(45) == "F"


def test_empty_marks_raise_error():
    with pytest.raises(ValueError):
        calculate_average([])


def test_out_of_range_mark_raises_error():
    with pytest.raises(ValueError):
        calculate_average([75, 110])
