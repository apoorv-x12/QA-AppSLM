from transformers import AutoModelForQuestionAnswering, AutoTokenizer

MODEL_NAME = "deepset/roberta-base-squad2"
CACHE_DIR = "./models"

# Load from or store to local directory
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)
model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME, cache_dir=CACHE_DIR)

print("Model and tokenizer loaded and cached to './models'.")
