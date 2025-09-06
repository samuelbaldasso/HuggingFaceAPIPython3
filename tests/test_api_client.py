import unittest
from unittest.mock import patch, MagicMock
from src.api_client import HuggingFaceClient

class TestHuggingFaceClient(unittest.TestCase):
    @patch('src.api_client.AutoModelForCausalLM')
    @patch('src.api_client.AutoTokenizer')
    def test_query_success(self, mock_tokenizer_class, mock_model_class):
        # Mock tokenizer
        mock_tokenizer = MagicMock()
        mock_tokenizer_class.from_pretrained.return_value = mock_tokenizer
        mock_tokenizer.return_tensors = "pt"
        mock_tokenizer.decode.return_value = 'Olá, mundo!'
        mock_tokenizer.side_effect = lambda *args, **kwargs: {'input_ids': [[1, 2, 3]]}
        # Mock model
        mock_model = MagicMock()
        mock_model_class.from_pretrained.return_value = mock_model
        mock_model.generate.return_value = [[1, 2, 3]]
        client = HuggingFaceClient(model_name='mock-model')
        result = client.query('Olá')
        self.assertEqual(result, 'Olá, mundo!')

if __name__ == '__main__':
    unittest.main()
