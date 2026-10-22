"""Pruebas del requisito R3: subtotal por cantidad de miembros."""

import unittest

from catalogo import calcular_subtotal


class TestSubtotal(unittest.TestCase):
    """Verifica el cálculo antes de descuentos y recargos."""

    def test_subtotal_sin_extras(self):
        self.assertEqual(calcular_subtotal("BASIC", [], 1), 30)
        self.assertEqual(calcular_subtotal("PREMIUM", [], 3), 210)

    def test_subtotal_con_un_extra(self):
        self.assertEqual(calcular_subtotal(
            "STANDARD", ["PERSONAL_TRAINING"], 1), 70)

    def test_multiplica_plan_y_extras_por_todos_los_miembros(self):
        self.assertEqual(calcular_subtotal(
            "STANDARD", ["GROUP_CLASSES", "PERSONAL_TRAINING"], 4), 340)

    def test_subtotal_con_extras_premium(self):
        self.assertEqual(calcular_subtotal(
            "PREMIUM", ["SPA", "SPECIALIZED_PROGRAM"], 3), 420)

    def test_no_aplica_descuento_grupal(self):
        self.assertEqual(calcular_subtotal("BASIC", ["GROUP_CLASSES"], 2), 90)

    def test_cantidad_invalida(self):
        for miembros in [0, -1, 1.5, "2", None, True, False]:
            with self.subTest(miembros=miembros):
                self.assertEqual(calcular_subtotal("BASIC", [], miembros), -1)

    def test_seleccion_invalida(self):
        for plan, extras in [
            ("GOLD", []), ("BASIC", ["SPA"]),
            ("PREMIUM", ["UNKNOWN"]), ("BASIC", None),
        ]:
            with self.subTest(plan=plan, extras=extras):
                self.assertEqual(calcular_subtotal(plan, extras, 1), -1)


if __name__ == "__main__":
    unittest.main()
