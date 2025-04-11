from transformers import pipeline

def qa(question: str):

    qa_pipeline = pipeline(
        "question-answering",
         model="deepset/roberta-base-squad2"
    )

    context = """
    Paris is the capital and most populous city of France, with an estimated population of 2.2 million in 2020.
    It is  the center of the Île-de-France region, and the seat of government of France.
    """

    return qa_pipeline({
        "question": question,
        "context": context
    })

