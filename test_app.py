import unittest
from app import app


class TestLivrosAPI(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    def test_obter_livros_status_code(self):
        response = self.client.get("/livros")
        self.assertEqual(response.status_code, 200)

    def test_obter_livros_content_type(self):
        response = self.client.get("/livros")
        self.assertIn("application/json", response.content_type)

    def test_obter_livros_conteudo(self):
        response = self.client.get("/livros")
        data = response.get_json()

        self.assertIn("livros", data)
        self.assertIsInstance(data["livros"], list)
        self.assertEqual(len(data["livros"]), 3)

        campos_obrigatorios = {"id", "titulo", "autor", "ano"}
        for livro in data["livros"]:
            self.assertTrue(campos_obrigatorios.issubset(livro.keys()))

    def test_metodo_nao_permitido(self):
        response = self.client.post("/livros")
        self.assertEqual(response.status_code, 405)

    def test_rota_inexistente(self):
        response = self.client.get("/rota-que-nao-existe")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
