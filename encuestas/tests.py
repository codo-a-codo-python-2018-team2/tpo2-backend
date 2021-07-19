from django.test import TestCase

# Create your tests here.

class MyIntegrationTest(TestCase):

    def setUp(self) -> None:
        '''
            Inicializa el set de pruebas.
        '''
        return super().setUp()

    def testHelloWrold(self):
        response = self.client.get("/users/")
        self.assertContains(response , "Hello world from Django for Codo a Codo 4.0")

    def testSatusCodeHelloWorld(self):
        response = self.client.get("/users/")
        self.assertEqual(response.status_code, 200 )

    def testProbarUrlSofia(self):
        response = self.client.get("/sofia/")
        self.assertContains(response , "Esta es la respuesta de Sofía Ferro")

    def testUrlJose(self):
        response = self.client.get("/jose/")
        self.assertContains(response, "Esta es la respuesta creada por Jose Guevara")
