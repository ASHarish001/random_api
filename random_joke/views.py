import json, random
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

@api_view(['GET'])
def all_joke_types(request):
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    # print(jokes, type(jokes))
    all_types = [joke.get("type") for joke in jokes]
    unique_types = list(set(all_types))
    unique_types.sort()
    return Response(unique_types)

@api_view(['GET'])
def random_joke(request):
    #load jokes from './jokes.json'
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    joke = random.choice(jokes)    
    return Response(joke)

@api_view(['GET'])
def random_jokes(request):
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    count = int(request.query_params.get('count'))
    if count > len(jokes):
        return Response(jokes)
    elif count <= 0:
        joke = random.choice(jokes)
        return Response(joke)
    n_jokes = random.sample(jokes, count)
    return Response(n_jokes)

def plain_random_joke(request):
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    joke = random.choice(jokes)
    return JsonResponse(joke)

@api_view(['GET'])
def all_jokes(request):
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    # print(len(jokes))
    return Response(jokes)

@api_view(['GET'])
def random_jokes_by_type(request):
    print(request.query_params)
    print(type(request.query_params))
    joke_type = request.query_params.get('type')
    count = request.query_params.get('count')
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    all_jokes_by_type = [joke for joke in jokes if joke.get('type') == joke_type]
    if not all_jokes_by_type:
        return Response({'error': f'No jokes found for type: {joke_type}'}, status=404)
    if count is None:
        return Response(random.choice(all_jokes_by_type))
    number = int(count)
    if number <= 0:
        return Response(random.choice(all_jokes_by_type))
    if number > len(all_jokes_by_type):
        return Response(all_jokes_by_type)
    return Response(random.sample(all_jokes_by_type, number))

def plain_random_jokes_by_type(request):
    print(request.GET)
    print(type(request.GET))
    joke_type = request.GET.get('type')
    count = request.GET.get('count')
    jokes_file = os.path.join(os.path.dirname(__file__), 'jokes.json')
    with open(jokes_file, encoding='utf-8') as f:
        jokes = json.load(f)
    all_jokes_by_type = [joke for joke in jokes if joke.get('type') == joke_type]
    if not all_jokes_by_type:
        return JsonResponse({'error': f'No jokes found for type: {joke_type}'}, status=404)
    if count is None:
        return JsonResponse(random.choice(all_jokes_by_type))
    number = int(count)
    if number <= 0:
        return JsonResponse(random.choice(all_jokes_by_type))
    if number > len(all_jokes_by_type):
        return JsonResponse(all_jokes_by_type, safe=False)
    return JsonResponse(random.sample(all_jokes_by_type, number), safe=False)