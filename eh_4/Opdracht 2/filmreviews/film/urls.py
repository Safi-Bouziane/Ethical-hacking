from django.urls import path
from . import views

urlpatterns = [
    path('<int:film_id>', views.detail, name='detail'),
    path('<int:film_id>/maakreview', views.maakreview, name='maakreview'),
    path('review/<int:review_id>', views.wijzigreview, name='wijzigreview'),
    path('review/<int:review_id>/verwijder', views.verwijderreview, name='verwijderreview'),
]