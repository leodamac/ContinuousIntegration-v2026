"""Catálogo, validación y subtotal del gimnasio (R1, R2 y R3)."""

PRECIOS_PLANES = {
    "BASIC": 30,
    "STANDARD": 45,
    "PREMIUM": 70,
}

PRECIOS_EXTRAS = {
    "GROUP_CLASSES": 15,
    "PERSONAL_TRAINING": 25,
    "SPA": 30,
    "SPECIALIZED_PROGRAM": 40,
}

EXTRAS_PREMIUM = frozenset({"SPA", "SPECIALIZED_PROGRAM"})


def obtener_precio_plan(plan: str) -> int:
    """Devuelve el precio por persona, o -1 si el plan es inválido.

    Los nombres deben coincidir exactamente con los del catálogo.
    """
    if not isinstance(plan, str):
        return -1
    return PRECIOS_PLANES.get(plan, -1)


def obtener_precio_extras(plan: str, extras: list[str]) -> int:
    """Devuelve el precio de extras por persona, o -1 si son inválidos.

    Una lista vacía representa ningún extra. Cada extra se cobra una sola
    vez aunque aparezca repetido en la selección.
    """
    if obtener_precio_plan(plan) == -1 or not isinstance(extras, list):
        return -1

    seleccion = set()
    for extra in extras:
        if not isinstance(extra, str) or extra not in PRECIOS_EXTRAS:
            return -1
        if extra in EXTRAS_PREMIUM and plan != "PREMIUM":
            return -1
        seleccion.add(extra)

    return sum(PRECIOS_EXTRAS[extra] for extra in seleccion)


def calcular_subtotal(plan: str, extras: list[str], miembros: int) -> int:
    """Calcula (plan + extras) por miembros, o -1 si la selección es inválida.

    La cantidad de miembros debe ser un entero positivo. No aplica
    descuentos, recargos ni redondeo.
    """
    if isinstance(miembros, bool) or not isinstance(miembros, int) or miembros < 1:
        return -1

    precio_plan = obtener_precio_plan(plan)
    precio_extras = obtener_precio_extras(plan, extras)
    if precio_plan == -1 or precio_extras == -1:
        return -1

    return (precio_plan + precio_extras) * miembros
