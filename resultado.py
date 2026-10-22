"""Resultado final de la cotización del gimnasio (R7)."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def finalizar_resultado(
    monto: int | float | Decimal,
    seleccion_valida: bool = True,
    confirmado: bool = True,
) -> int:
    """Redondea el monto final o devuelve -1 si es inválido o se cancela.

    El monto debe recibirse después de los descuentos y del recargo.
    La interfaz comunica la validación y la confirmación mediante booleanos;
    esta función no solicita datos ni imprime resultados.
    """
    if seleccion_valida is not True or confirmado is not True:
        return -1
    if isinstance(monto, bool) or not isinstance(monto, (int, float, Decimal)):
        return -1

    try:
        valor = Decimal(str(monto))
        if not valor.is_finite() or valor < 0:
            return -1
        return int(valor.to_integral_value(rounding=ROUND_HALF_UP))
    except (InvalidOperation, ValueError, OverflowError):
        return -1
