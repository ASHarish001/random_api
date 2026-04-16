from django.http import JsonResponse

def urls_available(request):
    return JsonResponse(
        {
            'prepend base': 'http://127.0.0.1:8000/',
            'for a random joke':'jokes/random_joke/',
            'all jokes': 'jokes/all_jokes/'
        }
    )