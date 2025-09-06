# Hugging Face API

Projeto Python para consumir LLMs da HuggingFace via API pública ou localmente com transformers.

## Como usar

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. (Opcional) Defina sua chave de API HuggingFace na variável de ambiente `HF_API_TOKEN` para uso via API.

3. Para rodar localmente (recomendado para modelos pequenos):

   - Edite `src/api_client.py` e defina o modelo desejado (ex: `gpt2`).
   - Execute:

     ```sh
     python src/main.py
     ```

4. Para rodar via API HuggingFace (HTTP):
   - Altere o client para usar requests e a URL da API.
   - Defina o token no `.env` ou variável de ambiente.

## Estrutura

- src/api_client.py: Cliente para HuggingFace (local ou API)
- src/main.py: Interface de linha de comando
- tests/: Testes automatizados
