from decimal import Decimal

GROUP_FACTOR = Decimal("0.90")


def apply_group_discount(amount: Decimal, members: int) -> Decimal:
    """R4: 10% de descuento con 2 o mas miembros."""
    return amount * GROUP_FACTOR if members >= 2 else amount