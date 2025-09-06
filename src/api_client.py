import os
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class HuggingFaceClient:
    def __init__(self, model_name=None):
        load_dotenv()
        self.model_name = model_name or 'gpt2'
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name, trust_remote_code=True)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name, trust_remote_code=True, dtype="auto")

    def query(self, prompt, max_length=256):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        with torch.no_grad():
            outputs = self.model.generate(**inputs, max_length=max_length)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
