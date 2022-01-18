

from typing import List
from sentence_transformers import SentenceTransformer, InputExample, losses, util
from torch.utils.data import DataLoader

from api.models import Passage


def get_extractions(model, passage: str, questions: List[str], k=2) -> List[str]:
    '''
    Get the extracted parts from the passage for the corresponding questions
    '''
    temp = []

    # do some filtering of punctuation
    context = passage.replace(". ", ".").replace("\n", "").split(".")

    # encode the text into vectors
    embed = model.encode(context)

    # running semantic search for every question given, and retrieving 'k' top matches
    for question in questions:
        res = util.semantic_search(query_embeddings=model.encode(
            question), corpus_embeddings=embed, top_k=k)
        temp.append(res[0])

    # map all the extractions into an array
    qs = ['. '.join([context[c[x]['corpus_id']]
                    for x in range(len(c))]) + '.' for i, c in enumerate(temp)]

    return qs


def fine_tune_model(model, passage: str, epochs=1):
    corpus = passage.replace(". ", ".").replace("\n", "").split(".")

    train_examples = [InputExample(texts=corpus, label=1.0)]

    train_dataloader = DataLoader(train_examples, shuffle=False, batch_size=16)
    train_loss = losses.CosineSimilarityLoss(model)

    model.fit(train_objectives=[
              (train_dataloader, train_loss)], epochs=epochs, warmup_steps=1)

    return model


def start_model():
    model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')

    passages = Passage.objects.all()

    passages = [passage.passage_text for passage in passages]

    model = fine_tune_model(model, '.'.join(passages), epochs=2)

    print("Model loaded\n")

    return model


def get_score(model, passage: str, questions: List[str], answers: List[str]) -> List[float]:
    model = fine_tune_model(model, passage)
    correct_answers = get_extractions(model, passage, questions)

    score = []

    for ca, a in zip(correct_answers, answers):
        cos_similarity = util.cos_sim(
            model.encode(ca), model.encode(a)).numpy()[0][0]
        score.append(cos_similarity)

    return score
