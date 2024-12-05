from django.test import TestCase
from .models import Vehiculo

class VehiculoTestCase(TestCase):
    def setUp(self):
        Vehiculo.objects.create(
            marca='Ford',
            modelo='F-150',
            serial_carroceria='123ABC',
            serial_motor='456DEF',
            categoria='Carga',
            precio=22000,
        )

    def test_vehiculo_creation(self):
        vehiculo = Vehiculo.objects.get(marca='Ford')
        self.assertEqual(vehiculo.modelo, 'F-150')
        self.assertEqual(vehiculo.categoria, 'Carga')
        self.assertEqual(vehiculo.precio, 22000)