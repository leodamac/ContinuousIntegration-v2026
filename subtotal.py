"""Subtotal por cantidad de miembros (R3)."""

from decimal import Decimal


def calcular_subtotal(precio_plan, precio_extras, miembros):
    """Recibe precios por persona validados por R1/R2; retorna -1 si son invalidos.

    No aplica descuentos, recargos ni redondeo.
    """
    if isinstance(miembros, bool) or not isinstance(miembros, int) or miembros < 1:
        return -1
    for precio in (precio_plan, precio_extras):
        if isinstance(precio, bool) or not isinstance(precio, (int, float, Decimal)):
            return -1
        if not Decimal(str(precio)).is_finite() or precio < 0:
            return -1
    return (Decimal(str(precio_plan)) + Decimal(str(precio_extras))) * miembros
