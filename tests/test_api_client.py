import os
import unittest
from unittest.mock import patch
from src.api_client import HuggingFaceClient

class TestHuggingFaceClient(unittest.TestCase):
    @patch('src.api_client.requests.post')
    def test_query_success(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = [{'generated_text': 'Olá, mundo!'}]
        client = HuggingFaceClient(api_token='fake-token')
        result = client.query('Olá')
        self.assertEqual(result[0]['generated_text'], 'Olá, mundo!')

    def test_missing_token(self):
        with self.assertRaises(ValueError):
            HuggingFaceClient(api_token=None)

if __name__ == '__main__':
    unittest.main()
