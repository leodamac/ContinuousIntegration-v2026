"""Catálogo y validación de planes del gimnasio (R1)."""

PRECIOS_PLANES = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}


def obtener_precio_plan(plan: str) -> int:
    """Devuelve el precio por persona, o -1 si el plan es inválido.

    Los nombres deben coincidir exactamente con los del catálogo.
    """
    if not isinstance(plan, str):
        return -1
    return PRECIOS_PLANES.get(plan, -1)
