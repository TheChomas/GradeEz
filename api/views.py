from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

cache_timeout = 60


@api_view(['GET'])
@cache_page(cache_timeout)
def apiOverview(request):
    api_urls = {
        'Post detail': '/api/post/<int:postId>/',
        'List posts': '/api/posts/',
    }

    return Response(api_urls)
