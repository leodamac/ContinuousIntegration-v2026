"""Pruebas del requerimiento R3."""
from decimal import Decimal
import unittest
from subtotal import calcular_subtotal


class TestSubtotal(unittest.TestCase):
    """Comprueba el subtotal sin descuentos ni redondeo."""

    def test_casos_validos(self):
        """Verifica casos validos."""
        for plan, extras, miembros, esperado in [(30,0,1,30),(45,25,1,70),
                                                (30,15,2,90),(45,40,4,340),(70,70,3,420)]:
            with self.subTest(plan=plan, extras=extras, miembros=miembros):
                self.assertEqual(calcular_subtotal(plan,extras,miembros),esperado)

    def test_preserva_decimales(self):
        """Verifica preserva decimales."""
        self.assertEqual(calcular_subtotal(Decimal("30.25"),Decimal("0.10"),3),
                         Decimal("91.05"))

    def test_miembros_invalidos(self):
        """Verifica miembros invalidos."""
        for miembros in [0,-1,1.5,"2",None,True,False]:
            with self.subTest(miembros=miembros):
                self.assertEqual(calcular_subtotal(30,0,miembros),-1)

    def test_precios_invalidos(self):
        """Verifica precios invalidos."""
        for precio in [-1,None,"30",True,float("nan"),float("inf")]:
            with self.subTest(precio=precio):
                self.assertEqual(calcular_subtotal(precio,0,1),-1)
                self.assertEqual(calcular_subtotal(30,precio,1),-1)
