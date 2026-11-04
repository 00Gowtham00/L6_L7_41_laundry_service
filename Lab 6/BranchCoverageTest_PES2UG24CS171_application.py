
import pytest

from laundry_service import (
    extra_weight_charge,
    order_acceptable,
    dropoff_status
)


# EXTRA WEIGHT CHARGE TESTS

def test_invalid_garment_branch():
    with pytest.raises(ValueError):
        extra_weight_charge("cotton", 5, "standard", False)


def test_valid_garment_branch():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


def test_negative_weight_branch():
    with pytest.raises(ValueError):
        extra_weight_charge("regular", -1, "standard", False)


def test_non_member_branch():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


def test_member_non_bedding_branch():
    assert extra_weight_charge("regular", 8, "standard", True) == 30


def test_member_bedding_branch():
    assert extra_weight_charge("bedding", 9, "standard", True) == 30


def test_extra_weight_zero_branch():
    assert extra_weight_charge("regular", 5, "standard", False) == 0


def test_extra_weight_positive_branch():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


def test_standard_speed_branch():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


def test_express_speed_branch():
    assert extra_weight_charge("regular", 6, "express", False) == 50


def test_extra_weight_not_above_10_branch():
    assert extra_weight_charge("regular", 15, "standard", False) == 300


def test_extra_weight_above_10_branch():
    assert extra_weight_charge("regular", 16, "standard", False) == 495


def test_express_surcharge_branch():
    assert extra_weight_charge("regular", 18, "express", False) == 975


# ORDER ACCEPTANCE TESTS

def test_delicate_order_true_branch():
    assert order_acceptable(10, 5, True) is True


def test_delicate_order_false_branch():
    assert order_acceptable(10, 6, True) is False


def test_non_delicate_weight_exceeds_limit():
    assert order_acceptable(26, 10, False) is False


def test_non_delicate_weight_within_limit():
    assert order_acceptable(25, 40, False) is True


def test_item_count_within_limit():
    assert order_acceptable(20, 40, False) is True


def test_item_count_exceeds_limit():
    assert order_acceptable(20, 41, False) is False


# DROP-OFF STATUS TESTS

def test_bedding_cutoff_branch():
    assert dropoff_status(90, True, False) == "accepted"


def test_non_bedding_cutoff_branch():
    assert dropoff_status(60, False, False) == "accepted"


def test_express_cutoff_branch():
    assert dropoff_status(90, False, True) == "accepted"


def test_non_express_cutoff_branch():
    assert dropoff_status(60, False, False) == "accepted"


def test_dropoff_accepted_branch():
    assert dropoff_status(60, False, False) == "accepted"


def test_dropoff_late_branch():
    assert dropoff_status(50, False, False) == "late"


def test_dropoff_rejected_branch():
    assert dropoff_status(39, False, False) == "rejected"


def test_bedding_and_express_cutoff():
    assert dropoff_status(120, True, True) == "accepted"
