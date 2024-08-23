"""
This script fine-tunes a GPT-2 model for custom text generation tasks.
"""


from transformers import GPT2Tokenizer, GPT2LMHeadModel

model_neme="gpt-2"

tokenizer=GPT2tokenizer.from_pretrained(model_name)
model=GPT2LMHeadModel.from_pretrained(model_name)

try:
    from transformers import GPT2Tokenizer, GPT2LMHeadModel
    print("Transformers library is correctly installed and imported.")
except ImportError as e:
    print(f"Error: {e}")

    print("hello world")
    