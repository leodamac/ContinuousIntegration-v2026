from decimal import Decimal

from pricing_rules import apply_group_discount


def D(x):
    return Decimal(str(x))


# ---- R4 ----
def test_r4_one_member_no_discount():
    assert apply_group_discount(D(45), 1) == D(45)


def test_r4_two_members_ten_percent():
    assert apply_group_discount(D(90), 2) == D(81)


def test_r4_three_members_ten_percent():
    assert apply_group_discount(D(135), 3) == D("121.5")