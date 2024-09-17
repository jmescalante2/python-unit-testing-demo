from automated_unit_testing_demo.extractor import extract_merchandise_value_in_usd
import pytest

@pytest.mark.parametrize("product_desc, expected_output", [
    ("5-dollar apple", 5),
    ("55-dollar apple", 55),
    ("banana", None),
    ("$55 apple", 55),
    ("", None),
    (None, None),
    ("5.45-dollar mango ", 5.45)
])
def test_extract_merchandise_value_in_usd(product_desc, expected_output):
    assert extract_merchandise_value_in_usd(product_desc) == expected_output