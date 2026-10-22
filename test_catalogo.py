"""Pruebas del requisito R1: planes y precios por persona."""

import unittest

from catalogo import obtener_precio_plan


class TestPlanes(unittest.TestCase):
    """Verifica el catálogo y el rechazo de planes inválidos."""

    def test_precios_de_planes_validos(self):
        """Verifica precios de planes validos."""
        for plan, precio in [("BASIC", 30), ("STANDARD", 45), ("PREMIUM", 70)]:
            with self.subTest(plan=plan):
                self.assertEqual(obtener_precio_plan(plan), precio)

    def test_planes_invalidos(self):
        """Verifica planes invalidos."""
        for plan in ["GOLD", "", "basic", " BASIC ", None, 30, []]:
            with self.subTest(plan=plan):
                self.assertEqual(obtener_precio_plan(plan), -1)


if __name__ == "__main__":
    unittest.main()
