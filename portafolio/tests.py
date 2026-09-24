from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Creacion


class GestionCreacionesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='editor')
        cls.categoria = Categoria.objects.create(nombre='Bombones de autor')
        cls.creacion = Creacion.objects.create(
            nombre='Bombón amargo', categoria=cls.categoria,
            descripcion='Chocolate de alta calidad', imagen='https://example.com/bombon.jpg',
        )

    def setUp(self):
        self.client.force_login(self.user)

    def payload(self, **changes):
        data = {'nombre': 'Nueva creación', 'categoria': self.categoria.pk,
                'descripcion': 'Chocolate artesanal', 'imagen': 'https://example.com/nueva.jpg'}
        data.update(changes)
        return data

    def test_list_and_standalone_forms(self):
        response = self.client.get(reverse('gestion-creaciones'))
        self.assertContains(response, 'data-modal')
        self.assertContains(response, 'Bombón amargo')
        for url in [reverse('gestion-creacion-nueva'), reverse('gestion-creacion-editar', args=[self.creacion.pk])]:
            response = self.client.get(url)
            self.assertContains(response, '<html lang="es">')
            self.assertContains(response, 'creation-form')

    def test_modal_fragment_and_invalid_submission(self):
        url = reverse('gestion-creacion-nueva')
        response = self.client.get(url, HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertContains(response, 'Nueva creación')
        self.assertNotContains(response, '<html')
        response = self.client.post(url, self.payload(nombre=''), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 422)
        self.assertContains(response, 'errorlist', status_code=422)
        self.assertEqual(Creacion.objects.count(), 1)

    def test_create_and_update_from_modal(self):
        response = self.client.post(reverse('gestion-creacion-nueva'), self.payload(), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.json()['redirect'], reverse('gestion-creaciones'))
        self.assertTrue(Creacion.objects.filter(nombre='Nueva creación').exists())
        self.creacion.activo = False
        self.creacion.save()
        response = self.client.post(reverse('gestion-creacion-editar', args=[self.creacion.pk]),
        self.payload(nombre='Nombre editado'), HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.creacion.refresh_from_db()
        self.assertEqual(self.creacion.nombre, 'Nombre editado')
        self.assertFalse(self.creacion.activo)

    def test_toggle_and_authentication(self):
        url = reverse('gestion-creacion-toggle', args=[self.creacion.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        self.client.post(url)
        self.creacion.refresh_from_db()
        self.assertFalse(self.creacion.activo)
        self.client.logout()
        self.assertEqual(self.client.get(reverse('gestion-creaciones')).status_code, 302)
        self.assertEqual(self.client.post(reverse('gestion-creacion-nueva'), self.payload(),
        HTTP_X_REQUESTED_WITH='XMLHttpRequest').status_code, 302)
