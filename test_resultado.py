"""Pruebas de R7: redondeo final, selección inválida y cancelación."""

from decimal import Decimal
import unittest

from resultado import finalizar_resultado


class TestResultado(unittest.TestCase):
    """Verifica el resultado recibido después de R4, R5 y R6."""

    def test_mitades_se_redondean_hacia_arriba(self):
        for monto, esperado in [(121.5, 122), (214.5, 215), (2.5, 3), (0.5, 1)]:
            with self.subTest(monto=monto):
                self.assertEqual(finalizar_resultado(monto), esperado)

    def test_redondeo_a_entero_mas_cercano(self):
        for monto, esperado in [(30, 30), (81, 81), (411.7, 412),
                                (625.6, 626), (121.49, 121), (0, 0)]:
            with self.subTest(monto=monto):
                self.assertEqual(finalizar_resultado(monto), esperado)

    def test_decimal_con_precision_cerca_de_la_mitad(self):
        self.assertEqual(finalizar_resultado(Decimal("121.499999999999999")), 121)
        self.assertEqual(finalizar_resultado(Decimal("121.500000000000001")), 122)

    def test_seleccion_invalida(self):
        self.assertEqual(finalizar_resultado(30, seleccion_valida=False), -1)

    def test_cancelacion(self):
        self.assertEqual(finalizar_resultado(30, confirmado=False), -1)

    def test_montos_invalidos(self):
        for monto in [-1, -0.1, None, "30", True, float("nan"),
                      float("inf"), float("-inf"), Decimal("NaN")]:
            with self.subTest(monto=monto):
                self.assertEqual(finalizar_resultado(monto), -1)


if __name__ == "__main__":
    unittest.main()
