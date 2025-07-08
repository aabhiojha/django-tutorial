from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet-list'), # type: ignore
    path('snippets/<int:pk>/', views.snippet_details), # type: ignore
]

urlpatterns = format_suffix_patterns(urlpatterns)