import os
from api_client import HuggingFaceClient
import json

def main():
    print('--- Cliente HuggingFace LLM ---')
    prompt = input('Digite seu prompt: ')
    client = HuggingFaceClient()
    try:
        resposta = client.query(prompt)
        print('\nResposta do modelo:')
        print(json.dumps(resposta, indent=2, ensure_ascii=False))
        if isinstance(resposta, list) and 'generated_text' in resposta[0]:
            print('\nTexto gerado:')
            print(resposta[0]['generated_text'])
    except Exception as e:
        print(f'Erro ao consultar a API: {e}')

if __name__ == '__main__':
    main()
