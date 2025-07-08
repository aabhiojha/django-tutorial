from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # type: ignore
    path('snippets/<int:pk>/', views.SnippetDetails.as_view()), # type: ignore
]

urlpatterns = format_suffix_patterns(urlpatterns)