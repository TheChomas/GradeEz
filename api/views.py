from sentence_transformers import SentenceTransformer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from ..utils.neural import get_score, start_model

cache_timeout = 60

# model = None
model = start_model()


@api_view(['GET'])
@cache_page(cache_timeout)
def api_overview(request):
    api_urls = {
        'Overview': '/  GET',
        'Evaluate passage': '/api/eval/  POST',
    }

    return Response(api_urls)


@api_view(['POST'])
def evaluate_questions(request):

    passage = request.data['passage']
    questions = request.data['questions']
    answers = request.data['answers']

    res = get_score(model, passage, questions, answers)

    return Response(res)
