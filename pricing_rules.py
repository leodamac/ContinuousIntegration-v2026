from decimal import Decimal

GROUP_FACTOR = Decimal("0.90")
SURCHARGE_FACTOR = Decimal("1.15")


def apply_group_discount(amount: Decimal, members: int) -> Decimal:
    """R4: 10% de descuento con 2 o mas miembros."""
    return amount * GROUP_FACTOR if members >= 2 else amount


def apply_special_offer(amount: Decimal) -> Decimal:
    """R5: si > 400 resta 50; si no, si > 200 resta 20 (nunca ambos)."""
    if amount > 400:
        return amount - Decimal("50")
    if amount > 200:
        return amount - Decimal("20")
    return amount


def apply_premium_surcharge(amount: Decimal, has_premium_extra: bool) -> Decimal:
    """R6: +15% si hay al menos un extra premium."""
    return amount * SURCHARGE_FACTOR if has_premium_extra else amount