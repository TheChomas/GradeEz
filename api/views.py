from sentence_transformers import SentenceTransformer, InputExample, losses, util
from torch.utils.data import DataLoader

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from .neural import get_score

cache_timeout = 60

model = SentenceTransformer('paraphrase-multilingual-mpnet-base-v2')
print("Model loaded\n")


@api_view(['GET'])
@cache_page(cache_timeout)
def api_overview(request):
    api_urls = {
        'Overview': '/ GET',
        'Evaluate passage': '/api/posts/',
    }

    return Response(api_urls)


@api_view(['POST'])
@cache_page(cache_timeout)
def evaluate_questions(request):

    passage = request.data['passage']
    questions = request.data['questions']
    answers = request.data['answers']

    res = get_score(model, passage, questions, answers)

    return Response(res)
