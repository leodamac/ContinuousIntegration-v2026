"""Pruebas del requisito R2: selección y compatibilidad de extras."""

import unittest

from catalogo import obtener_precio_extras


class TestExtras(unittest.TestCase):
    """Comprueba precios, restricciones y selecciones inválidas."""

    def test_sin_extras(self):
        """Verifica sin extras."""
        for plan in ["BASIC", "STANDARD", "PREMIUM"]:
            with self.subTest(plan=plan):
                self.assertEqual(obtener_precio_extras(plan, []), 0)

    def test_precio_individual_de_cada_extra(self):
        """Verifica precio individual de cada extra."""
        for extra, precio in [
            ("GROUP_CLASSES", 15), ("PERSONAL_TRAINING", 25),
            ("SPA", 30), ("SPECIALIZED_PROGRAM", 40),
        ]:
            with self.subTest(extra=extra):
                self.assertEqual(obtener_precio_extras("PREMIUM", [extra]), precio)

    def test_extras_comunes_en_todos_los_planes(self):
        """Verifica extras comunes en todos los planes."""
        for plan in ["BASIC", "STANDARD", "PREMIUM"]:
            with self.subTest(plan=plan):
                self.assertEqual(obtener_precio_extras(
                    plan, ["GROUP_CLASSES", "PERSONAL_TRAINING"]), 40)

    def test_combinacion_de_extras_premium(self):
        """Verifica combinacion de extras premium."""
        self.assertEqual(obtener_precio_extras(
            "PREMIUM", ["SPA", "SPECIALIZED_PROGRAM", "PERSONAL_TRAINING"]), 95)

    def test_extras_premium_rechazados_en_otros_planes(self):
        """Verifica extras premium rechazados en otros planes."""
        for plan in ["BASIC", "STANDARD"]:
            for extra in ["SPA", "SPECIALIZED_PROGRAM"]:
                with self.subTest(plan=plan, extra=extra):
                    self.assertEqual(obtener_precio_extras(plan, [extra]), -1)

    def test_extra_desconocido_invalida_toda_la_seleccion(self):
        """Verifica extra desconocido invalida toda la seleccion."""
        self.assertEqual(obtener_precio_extras(
            "PREMIUM", ["GROUP_CLASSES", "UNKNOWN"]), -1)

    def test_plan_invalido(self):
        """Verifica plan invalido."""
        self.assertEqual(obtener_precio_extras("GOLD", []), -1)

    def test_formato_invalido(self):
        """Verifica formato invalido."""
        for extras in [None, "SPA", [None], [[]], [15], ["spa"]]:
            with self.subTest(extras=extras):
                self.assertEqual(obtener_precio_extras("PREMIUM", extras), -1)

    def test_extra_repetido_se_cobra_una_vez(self):
        """Verifica extra repetido se cobra una vez."""
        self.assertEqual(obtener_precio_extras("BASIC", [
            "GROUP_CLASSES", "GROUP_CLASSES"]), 15)


if __name__ == "__main__":
    unittest.main()
