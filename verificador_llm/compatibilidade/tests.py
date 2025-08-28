from django.test import TestCase

class CompatibilidadeTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_template_used(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'compatibilidade/home.html')

    def test_compatibility_calculation(self):
        response = self.client.post('/', {'ram': 16, 'vram': 8, 'gpu-model': 'mid', 'cpu': 'mid'})
        self.assertContains(response, 'Resultados da Compatibilidade')  # Verifica se a página contém o título dos resultados
        # Adicione mais verificações conforme necessário para validar a lógica de compatibilidade
        # Exemplo: self.assertContains(response, 'Compatível') ou outros resultados esperados
