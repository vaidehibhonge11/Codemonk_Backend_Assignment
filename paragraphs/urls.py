# paragraphs/urls.py
from django.urls import path
from .views import CreateUserView, LoginView, ParagraphListCreateView, ParagraphSearchView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('paragraphs/', ParagraphListCreateView.as_view(), name='paragraphs'),
    path('search/', ParagraphSearchView.as_view(), name='search'),
]
