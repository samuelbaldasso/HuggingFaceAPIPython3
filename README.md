# Hugging Face API

Projeto Python para consumir a API pública de LLM da HuggingFace.

## Como usar

1. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```
2. Defina sua chave de API HuggingFace na variável de ambiente `HF_API_TOKEN`.
3. Execute o script principal:
   ```sh
   python src/main.py
   ```

## Estrutura

- src/api_client.py: Cliente para a API HuggingFace
- src/main.py: Interface de linha de comando
- tests/: Testes automatizados
