try:
    from transformers import GPT2Tokenizer, GPT2LMHeadModel
    print("Transformers library is correctly installed and imported.")
except ImportError as e:
    print(f"Error: {e}")
