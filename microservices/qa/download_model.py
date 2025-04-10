from transformers import AutoModelForQuestionAnswering, AutoTokenizer

MODEL_NAME = "deepset/roberta-base-squad2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForQuestionAnswering.from_pretrained(MODEL_NAME)
