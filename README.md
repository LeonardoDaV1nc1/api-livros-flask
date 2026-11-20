# API de Livros com Python e Flask

## Objetivo da API
Disponibilizar uma API mínima em Python com Flask que retorna um objeto JSON contendo três livros cadastrados previamente numa lista em memória, através de uma rota HTTP `GET`.

## Rota disponibilizada
- **GET `/livros`** — disponível localmente em `http://127.0.0.1:5000/livros` e retorna um JSON com a chave `"livros"` contendo os três registos (`id`, `titulo`, `autor` e `ano`).

## Como instalar as dependências

1. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   ```
   - **Linux/macOS:**
     ```bash
     source venv/bin/activate
     ```
   - **Windows:**
     ```bash
     venv\Scripts\activate
     ```

2. Instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## Como executar a aplicação

Com o ambiente virtual ativado, execute:
```bash
python app.py
```

Em seguida, aceda a `http://127.0.0.1:5000/livros` no navegador ou numa ferramenta de teste de APIs (ex.: curl, Postman, Insomnia).

## Como executar os testes automatizados

Com o ambiente virtual ativado, execute:
```bash
python -m unittest -v
# ou
python test_app.py -v
```

---

## Respostas às questões de revisão

1. **Qual é a finalidade de `Flask(__name__)`?**  
   Indica ao Flask o nome do módulo ou pacote atual para que ele consiga localizar recursos relativos à aplicação (como pastas de templates ou ficheiros estáticos) e identificar corretamente o ponto de entrada da app.

2. **Qual é a função do decorador `@app.route()`?**  
   Associa um caminho de URL (como `"/livros"`) e os métodos HTTP permitidos (como `["GET"]`) à função Python logo abaixo, fazendo com que pedidos feitos para esse endereço executem essa função.

3. **Por que a rota `/livros` utiliza o método `GET`?**  
   Porque o objetivo é apenas consultar e ler os dados dos livros sem alterar o estado do servidor nem criar ou remover recursos, o que corresponde à semântica padrão do método HTTP `GET`.

4. **Qual é a finalidade de `jsonify()`?**  
   Converte estruturas de dados Python (como dicionários e listas) numa resposta HTTP válida no formato JSON, definindo automaticamente o cabeçalho `Content-Type: application/json`.

5. **Qual é a diferença entre uma lista Python e a representação JSON retornada pela API?**  
   A lista Python é uma estrutura de dados em memória usada pelo interpretador durante a execução do código, enquanto a representação JSON é um formato textual estruturado (pares chave-valor, arrays e tipos primitivos) serializado para transporte na resposta HTTP e consumido por outros sistemas ou clientes.

6. **O que acontece quando o servidor é iniciado com `app.run(debug=True)`?**  
   Ativa o modo de depuração: o servidor reinicia automaticamente quando deteta alterações no código e apresenta mensagens de erro detalhadas (*traceback*) no navegador caso ocorra alguma exceção.

7. **Qual endereço deverá ser acessado para consultar os livros localmente?**  
   `http://127.0.0.1:5000/livros`
