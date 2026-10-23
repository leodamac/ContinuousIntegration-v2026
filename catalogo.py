"""Catalogo y validacion de extras (R2)."""

PRECIOS_EXTRAS = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}

EXTRAS_PREMIUM = frozenset({"SPA", "SPECIALIZED_PROGRAM"})


def obtener_precio_extras(plan: str, extras: list[str]) -> int:
    """Devuelve el precio de extras por persona, o -1 si son inválidos.

    Una lista vacía representa ningún extra. Cada extra se cobra una sola
    vez aunque aparezca repetido en la selección.
    """
    if plan not in ("BASIC", "STANDARD", "PREMIUM") or not isinstance(extras, list):
        return -1

    seleccion = set()
    for extra in extras:
        if not isinstance(extra, str) or extra not in PRECIOS_EXTRAS:
            return -1
        if extra in EXTRAS_PREMIUM and plan != "PREMIUM":
            return -1
        seleccion.add(extra)

    return sum(PRECIOS_EXTRAS[extra] for extra in seleccion)
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
