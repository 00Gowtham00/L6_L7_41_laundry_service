
import pytest

from laundry_service import (
    extra_weight_charge,
    order_acceptable,
    dropoff_status
)


# ==========================================
# EXTRA WEIGHT CHARGE TEST CASES
# ==========================================

def test_invalid_garment_type():
    with pytest.raises(ValueError, match="unknown garment type"):
        extra_weight_charge("cotton", 5, "standard", False)


def test_negative_weight():
    with pytest.raises(ValueError, match="invalid weight"):
        extra_weight_charge("regular", -2, "standard", False)


def test_weight_within_included_limit():
    assert extra_weight_charge("regular", 4, "standard", False) == 0


def test_member_extra_included_weight():
    assert extra_weight_charge("regular", 8, "standard", True) == 30


def test_bedding_member_weight():
    assert extra_weight_charge("bedding", 9, "standard", True) == 30


def test_standard_extra_weight():
    assert extra_weight_charge("regular", 7, "standard", False) == 60


def test_express_extra_weight():
    assert extra_weight_charge("regular", 6, "express", False) == 50


def test_standard_weight_above_10():
    assert extra_weight_charge("regular", 16, "standard", False) == 495


def test_express_weight_above_10():
    assert extra_weight_charge("regular", 18, "express", False) == 975


# ==========================================
# ORDER ACCEPTANCE TEST CASES
# ==========================================

def test_delicate_order_accepted():
    assert order_acceptable(10, 5, True) is True


def test_delicate_order_rejected():
    assert order_acceptable(10, 6, True) is False


def test_order_weight_exceeds_limit():
    assert order_acceptable(26, 10, False) is False


def test_normal_order_accepted():
    assert order_acceptable(25, 40, False) is True


def test_normal_order_exceeds_item_limit():
    assert order_acceptable(25, 41, False) is False


# ==========================================
# DROP-OFF STATUS TEST CASES
# ==========================================

def test_dropoff_accepted():
    assert dropoff_status(60, False, False) == "accepted"


def test_dropoff_late():
    assert dropoff_status(50, False, False) == "late"


def test_dropoff_rejected():
    assert dropoff_status(39, False, False) == "rejected"


def test_bedding_dropoff_cutoff():
    assert dropoff_status(90, True, False) == "accepted"


def test_express_dropoff_cutoff():
    assert dropoff_status(120, True, True) == "accepted"
