from django.urls import path
from . import views

urlpatterns = [
    path('random_joke/', views.random_joke, name='random_joke'),
    path('random_jokes/', views.random_jokes, name='random_jokes'),
    path('plain_random_joke/', views.plain_random_joke, name='plain_random_joke'),
    path('all_jokes/', views.all_jokes, name='all_jokes'),
    path('all_joke_types/', views.all_joke_types, name='all_joke_types'),
    path('random_jokes_by_type/', views.random_jokes_by_type, name='random_jokes_by_type'),
    path('plain_random_jokes_by_type/', views.plain_random_jokes_by_type, name='plain_random_jokes_by_type')
]