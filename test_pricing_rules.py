"""Pruebas de las reglas de precios del gimnasio."""
from decimal import Decimal

from pricing_rules import (
    apply_group_discount,
    apply_special_offer,
    apply_premium_surcharge,
)


def to_decimal(x):
    """Verifica to decimal."""
    return Decimal(str(x))


# ---- R4 ----
def test_r4_one_member_no_discount():
    """Verifica r4 one member no discount."""
    assert apply_group_discount(to_decimal(45), 1) == to_decimal(45)


def test_r4_two_members_ten_percent():
    """Verifica r4 two members ten percent."""
    assert apply_group_discount(to_decimal(90), 2) == to_decimal(81)


def test_r4_three_members_ten_percent():
    """Verifica r4 three members ten percent."""
    assert apply_group_discount(to_decimal(135), 3) == to_decimal("121.5")


# ---- R5 ----
def test_r5_at_or_below_200_no_offer():
    """Verifica r5 at or below 200 no offer."""
    assert apply_special_offer(to_decimal(200)) == to_decimal(200)
    assert apply_special_offer(to_decimal(100)) == to_decimal(100)


def test_r5_above_200_minus_20():
    """Verifica r5 above 200 minus 20."""
    assert apply_special_offer(to_decimal(201)) == to_decimal(181)


def test_r5_exactly_400_minus_20():
    """Verifica r5 exactly 400 minus 20."""
    assert apply_special_offer(to_decimal(400)) == to_decimal(380)


def test_r5_above_400_minus_50_not_both():
    """Verifica r5 above 400 minus 50 not both."""
    assert apply_special_offer(to_decimal(401)) == to_decimal(351)
    assert apply_special_offer(to_decimal(594)) == to_decimal(544)


# ---- R6 ----
def test_r6_with_premium_extra_plus_15():
    """Verifica r6 with premium extra plus 15."""
    assert apply_premium_surcharge(to_decimal(358), True) == to_decimal("411.7")


def test_r6_without_premium_extra_unchanged():
    """Verifica r6 without premium extra unchanged."""
    assert apply_premium_surcharge(to_decimal(286), False) == to_decimal(286)


# ---- Cadena R4 -> R5 -> R6 (casos de la tabla) ----
def test_chain_premium_spa_specialized_3_members():
    """Verifica chain premium spa specialized 3 members."""
    a = apply_group_discount(to_decimal(420), 3)
    a = apply_special_offer(a)
    a = apply_premium_surcharge(a, True)
    assert a == to_decimal("411.7")


def test_chain_standard_4_members_no_premium():
    """Verifica chain standard 4 members no premium."""
    a = apply_group_discount(to_decimal(340), 4)
    a = apply_special_offer(a)
    a = apply_premium_surcharge(a, False)
    assert a == to_decimal(286)
