from decimal import Decimal

from pricing_rules import (
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge,
)


def D(x):
    return Decimal(str(x))


# ---- R4 ----
def test_r4_one_member_no_discount():
    assert apply_group_discount(D(45), 1) == D(45)


def test_r4_two_members_ten_percent():
    assert apply_group_discount(D(90), 2) == D(81)


def test_r4_three_members_ten_percent():
    assert apply_group_discount(D(135), 3) == D("121.5")


# ---- R5 ----
def test_r5_at_or_below_200_no_offer():
    assert apply_special_offer(D(200)) == D(200)
    assert apply_special_offer(D(100)) == D(100)


def test_r5_above_200_minus_20():
    assert apply_special_offer(D(201)) == D(181)


def test_r5_exactly_400_minus_20():
    assert apply_special_offer(D(400)) == D(380)


def test_r5_above_400_minus_50_not_both():
    assert apply_special_offer(D(401)) == D(351)
    assert apply_special_offer(D(594)) == D(544)


# ---- R6 ----
def test_r6_with_premium_extra_plus_15():
    assert apply_premium_surcharge(D(358), True) == D("411.7")


def test_r6_without_premium_extra_unchanged():
    assert apply_premium_surcharge(D(286), False) == D(286)


# ---- Cadena R4 -> R5 -> R6 (casos de la tabla) ----
def test_chain_premium_spa_specialized_3_members():
    a = apply_group_discount(D(420), 3)
    a = apply_special_offer(a)
    a = apply_premium_surcharge(a, True)
    assert a == D("411.7")


def test_chain_standard_4_members_no_premium():
    a = apply_group_discount(D(340), 4)
    a = apply_special_offer(a)
    a = apply_premium_surcharge(a, False)
    assert a == D(286)