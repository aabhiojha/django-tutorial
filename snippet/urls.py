from django.urls import path
from snippet import views

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet-list'), # type: ignore
    path('snippets/<int:pk>/', views.snippet_detail), # type: ignore
]
