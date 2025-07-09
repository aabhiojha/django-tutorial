from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('snippets/', views.SnippetList.as_view()), # type: ignore
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()), # type: ignore
    path('login/', views.login), # type: ignore
    path('signup/', views.signup), # type: ignore
    path('test/', views.test_token), # type: ignore
]

urlpatterns = format_suffix_patterns(urlpatterns)   